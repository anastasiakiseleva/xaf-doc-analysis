---
uid: DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportOptions
name: ExportOptions
type: Property
summary: Specifies the export options to be applied when data is exported.
syntax:
  content: public ExportOptionsBase ExportOptions { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraPrinting.ExportOptionsBase
    description: An [](xref:DevExpress.XtraPrinting.ExportOptionsBase) object which specifies the export options to be applied when data is exported.
seealso:
- linkId: "113287"
---
When handling the [ExportController.CustomExport](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomExport) event, use the **ExportOptions** parameter to customize the options that will be applied when the data is exported. Cast the object returned by this property to one of the following types in dependence on the value returned by the [CustomExportEventArgs.ExportTarget](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportTarget) parameter:

| [](xref:DevExpress.XtraPrinting.ExportTarget) | Export Options |
|---|---|
| ExportTarget.Xls | [](xref:DevExpress.XtraPrinting.XlsExportOptions) |
| ExportTarget.Xlsx | [](xref:DevExpress.XtraPrinting.XlsxExportOptions) |
| ExportTarget.Html | [](xref:DevExpress.XtraPrinting.HtmlExportOptions) |
| ExportTarget.Mht | [](xref:DevExpress.XtraPrinting.MhtExportOptions) |
| ExportTarget.Pdf | [](xref:DevExpress.XtraPrinting.PdfExportOptions) |
| ExportTarget.Text | [](xref:DevExpress.XtraPrinting.TextExportOptions) |
| ExportTarget.Rtf | [](xref:DevExpress.XtraPrinting.RtfExportOptions) |
| ExportTarget.Csv | [](xref:DevExpress.XtraPrinting.CsvExportOptions) |
| ExportTarget.Image | [](xref:DevExpress.XtraPrinting.ImageExportOptions) |

You can also cast **ExportOptions** to **IDataAwareExportOptions** to switch from **DataAware** to **WYSIWYG** export type (see [](xref:DevExpress.Export.ExportType)). For details, refer to the [](xref:DevExpress.ExpressApp.SystemModule.IDataAwareExportable) topic.