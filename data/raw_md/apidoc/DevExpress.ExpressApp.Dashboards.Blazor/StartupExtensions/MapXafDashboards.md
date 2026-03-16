---
uid: DevExpress.ExpressApp.Dashboards.Blazor.StartupExtensions.MapXafDashboards(Microsoft.AspNetCore.Routing.IEndpointRouteBuilder,System.String,System.String)
name: MapXafDashboards(IEndpointRouteBuilder, String, String)
type: Method
summary: Registers the required [Dashboards Module](xref:117449) routes in the application's @Microsoft.AspNetCore.Routing.IEndpointRouteBuilder.
syntax:
  content: public static void MapXafDashboards(this IEndpointRouteBuilder endpoints, string dashboardEndpoint = "api/dashboard", string dashboardControllerName = "XafBlazorDashboard")
  parameters:
  - id: endpoints
    type: Microsoft.AspNetCore.Routing.IEndpointRouteBuilder
    description: The application's route builder.
  - id: dashboardEndpoint
    type: System.String
    defaultValue: "\"api/dashboard\""
    description: The endpoint URL prefix used to send data requests to a server.
  - id: dashboardControllerName
    type: System.String
    defaultValue: "\"XafBlazorDashboard\""
    description: The Controller name without the `Controller` suffix.
seealso: []
---
Call this method in the **Startup.Configure** method when you [add the Dashboards Module to your ASP.NET Core Blazor application](xref:117449#add-the-dashboards-module-to-your-application):

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp)
```csharp{9}
using DevExpress.ExpressApp.Dashboards.Blazor;
// ...
public class Startup {
    // ...
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env) {
        // ...
        app.UseEndpoints(endpoints => {
            endpoints.MapXafDashboards();
            // ...
        }
    }
    // ...
}
```
***

[`UseEndpoints`]: xref:Microsoft.AspNetCore.Builder.EndpointRoutingApplicationBuilderExtensions.UseEndpoints*
