---
uid: "112654"
seealso:
- linkId: "2048"
title: Relationships Between Persistent Objects in Code and UI
owner: Ekaterina Kiseleva
---
# Relationships Between Persistent Objects in Code and UI

When designing a business model, it can be necessary to set specific relationships between business objects. This topic describes how to set these relationships between [persistent objects](xref:112570) in an XPO application and demonstrates how these relationships will be organized in a UI.

> [!TIP]
> To learn about the relationships between entities in EF Core, refer to the following help topic: [Relationships Between Entities in Code and UI (EF Core)](xref:402958)

The "Many" side of an association, which is a collection property, is displayed in the UI using the **ListPropertyEditor** in WinForms applications. To show the "One" side that is a reference property, the **LookupPropertyEditor** is used. If [](xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute) is applied to the reference property with the [ExpandObjectMembers.Never](xref:DevExpress.Persistent.Base.ExpandObjectMembers.Never) parameter, **ObjectPropertyEditor** is used instead. Each object collection has an individual [Actions](xref:112622) set, which depends on the collection type. You can manage the **New**, **Delete**, **Link**, or **Unlink** Action's visibility in the Model Editor. Set the List View's [AllowNew](xref:DevExpress.ExpressApp.Model.IModelView.AllowNew), [AllowDelete](xref:DevExpress.ExpressApp.Model.IModelView.AllowDelete), [AllowLink](xref:DevExpress.ExpressApp.Model.IModelListView.AllowLink), or [AllowUnlink](xref:DevExpress.ExpressApp.Model.IModelListView.AllowUnlink) property to **false** to hide these Actions.

If a child object is aggregated (i.e., this object is considered a part of a master object and decorated with the [](xref:DevExpress.Xpo.AggregatedAttribute)), an `XPNestedObjectSpace` [Object Space](xref:113707) is created for its Detail View, because this object should not be physically saved to the database until its owner is saved. If a child object is not aggregated (i.e., it can exist separately), a separate `XPObjectSpace` is used for its Detail View. A nested List View where objects from the detail collections are shown uses the same master `XPObjectSpace` regardless of the aggregation.

## One-to-Many (Non Aggregated)
The relationship between `Department` and `Contacts` illustrates the One-to-Many type, when many `Contacts` can be included in one Department. In this example, the `Department` object contains a child `ContactsCollection` and is the "One" side of its One-to-Many relationship.

![NonAggregatedOneToMany_Win](~/images/nonaggregatedonetomany_win127270.png)

The List View that displays the `ContactsCollection` is accompanied by a **New** Action. This Action allows end users to add new `Contact` objects to one of the existing `Department` objects (including the current object). In addition, the **Link** and **Unlink** Actions are available and allow you to add and remove a reference to a `Contact` object from another collection.

Non-aggregated objects are created in their own Object Space. The new `Contact` objects created within the `Department` Detail View can be saved separately from the parent object.

The following code snippet demonstrates how to implement this type of relationship:

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Contact : XPObject {
    //...
    private Department department;
    [Association("Department-Contacts")]
    public Department Department {
        get { return department; }
        set { SetPropertyValue(nameof(Department), ref department, value); }
    }
}
[DefaultClassOptions]
public class Department : XPObject {
    //...
    [Association("Department-Contacts")]
    public XPCollection<Contact> ContactsCollection {
        get { return GetCollection<Contact>(nameof(ContactsCollection)); }
    }
}
```

***

## One-to-Many (Aggregated)
Let's assume that a Contact has a collection of Notes, which are aggregated with their parent Contact. In this case, the `Note` object declares the "One" aggregated side of the One-to-Many relationship with the `Contact` object.

![AggregatedOneToMany_Win](~/images/aggregatedonetomany_win127264.png)


The List View that displays the `NotesCollection` is accompanied by the **New** Action. This Action allows end users to add new `Note` objects. Note that in this instance, the `Contact` property of the new `Note` objects will be automatically set to the current `Contact` and this editor is not displayed in the UI.

Aggregated objects are created in the parent object's [Object Space](xref:113707). As such, the new `Note` objects created within the **Contact** Detail View will be saved when their parent object is saved, and will be deleted when their parent object is deleted (cascade deletion mechanism).

The following code snippet demonstrates how to implement this type of relationship:

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Contact : XPObject {
    //...
    [Association("Contact-Notes"), DevExpress.Xpo.Aggregated]
    public XPCollection<Note> NotesCollection {
        get { return GetCollection<Note>(nameof(NotesCollection)); }
    }
}
[DefaultClassOptions]
public class Note : XPObject {
    //...
    private Contact contact;
    [Association("Contact-Notes")]
    public Contact Contact {
        get { return contact; }
        set { SetPropertyValue(nameof(Contact), ref contact, value); }
    }
}
```

***

## Many-to-Many
For example, each `Contact` can have a collection of `Tasks` and each `Task` can be assigned to a number of `Contacts`. Thus, the relationship between the `Contact` and `Task` objects is described as Many-to-Many.

![ManyToManyObject_Win](~/images/manytomanyobject_win127272.png)

The List View for the `TasksCollection` includes the **Link** Action that allows users to reference existing Task objects.

