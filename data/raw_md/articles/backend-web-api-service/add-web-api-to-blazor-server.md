---
uid: "403561"
title: 'Integrate the Web API into an Existing XAF Blazor Application'
owner: Eugenia Simonova
seealso:
- linkType: HRef
  linkId: https://learn.microsoft.com/en-us/dotnet/architecture/blazor-for-web-forms-developers/app-startup#blazor-server-startup-structure
  altText: Blazor Server Startup Structure
- linkId: DevExpress.ExpressApp.WebApi.Services.WebApiOptions
- linkId: DevExpress.ExpressApp.WebApi.Services.WebApiOptions.BusinessObject``1
- linkId: "403394"  
- linkId: "403505"
- linkType: HRef
  linkId: https://community.devexpress.com/blogs/news/archive/2023/05/01/authorize-ef-core-crud-operations-and-download-reports-in-blazor-webassembly-with-odata-web-api.aspx
  altText: Authorize EF Core CRUD Operations and Download Reports in Blazor WebAssembly with OData Web API
---

# Integrate the Web API into an Existing XAF Blazor Application

This topic describes how to add the [Web API](xref:403394) service to a Blazor Server project. 

## Add Web API Service: Core Functionality

### Install NuGet Packages

Install the following NuGet packages to the Blazor Server project (_MySolution.Blazor.Server_):

  * **DevExpress.ExpressApp.WebApi** 
  * **Swashbuckle.AspNetCore**
  * **DevExpress.ExpressApp.WebApi.Xpo** - XPO applications only

See the following topic for more information on how to install DevExpress NuGet packages: [](xref:116042).     

### Add Service Configuration Code

Use the code below to configure services for the **Web API**:

  **File:** _MySolution.Blazor.Server\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.WebApi.Services;
using Microsoft.OpenApi.Models;
using Microsoft.AspNetCore.OData;
// ...
public void ConfigureServices(IServiceCollection services) {
// ...     
    services.AddXafWebApi(Configuration, options => { 
        // To make a Business Object available via Web API and
        // to generate GET, POST, PUT, and DELETE HTTP methods for it,
        // uncomment the following line.
        // !!!
        // options.BusinessObject<YourBusinessObject>();
        // !!!
    })
    // In EF Core applications, do nothing. 
    // In XPO applications, uncomment the following line.
    // !!!
    // .AddXpoServices()
    // !!!
    ;
    services.AddControllers().AddOData((options, serviceProvider) => {
        options
            .AddRouteComponents("api/odata", new EdmModelBuilder(serviceProvider).GetEdmModel())
            .EnableQueryFeatures(100);
    });
    services.AddSwaggerGen(c => {
        c.EnableAnnotations();
        c.SwaggerDoc("v1", new OpenApiInfo {
            Title = "MySolution API",
            Version = "v1",
            Description = @"Use AddXafWebApi(Configuration, options) in the MySolution.Blazor.Server\Startup.cs file to make Business Objects available in the Web API."
        });
    });
}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env) {
    if(env.IsDevelopment()) {
        // ...
        app.UseSwagger();
        app.UseSwaggerUI(c => {
            c.SwaggerEndpoint("/swagger/v1/swagger.json", "MySolution WebApi v1");
        });
    }
    // ...
}

```
[`AddOData`]: https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.odata.odatamvcbuilderextensions.addodata
[`AddSwaggerGen`]: https://learn.microsoft.com/en-us/aspnet/core/tutorials/getting-started-with-swashbuckle#add-and-configure-swagger-middleware
[`UseSwagger`]: https://learn.microsoft.com/en-us/aspnet/core/tutorials/getting-started-with-swashbuckle#add-and-configure-swagger-middleware
[`UseSwaggerUI`]: https://learn.microsoft.com/en-us/aspnet/core/tutorials/getting-started-with-swashbuckle#add-and-configure-swagger-middleware
[`AddXafWebApi`]: xref:DevExpress.ExpressApp.WebApi.Services.WebApiStartupExtensions.AddXafWebApi(Microsoft.Extensions.DependencyInjection.IServiceCollection,Microsoft.Extensions.Configuration.IConfiguration,System.Action{DevExpress.ExpressApp.WebApi.Services.WebApiOptions})
[`BusinessObject`]: xref:DevExpress.ExpressApp.WebApi.Services.WebApiOptions.BusinessObject``1
[`options`]: xref:DevExpress.ExpressApp.WebApi.Services.WebApiOptions
***

### Configure Authentication Settings (Optional)

The **Web API** supports all standard ASP.NET Core [authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication) techniques. See the following topic for more information: [Authentication in Web API projects](xref:403413).

### Create Endpoints and Test the Web API 

You can now [create endpoints and test the Web API](xref:403551).


## Add Web API Service: Additional Modules

You can enable additional Web API Service modules in an existing application. For instructions, please refer to the topic that describes the required module:

- [Obtain a Report from a Web API Controller Endpoint](xref:404176)
- [Validate Data Sent to Web API Endpoints](xref:404223)
- [Audit Trail: Log Data Changes Made via Web API Endpoints](xref:404262)

A number of modules are available to you right away, without the need for manual registration:

- [Obtain BLOB Data from a Web API Controller Endpoint](xref:404207)
- [Execute CRUD Operations for Non-Persistent Objects](xref:404233)
- [Obtain Localization Strings from a Web API Controller Endpoint](xref:403982)

>[!note]
 Additional modules listed above ship only as part of the [DevExpress Universal Subscription](https://www.devexpress.com/subscriptions/universal.xml).
