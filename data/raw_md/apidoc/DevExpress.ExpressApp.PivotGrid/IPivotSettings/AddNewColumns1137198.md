---
uid: DevExpress.ExpressApp.PivotGrid.IPivotSettings.AddNewColumns
name: AddNewColumns
type: Property
summary: Specifies whether columns deleted via the [IPivotSettings.Settings](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.Settings) property in the current [Application Model](xref:112580) layer, but existing in previous layers, should be retained in the [Pivot Grid List Editor](xref:113303).
syntax:
  content: |-
    [DefaultValue(true)]
    bool AddNewColumns { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if columns deleted in the current Application Model layer, but existing in previous layers, should be retained in the Pivot Grid List Editor; otherwise, **false**.'
seealso: []
---
