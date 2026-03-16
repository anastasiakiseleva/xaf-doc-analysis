---
uid: DevExpress.ExpressApp.SystemModule.ExportController.CustomExport
name: CustomExport
type: Event
summary: Occurs when executing the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction). Allows you to customize export options and/or implement a custom export.
syntax:
  content: public event EventHandler<CustomExportEventArgs> CustomExport
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ExportController.Exported
---
The **CustomExport** event occurs before export. The handler's [CustomExportEventArgs.ExportOptions](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportOptions) parameter allows you to customize export options for the required export format. To get the target format in which the data is about to be exported, use the handler's [CustomExportEventArgs.ExportTarget](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportTarget) parameter.

You can also customize the export options that are provided by the control to be exported. To access this control, use the [CustomExportEventArgs.Printable](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.Printable) event handler parameter. To learn how to change the control's export settings, refer to the parameter's description.

If you need to implement a custom export, use the [CustomExportEventArgs.Stream](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.Stream) and [CustomExportEventArgs.Printable](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.Printable) parameters. In addition, if you don't need the default export operation to be performed, set the handler's **Handled** parameter to **true**.

Refer to the [How to: Customize the Export Action Behavior](xref:113287) topic, to see an example of handling this event.