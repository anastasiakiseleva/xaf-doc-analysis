---
uid: "116106"
title: "How to: Show Persistent Objects in a Non-Persistent Object's View"
seealso:
  - linkId: '403100'
    altText: "Show Non-Persistent Objects in a Persistent Object's View"
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/xaf-how-to-show-persistent-objects-in-a-non-persistent-objects-view
    altText: Example - How to show persistent objects in a non-persistent object's view
---
# How to: Show Persistent Objects in a Non-Persistent Object's View

This topic describes how to declare a [reference](xref:113572) or [collection](xref:113568) property of a persistent type in a [non-persistent class](xref:116516) and display it in the UI.

## Persistent Reference Property
Implement the following non-persistent class:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
[DomainComponent, DefaultClassOptions]
public class NonPersistentObject {
    // ...
    public string Name { get; set; }
    public Person Owner { get; set; }
    // ...
}
```

***

> [!NOTE]
> [!include[NonPersistent_RecommendedInterfaces](~/templates/nonpersistent_recommendedinterfaces111883.md)]

> [!TIP]
> Use the approach demonstrated in the following topic to support save and load operations for non-persistent objects: [How to: Perform CRUD Operations with Non-Persistent Objects](xref:115672).

In this example, `Person` is a persistent class from the [Business Class Library](xref:112571). You can use a custom business class instead of `Person`.

Run the application and create a new `NonPersistentObject`. In its Detail View, the lookup editor for the `Owner` property is empty and you cannot choose an existing `Person`.

![PersistentInNonPresistent1](~/images/persistentinnonpresistent1123201.png)

The [](xref:DevExpress.ExpressApp.NonPersistentObjectSpace) created for the current View cannot process the `Person` persistent object. Follow the steps below to create a persistent Object Space for this type.

[!include[<an additional Object Space that can handle the `Person` type>](~/templates/PopulateAdditionalObjectSpace_example.md)]

The image below demonstrates the result.

![PersistentInNonPresistent2](~/images/persistentinnonpresistent2123202.png)

## Persistent Collection
You can add the `Owners` collection instead of the `Owner` reference property, as shown in the code snippet below.

# [C#](#tab/tabid-csharp)

```csharp
[DomainComponent, DefaultClassOptions]
public class NonPersistentObject{
    // ... 
    public string Name { get; set; }
    private IList<Person> owners = new List<Person>();
    public IList<Person> Owners {
        get {
            return owners;
        }
    }
}
```

***

To allow users to add and remove `Owners` with the `Link` and `Unlink` Actions, create an additional Object Space for the `Person` type, as demonstrated in the [previous section](#persistent-reference-property).

![Link action](~/images/persistentinnonpresistent_collection129583.png)

For a more complex example, refer to the following GitHub repository: [How to edit a collection of persistent objects linked to a non-persistent object](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Edit-Linked-Persistent-Objects-Demo).

## Initialize Persistent Property Values
Implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface in your non-persistent class and use the [IObjectSpace.GetObjects\<T>](xref:DevExpress.ExpressApp.IObjectSpace.GetObjects*) method to get persistent objects.

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
[DomainComponent, DefaultClassOptions]
public class NonPersistentObject : IObjectSpaceLink {
    public string Name { get; set; }
    private Person owner;
    public Person Owner {
        get {
            if (owner == null) {
                owner = ObjectSpace.GetObjects<Person>(CriteriaOperator.Parse("FirstName='Sam'")).FirstOrDefault();
            }
            return owner;
        }
        set { owner = value; }
    }
    private IList<Person> owners;
    public IList<Person> Owners {
        get {
            if (owners == null) {
                owners = ObjectSpace.GetObjects<Person>(CriteriaOperator.Parse("StartsWith(FirstName, 'B')")) ;
            }
            return owners;
        }
        internal set { owners = value; }
    }
    private IObjectSpace objectSpace;
    [Browsable(false)]
    public IObjectSpace ObjectSpace {
        get { return objectSpace; }
        set { objectSpace = value; }
    }
}
```

***

If you create a new `NonPersistentObject` in the UI, its `Owner` property and `Owner` collection are initialized.

![Non Persistent Object in UI](~/images/persistentinnonpresistent_init129584.png)

## Refresh Linked Persistent Objects

The [Refresh](xref:DevExpress.ExpressApp.SystemModule.RefreshController.RefreshAction) Action does not affect non-persistent object Views. Follow the steps below to allow non-persistent objects and persistent objects linked to them to reload.

