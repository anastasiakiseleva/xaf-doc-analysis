---
uid: "402990"
title: 'How to: Initialize Business Objects with Default Property Values in Entity Framework Core'
owner: Yekaterina Kiseleva
seealso:
  - linkType: HRef
    linkId: xref:113152#initialize-the-object-owner-createdby-updatedby-properties
    altText: How to implement the CreatedBy, CreatedOn and UpdatedBy, UpdatedOn properties in a business class
  - linkId: "113711"
---
# How to: Initialize Business Objects with Default Property Values in Entity Framework Core

When designing business classes, a common task is to ensure that a newly created business object is initialized with default property values. This topic explains how different types of properties can be initialized. As an example, a Contact business class will be implemented. After a Contact object is created, its properties will be initialized with default values.

![Initialize objects in ASP.NET Core Blazor applications](~/images/initializeobjects_blazor.png)

> [!Note]
> Similar example for XPO is available in the following help topic: [How to: Initialize Business Objects with Default Property Values in XPO](xref:113258)

## Simple Property
You can support an [](xref:DevExpress.ExpressApp.IXafEntityObject) interface in your business classes. This interface declares the [IXafEntityObject.OnCreated](xref:DevExpress.ExpressApp.IXafEntityObject.OnCreated) method intended for object initialization. The **OnCreated** method is called only once for an object - after the object is created. Whenever you need to initialize an object, place the initialization code into the **OnCreated** method body. The following code snippet demonstrates how simple value properties can be initialized.

```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.BaseImpl.EF;
// ...
public class Contact : IXafEntityObject {
    //...
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    public virtual TitleOfCourtesy TitleOfCourtesy { get; set; }
    public virtual IList<PhoneNumber> PhoneNumbers { get; set; } = new ObservableCollection<PhoneNumber>();
    //...
    void IXafEntityObject.OnCreated() {
        FirstName = "Sam";
        TitleOfCourtesy = TitleOfCourtesy.Mr;
    }
    void IXafEntityObject.OnLoaded() { }
    void IXafEntityObject.OnSaving() { }
}

public class PhoneNumber : BaseObject {
    public virtual string Number { get; set; }
	public virtual string PhoneType { get; set; }
    public virtual Contact Contact { get; set; }
    // ...
}

public enum TitleOfCourtesy {
    Dr,
    Miss,
    Mr,
    Mrs,
    Ms
};

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
You can also inherit your class from  the [DevExpress.Persistent.BaseImpl.EF.BaseObject](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) class that implements the `IXafEntityObject` interface:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.BaseImpl.EF;
using MainDemo.Module.BusinessObjects;
using System.Collections.ObjectModel;
public class ContactBase2 : BaseObject {
    //...
    public virtual string FirstName { get; set; }
    public virtual string LastName { get; set; }
    public virtual TitleOfCourtesy TitleOfCourtesy { get; set; }
    public virtual IList<PhoneNumber> PhoneNumbers { get; set; } = new ObservableCollection<PhoneNumber>();
    //...
    public override void OnCreated() {
        FirstName = "Sam";
        TitleOfCourtesy = TitleOfCourtesy.Mr;
    }
}
```


To see another example of initializing a simple property, refer to the [Initialize Business Object Properties (EF Core)](xref:402982) tutorial lesson.

## Reference Property
Initialization of reference properties differs from initialization of simple properties, primarily in that you may need to obtain a reference to an existing object. For this purpose, use the [IObjectSpace.FindObject](xref:DevExpress.ExpressApp.IObjectSpace.FindObject*)  method of the object's [Object Space](xref:113707). To access the Object Space from the business object code, you should support the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface.

[!include[](~/templates/createobjectinefcore.md)]

## Collection Property
The following code snippet demonstrates how to populate the Phones collection with predefined phone numbers.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.BaseImpl.EF;
using MainDemo.Module.BusinessObjects;
using System.Collections.ObjectModel;
//...
public class Contact : IXafEntityObject {
    //...
    void IXafEntityObject.OnCreated() {
        // ...
        PhoneNumber phone1 = ObjectSpace.FirstOrDefault<PhoneNumber>(
            n => n.Number == "555-0101");
        PhoneNumber phone2 = ObjectSpace.FirstOrDefault<PhoneNumber>(
            n => n.Number == "555-0102");
        if(phone1 != null) { PhoneNumbers.Add(phone1); }
        if(phone2 != null) { PhoneNumbers.Add(phone2); }
    }
    [Aggregated]
    public virtual IList<PhoneNumber> PhoneNumbers { get; set; } = new ObservableCollection<PhoneNumber>();
    void IXafEntityObject.OnLoaded() { }
    void IXafEntityObject.OnSaving() { }

    IObjectSpace ObjectSpace {
        get { return ((IObjectSpaceLink)this).ObjectSpace; }
    }
}

```

You can also create a **BaseObject** descendant:

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.BaseImpl.EF;
using MainDemo.Module.BusinessObjects;
using System.Collections.ObjectModel;
//...
public class ContactBase : BaseObject {
    //...
    public override void OnCreated() {
        // ...
        PhoneNumber phone1 = ObjectSpace.FirstOrDefault<PhoneNumber>(
            n => n.Number == "555-0101");
        PhoneNumber phone2 = ObjectSpace.FirstOrDefault<PhoneNumber>(
            n => n.Number == "555-0102");
        if(phone1 != null) { PhoneNumbers.Add(phone1); }
        if(phone2 != null) { PhoneNumbers.Add(phone2); }
    }
    [Aggregated]
    public virtual IList<PhoneNumber> PhoneNumbers { get; set; } = new ObservableCollection<PhoneNumber>();
}
```

## Calculated Property
A calculated property value is automatically updated when the associated property values are changed. To learn how to implement a regular calculated property, refer to the [](xref:404195) tutorial lesson. To learn how to implement a calculated property based on property values of the objects contained in a child object collection. <!--Refer to the [How to: Calculate a Property Value Based on Values from a Detail Collection](xref:113179) help topic.-->

## Initialize an Object Created via the New Action
In certain scenarios, you may need to initialize only objects created specifically via the **New** [Action](xref:112622). To learn how to do this, refer to the [How to: Initialize an Object Created Using the New Action](xref:112912) help topic.

## Initialize a Property of a Child Object with a Value Taken from a Master Object
You can set the default value for the child object's property within the setter of a property that refers to the master object.
 
# [C#](#tab/tabid-csharp)

```csharp
public class ChildObject {
    // ...
    public virtual MasterObject MasterObject {
        get { return masterObject; }
        set {
            if (master == value) return;
            masterObject = value;
            if (value != null) {
                this.SomeProperty = value.DefaultForChildren;
            }
        }
    }
}
```

***

Since the reference property of a child object will not be initialized until committing changes, it is necessary to use a [](xref:DevExpress.ExpressApp.ViewController) to initialize the child object depending on the master object (see [How to: Initialize an Object Created Using the New Action](xref:112912)).
