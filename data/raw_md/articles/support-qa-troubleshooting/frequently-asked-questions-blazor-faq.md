---
uid: "403277"
title: Frequently Asked Questions - Blazor UI (FAQ)
---
# Frequently Asked Questions - Blazor UI (FAQ)

## Differences between XAF Blazor UI and XAF WinForms UI


**Q:** Why do XAF Blazor UI apps implement different behavior/options?

**A:** ASP.NET Core Blazor and .NET WinForms are three distinct Microsoft technologies/frameworks, with release dates about 20 years apart. Platform architecture is naturally very different: the view on application development and security has evolved, as did usage scenarios and developer requirements. And you may not be sure, given the platform choice, if you should go with a "proven and tested" versus "most modern" technology.

Even though Blazor is the youngest of the three, we believe it is ready for most line-of-business applications. We recommend that you use XAF Blazor UI for new applications. You can also transfer existing apps.

XAF Blazor UI offers numerous unique benefits over Web Forms such as the following:

* .NET vs .NET Framework ([review a comparison by Microsoft](https://learn.microsoft.com/en-us/dotnet/standard/choosing-core-framework-server)).
* Cross-platform support (run on multiple platforms - Windows, Linux, and macOS - and use desktop and mobile web browsers).
* [More flexible deployment](xref:403362) (use a cloud provider such as Azure, Docker containers hosted in Linux or Windows infrastructure, or even Kubernetes for increased performance/scalability).
* [Dependency Injection](xref:404364) and microservice architecture support (add, replace, or extend XAF services/modules).
* [Backend Web API Service](xref:403394) (consume XAF data and business logic from any external application or service).
* [Entity Framework Core](xref:404186) (access data using the ORM developed by Microsoft and used by millions of developers).
* [Multi-Tenancy Module](xref:404436) (implement multi-tenant or SaaS-ready applications with multiple databases).
* [OAuth2 Authentication](xref:402197) (use Microsoft Entra ID or Google providers).
* [End-User/Runtime Layout Customization](xref:404353) (create and manage detail form UI directly in the web browser).

If you migrate your applications, keep in mind that not all solutions applicable to WinForms or Web Forms are suitable for Blazor. Our approach towards Blazor development does not mean identical replication of behavior from our Web Forms or WinForms modules and features. You may need to adjust your applications if you transition to Blazor.

If you find reasons against transition, you can continue using the WinForms UI. In such cases, please let us know why you chose not to migrate. Reach out to us at our [Support Center](https://supportcenter.devexpress.com/ticket/list?preset=mytickets) and tell us about your use cases and requirements. Your feedback and insights are incredibly valuable in shaping our offerings to best meet your needs.

## Reuse Existing .NET Framework Code

**Q:** I want to create a Blazor UI application based on an existing XAF .NET Framework application. How do I proceed? 

**A:** You can re-use most ORM data models and platform-agnostic controllers in Blazor UI with minimal or no changes. The basic CRUD and data view XAF APIs are platform-agnostic, for example, [](xref:DevExpress.ExpressApp.IObjectSpace), [](xref:DevExpress.ExpressApp.ViewController), [](xref:DevExpress.ExpressApp.View), or [](xref:DevExpress.ExpressApp.Frame).

You can add existing platform-independent modules to an XAF Blazor UI project. You can convert required modules to .NET 8+: [.NET Support and Migration from .NET Framework](xref:401253). Once conversion is complete, refer to the following help topic section for further details: ([Register a Built-in XAF Module](xref:118047)). 

All platform-dependent code should be rewritten. Blazor applications have a different architecture and life cycle; the code that was common for ASP.NET Web Forms and Windows Forms may need to be changed for Blazor. Refer to the following article for more information: [An introduction to Blazor for ASP.NET Web Forms developers](https://learn.microsoft.com/en-us/dotnet/architecture/blazor-for-web-forms-developers/introduction).

## Add a Custom XAF Module

**Q:** How do I add a new custom XAF module to an existing Blazor solution?

**A:** Refer to the following documentation topic for instructions: <xref:405523>. 

## Integrate Custom UI Components

**Q:** How do I use components that are not integrated in the Blazor UI by default?

**A:** Review the list of DevExpress [Blazor](https://demos.devexpress.com/blazor/) and [JavaScript (DevExtreme)](https://js.devexpress.com/Demos/) UI components and the following XAF integration articles: 

- [Implement a List Editor Based on a Custom Component](xref:403258)
    * [Pivot Grid](https://supportcenter.devexpress.com/ticket/details/t994515/blazor-how-to-integrate-the-pivot-grid-into-an-xaf-app)
    * [TreeList](xref:DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor)
- [Access Grid Control Settings](xref:402154)
- [Implement a Property Editor Based on a Custom Component](xref:402189)
    * [Simple Button](xref:113653)
    * [Multiple File Upload, Tag Box, Lookup, Markup Content Property Editors](https://github.com/eXpandFramework/Reactive.XAF/tree/master/src/Modules/Blazor)
    * [Progress Bar in Grid List Editor Cells](https://supportcenter.devexpress.com/ticket/details/t1003220/blazor-how-to-implement-a-progress-bar-in-grid-list-editor-cells)
- [Access Detail View Property Editor Settings](xref:402153) | [Customize a Built-in Property Editor](xref:402188)
- [Add DevExtreme Widgets to an Application](xref:403578)
- [Integrate a custom DevExtreme component and bind it to a data source](https://supportcenter.devexpress.com/ticket/details/t943982/blazor-how-to-integrate-a-custom-devextreme-component-and-bind-it-to-a-data-source)

- [Show a fully custom non-XAF web form (with custom controls, JavaScript, Razor components, etc.)](https://supportcenter.devexpress.com/ticket/details/t939883/blazor-how-to-show-a-fully-custom-non-xaf-web-page-with-custom-controls-javascript-razor)
- [How to implement a QR / barcode scanner using a camera of a mobile device](https://supportcenter.devexpress.com/ticket/details/t867142/xaf-blazor-how-to-implement-a-qr-barcode-scanner-using-a-camera-of-a-mobile-device)
- [Create a Custom Blazor Application Template](xref:403452)
- [Implement a custom Action type](https://supportcenter.devexpress.com/ticket/details/t1101292/xaf-blazor-how-to-create-a-custom-action-type)
- [Control Property Visibility in Filter Editors](xref:113564#property-visibility-customization-in-filter-editors)
- [](xref:404698)
- [](xref:404700)
- [](xref:404428#aspnet-core-blazor)

You can review how we implement List and Property Editors. This may help you integrate custom components. See the files in the following folder: _[!include[Localization-Overview-Intro](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp\DevExpress.ExpressApp.Blazor\Editors\_.

## Access ASP.NET Core DI Services through IServiceProvider

**Q:** How do I access services from a built-in ASP.NET Core service container (IServiceProvider)?

**A:** To access `BlazorApplication.IServiceProvider`, use the following code: [XafApplication.ServiceProvider](xref:DevExpress.ExpressApp.XafApplication.ServiceProvider). For more information, see the following topic: [](xref:404364).

You may find the following examples helpful:

* Download files or navigate to a URL using custom XAF Actions: [a code example](https://supportcenter.devexpress.com/ticket/details/t944452/xaf-blazor-how-to-open-an-external-hyper-link-using-an-xaf-action-menu-command-for) that uses the standard ASP.NET Core [NavigationManager](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/routing#uri-and-navigation-state-helpers) service.
* Read a connection string or other values from appsettings.json in code using a ViewController: [a code example](https://supportcenter.devexpress.com/ticket/details/t957990/blazor-how-to-read-connection-string-and-other-values-from-the-configuration-file) that uses the standard ASP.NET Core [IConfiguration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration) service.
* Access HttpContext to get cookies, user agent, client IP address, query string and other request information: [a ticket](https://supportcenter.devexpress.com/ticket/details/t975297/blazor-obtain-request-information-from-httpcontext-query-string-parameter-for-auto-login) with more information on the standard ASP.NET Core [IHttpContextAccessor](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.ihttpcontextaccessor) service.
* Access JSRuntime to call JavaScript from .NET code: [a code example](xref:403531#create-a-server-side-controller) that uses the standard ASP.NET Core [IJSRuntime](https://learn.microsoft.com/en-us/aspnet/core/blazor/call-javascript-from-dotnet) service.<!-- TODO --> 
* [Access IHttpClientFactory to make HTTP requests](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-requests).


## Using GPS and Camera on Mobile Devices

**Q:** Can I upload photos from a mobile device camera in XAF Blazor apps?

**A:** Yes. Evolving web development standards and modern browsers made it possible to accomplish many hardware-related tasks (GPS, camera, etc.) in such applications. See also: [How to implement a QR / barcode scanner using a camera of a mobile device](https://supportcenter.devexpress.com/ticket/details/t867142/xaf-blazor-how-to-implement-a-qr-barcode-scanner-using-a-camera-of-a-mobile-device).

![XAF Blazor Server Mobile Upload Files](~/images/XAF_Blazor_Server_Mobile_Upload_Files.png)

## Deployment

**Q:** Can I deploy XAF Blazor apps to Cloud platforms (Azure, AWS, etc.), Linux (with Nginx or Apache), Windows (with IIS), Docker, and Kubernetes?

**A:** Yes, absolutely. For more information, refer to the following help topics:

* [](xref:403362)
* [](xref:404613)
* [](xref:404614)
* [](xref:404717)

## High Load and Scaling

**Q:** Is Blazor UI appropriate for applications with thousands of concurrent users?
    
**A:** We cannot recommend XAF's Blazor UI for high-load applications that should serve hundreds or thousands of concurrent web clients on a single web server. Refer to the following topic for details: [Deployment Recommendations for XAF Blazor UI Applications](xref:403362).

## Offline Mode Support

**Q:** Does XAF Blazor UI support offline mode?

**A:** No. The current Blazor Server platform requires a permanent connection to a server. 

## Supported Identity Providers

**Q:** Does XAF's Blazor UI support OAuth2 (Azure AD, Microsoft 365, Google Firebase, etc.) or JWT authentication (Identity Server, Auth0, etc.)?

**A:** Yes, XAF supports these identity providers with the help of built-in ASP.NET Core capabilities and XAF's security system extensibility. You may find the following examples helpful:
- [How to: Use Active Directory and OAuth2 Authentication Providers in Blazor Applications](xref:402197)
- [Identity Server usage example](https://github.com/biohazard999/IDSDemoXaf)
- [Xenial Identity: Pure XPO based IdentityServer](https://www.youtube.com/watch?v=9Nlq2HCfMFU)

## Supported Browsers

**Q:** What are the supported desktop and mobile web browsers?

**A:** You can find the supported browser list in the following Microsoft article: [https://learn.microsoft.com/en-us/aspnet/core/blazor/supported-platforms](https://learn.microsoft.com/en-us/aspnet/core/blazor/supported-platforms) (Microsoft Internet Explorer 11 and older versions are not supported).

We test the XAF Blazor UI in the following environments:

- The latest desktop Google Chrome and Mozilla FireFox versions (automated tests and screenshot-based tests with EasyTest and Selenium).
- The latest versions of Google Chrome on Android, Safari (including iOS), and Microsoft Edge (manual testing).

## Keep Connection Alive

The XAF Blazor UI is a regular ASP.NET Core Blazor Server application that uses `SignalR` to keep a connection to the server alive. Use the following solution to manage this behavior: [Timeout and keepalive settings](https://learn.microsoft.com/en-us/aspnet/signalr/overview/guide-to-the-api/handling-connection-lifetime-events#timeoutkeepalive).

## Blazor WebAssembly

**Q:** Does XAF Blazor UI support WebAssembly?

**A:** XAF Blazor UI generates an application based on the [Blazor Server](https://learn.microsoft.com/en-us/aspnet/core/blazor/hosting-models#blazor-server) hosting model. You can also build a custom Blazor WebAssembly app and reuse parts of your XAF project: data model, select modules (such as Security, Reporting, File Attachments), and custom logic. Use our backend [Web API Service](xref:403394) for this purpose. Review the corresponding [GitHub Example & Tutorial](https://go.devexpress.com/XAF_Security_NonXAF_Blazor_WebAssembly.aspx) for more information.
