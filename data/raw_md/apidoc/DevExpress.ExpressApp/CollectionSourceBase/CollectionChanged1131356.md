---
uid: DevExpress.ExpressApp.CollectionSourceBase.CollectionChanged
name: CollectionChanged
type: Event
summary: Occurs after the Collection Source's collection has been recreated.
syntax:
  content: public event EventHandler CollectionChanged
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.CollectionChanging
- linkId: DevExpress.ExpressApp.CollectionSourceBase.ResetCollection(System.Boolean)
---
Handle this event to access a Collection Source's collection in a [View Controller](xref:112621). Subscribe to this event and perform your code in the event handler. Do not perform the collection-dependent code after the Controller has been activated. This is so, because while View Controllers are activating for a List View, the List View's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) property may return _null_.

This event is raised by the [CollectionSourceBase.ResetCollection](xref:DevExpress.ExpressApp.CollectionSourceBase.ResetCollection(System.Boolean)) method, if the recreated collection differs from the previously existing one.