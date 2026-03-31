---
uid: "113601"
seealso:
- linkId: "113703"
- linkId: "114515"
title: 'How to: Print a Report Without Displaying a Preview'
---

# How to: Print a Report Without Displaying a Preview

This topic describes how to implement the **PrintContacts** [Action](xref:112622), which prints the "Contacts Report" report without displaying its preview. Note that this Action is not designed for reports with end-user-specified parameters (reports that use [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) parameters or native XtraReport parameters).

You can also use the code from this example to access an [](xref:DevExpress.XtraReports.UI.XtraReport) object and then export or email the report content as illustrated in the tutorials listed in the [Exporting Reports](xref:1302) document.

We recommend that you review the following XtraReports help topics and examples before you proceed:

* [Printing a Report](xref:5191)
* [](xref:404502)
* [How to print a report without displaying it in a web application](https://supportcenter.devexpress.com/ticket/details/t227361/reporting-for-asp-net-webforms-how-to-print-or-export-a-report-without-showing-a-preview)

> [!Tip]
> A complete sample project is available in the following DevExpress GitHub Example: [XAF - How to Print a report without displaying a preview](https://github.com/DevExpress-Examples/xaf-print-a-report-without-displaying-a-preview).

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

## Create the PrintContacts Action in an Abstract Platform-Agnostic Controller

In the application's [main module project](xref:118045), implement the following abstract [Controller](xref:112621) class.

**File:** _MySolution.Module/Controllers/PrintContactsController.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MySolution.Module.BusinessObjects;
// ...
public abstract class PrintContactsController : ObjectViewController<ListView, Contact> {
    public PrintContactsController() {
        SimpleAction printAction = new SimpleAction(this, "PrintContacts", PredefinedCategory.Reports);
        printAction.ImageName = "Action_Printing_Print";
        printAction.Execute += delegate (object sender, SimpleActionExecuteEventArgs e) {
            PrintReport("ContactReport", e.SelectedObjects);
        };
        }
    protected abstract void PrintReport(string reportDisplayName, System.Collections.IList selectedObjects);
}
```

***

[`ObjectViewController`]: xref:DevExpress.ExpressApp.ObjectViewController`2
[`ListView`]: xref:DevExpress.ExpressApp.ListView
[`SimpleAction`]: xref:DevExpress.ExpressApp.Actions.SimpleAction
[`ImageName`]: xref:DevExpress.ExpressApp.Actions.ActionBase.ImageName
[`Execute`]: xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute

As you can see, the **PrintContactsController** targets **Contact** objects, so it will be activated when a user selects **Contact** in the navigation. The Controller introduces the **PrintContacts** [](xref:DevExpress.ExpressApp.Actions.SimpleAction). The abstract **PrintReport** method is called when the Action is executed (see [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute)). This method takes two parameters:

`reportDisplayName`
:    The display name of a report to print. Implementations will use this value to find the specified report in the report storage.

`selectedObjects`
:    The list of objects selected in the List View. Implementations will use this information to filter printed reports. 

The next two sections explain how to implement the **PrintReport** method in WinForms and ASP.NET Core Blazor projects.

## Implement Report Printing for WinForms

In the WinForms [module project](xref:118045), inherit the **PrintContactsController**. If your solution does not contain this project, add the Controller to the WinForms [application project](xref:118045). In the Controller, implement the **PrintReport** method in the following manner:

**File:** _MySolution.Win/Controllers/WinInstantPrintReportController.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.Xpo;
using DevExpress.Xpo.DB;
using DevExpress.XtraReports.UI;
using InstantPrintReportsV2Example.Module.Controllers;
using Microsoft.Extensions.DependencyInjection;
// ...
public class WinInstantPrintReportController : PrintContactsController {
    readonly IReportExportService reportExportService;
    public WinInstantPrintReportController() : base() { }

    [ActivatorUtilitiesConstructor]
    public WinInstantPrintReportController(IServiceProvider serviceProvider) : base() { 
        reportExportService = serviceProvider.GetRequiredService<IReportExportService>();
    }

    protected override void PrintReport(string reportDisplayName, System.Collections.IList selectedObjects) {
        using XtraReport report = reportExportService.LoadReport<ReportDataV2>(r => r.DisplayName == reportDisplayName);
        // Filter and sort report data.
        CriteriaOperator objectsCriteria = ((BaseObjectSpace)ObjectSpace).GetObjectsCriteria(((ObjectView)View).ObjectTypeInfo, selectedObjects);
        SortProperty[] sortProperties = { new SortProperty("Age", SortingDirection.Descending) };
        reportExportService.SetupReport(report, objectsCriteria.ToString(), sortProperties);
        report.PrintDialog();
    }
}
```

***

[`XtraReport`]: xref:DevExpress.XtraReports.UI.XtraReport
[`LoadReport`]: xref:DevExpress.ExpressApp.ReportsV2.ReportStorageBase.LoadReport(DevExpress.ExpressApp.ReportsV2.IReportDataV2)
[`BaseObjectSpace`]: xref:DevExpress.ExpressApp.BaseObjectSpace
[`CriteriaOperator`]: xref:DevExpress.Data.Filtering.CriteriaOperator
[`SortProperty`]: xref:DevExpress.Xpo.SortProperty

The Controller implementation injects the `IReportExportService`. The following API available through this service is used:

`IReportExportService.LoadReport`
:   Searches for a report in the report storage based on the specified criteria and loads the found report's data from the storage.
`IReportExportService.SetupReport`
:   Initializes the specified report. The above code sample uses an overload of this method that also filters and sorts report data.

The **XtraReport**'s **PrintDialog** extension method is then called to invoke a print dialog. An end user can specify a printer and other print options before the document is printed.

> [!IMPORTANT]
> Ensure that the _DevExpress.XtraPrinting[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_ assembly is referenced. The **PrintDialog** extension method is implemented in this assembly.

The result is demonstrated in the image below.

![InstantPrintReport_Win](~/images/instantprintreport_win117406.png)


## Implement Report Printing for ASP.NET Core Blazor (Export a Report to a PDF File)

In the ASP.NET Core Blazor project, add the following JavaScript code to _Pages/_Host.cshtm_:

**File:** *MySolution.Blazor.Server/Pages/_Host.cshtml*

# [Razor](#tab/tabid-razor)

```Razor
<!DOCTYPE html>
<html lang="en">
...
<body>
    ...
    <script>
        window.downloadFileFromStream = async (fileName, contentStreamReference) => {
            const arrayBuffer = await contentStreamReference.arrayBuffer();
            const blob = new Blob([arrayBuffer]);
            const url = URL.createObjectURL(blob);
            const anchorElement = document.createElement('a');
            anchorElement.href = url;
            anchorElement.download = fileName ?? '';
            anchorElement.click();
            anchorElement.remove();
            URL.revokeObjectURL(url);
        }
    </script>
</body>
```

***

The `downloadFileFromStream` function forces a user's browser to download an exported report file from the specified stream.

Inherit the **PrintContactsController**. In the Controller, implement the **PrintReport** method in the following manner:

**File:** _MySolution.Blazor.Server/Controllers/BlazorPrintContactsController.cs_

# [C#](#tab/tabid-csharp1)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.Data.Helpers;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.Xpo;
using DevExpress.XtraReports.UI;
using InstantPrintReportsV2Example.Module.Controllers;
using Microsoft.JSInterop;
using DevExpress.Xpo.DB;
using DevExpress.ReportServer.ServiceModel.DataContracts;
using Microsoft.Extensions.DependencyInjection;
// ...
public class BlazorPrintContactsController : PrintContactsController {
    readonly IReportExportService reportExportService;
    readonly IJSRuntime jsRuntime;
    public BlazorPrintContactsController() : base() { }

    [ActivatorUtilitiesConstructor]
    public BlazorPrintContactsController(IServiceProvider serviceProvider) : base() {
        reportExportService = serviceProvider.GetRequiredService<IReportExportService>();
        jsRuntime = serviceProvider.GetRequiredService<IJSRuntime>();
    }

    protected override async void PrintReport(string reportDisplayName, System.Collections.IList selectedObjects) {
        using XtraReport report = reportExportService.LoadReport<ReportDataV2>(r => r.DisplayName == reportDisplayName);
        // Filter and sort report data
        CriteriaOperator objectsCriteria = ((BaseObjectSpace)ObjectSpace).GetObjectsCriteria(((ObjectView)View).ObjectTypeInfo, selectedObjects);
        SortProperty[] sortProperties = { new SortProperty("Age", SortingDirection.Descending) };
        reportExportService.SetupReport(report, objectsCriteria.ToString(), sortProperties);

        using Stream s = reportExportService.ExportReport(report, DevExpress.XtraPrinting.ExportTarget.Pdf);
        using var streamRef = new DotNetStreamReference(s);
        var fileName = reportDisplayName + ".pdf";
        await jsRuntime.InvokeVoidAsync("downloadFileFromStream", fileName, streamRef);
    }
}
```

***

The controller's `PrintReport` method implementation injects the `IReportExportService` and uses the same API of this service as the WinForms controller implementation with the addition of the following method:

`IReportExportService.ExportReport`
:   Exports the specified report to the specified format and returns a [](xref:System.IO.Stream) that can be used to read the exported report data.

A reference to the stream returned by the `ExportReport` method is passed to the `downloadFileFromStream` JavaScript function to force the browser to download an exported _.pdf_ file from this stream.

The result is demonstrated in the image below.

![InstantPrintReport_Blazor](~/images/InstantPrintReport_Blazor.png)
