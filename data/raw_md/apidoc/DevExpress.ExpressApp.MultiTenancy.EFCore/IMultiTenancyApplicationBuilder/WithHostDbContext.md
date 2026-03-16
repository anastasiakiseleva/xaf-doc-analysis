---
uid: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithHostDbContext(System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},System.Boolean,System.Boolean,System.Boolean)
name: WithHostDbContext(Action<IServiceProvider, DbContextOptionsBuilder>, Boolean, Boolean, Boolean)
type: Method
summary: Configures `DbContext` used by the application to access the host database containing tenant settings.
syntax:
  content: IMultiTenancyApplicationBuilder WithHostDbContext(Action<IServiceProvider, DbContextOptionsBuilder> configureServiceDbContext, bool isMiddleTier = false, bool enableOptimisticLock = true, bool enableDeferredDeletion = true)
  parameters:
  - id: configureServiceDbContext
    type: System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder}
    description: A delegate that configures `DbContext`.
  - id: isMiddleTier
    type: System.Boolean
    defaultValue: "False"
    description: '`true` if the application uses the [Middle Tier Security](xref:113439); otherwise, `false`.'
  - id: enableOptimisticLock
    type: System.Boolean
    defaultValue: "True"
    description: '`true` to enable [Optimistic Locking](xref:405384); otherwise, `false`.'
  - id: enableDeferredDeletion
    type: System.Boolean
    defaultValue: "True"
    description: '`true` to enable [Soft Deletion (Deferred Object Deletion)](xref:405259); otherwise, `false`.'
  return:
    type: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder
    description: The application builder that processed the action.
seealso: []
---
