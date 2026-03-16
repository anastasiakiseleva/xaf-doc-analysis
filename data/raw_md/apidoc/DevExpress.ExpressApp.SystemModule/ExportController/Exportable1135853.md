---
uid: DevExpress.ExpressApp.SystemModule.ExportController.Exportable
name: Exportable
type: Property
summary: Specifies the [List Editor](xref:113189) whose data is to be exported by the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction).
syntax:
  content: public IExportable Exportable { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.IExportable
    description: An [](xref:DevExpress.ExpressApp.SystemModule.IExportable) object that is the List Editor to be exported.
seealso: []
---
To enable List Editors to be exported by the ExportController, they must implement the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface. Nealy all XAF built-in List Editors implement this interface, and thus can be exported by the ExportController. Use the `Exportable` property to access the List Editor to be exported by the current ExportController. This property returns the current List View's List Editor cast to the `IExportable` interface. If the current View does not display a List View or its List Editor does not implement the `IExportable` interface, the property returns `null`. In this instance, the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) Action is not activated.

In addition, use this property if you need to set another editor instead of the default one. In this instance, the [ExportController.AutoUpdateExportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.AutoUpdateExportable) property is set to `false` automatically. The system will not update this property when the current List View's List Editor is changed. However, set the `AutoUpdateExportable` property to `true` when you need to return the control under the exportable editor to the system.