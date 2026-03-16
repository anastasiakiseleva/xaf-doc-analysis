---
uid: DevExpress.ExpressApp.SystemModule.IExportable.OnExporting
name: OnExporting()
type: Method
summary: Performs the required pre-export actions under the current exportable editor.
syntax:
  content: void OnExporting()
seealso: []
---
This method is called by the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) before it starts to export the current exportable List Editor's [IExportable.Printable](xref:DevExpress.ExpressApp.SystemModule.IExportable.Printable) control.

When supporting the **IExportable** interface in a custom List Editor, implement the **OnExporting** method so that it performs the operations required on the Editor's control before export.