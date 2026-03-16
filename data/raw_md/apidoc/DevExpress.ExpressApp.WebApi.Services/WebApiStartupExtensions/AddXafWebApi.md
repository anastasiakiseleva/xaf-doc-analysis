---
uid: DevExpress.ExpressApp.WebApi.Services.WebApiStartupExtensions.AddXafWebApi(Microsoft.Extensions.DependencyInjection.IServiceCollection,Microsoft.Extensions.Configuration.IConfiguration,System.Action{DevExpress.ExpressApp.WebApi.Services.WebApiOptions})
name: AddXafWebApi(IServiceCollection, IConfiguration, Action<WebApiOptions>)
type: Method
summary: An [extension](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/extension-methods) method that adds [Web API](xref:403394) services to the service collection.
syntax:
  content: public static XafWebApiBuilder AddXafWebApi(this IServiceCollection services, IConfiguration configuration, Action<WebApiOptions> configureOptions)
  parameters:
  - id: services
    type: Microsoft.Extensions.DependencyInjection.IServiceCollection
    description: A service collection for which the **AddXafWebApi** extension method is called.
  - id: configuration
    type: Microsoft.Extensions.Configuration.IConfiguration
    description: The application configuration.
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.WebApi.Services.WebApiOptions}
    description: An Action delegate that configures Web API services.
  return:
    type: DevExpress.ExpressApp.WebApi.Services.XafWebApiBuilder
    description: ''
seealso:
- linkId: "403551"
---
The following code creates endpoints for the **ApplicationUser** and **Contact** business objects:

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
# [C#](#tab/tabid-csharp)
```csharp
using MySolution.Module.BusinessObjects;
namespace MySolution.WebApi {
    public class Startup {
        public Startup(IConfiguration configuration) {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXafWebApi(Configuration, options => {
                options.BusinessObject<ApplicationUser>();
                options.BusinessObject<Contact>();
            })
            // in XPO applications, uncomment the following line
            // .AddXpoServices(); 
            // ...
        }
        // ...
    }
}
```
***
