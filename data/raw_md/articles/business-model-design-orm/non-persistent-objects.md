---
uid: "116516"
title: Non-Persistent Objects
owner: Ekaterina Kiseleva
seealso:
  - linkId: "116106"
  - linkId: DevExpress.ExpressApp.SystemModule.LinkUnlinkController.RequirePersistentType
  - linkType: HRef
    linkId: https://www.youtube.com/watch?v=RUyXX2pJcjM&t=1740s
    altText: 'Cross-Platform .NET App UI: Data Access in DevExpress XAF & ORM-related Performance Considerations'
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/xaf-how-to-show-persistent-objects-in-a-non-persistent-objects-view
    altText: Example - How to show persistent objects in a non-persistent object's view
  - linkType: HRef
    linkId: https://github.com/DevExpress-Examples/XAF-CRUD-for-Non-Persistent-Objects-Stored-Remotely
    altText: 'GitHub Example: XAF - How to Implement CRUD Operations for Non-Persistent Objects Stored Remotely'
---
# Non-Persistent Objects

A non-persistent class is a type of [business class](xref:113664). XAF generates a UI for this class but does not bind it to an application's database table. You can use this class to display a [List or Detail View](xref:112611) with temporary data generated in code or loaded from storage. You can also use it to display an empty View (dialog) and process the user's input.

## Important Notes

