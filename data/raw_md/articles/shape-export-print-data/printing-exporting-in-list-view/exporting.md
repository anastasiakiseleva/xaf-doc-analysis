---
uid: "113362"
seealso: []
title: Exporting
owner: Ekaterina Kiseleva
---
# Exporting

XAF allows you to export [List View](xref:112611) data and analysis data to various formats (XLS, PDF, CSV, etc.). The following [View Controller](xref:112621) ship with the export functionality:

* @DevExpress.ExpressApp.SystemModule.ExportController -- Exports List View data.

## Export List View Data (ASP.NET Core Blazor and Windows Forms)

The [Export Controller](xref:DevExpress.ExpressApp.SystemModule.ExportController) is designed to export List View data. If the default implementation of the Export Controller does not meet your needs, handle its events or the events of its platform-specific descendant:

ASP.NET Core Blazor
:   @DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController
Windows Forms
:   @DevExpress.ExpressApp.Win.SystemModule.WinExportController

The controllers mentioned above contain the **Export to** Action. To see examples of how to customize this Action, refer to the following topic: [](xref:113287).

The **Export to** Action is activated for the current List View if the [List Editor](xref:113189) supports the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface and the List Editor's control supports the `IPrintable` interface. Editors that meet these criteria depend on your application platform.

{|
|-

! Platform
! List Editors that Support IExportable
|-

| ASP.NET Core Blazor
| @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor

@DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor

@DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor
|-

| Windows Forms
| @DevExpress.ExpressApp.Win.Editors.GridListEditor

@DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor

@DevExpress.ExpressApp.Chart.Win.ChartListEditor

@DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor

@DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor
|}

When you use any of the XAF List Editors mentioned above, your application already includes the export functionality without the need to add a line of code. If you use a custom List Editor to present a List View, its data can be exported as well. To do this, make sure that this List Editor supports the **IExportable** interface and the editor's control implements the **IPrintable** interface.

### ASP.NET Core Blazor

The **Export to** Action exports List View data to a memory stream. This Action is displayed in List Views whose @DevExpress.ExpressApp.Model.IModelListView.EditorType is @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor or @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor.

The supported export formats are:

* PDF
* CSV
* XLS 
* XLSX

To export List View data, follow the steps below:

1. Click **Export to | {Format_Name} File** on the List View main toolbar.

    ![DevExpress XAF - Export ListView Data in ASP.NET Core Blazor apps](~/images/blazor-listview-custom-export.png)

1. The application saves the exported file to your device. The file name is the name of the exported List View.

To perform this operation, XAF uses the data-aware export that ships with the DevExpress Blazor Grid. For more information on this functionality and its limitations, refer to the following topic: [Blazor Grid - Export Data](xref:404338).

### Windows Forms

The **Export to** Action exports data to a file stream. The supported file formats are:

* XLS 
* HTML 
* Text 
* MHT 
* PDF 
* RTF 
* Image

To export List View data, follow the steps below:

1. Select **File | Export to | {Format_Name} File** from the main menu.

    ![Export_1](~/images/export_1116692.png)

1. Specify a file name/location and click **Save**.

    ![Export_SaveAs](~/images/export_saveas116766.png)

    To localize the **Save as type** filter captions, use the **Localization** | **OpenSaveDialogFilters** node in the [Model Editor](xref:112582).
