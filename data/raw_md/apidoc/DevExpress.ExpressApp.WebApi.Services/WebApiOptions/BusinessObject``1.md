---
uid: DevExpress.ExpressApp.WebApi.Services.WebApiOptions.BusinessObject``1
name: BusinessObject<T>()
type: Method
summary: Generates HTTP endpoints for the business object class passed as a parameter.
syntax:
  content: |-
    public BusinessObjectConfigurator<T> BusinessObject<T>()
        where T : class
  typeParameters:
  - id: T
    description: The business object class for which the [Web API Service](xref:403394) generates HTTP endpoints.
  return:
    type: DevExpress.ExpressApp.WebApi.Services.BusinessObjectConfigurator{{T}}
    description: ''
seealso:
- linkId: "403394"
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

[`AddXafWebApi`]: xref:DevExpress.ExpressApp.WebApi.Services.WebApiStartupExtensions.AddXafWebApi(Microsoft.Extensions.DependencyInjection.IServiceCollection,Microsoft.Extensions.Configuration.IConfiguration,System.Action{DevExpress.ExpressApp.WebApi.Services.WebApiOptions})