* Do not inherit a non-persistent class from an XPO persistent class (including [Base Persistent Classes](xref:113146)). Otherwise, the [](xref:DevExpress.Xpo.Exceptions.SessionMixingException) or [ObjectDisposedException](xref:System.ObjectDisposedException) can occur in your application because the `NonPersistentObjectSpace` and `NonPersistentObjectSpaceProvider` are designed to work with a [Session](xref:DevExpress.Xpo.Session).
* Do not use the [](xref:DevExpress.Xpo.NonPersistentAttribute) to make a class non-persistent. For this purpose, apply the [](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) to a [POCO](https://en.wikipedia.org/wiki/Plain_Old_CLR_Object) class as shown in the [Basic Non-Persistent Class Implementation](#basic-non-persistent-class-implementation) section. 
* The [Type permissions](xref:404633#type-permissions) list does not include non-persistent object types and everyone can access them. Refer to the [Restrict Non-Persistent Types Access](xref:404633#restrict-non-persistent-types-access) section to learn how to include these types in the **Type permissions** list.

## Basic Non-Persistent Class Implementation
In the [module project](xref:118045), declare a regular class and add the [](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) to implement a non-persistent class. 

You can inherit your class from the following classes that implement the [INotifyPropertyChanged](xref:System.ComponentModel.INotifyPropertyChanged) and [](xref:DevExpress.ExpressApp.IXafEntityObject) interfaces and support [Custom Fields](xref:113583):

| Class | Implements IObjectSpaceLink | Contains the Auto-Generated Primary Key Property |
|---|:---:|:---:|
| `NonPersistentBaseObject` | Yes | Yes, Oid (Guid type) |
| `NonPersistentLiteObject` | No | Yes, Oid (Guid type) |
| `NonPersistentObjectImpl` | Yes | No |
| `NonPersistentEntityObject` | No | No |


> [!NOTE]
> [!include[NonPersistentObjectsWithIObjectSpaceLink](~/templates/NonPersistentObjectsWithIObjectSpaceLink.md)]

The following code example shows how to implement a non-persistent class:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
// ...
[DomainComponent]
public class MyNonPersistentObject : NonPersistentBaseObject {
    private String name;
    private String description;
    public override void OnSaving() {
        base.OnSaving();
        // ...
    }
    public String Name {
        get { return name; }
        set { SetPropertyValue(ref name, value); }
    }
    public String Description {
        get { return description; }
        set { SetPropertyValue(ref description, value); }
    }
}
```

***

XAF automatically registers the class with this attribute in the [Types Info Subsystem](xref:113669) and adds it to the [Application Model](xref:112579). Rebuild the solution and open the [Model Editor](xref:112582) to ensure that XAF added the class to the **BOModel** node and created the corresponding List and Detail Views.

![NonPersistentObjectModel](~/images/nonpersistentobjectmodel124023.png)

XAF can display this `MyNonPersistentObject` Detail View in a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) popup dialog. See the following help topic for details: [](xref:402158).

![MyNonPersistentObjectPopup](~/images/mynonpersistentobjectpopup124025.png)

You can also use the [](xref:DevExpress.Persistent.Base.ActionAttribute) to show a non-persistent object's popup. For this purpose, apply this attribute to a business class method that takes a non-persistent type parameter.

### Examples:

* [How to: Create an Action Using the Action Attribute](xref:112619)
* [How to: Display a List of Non-Persistent Objects in a Popup Dialog](xref:113167)
* [How to: Display and Edit Simple Type Values in a Lookup Property Editor](xref:403100)

## Non-Persistent Object Space

@DevExpress.ExpressApp.NonPersistentObjectSpace is an [Object Space](xref:113707) for managing non-persistent object instances in your application. You can create, read, or update these objects in code if your @DevExpress.ExpressApp.XafApplication supports this Object Space type. The [Template Kit](xref:405447) automatically registers the non-persistent Object Space Provider, but for projects created with older XAF versions, you need to register it manually. Call the [AddNonPersistent](xref:DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderBuilderExtensions.AddNonPersistent``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{``0},System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderOptions})) method in the @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder.ObjectSpaceProviders property.

# [MySolution.Blazor.Server/Startup.cs | MySolution.Win/Startup.cs | MySolution.WebApi/Startup.cs](#tab/tabid-csharp)

```csharp
builder.ObjectSpaceProviders
    // ...
    .AddNonPersistent();
// ...
```

***

### Common Information

[!include[](~/templates/objectspaceprovidersorder.md)]

> [!IMPORTANT]
> `NonPersistentObjectSpace` cannot handle persistent objects. To process these objects, create an additional Object Space for the persistent object type and add it to the [NonPersistentObjectSpace.AdditionalObjectSpaces](xref:DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces) collection. For more information, refer to the following help topic: [How to: Show Persistent Objects in a Non-Persistent Object's View](xref:116106). 
>
> Also, note that you may need to refresh and dispose of Object Spaces from this collection and the parent non-persistent Object Space simultaneously. To do this automatically, use the following properties and fields:
> * @DevExpress.ExpressApp.CompositeObjectSpace.AutoRefreshAdditionalObjectSpaces / @DevExpress.ExpressApp.CompositeObjectSpace.AutoRefreshAdditionalObjectSpacesByDefault
> * @DevExpress.ExpressApp.CompositeObjectSpace.AutoDisposeAdditionalObjectSpaces / @DevExpress.ExpressApp.CompositeObjectSpace.AutoDisposeAdditionalObjectSpacesByDefault

Use the [](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)) method to create an Object Space and manage non-persistent objects in your code (for example, in the [Controller](xref:112621)'s code):

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
// ...
public class ShowDetailViewController : ViewController<ListView> {
    // ...
    void showDetailViewAction_CustomizePopupWindowParams(
        object sender, CustomizePopupWindowParamsEventArgs e) {
        IObjectSpace newObjectSpace = Application.CreateObjectSpace(typeof(NonPersistentObject));
        // ...
    }
}
```

***

When you create a `NonPersistentObjectSpace` instance in a Controller (for example, to show a custom dialog), you can customize it in the Controller's code.

To specify default settings for all [NonPersistentObjectSpaces](xref:DevExpress.ExpressApp.NonPersistentObjectSpace) in your application, handle the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event in the application builder code within the application's `Startup.cs` file and subscribe to the required [`NonPersistentObjectSpace`](xref:DevExpress.ExpressApp.NonPersistentObjectSpace) events:

    **File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp;
    // ...
    builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
        NonPersistentObjectSpace nonPersistentObjectSpace = context.ObjectSpace as NonPersistentObjectSpace;
        if(nonPersistentObjectSpace != null) {
            // Subscribe to NonPersistentObjectSpace events and customize their properties
        }
    };
    // ...
    ```

    ***

To supply data to non-persistent objects, handle the following `NonPersistentObjectSpace` events raised when the Object Space loads non-persistent objects:

* [NonPersistentObjectSpace.ObjectGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectGetting)
* [NonPersistentObjectSpace.ObjectsGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting)
* [NonPersistentObjectSpace.ObjectByKeyGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectByKeyGetting)

Since these events are raised to request any non-persistent object (declared in custom or built-in Modules), check the object type passed in event parameters before modifying the events' output parameters.

You can use the **New**, **Delete**, and **Save** Actions to manipulate non-persistent objects. The [NonPersistentObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ModifiedObjects) collection contains all modified objects. Newly created and deleted objects are added to this collection automatically. To add an existing object to this collection, use the [IObjectSpace.SetModified(Object)](xref:DevExpress.ExpressApp.IObjectSpace.SetModified*) method. If an object implements the @System.ComponentModel.INotifyPropertyChanged interface, you can set @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChange or @DevExpress.ExpressApp.NonPersistentObjectSpace.AutoSetModifiedOnObjectChangeByDefault to `true` to add this object to the @DevExpress.ExpressApp.IObjectSpace.ModifiedObjects collection automatically when its property is changed.

### Examples

* [How to: Display a Non-Persistent Object's List View from the Navigation](xref:114052)
* [How to: Display a Non-Persistent Object's Detail View from the Navigation](xref:113471)
* [How to: Perform CRUD Operations with Non-Persistent Objects](xref:115672)
* [How to: Display Non-Persistent Objects in a Report](xref:114516)

## Key Property
Key properties are required in ASP.NET Core Blazor applications. Use the [](xref:DevExpress.ExpressApp.Data.KeyAttribute) to declare a key property.

The following code snippet demonstrates how to declare a key property in a non-persistent class. The [BrowsableAttribute](xref:System.ComponentModel.BrowsableAttribute) hides this property from the UI.

# [C#](#tab/tabid-csharp)

```csharp
[DomainComponent]
public class NonPersistentObject {
    [Browsable(false)]
    [DevExpress.ExpressApp.Data.Key]
    public int Oid { get; set; }
    // ...
}
```

***

> [!IMPORTANT]
> Use the `Key` attribute from the `DevExpress.ExpressApp.Data` namespace only (not from the [System.ComponentModel.DataAnnotations](xref:System.ComponentModel.DataAnnotations) or [](xref:DevExpress.Xpo) namespace).

You can also inherit the non-persistent class from `NonPersistentBaseObject` or `NonPersistentLiteObject` that implements the read-only `Oid` key property of the `Guid` type. This key is initialized with a random value in a constructor.

You can allow users to open a specific non-persistent object instance from the [Navigation](xref:113198):

1. [Add an item to the navigation](xref:402131). Set its [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) property to the identifier of the non-persistent object's DetailView and the [IModelNavigationItem.ObjectKey](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.ObjectKey) property to an arbitrary integer value.

   ![NonPersistentKey](~/images/nonpersistentkey123148.png)

2. Subscribe to the [NonPersistentObjectSpace.ObjectByKeyGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectByKeyGetting) event handler. Find an object instance whose type matches the event's `e.ObjectType` parameter and whose key value coincides with the `e.Key` parameter. Pass this object to the event's `e.Object` parameter.

**Example:** [How to: Display a Non-Persistent Object's Detail View from the Navigation](xref:113471)

## Filter and Sort Non-Persistent Objects

You can use the `DevExpress.ExpressApp.DynamicCollection` to filter and sort a collection of non-persistent objects. Follow the steps below to do this.

1. Handle the [NonPersistentObjectSpace.ObjectsGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting) event.
2. In this event handler, create a new `DynamicCollection` and subscribe to its `FetchObjects` event. This event is raised after sort or filter parameters are changed or the collection is reloaded.
3. Pass a list of non-persistent objects to the _Objects_ event argument. You can filter and sort this list based on event arguments; to do this automatically, set the `ShapeData` argument to `true`.
4. Pass the `DynamicCollection` instance to the `NonPersistentObjectSpace.ObjectsGetting` event's `Objects` argument.

The following code demonstrates how you can implement it in a _.NET_ application:

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Collections.Generic;
using DevExpress.ExpressApp;
// ...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
    NonPersistentObjectSpace nonPersistentObjectSpace = context.ObjectSpace as NonPersistentObjectSpace;
    if (nonPersistentObjectSpace != null) {
        nonPersistentObjectSpace.ObjectsGetting += NonPersistentObjectSpace_ObjectsGetting;
    }
};
// ...
private void NonPersistentObjectSpace_ObjectsGetting(object sender, ObjectsGettingEventArgs e) {
    if (e.ObjectType == typeof(Contact)) {
        DynamicCollection collection = new DynamicCollection((IObjectSpace)sender, e.ObjectType, e.Criteria, e.Sorting, e.InTransaction);
        collection.FetchObjects += DynamicCollection_FetchObjects;
        e.Objects = collection;
    }
}
private void DynamicCollection_FetchObjects(object sender, FetchObjectsEventArgs e) {
    if (e.ObjectType == typeof(Contact)) {
        e.Objects = contacts; // Your collection of non-persistent objects.
        e.ShapeData = true; // Set to true if the supplied collection is not already filtered and sorted.
    }
}
```

***

To see the full example, refer to the following GitHub repository: [How to filter and sort Non-Persistent Objects](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Filtering-Demo).

If users can create new objects in Lookup List Views, cache the collection that the `DynamicCollection.FetchObjects` event returns. Otherwise, newly added objects disappear from the Lookup List View after it is reopened. The following GitHub repository shows how to do this: [How to edit Non-Persistent Objects nested in a Persistent Object](https://github.com/DevExpress-Examples/XAF_Non-Persistent-Objects-Nested-In-Persistent-Objects-Demo).


## INotifyPropertyChanged Support
All of the base non-persistent classes listed above implement [INotifyPropertyChanged](xref:System.ComponentModel.INotifyPropertyChanged). To use this interface's functionality, declare property setters as follows:

```csharp{10}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
// ...
[DomainComponent]
public class MyNonPersistentObject : NonPersistentBaseObject {
    //... 
    private String description;
    public String Description {
        get { return description; }
        set { SetPropertyValue(ref description, value); }
    }
}
```

If you do not use base classes, implement the [INotifyPropertyChanged](xref:System.ComponentModel.INotifyPropertyChanged) interface in your non-persistent class to use XAF features that track and handle property value changes (for example, [Conditional Appearance](xref:113286)). Call the `OnPropertyChanged` method from the property setter to trigger the [PropertyChanged](xref:System.ComponentModel.INotifyPropertyChanged.PropertyChanged) event. The Object Space handles this event internally. Then the `PropertyChanged` event triggers the [IObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.IObjectSpace.ObjectChanged) event.  

**Example:** [How to: Perform CRUD Operations with Non-Persistent Objects](xref:115672) | [](xref:117395)

## IXafEntityObject and IObjectSpaceLink Support
Implement the [](xref:DevExpress.ExpressApp.IXafEntityObject) interface to add custom business logic to the non-persistent class code. This interface declares the `OnCreated` and `OnSaved` methods that are called when the Object Space creates or saves an object. You can also implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface and use the Object Space that the [IObjectSpaceLink.ObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceLink.ObjectSpace) property returns. This allows you to [query other objects](xref:113711) in the same and additional Object Spaces.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
[DomainComponent]
public class MyNonPersistentObject : IXafEntityObject, IObjectSpaceLink{
    // ...
    void IXafEntityObject.OnCreated() {
        // Place the entity initialization code here.
        // You can use Object Space methods, for example, to initialize reference properties:
        // this.Address = objectSpace.CreateObject<Address>();
    }
    void IXafEntityObject.OnLoaded() {
        // Place the code that is executed each time the entity is loaded here. Explicitly call this method in your code if needed.
    }
    void IXafEntityObject.OnSaving() {
        // Place the code that is executed each time the entity is saved here.
    }
    IObjectSpace IObjectSpaceLink.ObjectSpace {
        get { return objectSpace; }
        set { objectSpace = value; }
    }
}
```

***

When a non-persistent object contains a reference to one persistent object and another persistent object references this non-persistent object, the [IObjectSpaceLink.ObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceLink.ObjectSpace) property may return an Additional Object Space instead of its owner Object Space. To get the owner Object Space, use the [IObjectSpace.Owner](xref:DevExpress.ExpressApp.IObjectSpace.Owner) property (see the code below):

# [C#](#tab/tabid-csharp)

```csharp
IObjectSpace ownerObjectSpace = (ObjectSpace.Owner as IObjectSpace) ?? ObjectSpace;
```

***

**Example:** [How to: Perform CRUD Operations with Non-Persistent Objects](xref:115672)

## Non-Persistent Object Template
You can use a Visual Studio template to create a non-persistent class. Open the [Template Kit](xref:405447#create-a-new-item) switch to the **XAF** category, and choose the **XAF Business Object** | **Non-Persistent Object** item. The added class can be used in various complex scenarios listed in this topic.

![NonPersistentObjectTemplate](~/images/template-kit/template-kit-add-non-persistent-object.png)

This non-persistent class includes the `IXafEntityObject`, `IObjectSpaceLink`, and `INotifyPropertyChanged` interface implementations, and an integer type key property.
