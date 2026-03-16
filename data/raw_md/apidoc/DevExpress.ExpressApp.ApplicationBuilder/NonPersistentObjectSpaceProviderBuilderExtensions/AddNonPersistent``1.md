---
uid: DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderBuilderExtensions.AddNonPersistent``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{``0},System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderOptions})
name: AddNonPersistent<TContext>(IObjectSpaceProviderServiceBasedBuilder<TContext>, Action<IServiceProvider, NonPersistentObjectSpaceProviderOptions>)
type: Method
summary: Adds the @DevExpress.ExpressApp.NonPersistentObjectSpaceProvider to your ASP.NET Core Blazor application.
syntax:
  content: |-
    public static IObjectSpaceProviderServiceBasedBuilder<TContext> AddNonPersistent<TContext>(this IObjectSpaceProviderServiceBasedBuilder<TContext> builder, Action<IServiceProvider, NonPersistentObjectSpaceProviderOptions> configureOptions = null)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderOptions}
    defaultValue: "null"
    description: Options that allow you to configure the Object Space Provider.
  typeParameters:
  - id: TContext
    description: The @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
seealso: []
---

The following example demonstrates how to use this method:

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
            builder.ObjectSpaceProviders
                // ...
                .AddNonPersistent();
        });
        // ...
    }
}
```
***