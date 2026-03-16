---
uid: DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderBuilderExtensions.AddEFCore``1(DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{``0},System.Action{DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderOptionsBuilder})
name: AddEFCore<TContext>(IObjectSpaceProviderBuilder<TContext>, Action<EFCoreObjectSpaceProviderOptionsBuilder>)
type: Method
summary: Adds the @DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1 to your WinForms application.
syntax:
  content: |-
    public static DbContextBuilder<TContext> AddEFCore<TContext>(this IObjectSpaceProviderBuilder<TContext> builder, Action<EFCoreObjectSpaceProviderOptionsBuilder> configureObjectSpaceProviderOptions = null)
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
  - id: configureObjectSpaceProviderOptions
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderOptionsBuilder}
    defaultValue: "null"
    description: Options that allow you to configure the Object Space Provider.
  typeParameters:
  - id: TContext
    description: The @DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.DbContextBuilder{{TContext}}
    description: '[!include[IObjectSpaceProviderBuilder_Parameter_Description](~/templates/IObjectSpaceProviderBuilder_Parameter_Description.md)]'
seealso: []
---

This method must be used together with one of the following methods:

* @DevExpress.ExpressApp.ApplicationBuilder.DbContextBuilder`1.WithDbContext``1(System.Action{DevExpress.ExpressApp.XafApplication,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},Microsoft.Extensions.DependencyInjection.ServiceLifetime)
* @DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextBuilderExtensions.WithAuditedDbContext``1(DevExpress.ExpressApp.ApplicationBuilder.DbContextBuilder{``0},System.Action{DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextConfigurator},Microsoft.Extensions.DependencyInjection.ServiceLifetime)

The following example demonstrates how to use the `AddEFCore` method:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{9-13}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.ObjectSpaceProviders
            .AddEFCore()
            .WithDbContext<MySolutionEFCoreDbContext>((application, options) => {
                // ...
            })
            .AddNonPersistent();
    }
    // ...
}
```
***