---
uid: DevExpress.ExpressApp.ApplicationBuilder.SecuredObjectSpaceProviderBuilderExtensions.AddSecuredXpo``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{``0},System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.SecuredXPObjectSpaceProviderOptions})
name: AddSecuredXpo<TContext>(IObjectSpaceProviderServiceBasedBuilder<TContext>, Action<IServiceProvider, SecuredXPObjectSpaceProviderOptions>)
type: Method
summary: Adds the @DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider to your ASP.NET Core Blazor application.
syntax:
  content: |-
    public static IObjectSpaceProviderServiceBasedBuilder<TContext> AddSecuredXpo<TContext>(this IObjectSpaceProviderServiceBasedBuilder<TContext> builder, Action<IServiceProvider, SecuredXPObjectSpaceProviderOptions> configureOptions)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.SecuredXPObjectSpaceProviderOptions}
    description: Options that allow you to configure the secured Object Space Provider.
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
```csharp{11-19}
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
                .AddSecuredXpo((serviceProvider, options) => {
                    string connectionString = null;
                    if(Configuration.GetConnectionString("ConnectionString") != null) {
                        connectionString = Configuration.GetConnectionString("ConnectionString");
                    }
                    ArgumentNullException.ThrowIfNull(connectionString);
                    options.ConnectionString = connectionString;
                })
                .AddNonPersistent();
        });
        // ...
    }
}
```
***
