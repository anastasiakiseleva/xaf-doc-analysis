---
uid: DevExpress.ExpressApp.SystemModule.ExportController.AutoUpdateExportable
name: AutoUpdateExportable
type: Property
summary: Specifies whether the [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) property is set and updated internally, in a default manner.
syntax:
  content: |-
    [DefaultValue(true)]
    public bool AutoUpdateExportable { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the exportable editor is determined and updated automatically; otherwise, **false**.'
seealso: []
---
By default, this property is set to **true**. This means that the current List View's List Editor is set as the editor to be exportable. When you set another editor to the [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) property, the **AutoUpdateExportable** property is set to **false** automatically. In this instance, the system won't rewrite your exportable editor when the current List View's List Editor is changed. However, you can set the **AutoUpdateExportable** property to **true** to return the system's control under the exportable editor.