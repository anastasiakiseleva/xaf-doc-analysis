---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.ValidationApplicationBuilderExtensions.AddValidation(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Validation.ValidationModuleOptions})
name: AddValidation(IModuleBuilder<IWinApplicationBuilder>, Action<ValidationModuleOptions>)
type: Method
summary: '[!include[<\[Validation Module\](xref:113684)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddValidation(this IModuleBuilder<IWinApplicationBuilder> builder, Action<ValidationModuleOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Validation.ValidationModuleOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Validation Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---

The following example demonstrates how to use this method:

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
            .AddValidation(options => {
                options.AllowValidationDetailsAccess = false;
                options.Events.OnCustomNeedToValidateRule += (context) => {
                    //...
                };
            })
        // ...
    }
    // ...
}
```
***
