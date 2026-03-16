---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController.DetailView
name: DetailView
type: Property
summary: Gets the current Detail View.
syntax:
  content: |-
    [Browsable(false)]
    public DetailView DetailView { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DetailView
    description: A [](xref:DevExpress.ExpressApp.DetailView) object which is the current Detail View.
seealso: []
---
The **DetailView** value is the [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) value converted to the [](xref:DevExpress.ExpressApp.DetailView) type, or null if the current View is not a Detail View.