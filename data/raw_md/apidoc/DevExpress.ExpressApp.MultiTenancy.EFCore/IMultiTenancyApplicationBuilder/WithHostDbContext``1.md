---
uid: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithHostDbContext``1(System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},System.Boolean)
name: WithHostDbContext<TServiceDbContext>(Action<IServiceProvider, DbContextOptionsBuilder>, Boolean)
type: Method
summary: Configures `DbContext` used by the application to access the host database containing tenant settings.
syntax:
  content: |-
    IMultiTenancyApplicationBuilder WithHostDbContext<TServiceDbContext>(Action<IServiceProvider, DbContextOptionsBuilder> configureServiceDbContext, bool isMiddleTier = false)
        where TServiceDbContext : DbContext
  parameters:
  - id: configureServiceDbContext
    type: System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder}
    description: A delegate that configures `DbContext`.
  - id: isMiddleTier
    type: System.Boolean
    defaultValue: "False"
    description: '`true` if the application uses the [Middle Tier Security](xref:113439); otherwise, `false`.'
  typeParameters:
  - id: TServiceDbContext
    description: The type of `DbContext` object used to access the host database.
  return:
    type: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder
    description: The application builder that processed the action.
seealso:
- linkId: "404436"
---
