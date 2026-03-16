---
uid: DevExpress.ExpressApp.ApplicationBuilder.AuditedDbContextConfigurator.Configure``2(System.Action{DevExpress.ExpressApp.XafApplication,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},System.Action{DevExpress.ExpressApp.XafApplication,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder},System.Action{DevExpress.Persistent.BaseImpl.EFCore.AuditTrail.AuditTrailOptions})
name: Configure<TBusinessObjectDbContext, TAuditHistoryDbContext>(Action<XafApplication, DbContextOptionsBuilder>, Action<XafApplication, DbContextOptionsBuilder>, Action<AuditTrailOptions>)
type: Method
summary: Configures the main (business object) and additional (audit history) `DbContext` objects in WinForms applications with the [Audit Trail Module](xref:403104).
syntax:
  content: |-
    public abstract void Configure<TBusinessObjectDbContext, TAuditHistoryDbContext>(Action<XafApplication, DbContextOptionsBuilder> configureBusinessObjectDbContext, Action<XafApplication, DbContextOptionsBuilder> configureAuditHistoryDbContext, Action<AuditTrailOptions> configureAuditTrailOptions = null)
        where TBusinessObjectDbContext : DbContext where TAuditHistoryDbContext : DbContext
  parameters:
  - id: configureBusinessObjectDbContext
    type: System.Action{DevExpress.ExpressApp.XafApplication,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder}
    description: A delegate that configures the main application `DbContext`.
  - id: configureAuditHistoryDbContext
    type: System.Action{DevExpress.ExpressApp.XafApplication,Microsoft.EntityFrameworkCore.DbContextOptionsBuilder}
    description: A delegate that configures the additional `DbContext` that the Audit Trail Module uses to store records.
  - id: configureAuditTrailOptions
    type: System.Action{DevExpress.Persistent.BaseImpl.EFCore.AuditTrail.AuditTrailOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Audit Trail Module.
  typeParameters:
  - id: TBusinessObjectDbContext
    description: The main application `DbContext`.
  - id: TAuditHistoryDbContext
    description: The additional `DbContext` that the Audit Trail Module uses to store records.
seealso: []
---
The following example demonstrates how to use this method:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{14-23}
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

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{11-20}
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