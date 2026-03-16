---
uid: DevExpress.ExpressApp.ObjectViewController`2.ViewSelectedObjects
name: ViewSelectedObjects
type: Property
summary: Gets the list of selected objects (see [View.SelectedObjects](xref:DevExpress.ExpressApp.View.SelectedObjects)).
syntax:
  content: |-
    [Browsable(false)]
    public IList<ObjectType> ViewSelectedObjects { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{{ObjectType}}
    description: A typed list or selected object. The object type is specified using the [](xref:DevExpress.ExpressApp.ObjectViewController`2)'s **ObjectType** generic parameter.
seealso: []
---
In the [ServerView, InstantFeedback, InstantFeedbackView](xref:118450), and [DataView Mode](xref:118452) List View data access modes, reading this property value causes extra requests to the database for each selected object. If these requests are unwanted for performance reasons, use the [View.SelectedObjects](xref:DevExpress.ExpressApp.View.SelectedObjects) property which returns [](xref:DevExpress.ExpressApp.IObjectRecord) wrappers instead of business objects themselves.