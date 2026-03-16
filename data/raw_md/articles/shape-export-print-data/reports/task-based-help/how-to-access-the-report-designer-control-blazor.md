---
uid: "402261"
title: 'How to: Access the Report Designer Control (Blazor)'
owner: Yekaterina Kiseleva
---
# How to: Access the Report Designer Control (Blazor)

This example demonstrates how to access the Component Model of the @DevExpress.Blazor.Reporting.DxReportDesigner component that ASP.NET Core Blazor XAF applications use to display reports.

When a user customize a report at runtime, an ASP.NET Core Blazor application opens a Detail View that contains **ReportDesignerViewItem**. Follow the steps below to access this View Item and its component:

1. Add the **DevExpress.ExpressApp.ReportsV2.Blazor** NuGet package to the ASP.NET Core Blazor [application project](xref:118045) (_MySolution.Blazor.Server_).
2. Create a [View Controller](xref:112621). Set its @DevExpress.ExpressApp.ViewController.View property to `DetailView` and @DevExpress.ExpressApp.ViewController.TargetViewId to the View's identifier. The `ReportsBlazorModuleV2.ReportDesignerDetailViewName` constant stores this identifier.
3. In the overridden `OnActivated` method, call the @DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0}) method.
4. Use the `ComponentModel` property to access properties of the Report Designer.

[!include[<MySolution.Blazor.Server\Controllers\AccessReportDesignerController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2.Blazor;
// ...
public class AccessReportDesignerController : ViewController<DetailView> {
    public AccessReportDesignerController() {
        TargetViewId = ReportsBlazorModuleV2.ReportDesignerDetailViewName;
    }
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<ReportDesignerViewItem>(this, CustomizeDesignerViewItem);
    }
    private void CustomizeDesignerViewItem(ReportDesignerViewItem designerDetailItem) {
        // Access the Report Viewer properties
        string reportName = designerDetailItem.ComponentModel.ReportName;
        // ...
    }
}
```

***
