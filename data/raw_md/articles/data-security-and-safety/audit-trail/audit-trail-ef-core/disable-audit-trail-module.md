---
uid: "403496"
title: Disable the Audit Trail Module
---
# Disable the Audit Trail Module

## Disable the Module Permanently

To disable the [Audit Trail Module](xref:112782) and stop tracking changes in your application, use the standard `DbContextFactory` instead of `AuditedDbContext`. Configure database context options for audited and not-audited contexts. Call the [WithDbContext](xref:DevExpress.ExpressApp.ApplicationBuilder.DbContextServiceBasedBuilder`1.WithDbContext``1(System.Action{System.IServiceProvider,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},Microsoft.Extensions.DependencyInjection.ServiceLifetime)) method to disable the Audit Trail Module or [WithAuditedDbContext](xref:DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextBuilderExtensions.WithAuditedDbContext``1(DevExpress.ExpressApp.ApplicationBuilder.DbContextServiceBasedBuilder{``0},System.Action{DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextServiceBasedConfigurator},Microsoft.Extensions.DependencyInjection.ServiceLifetime)) method to enable the module.

> [!Note]
> With this technique, you cannot change the state of the Module during application execution.

The following example declares an additional `UseStandardDbContectFactory` field to switch between the audited and standard `DbContext` factories:

# [Startup.cs](#tab/tabid-csharp)

```csharp
bool UseStandardDbContectFactory = true;
//...
var dbContextServiceBuilder = builder.ObjectSpaceProviders
    .AddSecuredEFCore(options => options.PreFetchReferenceProperties());
Action<IServiceProvider, DbContextOptionsBuilder> configureDbContextOptions = (serviceProvider, dbContextOptions) => {
    //your dbContextOptions configuration here
};
Action<IServiceProvider, DbContextOptionsBuilder> configureAuditedDbContextOptions = (serviceProvider, dbContextOptions) => {
    //your auditedDbContextOptions configuration here
};
if (UseStandardDbContectFactory) {
    dbContextServiceBuilder.WithDbContext<MySolution.Module.BusinessObjects.MySolutionEFCoreDbContext>(configureDbContextOptions);
} else {
    dbContextServiceBuilder.WithAuditedDbContext(contexts => {
        contexts.Configure<MySolution.Module.BusinessObjects.MySolutionEFCoreDbContext, 
            MySolution.Module.BusinessObjects.MySolutionAuditingDbContext>(
                configureDbContextOptions,
                configureAuditedDbContextOptions);
    });
}
builder.ObjectSpaceProviders.AddNonPersistent();
```
***

## Disable the Module Temporarily

The `AuditTrailService.Enabled` property allows you to disable the Audit Trail Module for a specific scenario. You can use this technique in different parts of your application (for example, in Controllers).

The following example demonstrates this technique:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.EFCore;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EFCore.AuditTrail;
// ...
public class CustomController : ViewController<DetailView> {
    public CustomController() {
        SimpleAction customAction = new SimpleAction(this, "CustomAction", PredefinedCategory.View);
        customAction.Execute += CustomAction_Execute;
    }
    private void CustomAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        AuditTrailService auditTrailService = ((EFCoreObjectSpace)ObjectSpace).GetAuditTrailService();
        auditTrailService.Enabled = false;
        // non-tracked actions or changes
        auditTrailService.Enabled = true;
    }
}
```
***

> [!NOTE]
> * The `AuditTrailService.SaveCustomData` method ignores the `AuditTrailService.Enabled` property. You can use this method when the property is set to `false`.
> * If you use one Object Space in multiple places simultaneously, the Audit Trail Module does not track changes throughout the application when `AuditTrailService.Enabled` is set to `false`.