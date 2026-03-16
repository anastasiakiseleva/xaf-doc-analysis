---
uid: DevExpress.ExpressApp.ApplicationBuilder.SecuredObjectSpaceProviderBuilderExtensions.AddSecuredXpo``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{``0},System.Action{DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.ApplicationBuilder.SecuredXPObjectSpaceProviderOptions})
name: AddSecuredXpo<TContext>(IObjectSpaceProviderBuilder<TContext>, Action<XafApplication, SecuredXPObjectSpaceProviderOptions>)
type: Method
summary: Adds the @DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider to your WinForms application.
syntax:
  content: |-
    public static IObjectSpaceProviderBuilder<TContext> AddSecuredXpo<TContext>(this IObjectSpaceProviderBuilder<TContext> builder, Action<XafApplication, SecuredXPObjectSpaceProviderOptions> configureOptions)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.ApplicationBuilder.SecuredXPObjectSpaceProviderOptions}
    description: Options that allow you to configure the secured Object Space Provider.
  typeParameters:
  - id: TContext
    description: The @DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
seealso: []
---

The following example demonstrates how to use this method:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{9-12}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.ObjectSpaceProviders
            .AddSecuredXpo((application, options) => {
                options.ConnectionString = connectionString;
            })
            .AddNonPersistent();
    }
    // ...
}
```
***
