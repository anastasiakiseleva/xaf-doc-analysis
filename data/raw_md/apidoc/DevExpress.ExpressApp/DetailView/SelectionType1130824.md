---
uid: DevExpress.ExpressApp.DetailView.SelectionType
name: SelectionType
type: Property
summary: Returns the selection type supported by the current Detail View.
syntax:
  content: public override SelectionType SelectionType { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SelectionType
    description: A [](xref:DevExpress.ExpressApp.SelectionType) enumeration value representing the selection type supported by the current Detail View.
seealso:
- linkId: DevExpress.ExpressApp.ListView.SelectionType
---
The **SelectionType** property returns the [SelectionType.FocusedObject](xref:DevExpress.ExpressApp.SelectionType.FocusedObject) value, indicating that the DetailView can only have a single selected object represented by the currently focused object.