---
uid: "402082"
title: 'Audit Specific Operations'
owner: Yekaterina Kiseleva
---
# Audit Specific Operations

You can instruct Audit Trail Module not to log specific operations. For example, the following code samples demonstrate how to exclude the `ObjectChanged` and `ObjectCreated` records from the audit log.

Handle the [AuditTrailEvents.OnCustomizeAuditOperationTypeFilter](xref:DevExpress.ExpressApp.AuditTrail.AuditTrailEvents.OnCustomizeAuditOperationTypeFilter) event, check the current operation type, and set the @DevExpress.Persistent.AuditTrail.CustomAuditOperationTypeFilterEventArgs.SaveAuditOperation argument to `false`. 

## Exclude Operations Globally

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp-net6)

```csharp
using DevExpress.Persistent.AuditTrail;
// ...
builder.Modules
    .AddAuditTrailXpo(o => {
        o.Events.OnCustomizeAuditOperationTypeFilter = context => {
            if (context.AuditOperationType == AuditOperationType.ObjectChanged ||
                context.AuditOperationType == AuditOperationType.ObjectCreated) {
                context.SaveAuditOperation = false;
            }
        };
    })
```

***

## Exclude Operations in the Current Scope

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp-net6-blazor)

```csharp{18-23}
using DevExpress.ExpressApp.AuditTrail;
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Options;

public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddScoped<CircuitHandler, CircuitHandlerProxy>();
        services.AddXaf(Configuration, builder => {
            builder.Security
                .UseIntegratedMode(options => {
                    options.Events.OnLogon += context => {
                        string userName = ((ApplicationUser)context.User).UserName;
                        if (userName == "User") {
                            var auditOptions = context.ServiceProvider.GetRequiredService<IOptionsSnapshot<AuditTrailOptions>>().Value;
                            auditOptions.Events.OnCustomizeAuditOperationTypeFilter = context => {
                                if (context.AuditOperationType == AuditOperationType.ObjectChanged ||
                                    context.AuditOperationType == AuditOperationType.ObjectCreated) {
                                    context.SaveAuditOperation = false;
                                }
                            };
                        }
                    };
                    //...
                })
            // ...
        }
        // ...
    }
    // ...
}
```

# [C# (WinForms)](#tab/tabid-csharp-net6-winforms)

```csharp{16-21}
using DevExpress.ExpressApp.AuditTrail;
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Options;

public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                options.Events.OnLogon += context => {
                    string userName = ((ApplicationUser)context.User).UserName;
                    if (userName == "User") {
                        var auditOptions = context.ServiceProvider.GetRequiredService<IOptionsSnapshot<AuditTrailOptions>>().Value;
                        auditOptions.Events.OnCustomizeAuditOperationTypeFilter = context => {
                            if (context.AuditOperationType == AuditOperationType.ObjectChanged ||
                                context.AuditOperationType == AuditOperationType.ObjectCreated) {
                                context.SaveAuditOperation = false;
                            }
                        };
                    }
                };
                //...
            })
        // ...
    }
    // ...
}
```
***

Note that the `AuditTrailOptions` type is wrapped into `IOptionsSnapshot`, which is then passed as the `GetRequiredService` method's type parameter. This is done to adjust the Audit Trail module settings in the current scope only. For more information, refer to the following topic: [Use IOptionsSnapshot to read updated data](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options#use-ioptionssnapshot-to-read-updated-data).
