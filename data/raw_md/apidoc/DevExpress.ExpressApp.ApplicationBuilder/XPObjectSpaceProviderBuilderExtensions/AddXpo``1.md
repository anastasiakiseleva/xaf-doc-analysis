---
uid: DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderBuilderExtensions.AddXpo``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{``0},System.Action{DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions})
name: AddXpo<TContext>(IObjectSpaceProviderBuilder<TContext>, Action<XafApplication, XPObjectSpaceProviderOptions>)
type: Method
summary: Adds the @DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider to your WinForms application.
syntax:
  content: |-
    public static IObjectSpaceProviderBuilder<TContext> AddXpo<TContext>(this IObjectSpaceProviderBuilder<TContext> builder, Action<XafApplication, XPObjectSpaceProviderOptions> configureOptions)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions}
    description: Options that you can use to configure the XPO Object Space Provider.
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
            .AddXpo((application, options) => {
                options.ConnectionString = connectionString;
            })
            .AddNonPersistent();
    }
    // ...
}
```
***