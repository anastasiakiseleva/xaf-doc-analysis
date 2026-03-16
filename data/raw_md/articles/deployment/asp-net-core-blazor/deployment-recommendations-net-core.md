---
uid: "403362"
title: 'Deployment Recommendations for XAF ASP.NET Core Applications (Blazor Server, Middle Tier Server, or Web API Service)'
owner: Alexey Kazakov
---
# Deployment Recommendations for XAF ASP.NET Core Applications (Blazor Server, Middle Tier Server, or Web API Service)

> [!NOTE]
>
> Single-file deployment and executable option ([`<PublishSingleFile>`](https://docs.microsoft.com/en-us/dotnet/core/deploying/single-file)) is not supported.

## Azure Deployment

You can deploy XAF's ASP.NET Core applications to Azure. Refer to the following topic for step-by-step instructions:

* [Deploy a XAF ASP.NET Core Application to Azure App Service](xref:404614)

If you are new to Azure, refer to the following Microsoft deployment topic: [Host and deploy ASP.NET Core Blazor Server](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/server). 

Popular Azure deployment options for Blazor Server applications include:

- The default option with no additional settings and no WebSockets.
- [Application Request Routing (ARR)](https://learn.microsoft.com/en-us/aspnet/core/signalr/publish-to-azure-web-app?#configure-the-app-in-azure-app-service).
- [Azure SignalR Service](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/server#azure-signalr-service). This option requires additional setup in the _SolutionName.Blazor.Server/Startup.cs_ file. If you miss `ProxyHubConnectionHandler` in this file, you may receive the following error message: `"ValueManagerStorageAccessor.Storage is null likely due to incorrect Azure SignalR Service or Blazor application settings"`.
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    public void ConfigureServices(IServiceCollection services) {
        services.AddSingleton(
            typeof(HubConnectionHandler<>),
            typeof(ProxyHubConnectionHandler<>)
        );
    //...
    }
    ```
    ***
 

> [!NOTE]
>
> Set the static [AzureCompatibility.Enable](xref:DevExpress.Utils.AzureCompatibility.Enable) property to **true** at the application startup (at the top of the ConfigureServices method in the _SolutionName.Blazor.Server/Startup.cs_ file) to resolve issues with rendering and printing in Rich Text Editor, RichEditDocumentServer, Reports and PDF Export libraries on the Microsoft Azure Web Sites.


## Windows and Linux Deployment

You can deploy XAF ASP.NET Core application in Windows with IIS or Linux with Nginx/Apache (with or without Docker/Kubernetes). Refer to the following topics for more information on how to deploy your XAF ASP.NET Core (Blazor, Middle Tier Server or WebAPI) application to IIS and Linux:

* <xref:404613>
* <xref:404717>
* <xref:113238>

When you deploy your Blazor apps to IIS, activate the following features: 

- [WebSocket Protocol](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets#enabling-websockets-on-iis) 
- [Sticky sessions with Application Request Routing](https://learn.microsoft.com/en-us/iis/extensions/configuring-application-request-routing-arr/http-load-balancing-using-application-request-routing)

If your application includes [Reports](xref:113591), [Office](xref:400003) or [Dashboards](xref:117449) modules, and you're running it on Linux or macOS, additional setup may be required. If you encounter any issues with rendering or exporting documents and dashboards, consult the following help topics:

[!include[deployment-non-windows-additional-setup-links](~/templates/deployment-non-windows-additional-setup-links.md)]

You may also find these community resources helpful: 

- [Deploy and scale an XAF Blazor Server app: use Azure Kubernetes Service to serve hundreds of users](https://github.com/DevExpress/XAF-Blazor-Kubernetes-example)
- [XAF in Linux (Video by Joche Ojeda)](https://www.youtube.com/watch?v=tuOz914WdJk)
- [Monitor XAF's Blazor App on Ubuntu (Video by Joche Ojeda)](https://www.youtube.com/watch?v=DR3bva32jrw)
- [XAF Blazor .NET CLI application templates for Linux or macOS (by Joche Ojeda)](https://github.com/egarim/XafBlazorAndApiDotNetNew)


## High Load Scenarios, Load Testing, and Scalability

ASP.NET Core Blazor Server technology is designed to store the user's state in memory to combine fast responses to user actions with server-side data processing. This stateful architecture means that memory consumption increases with each user. After a certain number of simultaneous users, the application can reach its hosting machine's memory limit.

We cannot provide a universal calculator for web server hardware/software requirements, nor can we comment on overall performance without tests (every application is unique). The complexity of your business model and implemented behaviors are significant factors in throughput/performance. Ultimately, performance will depend on development decisions, application type, environment, and even tested use-case scenarios. A few examples of factors that affect application performance are the number of persistent classes and their fields, Controller design, Application Model customizations, availability of memory intensive operations to end-users (frequent import/export of large data amounts, or complex report generation).
    
XAF Blazor apps are stateful and are mostly used in a local Intranet with a limited set of users (often deployed internally). We cannot recommend XAF's Blazor UI for high-load applications that should serve hundreds or thousands of concurrent web clients on a single web server (even with vertical scaling). You can horizontally scale an XAF Blazor UI application with multiple web servers and loading balancing using standard ASP.NET deployment methods. Even with horizontal scaling, we recommend that you carefully:
- Test your XAF Web apps under conditions close to your production environment. Emulate the user load.
- Measure performance over time and decide on XAF's suitability after that.

You may find these community resources helpful:
 - [Deploy and scale an XAF Blazor Server app: use Azure Kubernetes Service to serve hundreds of users](https://github.com/DevExpress/XAF-Blazor-Kubernetes-example)
 - [XAF Blazor load testing on Linux and MySql using Puppeteer and GitHub Actions](https://github.com/DevExpress/xaf-blazor-app-load-testing-example)
 - [XAF ASP.NET Core Blazor UI deployment, scalability and load testing considerations](https://supportcenter.devexpress.com/ticket/details/s36497/xaf-asp-net-webforms-blazor-ui-deployment-scalability-and-load-testing-considerations)
 - [XAF Blazor load test with 100 clients (Video by Joche Ojeda)](https://www.youtube.com/watch?v=rPm41VEAM2Q)

## Cross-Platform Desktop Apps With Electron.NET

You can build cross platform desktop apps with ASP.NET Core (Razor Pages, MVC, Blazor). [Electron.NET](https://github.com/ElectronNET/Electron.NET) is a wrapper around a regular Electron application with an embedded ASP.NET Core application. The current Electron.NET CLI builds Windows/macOS/Linux binaries. For more information, watch the following video by Joche Ojeda: [XAF with Electron for Windows, MacOS and Linux](https://www.youtube.com/watch?v=8oMtdwKiiXo).

> [!NOTE]
> 
>DevExpress does not assist in administering web servers or hosting environments for customers. We do not consult on various server and operating system configurations as part of our support services. For more information, please review [the "Prerequisites" and "Technical Support Scope" sections](https://www.devexpress.com/products/net/application_framework/xaf-considerations-for-newcomers.xml). If you experience issues, we recommend that you first make sure that your deployment scenario works without XAF. Try a pure Blazor Server app (with the same database and XPO or EF Core for data access). Once you resolve issues with that application, an XAF Blazor app should work as expected.

## .NET Aspire Integration for Deployment and Development Environments

[.NET Aspire](https://learn.microsoft.com/en-us/dotnet/aspire/get-started/aspire-overview) is a collection of tools, templates, and packages for developing observable, production-ready applications. You can integrate .NET Aspire into your XAF Blazor application and utilize its orchestration features. Benefits include: 

* Simplify long and error-prone setup processes like those we describe in our documentation for [Azure App Service](xref:404614) and [Nginx](xref:404717) support on Linux, as well as other popular web server configurations.
* Provision required databases and other application resources for both development and deployment environments (for instance, using a [Docker setup](https://community.devexpress.com/blogs/news/archive/2023/04/06/develop-a-devexpress-xaf-and-web-api-solution-in-docker.aspx)).

Refer to the following documents for additional information on how to use Aspire tools in your XAF project:

* [.NET Aspire Support for an XAF Blazor Project- Introduction](https://community.devexpress.com/Blogs/news/archive/2025/03/25/net-aspire-support-for-an-xaf-blazor-project.aspx) | [GitHub example](https://github.com/DevExpress-Examples/xaf-blazor-aspire-support)
* [Custom Telemetry, Service Orchestration, Database Dependency](https://community.devexpress.com/Blogs/news/archive/2025/04/21/net-aspire-xaf-blazor-custom-telemetry-service-orchestration-database-dependency.aspx) | [GitHub example](https://github.com/DevExpress-Examples/xaf-blazor-aspire-advanced)