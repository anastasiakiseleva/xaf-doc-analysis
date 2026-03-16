---
uid: DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextBuilderExtensions.WithAuditedDbContext``1(DevExpress.ExpressApp.ApplicationBuilder.DbContextBuilder{``0},System.Action{DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextConfigurator},Microsoft.Extensions.DependencyInjection.ServiceLifetime)
name: WithAuditedDbContext<TContext>(DbContextBuilder<TContext>, Action<AuditedDbContextConfigurator>, ServiceLifetime)
type: Method
summary: Allows you to configure the main (business object) and additional (audit history) `DbContext` objects in WinForms applications with the [Audit Trail Module](xref:403104).
syntax:
  content: |-
    public static IObjectSpaceProviderBuilder<TContext> WithAuditedDbContext<TContext>(this DbContextBuilder<TContext> dbContextBuilder, Action<AuditedDbContextConfigurator> configureContexts, ServiceLifetime dbContextFactoryServiceLifetime = ServiceLifetime.Scoped)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: dbContextBuilder
    type: DevExpress.ExpressApp.ApplicationBuilder.DbContextBuilder{{TContext}}
    description: Allows you to configure `DbContext` objects.
  - id: configureContexts
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextConfigurator}
    description: A delegate that configures `DbContext` objects.
  - id: dbContextFactoryServiceLifetime
    type: Microsoft.Extensions.DependencyInjection.ServiceLifetime
    defaultValue: Scoped
    description: A [](xref:Microsoft.Extensions.DependencyInjection.ServiceLifetime) enumeration value that specifies the lifetime of the `DbContextFactory` service registered by the `WithAuditedDbContext` method.
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
```csharp{10-20}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.ObjectSpaceProviders
            .AddSecuredEFCore()
            .WithAuditedDbContext(contexts => {
                contexts.Configure<MySolutionDbContext, AuditingDbContext>(
                    (application, businessObjectDbContextOptions) => {
                        // ...
                    },
                    (application, auditHistoryDbContextOptions) => {
                        // ...
                    },
                    options => {
                        // ...
                    });
            });
    }
    // ...
}
```
***