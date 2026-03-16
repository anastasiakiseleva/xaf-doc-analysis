---
uid: DevExpress.ExpressApp.ApplicationBuilder.IXafApplicationBuilder`1.Modules
name: Modules
type: Property
summary: Provides access to @DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder`1 that allows you to register and configure [Modules](xref:118046) in your application.
syntax:
  content: IModuleBuilder<TBuilder> Modules { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: 'Allows you to register and configure [Modules](xref:118046) in your application. '
seealso: []
---
The following example demonstrates how to use this property:

### WinForms

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{8-10}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.Modules
            // ...
            .Add<CustomModule>(module => new CustomModule());
        // ...
    }
    // ...
}
```
***

### ASP.NET Core Blazor

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{10-12}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
// ...
public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            builder.Modules
                // ...
                .Add<CustomModule>(module => new CustomModule());
            // ...
        });
        // ...
    }
}
```
***