---
uid: DevExpress.ExpressApp.WebApi.Services.WebApiOptions.BusinessObject(System.Type)
name: BusinessObject(Type)
type: Method
summary: Generates HTTP endpoints for a type passed as a parameter.
syntax:
  content: public void BusinessObject(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A type for which the [Web API Service](xref:403394) generates HTTP endpoints.
seealso:
- linkId: "403394"
- linkId: "403551"
---
The following code creates endpoints for the type of the _user_ instance:

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

# [C#](#tab/tabid-csharp-1)
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
