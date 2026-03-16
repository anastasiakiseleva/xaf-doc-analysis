---
uid: "113707"
seealso:
- linkId: "117395"
title: Ways to Access an Object Space (the Database Context for CRUD Operations)
owner: Ekaterina Kiseleva
---
# Ways to Access an Object Space (the Database Context for CRUD Operations)

In XAF applications, all data-aware manipulations and custom business logic are performed via the Object Space. The Object Space is an abstraction on the database context. The Object Space allows you to query or edit data in the transaction. Object Space is an ORM-independent implementation of the well-known [Repository](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff649690(v=pandp.10)) and [Unit Of Work](https://learn.microsoft.com/en-us/archive/msdn-magazine/2009/june/the-unit-of-work-pattern-and-persistence-ignorance) design patterns.

Object Space members are declared in the [](xref:DevExpress.ExpressApp.IObjectSpace) interface. The @DevExpress.ExpressApp.BaseObjectSpace and @DevExpress.ExpressApp.CompositeObjectSpace classes implement the common code. XAF includes the following **CompositeObjectSpace** descendants:

* [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace) - used to access data via a [](xref:DevExpress.Xpo.Session) when the [XPO](xref:112600) data model is used.
* [](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace) - used to access data via a [DbContext](xref:Microsoft.EntityFrameworkCore.DbContext) when the [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core) data model is used.
* [](xref:DevExpress.ExpressApp.NonPersistentObjectSpace) - used to manage [non-persistent objects](xref:116516) that are not mapped to the database.

![ObjectSpaceDiagram](~/images/objectspacediagram117624.png)

In most cases, you will access Object Space via the [](xref:DevExpress.ExpressApp.IObjectSpace) interface and do not need to use these classes directly.

When implementing custom business logic ([](xref:113711)), [Object Space](xref:113707) is required if data the current business object exposes is insufficient for your logic, and you need to query more data. You may also use Object Space in your database initialization code, in complex [View Items](xref:112612), etc. This topic describes the API you can use to get Object Space in various contexts.

Once you have obtained or created an Object Space, you can use it to query or modify data (see [Create, Read, Update and Delete Data](xref:113711)).

## Get an Existing Object Space

XAF creates Object Spaces for each View in an application. To load data or perform custom logic with already loaded objects, use the approaches from the list below to get an Object Space from various contexts of your code.

### Get an Existing Object Space in a Controller

In XAF applications, an Object Space is automatically assigned for each [View](xref:112611). XAF Views listen to events of the Object Space assigned to a View. In a View Controller, you can access the Object Space with the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace). You can also use the protected **ViewController.ObjectSpace** property that refers to the same Object Space as **View.ObjectSpace**. A Window Controller does not expose a View directly. You can access the current [Frame](xref:112608) using the [Controller.Frame](xref:DevExpress.ExpressApp.Controller.Frame) property and get the View with [Frame.View](xref:DevExpress.ExpressApp.Frame.View). 

