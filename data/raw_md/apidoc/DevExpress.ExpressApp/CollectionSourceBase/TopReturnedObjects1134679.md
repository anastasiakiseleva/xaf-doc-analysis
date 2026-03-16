---
uid: DevExpress.ExpressApp.CollectionSourceBase.TopReturnedObjects
name: TopReturnedObjects
type: Property
summary: Specifies the number of objects that can be retrieved by the Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) from the database.
syntax:
  content: public int TopReturnedObjects { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the number of objects to be retrieved by the Collection Source's collection from the database. **0** indicates that all objects will be retrieved.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelListView.TopReturnedObjects
---
The **TopReturnedObjects** property has no effect in [Server, ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) modes. To limit the number of objects displayed by a List View, disable these modes.