In Many-to-Many collections, the **New** Action is hidden when @DevExpress.ExpressApp.SystemModule.NewObjectViewController.LinkNewObjectToParentImmediately is set to `true`. This aligns with the Many-to-Many relationship concept, but you can still create a new Task through the **Link** Action's pop-up window.

The **Unlink** Action for the `TasksCollection` allows users to remove `Task` object references from the collection.

The following code snippet demonstrates how to implement this type of relationship:

### Technique 1

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Contact : XPObject {
    //...
    [Association("Contacts-Tasks")]
    public XPCollection<Task> TasksCollection {
        get { return GetCollection<Task>(nameof(TasksCollection)); }
    }
}
[DefaultClassOptions]
public class Task : XPObject {
    //...
    [Association("Contacts-Tasks")]
    public XPCollection<Contact> ContactsCollection {
        get { return GetCollection<Contact>(nameof(ContactsCollection)); }
    }
}
```

***

### Technique 2 (with an Intermediate Object)

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Xpo;
using System.Collections.Generic;
using System.ComponentModel;
// ...
[DefaultClassOptions]
public class Contact : XPObject {
    // ...
    [Browsable(false)]
    [Association("Contact-ContactTasks"), Aggregated]
    public XPCollection<ContactTask> ContactTasks { 
        get { return GetCollection<ContactTask>(nameof(ContactTasks)); } }
    [ManyToManyAlias(nameof(ContactTasks), nameof(ContactTask.Task))]
    public IList<Task> TaskCollection {
        get { return GetList<Task>(nameof(TaskCollection)); }
    }
}
[DefaultClassOptions]
public class Task : XPObject {
    // ...
    [Browsable(false)]
    [Association("Task-ContactTasks"), Aggregated]
    public XPCollection<ContactTask> ContactTasks { 
        get { return GetCollection<ContactTask>(nameof(ContactTasks)); } }
    [ManyToManyAlias(nameof(ContactTasks), nameof(ContactTask.Contact))]
    public IList<Contact> ContactCollection {
        get { return GetList<Contact>(nameof(ContactCollection)); }
    }
}
// Uncomment the following line if your application uses the Security System. 
// [IntermediateObject(nameof(Contact), nameof(Task))]
public class ContactTask : XPObject {
    public ContactTask(Session session) : base(session) { }
    Contact fContact;
    [Association("Contact-ContactTasks")]
    public Contact Contact {
        get { return fContact; }
        set { SetPropertyValue<Contact>(nameof(Contact), ref fContact, value); }
    }
    Task fTask;
    [Association("Task-ContactTasks")]
    public Task Task {
        get { return fTask; }
        set { SetPropertyValue<Task>(nameof(Task), ref fTask, value); }
    }
}
```

***

For more information on this technique, refer to the following help topic: [Relationships Between Objects](xref:2041#technique-1-with-a-custom-intermediate-object).

## One-to-One
If each `Contact` can have only one unique `Address` and one `Address` cannot be assigned to many `Contacts`, this relationship is One-to-One.

![OneToOneObject_Win](~/images/onetooneobject_win127284.png)

This relationship doesn't provide a collection side. Note that in this instance, the `Contact` property of the new `Address` objects will be automatically set to the current `Contact`.

The following code snippet demonstrates how to implement this type of relationship:

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Contact : XPObject {
    //...
    private Address address;
    [Aggregated]
    public Address Address{
        get { return address; }
        set {
            if (address == value) return;
            Address prevAddress = address;
            address = value;
            if (IsLoading) return;
            if (prevAddress!= null && prevAddress.Contact == this)
                prevAddress.Contact = null;
            if (address != null)
                address.Contact = this;
            OnChanged(nameof(Address));
        }
    }
}
[DefaultClassOptions]
public class Address : XPObject {
    //...
    Contact contact = null;
    public Contact Contact {
        get { return contact; }
        set {
            if (contact == value)
                return;
            Contact prevContact = contact;
            contact = value;
            if (IsLoading) return;
            if (prevContact != null && prevContact.Address == this)
                prevContact.Address = null;
            if (contact != null)
                contact.Address = this;
            OnChanged(nameof(Contact));
        }
    }
}
```

***

## Self-Referencing Relationship

A self-referencing relationship allows an object's property to point to another object of the same type.

The following code snippet demonstrates how to create a hierarchical structure where an employee reports to a manager (who is also an employee):

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;

[DefaultClassOptions]
public class Employee : BaseObject {
    public Employee(Session session)
        : base(session) {
    }
    public override void AfterConstruction() {
        base.AfterConstruction();
    }
    string _firstName;
    public string FirstName {
        get {
            return _firstName;
        }
        set {
            SetPropertyValue(nameof(FirstName), ref _firstName, value);
        }
    }

    [Association]
    public XPCollection<Employee> Workers {
        get {
            return GetCollection<Employee>(nameof(Workers));
        }
    }
    Employee _manager;
    [Association]
    public Employee Manager {
        get {
            return _manager;
        }
        set {
            SetPropertyValue(nameof(Manager), ref _manager, value);
        }
    }
}
```

If you want to display your hierarchical objects in a List View tree control, extend your data model with [XAF's ITreeNode interface](xref:112837) and use [XAF Tree List Editors](xref:112836).