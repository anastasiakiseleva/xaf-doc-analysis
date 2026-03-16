---
uid: DevExpress.ExpressApp.CollectionSourceBase.ResetCollection(System.Boolean)
name: ResetCollection(Boolean)
type: Method
summary: Recreates a Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection).
syntax:
  content: public void ResetCollection(bool updateObjectsInCriteria = false)
  parameters:
  - id: updateObjectsInCriteria
    type: System.Boolean
    defaultValue: "False"
    description: '**true**, if criteria contain a reference to an object that should be reloaded; otherwise - **false**.'
seealso: []
---
This method clears the Collection Source's collection, disposes of the resources allocated by the collection and recreates it. The **ResetCollection** method raises two events - [CollectionSourceBase.CollectionChanging](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionChanging) and [CollectionSourceBase.CollectionChanged](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionChanged). Handle them to be notified when a collection is recreated.

Generally you do not need to call this method, it is called automatically by **XAF** in certain situations. For instance, when a [Detail View](xref:112611) contains a nested [List View](xref:112611) and the Detail View's [ViewItem.CurrentObject](xref:DevExpress.ExpressApp.Editors.ViewItem.CurrentObject) changes, **XAF** calls this method to recreate the nested List View's Collection Source's collection.
