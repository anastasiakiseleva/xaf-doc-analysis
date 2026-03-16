---
uid: DevExpress.ExpressApp.CollectionSourceBase.CollectionChanging
name: CollectionChanging
type: Event
summary: Occurs before the Collection Source's collection has been recreated.
syntax:
  content: public event EventHandler CollectionChanging
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.CollectionChanged
- linkId: DevExpress.ExpressApp.CollectionSourceBase.ResetCollection(System.Boolean)
---
This event is raised in the [CollectionSourceBase.ResetCollection](xref:DevExpress.ExpressApp.CollectionSourceBase.ResetCollection(System.Boolean)) method, before recreation of the Collection Source's collection takes place. Handle the **CollectionChanging** event to be notified when the Collection Source's collection is about to be recreated.