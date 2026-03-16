---
uid: DevExpress.ExpressApp.XafApplication.ServiceProvider
name: ServiceProvider
type: Property
summary: Provides access to @System.IServiceProvider.
syntax:
  content: |-
    [Browsable(false)]
    public IServiceProvider ServiceProvider { get; set; }
  parameters: []
  return:
    type: System.IServiceProvider
    description: An object that implements the @System.IServiceProvider interface.
seealso: []
---

Use this property to obtain an instance of @System.IServiceProvider. For more information, see the following topic: [](xref:404364).

> [!NOTE]
> To use this property in an XAF Windows Forms application, make sure that your application contains an integrated application builder.

You may find the following examples helpful:

* Download files or navigate to a URL using custom XAF Actions: [a code example](https://supportcenter.devexpress.com/ticket/details/t944452/xaf-blazor-how-to-open-an-external-hyper-link-using-an-xaf-action-menu-command-for) that uses the standard ASP.NET Core [NavigationManager](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/routing#uri-and-navigation-state-helpers) service.
* Read a connection string or other values from appsettings.json in code using a ViewController: [a code example](https://supportcenter.devexpress.com/ticket/details/t957990/blazor-how-to-read-connection-string-and-other-values-from-the-configuration-file) that uses the standard ASP.NET Core [IConfiguration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/) service.
* Access HttpContext to get cookies, user agent, client IP address, query string and other request information: [a ticket](https://supportcenter.devexpress.com/ticket/details/t975297/blazor-obtain-request-information-from-httpcontext-query-string-parameter-for-auto-login) with more information on the standard ASP.NET Core [IHttpContextAccessor](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.ihttpcontextaccessor) service.
* Access JSRuntime to call JavaScript from .NET code: [a code example](xref:113653) that uses the standard ASP.NET Core [IJSRuntime](https://learn.microsoft.com/en-us/aspnet/core/blazor/call-javascript-from-dotnet) service.
* [Access IHttpClientFactory to make HTTP requests](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-requests).