The previous options are suitable only for the simplest data manipulations that use an Object Space (for instance, modify a property of a current View object and commit changes). To process large amounts of data or create a new View with the [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*) or [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) methods, [create a new Object Space](#create-a-new-object-space) that is not bound to a current View instead of using the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property.

For more information on how to get an Object Space in an ASP.NET Core Controller, refer to the following section: [Create a New Object Space in Advanced ASP.NET Core Scenarios](#create-a-new-object-space-in-advanced-aspnet-core-scenarios).

**See also:** 
* [](xref:402156)
* [](xref:402158)
* [Add an Action with Option Selection](xref:402159)
* [IObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.IObjectSpace.ObjectChanged)

### Get an Existing Object Space in Business Object

#### In a EF Core Business Class

Classes that implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface can access an `IObjectSpace` object with the `IObjectSpaceLink.ObjectSpace` property.

Persistent EF Core classes implement the `IObjectSpace` interface at runtime. You can also use EF Core classes to implement this interface in following ways:
- Implement the `IObjectSpaceLink` interface.
- Inherit from the [DevExpress.Persistent.BaseImpl.EF.BaseObject](xref:DevExpress.Persistent.BaseImpl.EF.BaseObject) class.
- Use the DevExpress [Template Kit](xref:405447#create-a-new-item) to add a new **EF Core Business Object** that supports both `IXafEntityObject` and `IObjectSpaceLink` in your project.

If you additionally implement an [](xref:DevExpress.ExpressApp.IXafEntityObject), then you can place your logic into the [IXafEntityObject.OnCreated](xref:DevExpress.ExpressApp.IXafEntityObject.OnCreated), [IXafEntityObject.OnLoaded](xref:DevExpress.ExpressApp.IXafEntityObject.OnLoaded) and [IXafEntityObject.OnSaving](xref:DevExpress.ExpressApp.IXafEntityObject.OnSaving) methods. You can use the DevExpress [Template Kit](xref:405447#create-a-new-item) to add a new **EF Core Business Object** that supports both `IXafEntityObject` and `IObjectSpaceLink` in your project.

#### In an XPO Business Class
You do not need an Object Space inside a persistent class. Do not implement the **IObjectSpaceLink** and **IXafEntityObject** interfaces in this context. Instead, use the **Session** property and override the **AfterConstruction**, **OnLoaded**, and **OnSaving** methods respectively in an XPO class. For more information, review the following code diagnostics: [XAF0023](xref:404104) | [XAF0024](xref:404105).

#### In a Non-Persistent Business Class

Classes that implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface can access an `IObjectSpace` object with the `IObjectSpaceLink.ObjectSpace` property. To use this interface in non-persistent classes, use one of the following techniques:
- Implement this interface.
- Inherit from a base non-persistent class: [Basic Non-Persistent Class Implementation](xref:116516#basic-non-persistent-class-implementation)

**See also:** 
 - [](xref:DevExpress.ExpressApp.IObjectSpaceLink) | [](xref:DevExpress.ExpressApp.IXafEntityObject)
 - [](xref:DevExpress.Xpo.PersistentBase.Session) | [](xref:DevExpress.Xpo.PersistentBase.AfterConstruction) | [](xref:DevExpress.Xpo.PersistentBase.OnSaving)

### Get an Existing Object Space in a Module Updater

In a [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) descendant, you can use the protected **ModuleUpdater.ObjectSpace** property to access the Object Space instance that can be used for database update operations. Do not use a new Object Space to update the database.


**See also:** 
* [Supply Initial Data (EF Core)](xref:113631&t=21.2)

### Get an Existing Object Space in a List Editor

A reference to the [](xref:DevExpress.ExpressApp.CollectionSourceBase) object is automatically passed to the [IComplexListEditor.Setup](xref:DevExpress.ExpressApp.Editors.IComplexListEditor.Setup(DevExpress.ExpressApp.CollectionSourceBase,DevExpress.ExpressApp.XafApplication)) method if your custom [List Editor](xref:113189) supports the [](xref:DevExpress.ExpressApp.Editors.IComplexListEditor) interface. You can implement this interface and access the Object Space via the [CollectionSourceBase.ObjectSpace](xref:DevExpress.ExpressApp.CollectionSourceBase.ObjectSpace) property.


### Get an Existing Object Space in a View Item or a Property Editor

A reference to an Object Space is automatically passed to the [IComplexViewItem.Setup](xref:DevExpress.ExpressApp.Editors.IComplexViewItem.Setup(DevExpress.ExpressApp.IObjectSpace,DevExpress.ExpressApp.XafApplication)) method if your custom [View Item](xref:112612) or [Property Editor](xref:113097) supports the [](xref:DevExpress.ExpressApp.Editors.IComplexViewItem) interface. You can implement this interface and store the Object Space reference to a local variable for future use.


**See also:** [](xref:DevExpress.ExpressApp.Editors.IComplexViewItem)


### Access Object Space in Events

Object Space is also available using arguments passed to various events of the [](xref:DevExpress.ExpressApp.XafApplication) class.

| Event | Object Space Parameter |
|---|---|
| [XafApplication.CreateCustomCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreateCustomCollectionSource) | [CreateCustomCollectionSourceEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.CreateCustomCollectionSourceEventArgs.ObjectSpace) |
| [XafApplication.CreateCustomLogonWindowObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonWindowObjectSpace) | [CreateCustomPropertyCollectionSourceEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.CreateCustomPropertyCollectionSourceEventArgs.ObjectSpace) |
| [XafApplication.CreateCustomPropertyCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreateCustomPropertyCollectionSource) | [CreateCustomLogonWindowObjectSpaceEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.CreateCustomLogonWindowObjectSpaceEventArgs.ObjectSpace) |
| [XafApplication.ObjectSpaceCreated](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated) | [ObjectSpaceCreatedEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.ObjectSpaceCreatedEventArgs.ObjectSpace) |
| [XafApplication.ViewCreating](xref:DevExpress.ExpressApp.XafApplication.ViewCreating) | [ViewCreatingEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ObjectSpace) |

## Create a New Object Space

Create a new Object Space instance in the following scenarios:
 - You create a View using the [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*) or [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) methods in Controllers, custom List or Property Editors.
 - You need a View that does not react to modifications you perform in your business logic. For example, the Save and Cancel Actions become enabled when there are changes in the View's Object Space, because a View handles Object Space events to update the UI. You need to revert your changes in a separate Object Space without affecting changes in the View's Object Space.
 - You process large amounts of data (for instance, load and modify hundreds of related persistent objects).


> [!NOTE]
> With XPO, when you need to perform a bunch of operations, but avoid immediately updating the View's ObjectSpace, create a nested Object Space by using the [IObjectSpace.CreateNestedObjectSpace()](xref:DevExpress.ExpressApp.IObjectSpace.CreateNestedObjectSpace) or [XPObjectSpace.CreateNestedObjectSpace()](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateNestedObjectSpace) methods. When you commit a nested Object Space, changes in it are merged into the parent Object Space and are not persisted in a database. To persist changes in a database, commit the parent Object Space. Nested Object Spaces are implemented based on XPO [NestedUnitOfWork](xref:DevExpress.Xpo.NestedUnitOfWork) and inherit their behavior and specifics.

### Create a New Object Space in a Controller

Use the [XafApplication.CreateObjectSpace(Type)](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)) method to create an Object Space. Refer to the [](xref:DevExpress.ExpressApp.XafApplication) class description to see how to obtain an **XafApplication** instance in various contexts. For instance, the [Controller.Application](xref:DevExpress.ExpressApp.Controller.Application) property is available in a Controller context, and you can create an Object Space as follows:

# [C#](#tab/tabid-csharp)

```csharp
IObjectSpace objectSpace = this.Application.CreateObjectSpace(typeof(MyBusinessClass)); 
```
***

**See also:**

* [](xref:402155)
* [](xref:402158)
* [Add an Action with Option Selection](xref:402159)

### Create a New Object Space in Business Object

In most cases, it is sufficient to [get an existing Object Space](#get-an-existing-object-space) to perform custom logic inside EF Core and Non-Persistent Business Classes. 

You cannot create new Object Spaces in the business object context because an **XafApplication** instance is not available there. It is also NOT possible to access [Views](xref:112611), and other XAF UI-related entities within the business class code, because it violates [the separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) principle and is against the [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) architecture - your data model should not be tied to the UI. To access [](xref:DevExpress.ExpressApp.XafApplication), [Views](xref:112611), and other UI-related entities, implement [Controllers](xref:112621).

### Create a New Object Space in Advanced ASP.NET Core Scenarios

If you need to access an Object Space instance in a custom ASP.NET Core service or middleware, Web API controllers, custom Razor pages, and components, use [Dependency Injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection) to inject the [](xref:DevExpress.ExpressApp.IObjectSpaceFactory) or [](xref:DevExpress.ExpressApp.INonSecuredObjectSpaceFactory) interfaces and invoke their **CreateNonSecuredObjectSpace** method. Refer to the following help articles to find the examples: 
 - [](xref:403669) (XAF UI)
 - [](xref:403861) (Web API Service)

### Create a New Object Space in Non-XAF Apps 
In a non-XAF application, you can instantiate the [Object Space Provider](xref:DevExpress.ExpressApp.IObjectSpaceProvider) manually. Then, you can call the provider’s [CreateObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceProvider.CreateObjectSpace) method to create an Object Space. Refer to the following help article to find the example: [](xref:113709)


> [!IMPORTANT]
> You should manually [dispose](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable) of an Object Space when you are finished using it if you do not assign it to a View. An Object Space associated with a View is removed automatically together with this View.
