---
uid: DevExpress.ExpressApp.ApplicationBuilder.DbContextServiceBasedBuilder`1.WithDbContext``1(System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},Microsoft.Extensions.DependencyInjection.ServiceLifetime)
name: WithDbContext<TDbContext>(Action<IServiceProvider, DbContextOptionsBuilder>, ServiceLifetime)
type: Method
summary: Allows you to configure specified `DbContext`.
syntax:
  content: |-
    public IObjectSpaceProviderServiceBasedBuilder<TContext> WithDbContext<TDbContext>(Action<IServiceProvider, DbContextOptionsBuilder> configureOptions, ServiceLifetime dbContextFactoryServiceLifetime = ServiceLifetime.Scoped)
        where TDbContext : DbContext
  parameters:
  - id: configureOptions
    type: System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder}
    description: A delegate that configures `DbContext`.
  - id: dbContextFactoryServiceLifetime
    type: Microsoft.Extensions.DependencyInjection.ServiceLifetime
    defaultValue: Scoped
    description: A @Microsoft.Extensions.DependencyInjection.ServiceLifetime enumeration value that specifies the lifetime of the `DbContextFactory` service registered by the method.
  typeParameters:
  - id: TDbContext
    description: The type of a `DbContext` object.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{13-15}
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
                .WithDbContext<MySolutionDbContext>((serviceProvider, options) => {
                    // ...
                },ServiceLifetime.Transient);
        });
        // ...
    }
}
```
***