---
uid: DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextBuilderExtensions.WithAuditedDbContext``1(DevExpress.ExpressApp.ApplicationBuilder.DbContextServiceBasedBuilder{``0},System.Action{DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextServiceBasedConfigurator},Microsoft.Extensions.DependencyInjection.ServiceLifetime)
name: WithAuditedDbContext<TContext>(DbContextServiceBasedBuilder<TContext>, Action<AuditedDbContextServiceBasedConfigurator>, ServiceLifetime)
type: Method
summary: Allows you to configure `DbContext` objects in ASP.NET Core Blazor applications with the [Audit Trail Module](xref:403104).
syntax:
  content: |-
    public static IObjectSpaceProviderServiceBasedBuilder<TContext> WithAuditedDbContext<TContext>(this DbContextServiceBasedBuilder<TContext> dbContextBuilder, Action<AuditedDbContextServiceBasedConfigurator> configureContexts, ServiceLifetime dbContextFactoryServiceLifetime = ServiceLifetime.Scoped)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: dbContextBuilder
    type: DevExpress.ExpressApp.ApplicationBuilder.DbContextServiceBasedBuilder{{TContext}}
    description: Allows you to configure `DbContext` objects.
  - id: configureContexts
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextServiceBasedConfigurator}
    description: A delegate that configures `DbContext` objects.
  - id: dbContextFactoryServiceLifetime
    type: Microsoft.Extensions.DependencyInjection.ServiceLifetime
    defaultValue: Scoped
    description: A [](xref:Microsoft.Extensions.DependencyInjection.ServiceLifetime) enumeration value that specifies the lifetime of the `DbContextFactory` service registered by the `WithAuditedDbContext` method.
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
```csharp{13-24}
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
                .AddSecuredEFCore()
                .WithAuditedDbContext(contexts => {
                    contexts.Configure<MySolutionDbContext, AuditingDbContext>(
                        (serviceProvider, businessObjectDbContextOptions) => {
                            // ...
                        },
                        (serviceProvider, auditHistoryDbContextOptions) => {
                            // ...
                        },
                        options => {
                            // ...
                        });
                });
        });
        // ...
    }
}
```
***
