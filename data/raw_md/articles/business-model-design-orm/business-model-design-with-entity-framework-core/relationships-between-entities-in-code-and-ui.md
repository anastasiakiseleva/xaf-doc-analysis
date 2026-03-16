---
uid: "402958"
title: Relationships Between Entities in Code and UI (EF Core)
owner: Anastasiya Kisialeva
seealso:
  - linkId: "404429"
---
# Relationships Between Entities in Code and UI (EF Core)

When designing a business model, it can be necessary to set specific relationships between business objects. This topic describes how to set relationships between entities that are available in the WinForms and ASP.NET Core Blazor applications created with Entity Framework Core and demonstrates how these relationships will be organized in a UI.

> [!TIP]
> To learn about the relationships between objects in XPO, refer to the following help topic: [Relationships Between Persistent Objects in Code and UI (XPO)](xref:112654).

The "Many" side is a collection property. The UI displays it with the help of the `DevExpress.ExpressApp.Editors.ListPropertyEditor` in WinForms and ASP.NET Core Blazor applications. To show the "One" side, XAF uses `DevExpress.ExpressApp.Win.Editors.LookupPropertyEditor` and `DevExpress.ExpressApp.Blazor.Editors.LookupPropertyEditor`. If [](xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute) is applied to the reference property with the [ExpandObjectMembers.Never](xref:DevExpress.Persistent.Base.ExpandObjectMembers.Never) parameter, `DevExpress.ExpressApp.Win.Editors.ObjectPropertyEditor` and `DevExpress.ExpressApp.Blazor.Editors.ObjectPropertyEditor` are used instead. Each entity collection has an individual [Actions](xref:112622) set. This set depends on the collection type.

## One-to-Many (Non-Aggregated)

The relationship between Department and Contacts illustrates the One-to-Many type. Multiple ("Many") Contacts can be associated with a single ("One") Department. In this example, the `Department` entity contains a child `ContactsCollection` and is the "One" side of its One-to-Many relationship.

![NonAggregatedOneToManyObject_Win](~/images/nonaggregatedonetomany_win127270.png)

![NonAggregatedOneToManyObject_Blazor](~/images/nonaggregatedonetomany_blazor.png)

The List View that displays the `ContactsCollection` is accompanied by a **New** Action. This Action allows end users to add new `Contact` entities to an existing `Department` (including the current entity). In addition, the **Link** and **Unlink** Actions are available and allow you to add and remove a reference to a `Contact` object from another collection.

