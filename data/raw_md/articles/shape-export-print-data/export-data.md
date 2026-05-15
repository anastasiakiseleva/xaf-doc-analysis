---
uid: "113362"
seealso: []
title: Export Data
---
# Export Data

XAF allows users to export [List View](xref:112611) data and analysis data to various formats. The export functionality implements the @DevExpress.ExpressApp.SystemModule.ExportController that contains the **Export to** Action. The Action is activated for the current List View if the [List Editor](xref:113189) supports the @DevExpress.ExpressApp.SystemModule.IExportable interface and the List Editor's control supports the @DevExpress.XtraPrinting.IPrintable interface. The following editors meet these criteria:

{| class = "dx-no-border-table"
|-
| **Windows Forms List Editors**
* @DevExpress.ExpressApp.Win.Editors.GridListEditor
* @DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor
* @DevExpress.ExpressApp.Chart.Win.ChartListEditor
* @DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor
* @DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor
| **ASP.NET Core Blazor List Editors**
* @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor
* @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor
* @DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor
|}

When you use any of the XAF List Editors mentioned above, your application already includes the export functionality. If you use a custom List Editor to display List Views and want its data to be exportable, implement the @DevExpress.ExpressApp.SystemModule.IExportable interface in the List Editor and the @DevExpress.XtraPrinting.IPrintable interface in the control it uses. 

If the default implementation of the Export Controller does not meet your needs, handle its events or the events of its platform-specific descendant: @DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController or @DevExpress.ExpressApp.Win.SystemModule.WinExportController. You can find an example in the following help topic: <xref:113287>

## Export Data: ASP.NET Core Blazor

The **Export to** Action exports data to a file stream. The supported file formats are:

{| class = "dx-no-border-table"
|-
| * CSV
| * XLS 
| * XLSX
| * PDF
|}

![Export Actions in a XAF Blazor Application](~/images/xaf-blazor-export-actions.png)

To export data, XAF uses the data-aware export that ships with the DevExpress [Blazor Grid](xref:DevExpress.Blazor.DxGrid). For additional information on this functionality and its limitations, refer to the following topic: [Blazor Grid - Export Data](xref:404338).

## Export Data: Windows Forms

The **Export to** Action exports data to a file stream. The supported file formats are:

{| class = "dx-no-border-table"
|-
| * CSV
* HTML
| * Image
* MHT
| * PDF
* RTF
| * Text
* XLS
| * XLSX
* DOCX
|}


![Export Actions in a XAF WinForms Application](~/images/xaf-win-export-actions.png)