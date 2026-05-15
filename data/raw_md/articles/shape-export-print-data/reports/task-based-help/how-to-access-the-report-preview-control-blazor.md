---
uid: "402260"
title: 'How to: Access the Report Preview Control (ASP.NET Core Blazor)'
---
# How to: Access the Report Preview Control (ASP.NET Core Blazor)

This example accesses the @DevExpress.Blazor.Reporting.DxReportViewer component that ASP.NET Core Blazor XAF applications use to display reports.

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

## Customize the Report Viewer Toolbar

Handle the @DevExpress.Blazor.DxViewer.OnCustomizeToolbar event to customize the Report Viewer's toolbar.

> [!tip]
> The `ReportViewerModel` object allows you to implement any of the techniques described in the following help topic: <xref:404130>.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2.Blazor;
using Microsoft.AspNetCore.Components;
using DevExpress.Blazor.Reporting.Models;

namespace YourSolutionName.Blazor.Server.Controllers;

public class CustomizeReportViewerToolbar : ViewController<DetailView> {
        public CustomizeReportViewerToolbar() {
            TargetViewId = ReportsBlazorModuleV2.ReportViewerDetailViewName;
        }
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<ReportViewerViewItem>(this, CustomizeToolbar);
    }

    private void CustomizeToolbar(ReportViewerViewItem reportViewerViewItem) {
        reportViewerViewItem.ReportViewerModel.OnCustomizeToolbar = EventCallback.Factory.Create<ToolbarModel>(this, (m) => {
            var customToolbarItem = new ToolbarItem() {
                IconCssClass = "message",
                Text = "Show Message",
                Click = (args) => {
                    Application.ShowViewStrategy.ShowMessage("The button has been clicked", InformationType.Success);
                    return Task.CompletedTask;
                }
            };
            m.AllItems.Add(customToolbarItem);
        });
    }
}  
```