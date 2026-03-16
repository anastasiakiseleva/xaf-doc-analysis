---
uid: "113258"
seealso:
- linkId: '403711'
- linkId: '113152'
  altText: How to implement the CreatedBy, CreatedOn and UpdatedBy, UpdatedOn properties in a business class
title: 'Initialize Business Objects with Default Property Values in XPO'
owner: Ekaterina Kiseleva
---
# Initialize Business Objects with Default Property Values in XPO

When designing business classes, a common task is to ensure that a newly created business object is initialized with default property values. This topic explains how different types of properties can be initialized. As an example, a Contact business class will be implemented. After a Contact object is created, its properties will be initialized with default values.

![InitializeObjects_Win](~/images/initializeobjects_win116610.png)

> [!TIP]
> Similar example for EF Core is available in the following help topic: [How to: Initialize Business Objects with Default Property Values in Entity Framework Core](xref:402990)

## Simple Property
All the [base persistent classes](xref:113146) are derived from the [](xref:DevExpress.Xpo.PersistentBase) class. This class exposes the [PersistentBase.AfterConstruction](xref:DevExpress.Xpo.PersistentBase.AfterConstruction) method intended for object initialization. The AfterConstruction method is called only once for an object - after the object is created. Whenever you need to initialize an object, you should override these methods and place the initialization code into its body. As this method is specifically designed for initialization, there is no need to check the current object state when assigning values to the object properties. The following code snippet demonstrates how simple value properties can be initialized.

# [C#](#tab/tabid-csharp)

```csharp
public class Contact : Person {
//...
    public override void AfterConstruction() {
        base.AfterConstruction();

        FirstName = "Sam";
        TitleOfCourtesy = TitleOfCourtesy.Mr;
    }
}
```
***

## Reference Property
Initialization of reference properties differs from initialization of simple properties, primarily in that you may need to obtain a reference to an existing object. For this purpose, use the [Session.FindObject](xref:DevExpress.Xpo.Session.FindObject*) method of the object's [](xref:DevExpress.Xpo.Session).

[!include[](~/templates/createobjectinxpo.md)]

## Collection Property
To populate business object collections, use the [XPCollection.Add](xref:DevExpress.Xpo.XPCollection.Add(System.Object)) method. The following code snippet demonstrates how to populate the Phones collection with predefined phone numbers.

# [C#](#tab/tabid-csharp)

```csharp
public class Contact : Person {
//...
    public override void AfterConstruction() {
        base.AfterConstruction();

        PhoneNumber phone1 = Session.FindObject<PhoneNumber>(CriteriaOperator.Parse(
            "Number = '555-0101'"));
        PhoneNumber phone2 = Session.FindObject<PhoneNumber>(CriteriaOperator.Parse(
            "Number = '555-0102'"));
        PhoneNumbers.Add(phone1);
        PhoneNumbers.Add(phone2);
    }
}
```
***

## Calculated Property
A calculated property value is automatically updated when the associated property values are changed. To learn how to implement a regular calculated property, refer to the [Make a Property Calculable](xref:404195) tutorial lesson. To learn how to implement a calculated property based on property values of the objects contained in a child object collection, refer to the [How to: Calculate a Property Value Based on Values from a Detail Collection](xref:113179) help topic.

## Initialize an Object Created via the New Action
In certain scenarios, you may need to initialize only objects created specifically via the **New** [Action](xref:112622). To learn how to do this, refer to the [How to: Initialize an Object Created Using the New Action](xref:112912) help topic.

## Initialize a Property of a Child Object with a Value Taken from Master Object
You can set the default value for the child object's property within the setter of a property that refers to the master object.

# [C#](#tab/tabid-csharp)

```csharp
public class ChildObject : BaseObject {
    // ...
    public MasterObject MasterObject {
        get { return masterObject; }
        set {
            bool modified = SetPropertyValue(nameof(MasterObject), ref masterObject, value) ;
            if (!IsLoading && !IsSaving && value != null && modified) {
                this.SomeProperty = value.DefaultForChildren;
            }
        }
    }
}
```
***

It is impossible to obtain parent object values in a child object's **AfterConstruction** method because this method is called before any properties are initialized from an outside code. If you need to execute some code according to the assigned parent object, do this either in the **ChildObject.MasterObject** property setter or in the [XPBaseCollection.CollectionChanged](xref:DevExpress.Xpo.XPBaseCollection.CollectionChanged) event handler.
