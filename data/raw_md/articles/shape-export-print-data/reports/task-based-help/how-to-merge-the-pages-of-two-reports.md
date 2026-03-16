---
uid: "113606"
seealso: []
title: 'How to: Merge the Pages of Two Reports'
owner: Ekaterina Kiseleva
---
# How to: Merge the Pages of Two Reports

This example demonstrates how to modify report content before it is displayed. For information on how to add a separate report to the end of another report, refer to the [Add a Report to the End/Beginning](xref:400690) topic. [!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

Assume that you have two reports (called _First Report_ and _Second Report_) in your application. To [merge these two reports](xref:3321) right before they are displayed, implement the following helper class, which handles the _First Report_'s [AfterPrint](xref:DevExpress.XtraReports.UI.XRControl.AfterPrint) event. In the event handler, use the [IReportDataSourceHelper](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper) service to generate the _Second Report_ document. Handle the _First Report_'s [ModifyDocument](xref:DevExpress.XtraReports.UI.XtraReport.ModifyDocument(System.Action{DevExpress.XtraReports.IDocumentModifier})) event to append the generated _Second Report_ document's contents to the _First Report_. In this example, pages from the _Second Report_ will be appended to the pages of the _First Report_ when the _First Report_ is previewed.

# [C#](#tab/tabid-csharp)

```csharp{17-20}
using System;
using DevExpress.XtraReports.UI;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2;
// ...
public class MergeReportHelper {
    public static void MergeReportsBeforeShow(ReportLoadedContext context) {
        if (context.Report is XtraReport && context.Report.DisplayName == "First Report") {
            context.Report.AfterPrint += (sender, e) => {
                XtraReport firstReport = sender as XtraReport;

                var objectSpaceFactory = context.ServiceProvider.GetRequiredService<IObjectSpaceFactory>();
                using var objectSpace = objectSpaceFactory.CreateObjectSpace(typeof(ReportDataV2));
                IReportDataV2 reportData = objectSpace.FirstOrDefault<ReportDataV2>(data => data.DisplayName == "Second Report");
                if (reportData != null) {
                    var secondReport = context.ServiceProvider.GetRequiredService<IReportStorage>().LoadReport(reportData);
                    var dataSourceHelper = context.ServiceProvider.GetRequiredService<IReportDataSourceHelper>();
                    dataSourceHelper.SetupReport(secondReport);
                    secondReport.CreateDocument(false);
                    firstReport.ModifyDocument(x => x.AddPages(secondReport.Pages));
                    firstReport.PrintingSystem.ContinuousPageNumbering = true;
                }
            };
        }
    }
}
```

***

The [IReportDataSourceHelper.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.SetupReport*) method call is required to display a report in XAF. Without it, the [data source](xref:113593) will not supply data.

In the application's _Startup.cs file_, add the `OnReportLoaded` event handler to the `builder.Modules.AddReports` method call. In this event handler, call the `MergeReportHelper.MergeReportsBeforeShow` static method as shown below:

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{5-7}
// ...
builder.Modules
    .AddReports(options => {
        // ...
        options.Events.OnReportLoaded = context => {
            MergeReportHelper.MergeReportsBeforeShow(context);
        };
    })
// ...
```

***

The [ReportDataSourceHelper.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReport*) method call is required to display a report in XAF. Without it, the [data source](xref:113593) will not provide data.

Create an instance of the **MergeReportHelper** class after the application setup is complete. You can do it in the [platform-agnostic module](xref:118045) by handling the [XafApplication.SetupComplete](xref:DevExpress.ExpressApp.XafApplication.SetupComplete) event in the overridden [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method.

**File**: _MySolution.Module/Module.cs_

# [C#](#tab/tabid-csharp)

```csharp
public override void Setup(XafApplication application) {
    base.Setup(application);
    application.SetupComplete += delegate(object sender, EventArgs e) {
        new MergeReportHelper(((XafApplication)sender).Modules);
    };
}
```
***
