---
uid: DevExpress.ExpressApp.ApplicationBuilder.DbContextBuilder`1.WithDbContext``1(System.Action{DevExpress.ExpressApp.XafApplication,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},Microsoft.Extensions.DependencyInjection.ServiceLifetime)
name: WithDbContext<TDbContext>(Action<XafApplication, DbContextOptionsBuilder>, ServiceLifetime)
type: Method
summary: Allows you to configure specified `DbContext`.
syntax:
  content: |-
    public IObjectSpaceProviderBuilder<TContext> WithDbContext<TDbContext>(Action<XafApplication, DbContextOptionsBuilder> configureOptions, ServiceLifetime dbContextFactoryServiceLifetime = ServiceLifetime.Scoped)
        where TDbContext : DbContext
  parameters:
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.XafApplication,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder}
    description: A delegate that configures `DbContext`.
  - id: dbContextFactoryServiceLifetime
    type: Microsoft.Extensions.DependencyInjection.ServiceLifetime
    defaultValue: Scoped
    description: A @Microsoft.Extensions.DependencyInjection.ServiceLifetime enumeration value that specifies the lifetime of the `DbContextFactory` service registered by the method.
  typeParameters:
  - id: TDbContext
    description: The type of a `DbContext` object.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
seealso: []
---
