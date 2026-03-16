---
uid: "402083"
title: 'Specify Objects and Properties to Be Audited'
---
# Specify Objects and Properties to Be Audited

The Audit Trail Module [logs changes](xref:112782#tracked-changes) in the following objects and properties:

* Persistent classes.
* Public writable simple and reference properties defined in persistent classes.
* Public collection properties defined in persistent classes.

Read-only properties (those without a setter) and properties decorated with the @DevExpress.Xpo.NonPersistentAttribute are excluded from the audit trail.

You can modify default audit settings — specify objects and properties to be audited or excluded from the audit process. 

## Specify Audit Settings Globally

You can handle the `AuditTrailServiceRoot.CustomizeAuditTrailSettings` event or apply the @DevExpress.Persistent.Base.UseInAuditTrailAttribute to add or remove objects and properties in/from audit globally.

### Handle CustomizeAuditTrailSettings Event

Subscribe to the `AuditTrailServiceRoot.CustomizeAuditTrailSettings` event in the `AddAuditTrailXpo` method call to modify audit settings:

# [MySolution.Blazor.Server\Startup.cs | MySolution.Win\Startup.cs | MySolution.WebApi\Startup.cs](#tab/tabid-csharp)

```csharp{5-14}
using DevExpress.Persistent.AuditTrail;
// ...
builder.Modules
    .AddAuditTrailXpo(o => {
        o.Events.OnCustomizeAuditTrailSettings = context => {
            // Clear the default settings:
            context.AuditTrailSettings.Clear();
            // Add a type's specific properties: 
            context.AuditTrailSettings.AddType(typeof(MyObjectType1), "FirstPropertyToBeAudited", "SecondPropertyToBeAudited");
            // Add all properties of the type: 
            context.AuditTrailSettings.AddType(typeof(MyObjectType2));
            // Exclude the type's properties:
            context.AuditTrailSettings.RemoveProperties(typeof(MyObjectType2), "PropertyToBeExcluded");
        };
    })
```

***

### Apply UseInAuditTrail Attribute

Use the @DevExpress.Persistent.Base.UseInAuditTrailAttribute to specify whether a property takes part in audit.

# [MySolution.Module\BusinessObjects\MyClass.cs](#tab/tabid-csharp)
```csharp
// remove the persistent property from audit
[UseInAuditTrail(false)]
public string MyPersistentProperty { 
    get { return myPersistentProperty; }
    set { SetPropertyValue(nameof(MyPersistentProperty), ref myPersistentProperty, value); }
}

// add the non-persistent property in audit
[UseInAuditTrail(true)]
[NonPersistent]
public string MyNonPersistentProperty {
    get { return myNonPersistentProperty; }
    set { SetPropertyValue(nameof(MyNonPersistentProperty), ref myNonPersistentProperty, value); }
}
```
***

## Specify Audit Settings for the Current Scope

Use the service provider's `GetRequiredService` method to access audit trail options and modify audit settings in the current scope only. The following code sample demonstrates how to change audit settings based on the current user:

# [MySolution.Blazor.Server/Startup.cs](#tab/tabid-csharp-blazor)

```csharp{14-29}
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
                            auditOptions.Events.OnCustomizeAuditTrailSettings = context => {
                                // Clear the default settings:
                                context.AuditTrailSettings.Clear();
                                // Add a type's specific properties: 
                                context.AuditTrailSettings.AddType(typeof(MyObjectType1), "FirstPropertyToBeAudited", "SecondPropertyToBeAudited");
                                // Add all properties of the type: 
                                context.AuditTrailSettings.AddType(typeof(MyObjectType2));
                                // Exclude the type's properties:
                                context.AuditTrailSettings.RemoveProperties(typeof(MyObjectType2), "PropertyToBeExcluded");
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

# [MySolution.Win/Startup.cs](#tab/tabid-csharp-win)

```csharp{12-27}
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
                        auditOptions.Events.OnCustomizeAuditTrailSettings = context => {
                            // Clear the default settings:
                            context.AuditTrailSettings.Clear();
                            // Add a type's specific properties: 
                            context.AuditTrailSettings.AddType(typeof(MyObjectType1), "FirstPropertyToBeAudited", "SecondPropertyToBeAudited");
                            // Add all properties of the type: 
                            context.AuditTrailSettings.AddType(typeof(MyObjectType2));
                            // Exclude the type's properties:
                            context.AuditTrailSettings.RemoveProperties(typeof(MyObjectType2), "PropertyToBeExcluded");
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
