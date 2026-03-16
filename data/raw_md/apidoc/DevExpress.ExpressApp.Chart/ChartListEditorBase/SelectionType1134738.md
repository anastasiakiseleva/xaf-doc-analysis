---
uid: DevExpress.ExpressApp.Chart.ChartListEditorBase.SelectionType
name: SelectionType
type: Property
summary: Returns the selection type supported by the [](xref:DevExpress.ExpressApp.Chart.ChartListEditorBase).
syntax:
  content: public override SelectionType SelectionType { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SelectionType
    description: A [](xref:DevExpress.ExpressApp.SelectionType) enumeration value that represents the selection type supported by the current List Editor.
seealso: []
---
Charting List Editors do not support selection. So, this property always returns [SelectionType.None](xref:DevExpress.ExpressApp.SelectionType.None).