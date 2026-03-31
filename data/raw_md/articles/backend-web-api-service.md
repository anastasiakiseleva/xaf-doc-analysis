---
uid: "403394"
title: 'Backend Web API Service / REST API'
---
# Backend Web API Service / REST API
## Overview

The [Template Kit](xref:405447) creates a back-end **Web API Service (Web API)** with integrated authorization and CRUD operations powered by Microsoft EF Core and DevExpress XPO ORM library. You can use OAuth2, JWT, or custom strategies for authentication. The built-in [Security System](xref:113366) also filters out secure server data based on permissions granted to users.

The **Web API** creates URLs (endpoints) that allow you to perform CRUD operations from your non-XAF UI applications (for instance, .NET MAUI, JavaScript, or Blazor clients). It uses [ASP.NET Core OData](https://github.com/OData/AspNetCoreOData) to support paging, filters, and other OData options. This service can be hosted as part of a Blazor Server project or as a standalone ASP.NET Core project.

The **Web API** utilizes [Swagger (OpenAPI)](https://swagger.io/) to display and test endpoints. You can also test endpoints or consume the Web API with other platforms (for example, [Postman](https://www.postman.com/product/), .NET, or JavaScript).

![|XAF Web API](~/images/web-api.png)


The basic functions of our Web API Service (including the [Template Kit](xref:405447)) are available for free as part of our [.NET App Security & Web API Service](https://www.devexpress.com/products/net/application_framework/security-web-api-service.xml) **free offer**. To register your free copy today, please visit our [.NET App Security & Web API – Free Offer from DevExpress](https://www.devexpress.com/security-api-free/) page.

Additional services/benefits of our Web API Service ship as part of the DevExpress [Universal Subscription](https://www.devexpress.com/subscriptions/universal.xml) and include:
- Technical support and full source code.
- XAF's administrative UI to manage users and roles at runtime using WinForms and ASP.NET Core Blazor apps: [Getting Started Tutorial](xref:402125) | [Demos](https://www.devexpress.com/support/demos/?mtm_campaign=XAF&mtm_kwd=use-odata-to-send-requests#xaf).
- Localization functions (endpoints to obtain localized captions for classes, members, and custom UI elements).
- Advanced/enterprise functions such as audit trail, endpoints to download reports, file attachments, check validation, etc.

![|XAF's Blazor UI Demo, DevExpress|](~/images/xaf-blazor-ui-demo-devexpress.png)

**See Also**
- [Frequently Asked Questions](https://supportcenter.devexpress.com/ticket/details/t886740/faq-net-app-security-web-api-for-ef-core-xpo-orm) 
- [Overview and Tutorial Videos](https://www.youtube.com/playlist?list=PL8h4jt35t1wiM1IOux04-8DiofuMEB33G)
- [Survey - Your Feedback Matters](https://community.devexpress.com/blogs/news/archive/2022/06/20/a-one-click-solution-for-role-based-access-control-asp-net-core-web-api-services-via-entity-framework-core-and-xpo-v22-1.aspx#survey)

## How to Use

You can add the **Web API** to an existing Blazor Server project or create a new project with this service:

* [](xref:403401)
* [](xref:403561)

After you add the Web API to your project, you can use it as described in the following topics:

* [](xref:403551)
* [](xref:403715)
* [](xref:403850)
* [](xref:403858)
* [](xref:403861)

Additionally, review our GitHub examples:

* [JavaScript with DevExtreme + ASP.NET Core Web API/OData App](https://go.devexpress.com/XAF_Security_NonXAF_DevExtreme_OData.aspx)
* [JavaScript with Svelte + ASP.NET Core Web API/OData App](https://github.com/oliversturm/demo-dx-webapi-js/tree/stage-4)
* [Blazor WebAssembly App](https://go.devexpress.com/XAF_Security_NonXAF_Blazor_WebAssembly.aspx)
* [.NET MAUI (iOS/Android) App](https://go.devexpress.com/XAF_Security_NonXAF_MAUI.aspx)
* [WinForms Application (with OData)](https://github.com/DevExpress-Examples/connect-winforms-grid-to-webapi-service)

## Authentication Options

The **Web API** supports all standard ASP.NET Core [authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication) techniques that you can specify in the _MySolution.WebApi\Startup.cs (MySolution.Blazor.Server.Startup.cs)_ file. See the following topic for details: [Authentication in Web API Projects](xref:403413).

## Performance Considerations

You can disable logging to improve the **Web API** performance. To do this, set the **LogLevel.DevExpress.ExpressApp** option to _None_.

**File:** _MySolution.Blazor.Server\appsettings.json_
(_MySolution.Blazor.Server\appsettings.Development.json_ for debugging)
# [JSON](#tab/tabid-json)

```JSON{6}
// ...
"LogLevel": {
    "Default": "Information",
    "Microsoft": "Warning",
    "Microsoft.Hosting.Lifetime": "Information",
    "DevExpress.ExpressApp": "None"
}
// ...
```
***

Use logging options other than _None_ (for example, `DevExpress.ExpressApp =  Debug`) only for debugging purposes because logging reduces performance. See the following topic for more information: [Log Files](xref:112575).

## Limitations

- The capability to use [custom fields](xref:113583) in an XPO data model is not supported. The underlying ASP.NET Core Web API / OData v4 infrastructure accesses type information directly through reflection in the form of [System.Type](xref:System.Type) objects, which do not contain information about custom fields.

## FAQ

**Q: Is the .NET App Security & Web API free for commercial use?**

**A:** Absolutely. .NET App Security & Web API is available free-of-charge. To download your copy, visit: [https://www.devexpress.com/security-api-free/](https://www.devexpress.com/security-api-free/).

When you register for a free DevExpress product, you can use your registered product for as long as your needs dictate. Should an update be made available free-of-charge, you will be notified by email or on this website. Updates that are issued free-of-charge can also be used indefinitely. Please refer to the DevExpress [End User License Agreement](https://www.devexpress.com/Support/EULAs/security-api.xml) for detailed licensing information.

**Q: Do I have to include XAF UI dependencies in my project?**

**A:** Our Web API Service relies on Visual Studio 2022 and a few non-visual cross-platform .NET packages ([example](https://nuget.devexpress.com/packages/DevExpress.ExpressApp.Api.EFCore.All/22.1.5)). These include DevExpress.Data, DevExpress.Xpo, DevExpress.Document.Processor, and other core libraries. Though these packages have "XAF" or "ExpressApp" in their names, you do not need to pull XAF WinForms and ASP.NET Core Blazor dependencies in your projects.

In other words, if you do not require XAF, you are not forced to use it. Optionally, you can tell the [Template Kit](xref:405447) to create the Web API Service inside an XAF Blazor UI app. This could be helpful to those who wish to incorporate a web Admin Panel ([watch the video](https://www.youtube.com/watch?v=aV8YJ7LjW74&feature=youtu.be)) and an embedded API server within the same package (for easier hosting and maintenance). Again, this is entirely up to you. You can always use the Web API Service on a standalone basis.

**Q: Will I benefit from the Web API Service if I’m not developing XAF UI apps?**

**A:** Our Web API Service can be used outside of XAF-powered UI apps. Numerous developers have successfully used our Web API Service as a backend for their Angular, Vue, React, Blazor WebAssembly, Xamarin, and other .NET/JavaScript UI clients.

For more information in this regard, check out [our DevExtreme example on GitHub](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/22.1.1%2B/EFCore/ASP.NetCore/DevExtreme.OData). This example uses our client-side dxDataGrid with DevExpress.Data.ODataStore (just like many other CRUD apps powered by DevExtreme). We've also published a [video series where we built a .NET MAUI mobile app](https://www.youtube.com/playlist?list=PL8h4jt35t1wiM1IOux04-8DiofuMEB33G) that consumes our Web API Service (see also [.NET MAUI example sources](https://go.devexpress.com/XAF_Security_NonXAF_MAUI_EFCore.aspx)).

**Q: Do I have to learn a lot of XAF terminology to consume the Web API?**

**A:** As far as clients or consumers are concerned, our Web API Service is a standard ASP.NET Core OData 8.0 service -- use the standard [OData v4 query options](https://learn.microsoft.com/en-us/odata/overview) to consume our API. You can also use Swagger UI, Postman, developer tools within your favorite web browser, or standard .NET/JavaScript API.

We have published dozens of .NET code examples with the standard HttpClient: [Make HTTP Requests to the Web API from .NET Applications](xref:403715). You can find other examples in public community resources for your favorite client UI technology.

**Q: Will it take hours to get started?**

**A:** We ship a [1-Click solution to build CRUD REST API for popular usage scenarios](https://community.devexpress.com/blogs/news/archive/2022/06/20/a-one-click-solution-for-role-based-access-control-asp-net-core-web-api-services-via-entity-framework-core-and-xpo-v22-1.aspx) -- from zero to a running Swagger UI.

Simply run the Universal Component Installer from the [Download Manager](https://www.devexpress.com/ClientCenter/DownloadManager/) and enter the credentials for your DevExpress account ([free](https://www.devexpress.com/security-api-free/) or paid/Universal). Then, use the free [Template Kit in Visual Studio 2022+](https://go.devexpress.com/DevExpress_Template_Kit_VisualStudio.aspx) to create Web API Service. The Template Kit adds all required dependencies, Entity Framework DbContext, default access control rights, connection string, etc. For more information, refer to the following help topic: <xref:403401>.

**Q: Can I customize the API (add custom endpoints, remove data from response, and so on)?**

**A:** You can do everything that you can do with ASP.NET Core OData. Microsoft published lots of information in this regard here: [Create web APIs with ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/web-api).

To save time for our Web API Service users, we documented highly popular OData customizations on our website:

- [Create Custom Endpoints](xref:403858) | [Expose or Hide Business Object Properties](xref:403551#expose-or-hide-business-object-properties)
- [Change an EDM Model Structure using ODataModelBuilder](xref:403719#use-the-odatamodelbuilder) | [Customize OData Options](xref:403719)
- [Authenticate Users & Authorize CRUD Operations in .NET MAUI Apps with Web API Service & EF Core](https://www.youtube.com/watch?v=XPbJw-P0eIE&feature=youtu.be) (videos on YouTube)
- [Add Custom Web API Endpoints To Check Permissions & Query Media Data in .NET MAUI Apps with EF Core](https://www.youtube.com/watch?v=Pj9CbgzFT-A&feature=youtu.be) (videos on YouTube)
- [Preview Reports as PDF in .NET MAUI Apps using Backend Web API Service Endpoints with EF Core](https://www.youtube.com/watch?v=bn4iF5Gc9XY&feature=youtu.be) (videos on YouTube)

You can customize your own EF Core or XPO data model and fine-tune things at the XAF layer (security permissions, CRUD behavior, and so on).
