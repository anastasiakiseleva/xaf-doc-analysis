---
uid: DevExpress.ExpressApp.ApplicationBuilder.ObjectCloningApplicationBuilderExtensions.AddCloning``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.CloneObject.ObjectCloningOptions})
name: AddCloning<TBuilder>(IModuleBuilder<TBuilder>, Action<ObjectCloningOptions>)
type: Method
summary: '[!include[<\[Clone Object Module\](xref:112835)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: |-
    public static IModuleBuilder<TBuilder> AddCloning<TBuilder>(this IModuleBuilder<TBuilder> builder, Action<ObjectCloningOptions> configureOptions = null)
        where TBuilder : IApplicationBuilder<TBuilder>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.CloneObject.ObjectCloningOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Clone Object Module.
  typeParameters:
  - id: TBuilder
    description: ''
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates the method's usage:

### ASP.NET Core Blazor

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{12-14}
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
                .AddCloning(options => {
                    options.ClonerType = // ...
                })
            // ...
        });
        // ...
    }
}
```
***

### Windows Forms

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{10-12}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.Modules
            // ...
            .AddCloning(options => {
                options.ClonerType = // ...
            });
        // ...
    }
    // ...
}
```
***