---
uid: "113591"
seealso: []
title: Reports V2 Module
---
# Reports V2 Module

Reports are widely used in business applications to present data in human-readable and printer-friendly formats. The **Reports V2** module is introduced to simplify the integration of DevExpress [Reporting](xref:2162) into XAF applications. Note that WinForms and ASP.NET Core Blazor XAF applications are standard .NET applications, and the approaches described in the [GUI](xref:9820) and [Web Reporting](xref:9814) tutorials are fully applicable, but you need to create a user interface for reports access and implement a storage for user-defined reports manually. The **Reports V2** module provides ready-to-use solutions for these tasks, which cover the most popular scenarios.

With the **Reports V2** module, reports are represented by business objects that are stored with other persistent objects in the application database. A list of included reports (both predefined in Visual Studio and added by end-users) is displayed in the **Reports** List View, which can be invoked from the **Reports** navigation item. The **Reports** View is accompanied by the [Actions](xref:112622) used to manage reports (create, design, print, copy, etc.). Reports can also be executed from a business object context - you can select several objects and then use the **ShowInReport** Action to display these objects in a report.

> [!NOTE]
> If the solutions provided by the **Reports V2** module are not applicable in your particular scenario, feel free to integrate XtraReports in a custom way (see [How to: Show an XtraReport created at design time, without the use of XAF Reports module](xref:113645)).

## Reports V2 Capabilities

* Create, preview and print end-user reports at runtime and persist these reports in the database.
* Preview and print predefined reports designed by the developer in Visual Studio.
* Use predefined reports as templates for creating end-user reports.

## DevExpress Controls Used by the ReportsV2 Module

### WinForms
* [](xref:DevExpress.XtraReports.UserDesigner.XRDesignForm)  - used to design reports in WinForms (when the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property is set to **Standard**).
* [](xref:DevExpress.XtraReports.UserDesigner.XRDesignRibbonForm) - used to design reports in WinForms (when the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property is set to **Ribbon**).
* [](xref:DevExpress.XtraReports.UI.ReportPrintTool) - used to preview and print reports in WinForms applications.

**Examples**: [How to: Customize the WinForms Report Designer Form](xref:113604) | [How to: Use the Custom WinForms Report Designer](xref:113605) | [How to: Use the Custom Report Preview Form](xref:113603) | [How to Print a report without displaying a preview](https://github.com/DevExpress-Examples/xaf-print-a-report-without-displaying-a-preview)

### ASP.NET Core Blazor
* @DevExpress.Blazor.Reporting.DxReportDesigner - used to design reports in ASP.NET Core Blazor applications.
* @DevExpress.Blazor.Reporting.DxReportViewer - used to preview and print reports in ASP.NET Core Blazor applications.

**Examples**: [](xref:402261) | [](xref:402260) | [How to Print a report without displaying a preview](https://github.com/DevExpress-Examples/xaf-print-a-report-without-displaying-a-preview)

## Reports V2 Module Components
The Reports V2 Module consists of the following platform-agnostic and platform-specific components.

ReportsModuleV2
:   Add it to your platform-agnostic module in the _MySolution.Module\\Module.cs_ file (see [ModuleBase.RequiredModuleTypes](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes)).
ReportsWindowsFormsModuleV2
:   Add it to your WinForms application project in the _MySolution.Win\\WinApplication.cs_ file (see [XafApplication.Modules](xref:DevExpress.ExpressApp.XafApplication.Modules)).
ReportsBlazorModuleV2
:   Add it to your ASP.NET Core Blazor application project in the _MySolution.Blazor.Server\\BlazorApplication.cs_ file (see [XafApplication.Modules](xref:DevExpress.ExpressApp.XafApplication.Modules)).

Refer to the following topic to learn how to add modules to your application: <xref:118047>

## Report Data Type
Reports are persisted using business objects (entities) that implement the [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) interface. If you use XPO, the [](xref:DevExpress.Persistent.BaseImpl.ReportDataV2) persistent class implemented in the [Business Class Library](xref:112571) is used automatically. If you use Entity Framework, you should manually set the [ReportsModuleV2.ReportDataType](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportDataType) property to [](xref:DevExpress.Persistent.BaseImpl.EF.ReportDataV2) and add this type to your **DBContext** (see [](xref:404206)). You can also use a custom report data type (see [How to: Add a Custom Column to the Reports List](xref:113672)).
