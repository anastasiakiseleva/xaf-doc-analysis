---
uid: DevExpress.ExpressApp.ObjectViewController`2.ViewCurrentObject
name: ViewCurrentObject
type: Property
summary: Gets the current object (see [View.CurrentObject](xref:DevExpress.ExpressApp.View.CurrentObject)).
syntax:
  content: |-
    [Browsable(false)]
    public ObjectType ViewCurrentObject { get; }
  parameters: []
  return:
    type: '{ObjectType}'
    description: An object of the type specified using the [](xref:DevExpress.ExpressApp.ObjectViewController`2)'s **ObjectType** generic parameter representing the View's current object.
seealso: []
---
In the [ServerView, InstantFeedback, InstantFeedbackView](xref:118450), and [DataView](xref:118452) List View data access modes, reading this property value causes an extra request to the database. If this request is unwanted for performance reasons, use the [View.CurrentObject](xref:DevExpress.ExpressApp.View.CurrentObject) property, which returns an [](xref:DevExpress.ExpressApp.IObjectRecord) wrapper instead of the business object itself.