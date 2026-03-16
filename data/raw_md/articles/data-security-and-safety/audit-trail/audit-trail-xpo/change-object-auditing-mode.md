---
uid: "402079"
title: 'Change Object Auditing Mode'
owner: Yekaterina Kiseleva
---
# Change Object Auditing Mode

The Audit Trail System supports several object auditing modes.

| Mode | Description |
|---|---|
| **Full** | All object changes are fully audited. This mode is the default. |
| **Lightweight** | Only object creation, deletion, and modification are audited. This mode does not audit names and values of changed properties. |
| **CreationOnly** | Only object creation is audited. Intended for data import purposes. |

This topic describes how to change the object auditing mode in various scenarios.

## Change Auditing Mode Globally

In the application's _Startup.cs_ file, add the following code to the `AddAuditTrailXpo` method call to change the auditing mode globally.

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.AuditTrail;
// ...
builder.Modules
    .AddAuditTrailXpo(o => {
        o.ObjectAuditingMode = ObjectAuditingMode.Lightweight;
    })
```

***

## Change Auditing Mode in the Current Scope

Use the service provider's `GetRequiredService` method to access the audit trail options and change the auditing mode in the current scope only. The following code sample demonstrates how to change the auditing mode based on the current user:

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp-net6-blazor)

```csharp{14-20}
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
                            auditOptions.ObjectAuditingMode = ObjectAuditingMode.Lightweight;
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

```csharp{12-18}
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
                        auditOptions.ObjectAuditingMode = ObjectAuditingMode.Lightweight;
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
