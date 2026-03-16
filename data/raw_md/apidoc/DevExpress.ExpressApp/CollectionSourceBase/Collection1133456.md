---
uid: DevExpress.ExpressApp.CollectionSourceBase.Collection
name: Collection
type: Property
summary: Provides access to the Collection Source's (see [](xref:DevExpress.ExpressApp.CollectionSourceBase)) collection of objects.
syntax:
  content: public object Collection { get; }
  parameters: []
  return:
    type: System.Object
    description: An object representing the Collection Source's collection of objects.
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode
- linkId: DevExpress.ExpressApp.CollectionSourceBase.Mode
- linkId: DevExpress.ExpressApp.BaseObjectSpace
---
Use this property to access the Collection Source's collection. A Collection Source's **Collection** holds the objects retrieved from a data source by an Object Space and displayed by a List View in a UI. You may need to access a Collection Source's collection, for example, to filter a [List View](xref:112611) on the data source level. To learn how to do it, refer to the [Criteria Property of a List View's Collection Source](xref:112988) topic.

The following table lists the events related to the Collection Source's collection.

| Event | Description |
|---|---|
| [CollectionSourceBase.CollectionChanging](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionChanging) | Occurs before the collection has been recreated. |
| [CollectionSourceBase.CollectionChanged](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionChanged) | Occurs after the collection has been recreated. |
| [CollectionSourceBase.CollectionReloading](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionReloading) | Occurs before the collection has been reloaded. |
| [CollectionSourceBase.CollectionReloaded](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionReloaded) | Occurs after the collection has been reloaded. |
| [CollectionSourceBase.CriteriaApplying](xref:DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplying) | Occurs before the collection has been filtered using the criteria defined in the [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria) dictionary. |
| [CollectionSourceBase.CriteriaApplied](xref:DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplied) | Occurs after the collection has been filtered using the criteria defined in the [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria) dictionary. |

Note, that while [View Controllers](xref:112621) are activating for a List View, the List View's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) property may return _null_. So, if you need to access a Collection Source's collection in a View Controller, do not perform the collection-dependent code after the Controller has been activated. Instead, subscribe to the [CollectionSourceBase.CollectionChanged](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionChanged) event, and perform your code in the event handler.

If the object returned by this property does not implement the **IEnumerable** interface, but you need to iterated through the retrieved objects, use the [CollectionSourceBase.List](xref:DevExpress.ExpressApp.CollectionSourceBase.List) property.

Be aware in which mode the current Collection's Collection Source is created: [CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode) and [CollectionSourceBase.Mode](xref:DevExpress.ExpressApp.CollectionSourceBase.Mode). This influences which objects are currently retrieved to the Collection.