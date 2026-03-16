---
uid: DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderBuilderExtensions.AddNonPersistent``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{``0},System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderOptions})
name: AddNonPersistent<TContext>(IObjectSpaceProviderBuilder<TContext>, Action<IServiceProvider, NonPersistentObjectSpaceProviderOptions>)
type: Method
summary: Adds the @DevExpress.ExpressApp.NonPersistentObjectSpaceProvider to your WinForms application.
syntax:
  content: |-
    public static IObjectSpaceProviderBuilder<TContext> AddNonPersistent<TContext>(this IObjectSpaceProviderBuilder<TContext> builder, Action<IServiceProvider, NonPersistentObjectSpaceProviderOptions> configureOptions = null)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderOptions}
    defaultValue: "null"
    description: Options that allow you to configure the Object Space Provider.
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
```csharp{8-10}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.ObjectSpaceProviders
            // ...
            .AddNonPersistent();
    }
    // ...
}
```
***
