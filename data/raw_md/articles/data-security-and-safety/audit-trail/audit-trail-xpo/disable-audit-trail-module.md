---
uid: "402080"
title: 'Disable the Audit Trail Module (XPO)'
---
# Disable the Audit Trail Module (XPO)

This topic demonstrates two options you can use to disable the [Audit Trail Module](xref:112782) in your application:
* [In a Configuration File](#in-a-configuration-file)  
  Disable the Module unconditionally.
* [In Application Code](#in-application-code)  
  Disable the Module for a specific scenario.

## In a Configuration File

Add the **EnableAuditTrail** key with the **False** value to an application's configuration file, as shown below:
# [XML](#tab/tabid-xml)

```XML
<appSettings>
    <!-- ... -->
    <add key="EnableAuditTrail" value ="False"/>
    <!-- ... -->
</appSettings>
```
***

## In Application Code

The Audit Trail Module runs as a service. You can use the service provider's `GetRequiredService` method to access the audit trail options:

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp-blazor)

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
                            auditOptions.Enabled = false;
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

# [C# (WinForms)](#tab/tabid-csharp-winforms)

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
                        auditOptions.Enabled = false;
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

The code snippet above handles the `SecurityEvents.OnLogon` event to disable audit for a certain user when they log in to the application. Note that the `AuditTrailOptions` type is wrapped into `IOptionsSnapshot`, which is then passed as the `GetRequiredService` method's type parameter. This is done to disable the Audit Trail module in the current scope only. For more information, refer to the following topic: [Use IOptionsSnapshot to read updated data](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options#use-ioptionssnapshot-to-read-updated-data).
