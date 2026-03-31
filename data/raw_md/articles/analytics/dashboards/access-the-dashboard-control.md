---
uid: "117454"
seealso: []
title: 'Access the Dashboard Control'
seealso:
  - linkId: '404466'
---
# Access the Dashboard Control

This topic describes how to access the @DevExpress.DashboardWin.DashboardViewer control in a WinForms application and the @DevExpress.DashboardBlazor.DxDashboard component model in an ASP.NET Core Blazor application.

> [!NOTE]
> Refer to the following help topic for information on how to access the @DevExpress.DashboardWin.DashboardDesigner control: [How to: Access the WinForms Dashboard Designer](xref:117716).

> [!IMPORTANT]
> Before you proceed, ensure that your platform-specific [application project](xref:118045) references the corresponding assemblies or NuGet packages:
>  * **WinForms**: the _DevExpress.Dashboard.v<:xx.x:>.Win.dll_ and _DevExpress.ExpressApp.Dashboards.Win.v<:xx.x:>.dll_ assemblies;
>  * **ASP.NET Core Blazor**: the _DevExpress.ExpressApp.Dashboards.Blazor.<:xx.x:>_ NuGet package.

## ASP.NET Core Blazor Applications

To access the @DevExpress.DashboardBlazor.DxDashboard component model, follow the steps below in the ASP.NET Core Blazor [application project](xref:118045) (_MySolution.Blazor.Server_) and WinForms [application project](xref:118045) (_MySolution.Win_). A component model defines a Blazor component in code. When you modify the model, the underlying component reflects these changes. Refer to the following help topic for more information on component models: [](xref:404767).

1. Add a [Controller](xref:112621) activated in the Dashboard Views.
2. In the Controller's `OnActivated` method, use the [](xref:DevExpress.ExpressApp.DashboardViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DashboardView,DevExpress.ExpressApp.Controller,System.Action{``0})) extension method to customize the `BlazorDashboardViewerViewItem` before the [DxDashboard](xref:DevExpress.DashboardBlazor.DxDashboard) component is rendered.
3. In the `CustomizeViewItemControl` method access the `BlazorDashboardViewerViewItem.ComponentModel` property (in ASP.NET Core Blazor applications) or `WinDashboardViewerViewItem.Viewer` (in Windows Forms applications).

The following code snippet sets the default dashboard working mode to `Designer`:

[!include[<MySolution.Blazor.Server\Controllers\BlazorDashboardController.cs>](~/templates/platform_specific_file_path.md)]

# [BlazorDashboardController.cs](#tab/tabid-csharp-blazor)

```csharp
using DevExpress.DashboardWeb;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Dashboards.Blazor.Components;
using DevExpress.Persistent.Base;

namespace MySolution.Blazor.Server.Controllers;
public class BlazorDashboardController : ObjectViewController<DetailView, IDashboardData> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<BlazorDashboardViewerViewItem>(this, item => {
            item.ComponentModel.WorkingMode = WorkingMode.Designer;
        });
    }
}
```

***

[!include[](~/templates/dashboard-view-item-customization-tip.md)]

The following code snippet enables Dashboard data printing:

**WinForms**  
[!include[<MySolution.Win\Controllers\WinDashboardController.cs>](~/templates/platform_specific_file_path.md)]
# [WinDashboardController.cs](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Dashboards.Win;

namespace MainDemo.Win.Controllers;
public class WinDashboardController : ObjectViewController<DetailView, IDashboardData> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<WinDashboardViewerViewItem>(this, item => {
            if (item.Control != null) {
                var dashboardViewer = ((WinDashboardViewerViewItem)item).Viewer;
                if (dashboardViewer != null) {
                    dashboardViewer.AllowPrintDashboardItems = true;
                }
            }
        });
    }
}
```
***
