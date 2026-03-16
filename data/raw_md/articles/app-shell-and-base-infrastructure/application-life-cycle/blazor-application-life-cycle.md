---
uid: "405323"
title: ASP.NET Core Blazor Server Application Life Cycle
owner: Vladislav Bogdanov
seealso:
- linkId: https://learn.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle
  linkType: HRef
  altText: ASP.NET Core Razor component lifecycle
- linkId: 404767
- linkId: 403277#differences-between-xaf-blazor-ui-and-xaf-winforms-ui
  altText: Differences between XAF Blazor UI and XAF WinForms UI
---
# ASP.NET Core Blazor Server Application Life Cycle

The following table outlines the main stages in the life cycle of an XAF Blazor application:

| Stage | Description |
|---|---|
| **Host Startup** | The application host starts. At this stage, the system does not create any XAF Application instances, does not access the database, and does not initialize the application model. |
| **Web API Initialization** | If the application includes a Web API service, the system creates an application instance to build the entity data model (EDM) and initialize singleton services such as `ITypesInfo`. This instance is destroyed after initialization. <br/>- In Integrated mode, the created application is a descendant of the @DevExpress.ExpressApp.Blazor.BlazorApplication class. You can use settings of this class, including the [builder.AddBuildStep](xref:DevExpress.ExpressApp.ApplicationBuilder.IXafApplicationBuilder`1.AddBuildStep(System.Action{DevExpress.ExpressApp.XafApplication})) method, to customize the application.<br/>- In Standalone mode, the created application is a `WarmUpApplication` class instance with customization limited to the [builder.AddBuildStep](xref:DevExpress.ExpressApp.ApplicationBuilder.IXafApplicationBuilder`1.AddBuildStep(System.Action{DevExpress.ExpressApp.XafApplication})) method. |
| **User Connects to the Server** | The system establishes a [SignalR hub connection](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/signalr?view=aspnetcore-9.0#control-when-the-reconnection-ui-appears). The `ProxyHubConnectionHandler` initializes the ValueManager storage container for the user session.<br/> To customize this stage, modify the following file: _SolutionName.Blazor.Server/Services/ProxyHubConnectionHandler.cs_.<br/> Note that [Azure SignalR Service](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/server/) requires you to set up the `ProxyHubConnectionHandler` in the _Startup.cs_ file. Refer to the following help topic for more information: [Azure Deployment](xref:403362#azure-deployment).
| **Creation of Circuit** | The `CircuitHandlerProxy` initializes required circuit services.<br/>To customize this stage, implement an `ICircuitHandler` and register it in the _SolutionName.Blazor.Server\Startup.cs_ file:<br/>`services.TryAddEnumerable(ServiceDescriptor.Scoped<ICircuitHandler,CircuitHandlerCustomizer>());` |
| **Logon Form Display** | The system creates an application instance for the logon form. After authentication, this instance is destroyed and the system creates a new application instance for the authenticated user.<br/>For more information, review the following help topic: <xref:113151>.|
| **User Authenticated** | The user is authenticated according to the configured [authentication scheme](xref:404462).<br/>Refer to the following help topic to learn how to customize the current stage of the workflow: <xref:404264>. |
| **Startup Popup Actions** | Startup popup actions (such as [ChangePasswordOnLogon](xref:112649)) are executed. These actions are registered in modules and are shown after authentication.<br/>Override the [`GetStartupActions`](xref:DevExpress.ExpressApp.ModuleBase.GetStartupActions) method in your module to modify the collection of startup actions. |
| **Main Window Display** | The application creates a [Show View Strategy](xref:DevExpress.ExpressApp.ShowViewStrategyBase) instance that displays the main window.<br/>You can use the `GetStartupActions` method to modify the default form creation process or display custom startup Views as described in the following KB article: [How to show a specific View at application startup, right after the logon window or after loading the main window](https://supportcenter.devexpress.com/ticket/details/k18099/how-to-show-a-specific-view-at-application-startup-right-after-the-logon-window-or-after) |
| **Circuit Closed** | The circuit is closed. |
| **Application Disposed** | The application instance is disposed when the Blazor application is closed (for instance, the browser or a tab is closed). If the client disconnects unexpectedly, the server waits one minute for reconnection. If the application client does not respond, the application is disposed. |

> [!important]
> * XAF Blazor authenticates each request. The authentication state is not retained between requests and the request source cannot be identified.
> * XAF Blazor UI supports [Interactive Server render mode](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes) only.