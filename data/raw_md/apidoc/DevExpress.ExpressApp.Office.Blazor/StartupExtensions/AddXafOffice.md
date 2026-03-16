---
uid: DevExpress.ExpressApp.Office.Blazor.StartupExtensions.AddXafOffice(Microsoft.Extensions.DependencyInjection.IServiceCollection)
name: AddXafOffice(IServiceCollection)
type: Method
summary: Registers the required [Office Module](xref:400003) services in the application's @Microsoft.Extensions.DependencyInjection.IServiceCollection.
syntax:
  content: public static IServiceCollection AddXafOffice(this IServiceCollection services)
  parameters:
  - id: services
    type: Microsoft.Extensions.DependencyInjection.IServiceCollection
    description: The collection of services registered in your application.
  return:
    type: Microsoft.Extensions.DependencyInjection.IServiceCollection
    description: The collection of services registered in your application. Allows you to chain further service registrations.
seealso: []
---
Call this method in the **Startup.ConfigureServices** method when you [add the Office Module to your ASP.NET Core Blazor application](xref:400003#add-the-office-module-to-your-application):

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Office.Blazor;
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services){
        //...
        services.AddXafOffice();
    }
    // ...
}
```
***