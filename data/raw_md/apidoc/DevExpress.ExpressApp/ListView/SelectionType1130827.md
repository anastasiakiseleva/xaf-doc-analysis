---
uid: DevExpress.ExpressApp.ListView.SelectionType
name: SelectionType
type: Property
summary: Returns the selection type supported by the current List View.
syntax:
  content: public override SelectionType SelectionType { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SelectionType
    description: A [](xref:DevExpress.ExpressApp.SelectionType) enumeration value representing the selection type supported by the current List View.
seealso: []
---
The **SelectionType** property returns the selection type of the View's List Editor (see [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor). If the Editor is not currently specified for the List View, the selection type of the base View is returned (see [View.SelectionType](xref:DevExpress.ExpressApp.View.SelectionType)).