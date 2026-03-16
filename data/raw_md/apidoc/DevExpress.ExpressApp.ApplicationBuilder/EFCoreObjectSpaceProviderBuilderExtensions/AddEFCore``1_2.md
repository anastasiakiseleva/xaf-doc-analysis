---
uid: DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderBuilderExtensions.AddEFCore``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{``0},System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderOptionsBuilder})
name: AddEFCore<TContext>(IObjectSpaceProviderServiceBasedBuilder<TContext>, Action<IServiceProvider, EFCoreObjectSpaceProviderOptionsBuilder>)
type: Method
summary: Adds the @DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1 to your ASP.NET Core Blazor application.
syntax:
  content: |-
    public static DbContextServiceBasedBuilder<TContext> AddEFCore<TContext>(this IObjectSpaceProviderServiceBasedBuilder<TContext> builder, Action<IServiceProvider, EFCoreObjectSpaceProviderOptionsBuilder> configureObjectSpaceProviderOptions)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
  - id: configureObjectSpaceProviderOptions
    type: System.Action{System.IServiceProvider,DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderOptionsBuilder}
    description: Options that allow you to configure the Object Space Provider.
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

The following example demonstrates how to use the `AddEFCore` method:

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
                .AddEFCore(options => options.PreFetchReferenceProperties())
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