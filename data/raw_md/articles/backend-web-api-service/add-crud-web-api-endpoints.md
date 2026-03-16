---
uid: "403551"
title: 'Add and Protect CRUD Web API Endpoints'
owner: Eugenia Simonova
seealso:
- linkId: "404488"
- linkId: "403413"
- linkId: "403504"
- linkId: "403505"
- linkId: "403715"
---

# Add and Protect CRUD Web API Endpoints

This topic describes how to create endpoints in a Web API Service application. See the following topics for information on how to create a project with the **Web API**:

* [Create a New Application with the Web API](xref:403401)
* [Add the Web API Service to a Blazor Server Project](xref:403561)

## Create Endpoints for Business Objects

In the _Startup.cs_ file, add or find the [services.AddXafWebApi](xref:DevExpress.ExpressApp.WebApi.Services.WebApiStartupExtensions.AddXafWebApi(Microsoft.Extensions.DependencyInjection.IServiceCollection,Microsoft.Extensions.Configuration.IConfiguration,System.Action{DevExpress.ExpressApp.WebApi.Services.WebApiOptions})) method call and use the **BusinessObject** method to create endpoints for business objects. The following code creates endpoints for the **ApplicationUser** and **Contact** business objects:

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
# [C#](#tab/tabid-csharp)
```csharp
using MySolution.Module.BusinessObjects;
// ...
namespace MySolution.WebApi {
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXafWebApi(Configuration, options => {
                options.BusinessObject<ApplicationUser>();
                options.BusinessObject<Contact>();
            })
            // In XPO applications, uncomment the following line:
            // .AddXpoServices(); 
            // ...
        }
        // ...    
    }
}
```
[`AddXafWebApi`]: xref:DevExpress.ExpressApp.WebApi.Services.WebApiStartupExtensions.AddXafWebApi(Microsoft.Extensions.DependencyInjection.IServiceCollection,Microsoft.Extensions.Configuration.IConfiguration,System.Action{DevExpress.ExpressApp.WebApi.Services.WebApiOptions})
[`BusinessObject`]: xref:DevExpress.ExpressApp.WebApi.Services.WebApiOptions.BusinessObject``1
[`options`]: xref:DevExpress.ExpressApp.WebApi.Services.WebApiOptions
***

### Create Endpoints for Shared Business Objects in Multi-Tenant Application

In [multi-tenant applications](xref:404436), the host database can maintain [shared business objects](xref:405451). To create endpoints for these objects, call the [WithSharedBusinessObjects (EF Core)](xref:DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithSharedBusinessObjects(System.Type[])) / [WithSharedBusinessObjects (XPO)](xref:DevExpress.ExpressApp.MultiTenancy.Xpo.IMultiTenancyApplicationBuilder.WithSharedBusinessObjects(System.Type[])) method to register shared host object types in the application builder.

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
# [C#](#tab/tabid-csharp)
```csharp
using MySolution.Module.BusinessObjects;
// ...
namespace MySolution.WebApi {
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXaf(Configuration, builder => {
                builder.AddMultiTenancy() 
                    .WithSharedBusinessObjects(typeof(SharedEntityType1), typeof(SharedEntityType2), ...) 
                    // ... 
            }
            services.AddXafWebApi(Configuration, options => {
                options.BusinessObject<SharedEntityType1>();
                options.BusinessObject<SharedEntityType2>();
            }))
            // In XPO applications, uncomment the following line:
            // .AddXpoServices(); 
            // ...
        }
        // ...    
    }
}
```
***

Refer to the following help topic for more information: <xref:405451>.

> [!important]
> To access shared objects, log in to a tenant account. The Web API service does not allow authorization using the host account.

[!include[configure-authorization-for-endpoints](~/templates/configure-authorization-for-endpoints.md)]
* [](xref:403413)

## Expose or Hide Business Object Properties

### Expose Properties

[ASP.NET Core Web API/OData](https://learn.microsoft.com/en-us/odata/webapi/getting-started) exposes public business class properties of simple/value types with a setter (writable) in a Web API response. Our Web API Service additionally exposes read-only calculated XPO properties of simple/value types without a setter (readonly) marked with [PersistentAliasAttribute](xref:DevExpress.Xpo.PersistentAliasAttribute).

ASP.NET Core Web API/OData does not initially include complex type, reference, and collection business class properties in a Web API response. To include complex type, reference, and collection business class properties in a Web API response, use [OData query](https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview) options:
 - [Get a Reference Object](xref:403715#get-a-reference-object)
 - [Get an Associated Collection](xref:403715#get-an-associated-collection)
 - [Change the Expansion Depth for Related Business Objects](xref:403719)

[!include[auto-expand-attribute-note](~/templates/auto-expand-attribute-note.md)]

### Hide Properties

To hide business class properties from the Web API Service's responses, decorate them with the [IgnoreDataMemberAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.ignoredatamemberattribute).

To specifically remove a property from the Web API Service's OData interface, use the `EntityTypeConfigurator.IgnoreProperty` method. In this instance, the specified property may belong to the class itself or to its ancestor:

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

# [C#](#tab/tabid-csharp)

```csharp{3-6}
services.AddXafWebApi(Configuration, options => { 
    options.BusinessObject<Contact>().ConfigureEntityType(b => {
        // Ignore this class's property.
        b.IgnoreProperty(o => o.Email);
        // Ignore a property of the parent `Person` class.
        b.IgnoreProperty(o => o.Company);
    }); 
}); 
```
***

The image below demonstrates the difference in the GET endpoint's response when the above code is used:

![Ignore Properties](~/images/customize-odata-ignore-properties.png)

For advanced OData entity model structure customization, refer to [Change an EDM Model Structure using ODataModelBuilder](xref:403719).
