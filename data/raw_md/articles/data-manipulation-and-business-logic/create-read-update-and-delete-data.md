---
uid: "113711"
title: Create, Read, Update and Delete Data
seealso:
- linkId: "115672"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-import-data-in-xaf
  altText: 'GitHub Example: How to import data in XAF'
---
# Create, Read, Update and Delete Data

You can create a business logic in the following places:

In Controllers

:   You can declare new and customize existing [Actions](xref:112622) and handle other [Controller](xref:112621) events. Once you have obtained or created an Object Space instance (as described in the [](xref:113707) topic), you can use it for data manipulation (create, read, update or delete data). 

In Model (business classes)

:   You can put logic into property getters and setters, implement methods that are triggered automatically when the object is created, loaded, saved, and deleted (see the [](xref:DevExpress.ExpressApp.IXafEntityObject) topic), and declare [action methods](xref:112619).
    
    This topic lists articles that describe how to implement common data-aware operations in Controllers with the corresponding Object Space methods, events, and business classes.

## Tasks

* [Create a New Object](xref:403616)
* [Load Objects](xref:403617)
* [Save Objects to Database](xref:403618)
* [Delete Objects from Database](xref:403619)
* [Evaluate Scalar Values and Fetch a Portion of Data](xref:403620)
* [Execute Business Logic When a Property is Changed and Track Modifications in Objects](xref:403621)
* [Refresh Objects and Rollback Changes](xref:403622)


## CRUD in XPO

When an XAF application uses XPO, an [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace) is created. Internally, it uses a [](xref:DevExpress.Xpo.UnitOfWork) to create, update, and delete business objects. From an `XPObjectSpace`, use the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) property to access a `UnitOfWork` instance. 

When you create a new XPO business object, the `XPObjectSpace`'s `UnitOfWork` is passed to the business class constructor. You can use the [](xref:DevExpress.Xpo.PersistentBase.Session) property to access the passed `UnitOfWork` instance in a business class. Use this instance to load and create business objects in business classes: [](xref:2025). 

When a new `XPObjectSpace` is created, a new `UnitOfWork` is also created. An `XPObjectSpace` can create a new `UnitOfWork`, for example, when you call the [IObjectSpace.Refresh](xref:DevExpress.ExpressApp.IObjectSpace.Refresh) method. This `UnitOfWork` [connects to a Data Layer or Object Layer](xref:2123) that corresponds to the current [ObjectSpaceProvider](xref:DevExpress.ExpressApp.IObjectSpaceProvider).


## CRUD in EF Core

Inside an EF Core business class, implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface in the class. XAF automatically assigns an Object Space instance to the `IObjectSpaceLink.ObjectSpace` property. For data manipulation in EF Core business classes, use the assigned Object Space APIs listed in the topics above.
