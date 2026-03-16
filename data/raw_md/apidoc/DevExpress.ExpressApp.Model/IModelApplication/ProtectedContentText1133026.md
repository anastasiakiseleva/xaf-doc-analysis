---
uid: DevExpress.ExpressApp.Model.IModelApplication.ProtectedContentText
name: ProtectedContentText
type: Property
summary: Specifies text that is displayed instead of the data protected by the [Security System](xref:113366).
syntax:
  content: |-
    [DefaultValue("*******")]
    string ProtectedContentText { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying text that is displayed instead of the data protected by the Security System.
seealso:
- linkId: DevExpress.ExpressApp.Editors.ListEditor.ProtectedContentText
- linkId: "113366"
---
The `ProtectedContentText` text is available at the UI level for grid and tree List Editors and for built-in Property Editors. The default control value is replaced by this text. No `ProtectedContentText` string exists at the data source level. Protected properties return default type values instead of actual values. The `null` value is returned for reference properties, zero - for integer properties, `DateTime.MinValue` for `DateTime` properties. These default values will be shown in reports, charts, pivot grids, the scheduler and in custom controls.