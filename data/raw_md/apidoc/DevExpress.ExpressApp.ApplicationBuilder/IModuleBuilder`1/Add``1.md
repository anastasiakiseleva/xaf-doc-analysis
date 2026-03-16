---
uid: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder`1.Add``1(System.Func{``0})
name: Add<TModule>(Func<TModule>)
type: Method
summary: Adds the specified [Module](xref:118046) to your application.This method allows you to use a custom module factory.
syntax:
  content: |-
    IModuleBuilder<TContext> Add<TModule>(Func<TModule> createModuleDelegate)
        where TModule : ModuleBase
  parameters:
  - id: createModuleDelegate
    type: System.Func{{TModule}}
    description: 'A delegate that creates the Module. '
  typeParameters:
  - id: TModule
    description: 'The type of the Module that this method adds to your application. '
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder`1
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

### WinForms

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{10}
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
```csharp{12}
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