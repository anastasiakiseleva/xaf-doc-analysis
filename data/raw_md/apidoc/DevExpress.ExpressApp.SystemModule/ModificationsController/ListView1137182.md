---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController.ListView
name: ListView
type: Property
summary: Gets the current List View.
syntax:
  content: |-
    [Browsable(false)]
    public ListView ListView { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ListView
    description: A [](xref:DevExpress.ExpressApp.ListView) object which is the current Detail View.
seealso: []
---
The **ListView** value is the [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) value converted to the [](xref:DevExpress.ExpressApp.ListView) type, or null if the current View is not a List View.