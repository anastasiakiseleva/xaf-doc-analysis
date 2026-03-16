---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.ValidationApplicationBuilderExtensions.AddValidation(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Validation.ValidationModuleOptions})
name: AddValidation(IModuleBuilder<IBlazorApplicationBuilder>, Action<ValidationModuleOptions>)
type: Method
summary: '[!include[<\[Validation Module\](xref:113684)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IBlazorApplicationBuilder> AddValidation(this IModuleBuilder<IBlazorApplicationBuilder> builder, Action<ValidationModuleOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Validation.ValidationModuleOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Validation Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---

The following example demonstrates how to use this method:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{13-15}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
using DevExpress.Persistent.BaseImpl;
// ...
public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            builder.Modules
                // ...
                .AddValidation(options => {
                    options.AllowValidationDetailsAccess = false;
                    options.Events.OnCustomNeedToValidateRule += (context) => {
                        //...
                    };
                })
            // ...
        });
        // ...
    }
}
```
***