> [!NOTE]
> If you get the "The DELETE statement conflicted with the REFERENCE constraint" exception when you delete a parent object, refer to the following section for a solution: [One-to-Many Behavior on Delete](#one-to-many-behavior-on-delete).

The following code snippet demonstrates how to implement this type of relationship:

# [Department - the "One" side (C#)](#tab/tabid-csharp-department)

```csharp{11}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Component.DataAnnotations;
// ...
[DefaultClassOptions]
public class Department : BaseObject {
    public virtual string Name { get; set; }
    public virtual IList<Contact> ContactsCollection { get; set; } = new ObservableCollection<Contact>();
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
# [Contact - the "Many" side (C#)](#tab/tabid-csharp-contact1)

```csharp{9}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel;
// ...
[DefaultClassOptions]
public class Contact : BaseObject {
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    public virtual Department Department { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
***

> [!IMPORTANT]
> [!include[inotifycollectionchanged-note](~/templates/inotifycollectionchanged-note.md)]

## One-to-Many (Aggregated)
Let's assume that a Contact has a collection of Notes, which are aggregated with their parent Contact. In this case, the `Note` entity declares the "One" aggregated side of the One-to-Many relationship with the **Contact** entity.

> [!NOTE]
> In Entity Framework Core, the aggregation mechanism doesn't support cascade deletion. Use the technique described in the following section: [One-to-Many Behavior on Delete](#one-to-many-behavior-on-delete). Alternatively, you can implement this functionality as described in the following section: [Cascade Deletion for Aggregated Entities](#cascade-deletion-for-aggregated-entities).

![AggregatedOneToManyObject_Win](~/images/aggregatedonetomany_win127264.png)

![AggregatedOneToManyObject_Blazor](~/images/aggregatedonetomany_blazor.png)

The List View that displays the `NotesCollection` is accompanied by the **New** Action. This Action allows end users to add new `Note` entities. Note that in this case, the `Contact` property of a new `Note` is automatically set to the current `Contact`.

A collection is aggregated if it is decorated with the [](xref:DevExpress.ExpressApp.DC.AggregatedAttribute). The following code snippet demonstrates how to implement this type of relationship:

# [Contact - the "One" side (C#)](#tab/tabid-csharp-contact2)

```csharp{12-13}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Contact {
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    [DevExpress.ExpressApp.DC.Aggregated]
    public virtual IList<Note> NotesCollection { get; set; } = new ObservableCollection<Note>();
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
# [Note - the "Many" side (C#)](#tab/tabid-csharp-note)
```csharp{9}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Note : BaseObject {
    public virtual string Text { get; set; }
    public virtual Contact Contact { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

## Many-to-Many
Consider the following entity relationship. A `Contact` can have a collection of `Tasks` and each `Task` can be assigned to a number of `Contacts`. Thus, the relationship between `Contact` and `Task` entities is Many-to-Many.

![NonAggregatedManyToManyObject_Win](~/images/manytomanyobject_win127272.png)

![NonAggregatedManyToManyObject_blazor](~/images/manytomanyobject_blazor.png)

The List View that displays the `TasksCollection` is accompanied by the **Link** Action. This action allows end users to add references to existing `Task` objects. The **New** Action is not applied to this collection due to unique conceptual properties of the Many-to-Many relationship. However, you can create a new `Task` in the **Link** Action's pop-up window.

End users can also use the **Unlink** Action to remove references to `Task` objects from the collection.

The following code snippet demonstrates how to implement this type of relationship:

# [Contact - the "Many" side (C#)](#tab/tabid-csharp-contact3)

```csharp{12}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Contact : BaseObject {
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    public virtual IList<Task> TasksCollection { get; set; } = new ObservableCollection<Task>();
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
# [Task - the "Many" side (C#)](#tab/tabid-csharp-task)

```csharp{13}
using System;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Task : BaseObject {
    public virtual string Subject { get; set; }
    public virtual DateTime DueDate { get; set; }
    public virtual IList<Contact> ContactsCollection { get; set; } = new ObservableCollection<Contact>();
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

> [!NOTE]
>
> XAF does not support usage scenarios where a many-to-many relationship is only defined on one side of a relation. Always define collection navigation properties on both sides of a relation as demonstrated in the code sample above. 

## One-to-One
Consider the following entity relationship. Each `Contact` can have only one unique `Address` and one `Address` cannot be assigned to many `Contacts`. This is a One-to-One relationship.

![Address_Win](~/images/onetooneobject_win127284.png)

![OneToOneObject_Blazor](~/images/onetooneobject_blazor.png)

This relationship doesn't provide a collection side. Note that in this instance, the `Contact` property of the new `Address` objects will be automatically set to the current `Contact`.

The following code snippet demonstrates how to implement this type of relationship. In this relationship type, it is important to explicitly declare a Primary Key of a parent entity as a Foreign Key in the related entity.

# [Contact - the "One" side (C#)](#tab/tabid-csharp-contact4)

```csharp{11}
using DevExpress.Persistent.Base;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Contact {
    [Key, Browsable(false)]
    public virtual Guid ID { get; set; }
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    public virtual Address Address { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
# [Address - the "One" side (C#)](#tab/tabid-csharp-address)

```csharp{10-11,14}
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using DevExpress.Persistent.Base;
// ...
[DefaultClassOptions]
[DefaultProperty(nameof(FullAddress))]
public class Address {
    [Key, Browsable(false)]
    [ForeignKey(nameof(Contact))]
    public virtual Guid ID { get; set; }
    public virtual string FullAddress { get; set; }
    public virtual string ZipPostal { get; set; }
    public virtual Contact Contact { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

## One-to-Many Behavior on Delete

When you delete a parent object, Entity Framework Core (in its default configuration) tries to load all related child objects. To delete an object without loading all its associations, add the following code snippet to the `OnModelCreating` method of your project's `DbContext`:

```csharp{6}
namespace YourApplicationName.Module.BusinessObjects;

public class YourApplicationNameDbContext : DbContext {
    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        base.OnModelCreating(modelBuilder);
        modelBuilder.SetOneToManyAssociationDeleteBehavior(DeleteBehavior.SetNull, DeleteBehavior.Cascade);
        // ...
    }
}
```

This code snippet sets up `DeleteBehavior.SetNull` for entities bound by the [non-aggregated](#one-to-many-non-aggregated) One-to-Many relationship and `DeleteBehavior.Cascade` for entities bound by the [aggregated](#one-to-many-aggregated) relationship.

> [!NOTE]
> New projects generated by the [Template Kit](xref:405447) already contain this code snippet.

Your associations may be more complex. For example, they can have links to base types. In such cases, you may need to use Fluent API to configure the association's behavior. For more information, refer to the following section: [Cascade Deletion for Aggregated Entities](#cascade-deletion-for-aggregated-entities).

## Cascade Deletion for Aggregated Entities
In applications with Entity Framework Core, aggregation does not use a nested [](xref:DevExpress.ExpressApp.IObjectSpace). To implement a cascade deletion mechanism, enforce it in the model builder in the `OnModelCreating` method. To do this, call the [OnDelete(DeleteBehavior.Cascade)](xref:Microsoft.EntityFrameworkCore.Metadata.Builders.ReferenceCollectionBuilder.OnDelete*) method as shown in the following code snippet:

# [C#](#tab/tabid-csharp)

```csharp
public class MySolutionDbContext : DbContext {
    //...
    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        modelBuilder.Entity<Contact>()
            .HasMany(r => r.NotesCollection)
            .WithOne(x => x.Contact)
            .OnDelete(DeleteBehavior.Cascade);
    }
}
```

***

For more information, refer to the following article: [Cascade Delete](https://learn.microsoft.com/en-us/ef/core/saving/cascade-delete).


## Self-Referencing Relationship

A self-referencing relationship allows an object's property to point to another object of the same type.

The following code snippet demonstrates how to create a hierarchical structure where an employee reports to a manager (who is also an employee):

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.ObjectModel;

[DefaultClassOptions]
public class Employee : BaseObject {
    public virtual String FirstName { get; set; }
    public virtual ObservableCollection<Employee> Workers { get; set; } = new ObservableCollection<Employee>();
    public virtual Employee Manager { get; set; }
}
```

If you want to display your hierarchical objects in a List View tree control, extend your data model with [XAF's ITreeNode interface](xref:112837) and use [XAF Tree List Editors](xref:112836).