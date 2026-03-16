---
uid: DevExpress.ExpressApp.Model.IModelListView.TopReturnedObjects
name: TopReturnedObjects
type: Property
summary: Specifies the number of objects retrieved by the collection of the [List View](xref:112611)'s Collection Source from the database.
syntax:
  content: |-
    [DefaultValue(0)]
    int TopReturnedObjects { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying collection specifying the number of objects retrieved by the collection of the List View's Collection Source from the database. **0** indicates that all objects are retrieved.
seealso: []
---
The **TopReturnedObjects** property has no effect in [Server, ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) mode. To limit the number of objects displayed by a List View, disable **Server** mode.

The **TopReturnedObjects** property has no effect in nested list views.