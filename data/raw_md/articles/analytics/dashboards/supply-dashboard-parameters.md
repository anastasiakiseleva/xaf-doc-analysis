---
uid: "404466"
title: 'Supply Dashboard Parameters (ASP.NET Core Blazor)'
---

# Supply Dashboard Parameters (ASP.NET Core Blazor)

[Dashboard parameters](xref:116918) are dynamic values that can replace constants in filter expressions, calculated fields and other cases. Use one of the techniques described below to supply these values in code.

Review the following table for a summary of all methods that can supply parameter values to Dashboards:

| Method | Sets Initial Values | User-editable | Can Change Current Dashboard Object * | Sets Values on Demand |
| - | - | - | - | - |
| [Custom Dashboard State Service](#use-a-custom-dashboard-state-service) | Yes | Yes | Yes | No |
| [The CustomParameters Event](#use-the-customparameters-event) | Yes | No | Yes | No |
| [The InitialDashboardState Property](#use-the-initialdashboardstate-property) | Yes | Yes | No | No |
| [Dashboard's Client-Side API](#use-the-client-side-javascript-api) | No | Yes | Yes | Yes |

\* For example, this happens if you use [Split Layout](xref:404203) or [Next/Previous Object Actions](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController). On the other hand, the current Dashboard object does not change [when you add a dashboard to navigation](xref:117453).

## Use a Custom Dashboard State Service

You can supply dashboard parameters with the initial [dashboard state](xref:DevExpress.DashboardCommon.DashboardState) if you implement a custom [dashboard state service](xref:DevExpress.DashboardWeb.IDashboardStateService):

**File:** _MySolution.Blazor.Server\\Services\\CustomDashboardStateService.cs_

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.DashboardCommon;
using DevExpress.DashboardWeb;
using System.Xml.Linq;

public class CustomDashboardStateService : IDashboardStateService {
    public DashboardState GetState(string dashboardId, XDocument dashboardDocument) {
        var dashboard = new Dashboard();
        dashboard.LoadFromXDocument(dashboardDocument);
        DashboardState dashboardState = new DashboardState();
        dashboardState.Parameters.Add(new DashboardParameterState("StringParameter", "StringValue", typeof(string)));
        if (dashboard.Parameters.Contains(p => p.Name == "IntParameter")) {
            dashboardState.Parameters.Add(new DashboardParameterState("IntParameter", 123, typeof(int)));
        }
        return dashboardState;
    }
}
```
***

To use the dashboard state service, register it with the [dashboard configurator](xref:DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator):

**File:** _MySolution.Blazor.Server\\Startup.cs_

# [C#](#tab/tabid-csharp)
```csharp{15}
using DevExpress.ExpressApp.Dashboards.Blazor;
using DevExpress.DashboardAspNetCore;
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            builder.Modules
                // ...
                .AddDashboards(options => {
                    options.DashboardDataType = typeof(DashboardData);
                    options.SetupDashboardConfigurator = (dashboardConfigurator, services) => {
                        dashboardConfigurator.SetDashboardStateService(new CustomDashboardStateService());
                    };
                });
            // ...
        })
    }
    // ...
}
```
***

## Use the CustomParameters Event

You can use the `DashboardConfigurator`'s [CustomParameters](xref:DevExpress.DashboardWeb.DashboardConfigurator.CustomParameters) event to supply parameter values.

**File:** _MySolution.Blazor.Server\\Startup.cs_

# [C#](#tab/tabid-csharp)
```csharp{15-20}
using DevExpress.ExpressApp.Dashboards.Blazor;
using DevExpress.DashboardAspNetCore;
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            builder.Modules
                // ...
                .AddDashboards(options => {
                    options.DashboardDataType = typeof(DashboardData);
                    options.SetupDashboardConfigurator = (dashboardConfigurator, services) => {
                        dashboardConfigurator.CustomParameters += (s, e) => {
                            var stringParameter = e.Parameters.FirstOrDefault(p => p.Name == "StringParameter");
                            if (stringParameter is not null) {
                                stringParameter.Value = "StringValue";
                            }
                        };
                    };
                });
            // ...
        })
    }
    // ...
}
```
***

For more information about Dashboard Configurator, refer to the following topic: [Customize the Dashboard Configurator (ASP.NET Core Blazor)](xref:403544).

## Use the InitialDashboardState Property

You can use the `DxDashboardModel.InitialDashboardState` property to supply parameters with the initial [dashboard state](xref:DevExpress.DashboardCommon.DashboardState) and set the initial dashboard state conditionally for a specific view.

**File:** _MySolution.Blazor.Server\\Controllers\\InitialDashboardStateController.cs_

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.DashboardAspNetCore;
using DevExpress.DashboardCommon;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Dashboards.Blazor.Components;
using DevExpress.Persistent.Base;

public class InitialDashboardStateController : ObjectViewController<DetailView, IDashboardData> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<BlazorDashboardViewerViewItem>(this, viewItem => {
            var dashboardState = new DashboardState();
            dashboardState.Parameters.Add(new DashboardParameterState("StringParameter", "StringValue", typeof(string)));
            dashboardState.Parameters.Add(new DashboardParameterState("IntParameter", 123, typeof(int)));
            viewItem.ComponentModel.InitialDashboardState = dashboardState.SaveToJson();
        });
    }
}
```
***

