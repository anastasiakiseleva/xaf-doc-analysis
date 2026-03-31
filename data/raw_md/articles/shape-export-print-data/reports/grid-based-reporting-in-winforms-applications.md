---
uid: "116114"
seealso: []
title: Grid Based Reporting in WinForms Applications
---
# Grid Based Reporting in WinForms Applications

This topic describes how you can create a report based on the grid control layout in a WinForms XAF application using [Advanced Grid Printing and Exporting](xref:114962).

You can easily generate a report from the grid data either at design time or at runtime, taking into account the grid layout. The [Reports V2 Module](xref:113591) adds the **New report** item to the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction).

![GridBasedReporting1](~/images/gridbasedreporting1123212.png)

Internally, the **New report** item is added by handling the [ExportController.ExportActionItemsCreated](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportActionItemsCreated) event from the [](xref:DevExpress.ExpressApp.ReportsV2.Win.WinGridReportExportController) Controller.

The **New report** item invokes the [Report Designer](xref:4256). The current grid layout is automatically converted to the report layout.  You can learn more about the report generation rules and limitations in the [Advanced Grid Printing and Exporting](xref:114962) topic.

![GridBasedReporting2](~/images/gridbasedreporting2123213.png)

If you click **Save**, the report is saved to the application database, together with other [user-defined reports](xref:113646).

By default, the report display name (see [XtraReport.DisplayName](xref:DevExpress.XtraReports.UI.XtraReport.DisplayName)) is set to the caption of the current View (see [View.Caption](xref:DevExpress.ExpressApp.View.Caption)). You can customize the display name by handling the [WinGridReportExportController.QueryReportDisplayName](xref:DevExpress.ExpressApp.ReportsV2.Win.WinGridReportExportController.QueryReportDisplayName) event.

To adjust the report generation options, use the [WinGridReportExportController.CustomizeReportGenerationOptions](xref:DevExpress.ExpressApp.ReportsV2.Win.WinGridReportExportController.CustomizeReportGenerationOptions) event.