1. Access the @DevExpress.ExpressApp.NonPersistentObjectSpace and set its @DevExpress.ExpressApp.CompositeObjectSpace.AutoRefreshAdditionalObjectSpaces property to `true`.
2. Subscribe to the [NonPersistentObjectSpace.ObjectGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectGetting) event. In the event handler, create a new instance of the non-persistent object and copy property values from the source object. To create copies of persistent objects linked to non-persistent objects, use the [IObjectSpace.GetObject](xref:DevExpress.ExpressApp.IObjectSpace.GetObject*) method.

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using System.ComponentModel;
// ...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
    CompositeObjectSpace compositeObjectSpace = context.ObjectSpace as CompositeObjectSpace;
    if (compositeObjectSpace != null) {
        if (!(compositeObjectSpace.Owner is CompositeObjectSpace)) {
            var objectSpaceProviderService = context.ServiceProvider.GetRequiredService<IObjectSpaceProviderService>();
            var objectSpaceCustomizerService = context.ServiceProvider.GetRequiredService<IObjectSpaceCustomizerService>();
            compositeObjectSpace.PopulateAdditionalObjectSpaces(objectSpaceProviderService, objectSpaceCustomizerService);
        }
    }
    NonPersistentObjectSpace nonPersistentObjectSpace = e.ObjectSpace as NonPersistentObjectSpace;
    if (nonPersistentObjectSpace != null) {
        nonPersistentObjectSpace.AutoRefreshAdditionalObjectSpaces = true;
        nonPersistentObjectSpace.ObjectGetting += NonPersistentObjectSpace_ObjectGetting;
    }
}
// ...
private void NonPersistentObjectSpace_ObjectGetting(object sender, ObjectGettingEventArgs e) {
    var objectSpace = (IObjectSpace)sender;
    if (e.SourceObject is NonPersistentObject) {
        var sourceObject = (NonPersistentObject)e.SourceObject;
        var targetObject = new NonPersistentObject();
        targetObject.Owner = objectSpace.GetObject<Person>(sourceObject.Owner);
        var owners = new List<Person>();
        foreach (var owner in sourceObject.Owners) {
            owners.Add(objectSpace.GetObject<Person>(owner));
        }
        targetObject.Owners = owners;
        e.TargetObject = targetObject;
    }
}
```

***

If you modify and save a `Person` in another View or in a database while the `NonPersistentObject` Detail View is open, click the [Refresh](xref:DevExpress.ExpressApp.SystemModule.RefreshController.RefreshAction) Action to refresh data in this View.

For a more complex example of a non-persistent object with linked persistent objects, refer to the following GitHub example: [How to refresh Non-Persistent Objects and reload nested Persistent Objects](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Reloading-Demo).

## Important Notes

[!include[DoNotShareNonPersistentObjects-note](~/templates/DoNotShareNonPersistentObjects-note.md)]

[`DomainComponent`]: xref:DevExpress.ExpressApp.DC.DomainComponentAttribute
[`DefaultClassOptions`]: xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute
[`IObjectSpaceLink`]: xref:DevExpress.ExpressApp.IObjectSpaceLink
[`IObjectSpace`]: xref:DevExpress.ExpressApp.IObjectSpace
[`GetObjects`]: xref:DevExpress.ExpressApp.IObjectSpace.GetObjects``1(DevExpress.Data.Filtering.CriteriaOperator)
[`CriteriaOperator`]: xref:DevExpress.Data.Filtering.CriteriaOperator
[`/\.(ObjectSpaceCreated)/`]: xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated
[`CompositeObjectSpace`]: xref:DevExpress.ExpressApp.CompositeObjectSpace 
[`AutoRefreshAdditionalObjectSpaces`]: xref:DevExpress.ExpressApp.CompositeObjectSpace.AutoRefreshAdditionalObjectSpaces
[`/\.(ObjectGetting)/`]: xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectGetting
[`ObjectSpaceCreatedEventArgs`]: xref:DevExpress.ExpressApp.ObjectSpaceCreatedEventArgs
[`PopulateAdditionalObjectSpaces`]: xref:DevExpress.ExpressApp.CompositeObjectSpace.PopulateAdditionalObjectSpaces(DevExpress.ExpressApp.XafApplication)
[`GetObject`]: xref:DevExpress.ExpressApp.IObjectSpace.GetObject``1(``0)
