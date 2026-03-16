---
uid: DevExpress.ExpressApp.SystemModule.ExportController.Exported
name: Exported
type: Event
summary: Occurs when executing the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction), when the export is completed.
syntax:
  content: public event EventHandler<CustomExportEventArgs> Exported
seealso: []
---
The **Exported** event occurs after an export operation has been completed. The handler's [CustomExportEventArgs.ExportTarget](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportTarget) and [CustomExportEventArgs.Stream](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.Stream) parameters specify the target export format and the exported data. Handle this event to perform custom post-export actions.

Refer to the [How to: Customize the Export Action Behavior](xref:113287) topic to see an example of handling this event.