## Use the Client-Side JavaScript API

You can use this technique to set dashboard parameters in response to an event (such as an Action execution).

1. Define a JavaScript function that sets dashboard state based on the parameter values passed to it:

    **File:** _MySolution.Blazor.Server\\Pages\\\_Host.cshtml_

    # [JavaScript](#tab/tabid-javascript)
    ```HTML
    <script>
        window.setDashboardParameters = function (parameters) {
            const dashboardControl = window.xafBlazorDashboard.getDashboardControl();
            if (dashboardControl) {
                dashboardControl.setDashboardState({ Parameters: parameters });
            }
        }
    </script>
    ```
    ***

2. Add a controller that invokes the function above when a condition is met (for example, when a user executes an Action):

    **File:** _MySolution.Blazor.Server\\Controllers\\SetDashboardParametersController.cs_

    # [C#](#tab/tabid-csharp)
    ```csharp{13-16}
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using Microsoft.JSInterop;

    public class SetDashboardParametersController : ObjectViewController<DetailView, IDashboardData> {
        public SetDashboardParametersController() {
            var simpleAction = new SimpleAction(this, "SetDashboardParameters", null);
            simpleAction.Execute += SimpleAction_Execute;
        }
        private void SimpleAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
            var jsRuntime = Application.ServiceProvider.GetRequiredService<IJSRuntime>();
            jsRuntime.InvokeVoidAsync("window.setDashboardParameters", 
                new Dictionary<string, object> {
                    { "StringParameter", "StringValue" },
                    { "IntParameter", 123 } });
        }
    }
    ```
    ***

[`AddDashboards`]: xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.DashboardsApplicationBuilderExtensions.AddDashboards*
[`IDashboardStateService`]: xref:DevExpress.DashboardWeb.IDashboardStateService
[`SetDashboardStateService`]: xref:DevExpress.DashboardWeb.DashboardConfigurator.SetDashboardStateService*
[`DashboardState`]: xref:DevExpress.DashboardCommon.DashboardState
[`DashboardParameterState`]: xref:DevExpress.DashboardCommon.DashboardParameterState
[`LoadFromXDocument`]: xref:DevExpress.DashboardCommon.Dashboard.LoadFromXDocument(System.Xml.Linq.XDocument)
[`SaveToJson`]: xref:DevExpress.DashboardWeb.DashboardStateExtensions.SaveToJson*
[`IJSRuntime`]: xref:Microsoft.JSInterop.IJSRuntime
[`InvokeVoidAsync`]: xref:Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync*
[`setDashboardState`]: xref:js-DevExpress.Dashboard.DashboardControl.setDashboardState(dashboardState)
[`CreateObjectSpace`]: xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)
[`CreateDetailView`]: xref:DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.Object)
[`SetView`]: xref:DevExpress.ExpressApp.Frame.SetView(DevExpress.ExpressApp.View)
