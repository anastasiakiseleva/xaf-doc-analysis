---
uid: DevExpress.ExpressApp.ApplicationBuilder.SecuredEFCoreObjectSpaceProviderBuilderExtensions.AddSecuredEFCore``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{``0},System.Action{DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderOptionsBuilder})
name: AddSecuredEFCore<TContext>(IObjectSpaceProviderServiceBasedBuilder<TContext>, Action<EFCoreObjectSpaceProviderOptionsBuilder>)
type: Method
summary: Adds the @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 to your ASP.NET Core Blazor application.
syntax:
  content: |-
    public static DbContextServiceBasedBuilder<TContext> AddSecuredEFCore<TContext>(this IObjectSpaceProviderServiceBasedBuilder<TContext> builder, Action<EFCoreObjectSpaceProviderOptionsBuilder> configureObjectSpaceProviderOptions = null)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
  - id: configureObjectSpaceProviderOptions
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderOptionsBuilder}
    defaultValue: "null"
    description: Options that allow you to configure the secured Object Space Provider.
  typeParameters:
  - id: TContext
    description: The @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.DbContextServiceBasedBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
seealso: []
---

This method must be used together with one of the following methods: 

* @DevExpress.ExpressApp.ApplicationBuilder.DbContextServiceBasedBuilder`1.WithDbContext``1(System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},Microsoft.Extensions.DependencyInjection.ServiceLifetime) 
* @DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextBuilderExtensions.WithAuditedDbContext``1(DevExpress.ExpressApp.ApplicationBuilder.DbContextServiceBasedBuilder{``0},System.Action{DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextServiceBasedConfigurator},Microsoft.Extensions.DependencyInjection.ServiceLifetime)

The following example demonstrates how to use the `AddSecuredEFCore` method:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{11-15}
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
                .AddSecuredEFCore()
                .WithDbContext<MySolutionEFCoreDbContext>((serviceProvider, options) => {
                    // ...
                })
                .AddNonPersistent();
        });
        // ...
    }
}
```
***