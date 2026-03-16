---
uid: DevExpress.ExpressApp.CollectionSourceBase.Disposed
name: Disposed
type: Event
summary: Occurs after a Collection Source has been disposed of.
syntax:
  content: public event EventHandler Disposed
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.Dispose
---
This event is raised as a result of calling the [CollectionSourceBase.Dispose](xref:DevExpress.ExpressApp.CollectionSourceBase.Dispose) method. This method releases all the resources allocated by the current **CollectionSourceBase** object. Handle this event to release custom resources after the current **CollectionSourceBase** has been disposed of.