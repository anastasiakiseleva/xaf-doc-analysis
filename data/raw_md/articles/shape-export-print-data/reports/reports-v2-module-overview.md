---
uid: "113591"
seealso: []
title: Reports V2 Module
---
# Reports V2 Module

Reports are widely used in business applications to present data in readable and printer-friendly formats. The **Reports V2** module simplifies integrating DevExpress [Reporting](xref:2162) into XAF applications. It enables users to create, preview, print, and store user reports in the database, as well as use and manage both predefined (Visual Studio) and user-created reports. 

All reports are presented by business objects in the application database, with a Reports List View to display them and various actions for managing them. Users can also select business objects and use the **ShowInReport** action to generate reports on selected data. 

If **Reports V2** does not fit certain needs, XtraReports can still be integrated manually. Refer to the following help topic for more information: <xref:113645>.

## DevExpress WinForms Controls Used by the ReportsV2 Module
* @DevExpress.XtraReports.UserDesigner.XRDesignForm  - used to design reports when the @DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle property is set to `Standard`.
* @DevExpress.XtraReports.UserDesigner.XRDesignRibbonForm - used to design reports when the @DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle property is set to `Ribbon`.
* @DevExpress.XtraReports.UI.ReportPrintTool - used to preview and print reports applications.

**Examples**: [How to: Customize the WinForms Report Designer Form](xref:113604) | [How to: Use the Custom WinForms Report Designer](xref:113605) | [How to: Use the Custom Report Preview Form](xref:113603) | [How to Print a report without displaying a preview](https://github.com/DevExpress-Examples/xaf-print-a-report-without-displaying-a-preview)

## DevExpress ASP.NET Core Blazor Controls Used by the ReportsV2 Module
* @DevExpress.Blazor.Reporting.DxReportDesigner - used to design reports.
* @DevExpress.Blazor.Reporting.DxReportViewer - used to preview and print reports.

**Examples**: [](xref:402261) | [](xref:402260) | [How to Print a report without displaying a preview](https://github.com/DevExpress-Examples/xaf-print-a-report-without-displaying-a-preview)

## Reports V2 Module Components

The Reports V2 Module consists of the following components:

* @DevExpress.ExpressApp.ReportsV2.ReportsModuleV2 -- Platform-agnostic Reports module.
* @DevExpress.ExpressApp.ReportsV2.Win.ReportsWindowsFormsModuleV2 -- WinForms-specific Reports module.
* @DevExpress.ExpressApp.ReportsV2.Blazor.ReportsBlazorModuleV2 -- Blazor-specific Reports module.

Refer to the following topic to learn how to add modules to your application: <xref:118047>

## Report Data Type

Reports V2 Module stores reports as business objects that implement the @DevExpress.ExpressApp.ReportsV2.IReportDataV2 interface. You should set the @DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportDataType property to `ReportDataV2` at application startup. **In EF Core projects**, you also need to add the report data type to `DBContext`. Refer to the following help topic for more information: <xref:404243>.

Alternatively, you can use a custom report data type. Refer to the following help topic for more information: <xref:113672>.