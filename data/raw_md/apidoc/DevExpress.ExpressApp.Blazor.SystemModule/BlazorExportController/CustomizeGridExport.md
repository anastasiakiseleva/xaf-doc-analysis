---
uid: DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController.CustomizeGridExport
name: CustomizeGridExport
type: Event
summary: Fires before the export operation.
syntax:
  content: public event EventHandler<GridExportEventArgs> CustomizeGridExport
seealso: []
---
The `CustomizeGridExport` event occurs before export. The handler's @DevExpress.ExpressApp.Blazor.SystemModule.GridExportEventArgsBase`1.Options parameter allows you to customize export options. To obtain the target format of the resulting file, use the handler's @DevExpress.ExpressApp.Blazor.SystemModule.GridExportEventArgsBase.ExportTarget parameter.

[!include[blazor-export-options](~/templates/blazor-export-options.md)]