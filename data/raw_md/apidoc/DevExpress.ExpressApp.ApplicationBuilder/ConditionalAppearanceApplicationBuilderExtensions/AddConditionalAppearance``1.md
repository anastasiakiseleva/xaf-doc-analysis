---
uid: DevExpress.ExpressApp.ApplicationBuilder.ConditionalAppearanceApplicationBuilderExtensions.AddConditionalAppearance``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0})
name: AddConditionalAppearance<TBuilder>(IModuleBuilder<TBuilder>)
type: Method
summary: '[!include[<\[Conditional Appearance Module\](xref:113286)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: |-
    public static IModuleBuilder<TBuilder> AddConditionalAppearance<TBuilder>(this IModuleBuilder<TBuilder> builder)
        where TBuilder : IApplicationBuilder<TBuilder>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  typeParameters:
  - id: TBuilder
    description: The @DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder or @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
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
            .AddConditionalAppearance();
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
                .AddConditionalAppearance();
            // ...
        });
        // ...
    }
}
```
***