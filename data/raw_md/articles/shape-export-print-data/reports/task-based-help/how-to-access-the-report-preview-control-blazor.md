---
uid: "402260"
title: 'How to: Access the Report Preview Control (ASP.NET Core Blazor)'
owner: Anastasiya Kisialeva
---
# How to: Access the Report Preview Control (ASP.NET Core Blazor)

This example accesses the @DevExpress.Blazor.Reporting.DxDocumentViewer component that ASP.NET Core Blazor XAF applications use to display reports.

When a user previews a report, an XAF ASP.NET Core Blazor application opens a Detail View that contains a `ReportViewerViewItem`. Follow the steps below to access this View Item and its component:

1. Add the Reports V2 Module to your application. For more information, refer to the following topic: [](xref:404243).
2. Create a Detail [View Controller](xref:112621) and specify the  @DevExpress.ExpressApp.ViewController.TargetViewId as `ReportsBlazorModuleV2.ReportViewerDetailViewName`.
3. Override the `OnActivated` method and access the Report Viewer's control as demonstrated in the following code snippet:
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.ReportsV2.Blazor;
    using DevExpress.XtraReports;

    namespace YourSolutionName.Blazor.Server.Controllers;

    public class AccessReportViewerController : ViewController<DetailView> {

        public AccessReportViewerController() {
            TargetViewId = ReportsBlazorModuleV2.ReportViewerDetailViewName;
        }

        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<ReportViewerViewItem>(this, CustomizeReportViewerViewItem);
        }

        private void CustomizeReportViewerViewItem(ReportViewerViewItem reportViewerViewItem) {
            //Access the Report Viewer's control.
            IReport report = reportViewerViewItem.ReportViewerModel.Report;
            // ...
        }
    }
    ```