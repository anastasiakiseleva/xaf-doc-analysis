---
uid: "112783"
seealso:
- linkId: "112782"
title: Miscellaneous Customizations of the Audit Trail System (XPO)
---
# Miscellaneous Customizations of the Audit Trail System (XPO)

## Implement Custom Persistent Object to be Used as the Audit Data Storage
The Audit Trail Module uses the `AuditDataItemPersistent` class as the audit data storage. To store extra audit information, inherit from this class or implement the `IAuditDataItemPersistent` interface. In the overridden `OnSaving` method of your `AuditDataItemPersistent` descendant, initialize extra properties based on the `AuditedObject`, `PropertyName`, and other information from the base class. Set the `AuditDataItemPersistentType` property to your class to use it instead of the default class.

## Specify the String Representation of the Null Value
The Audit Trail Module saves the null value as the "N/A" string. To change its string representation, navigate to the `Localization` | `AuditTrail` node in the Model Editor and specify the `NullValueString` property. 

![NullValueString property in Model Editor](~/images/NullValueString.png)

If you want to use a different null value representation in audit records in the UI, set `AuditTrailServiceRoot.AuditDataStore`'s `NullValueString` property as shown below.

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp-net6)

```csharp
using DevExpress.Persistent.AuditTrail;
// ...
builder.Modules
    .AddAuditTrailXpo(o => {
        o.Events.OnCustomizeAuditDataStore = context => {
            context.AuditDataStore.NullValueString = "";
        };
    })
```

***

## Customize the Blob Properties Storage Mechanism
The Audit Trail Module saves Blob property values as the "Blob data" string. Follow the steps below to customize this behavior.

> [!Note]
> You can also use this technique to specify the string representation of reference type properties.

1. Implement the `AuditDataStore` descendant and override its `GetDefaultStringRepresentation` method. 

    **File**: _MySolution.Module\CustomAuditDataStore.cs_.
    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.Persistent.AuditTrail;
    using DevExpress.Persistent.BaseImpl;
    // ...
    public class CustomAuditDataStore : AuditDataStore<AuditDataItemPersistent, AuditedObjectWeakReference> {
        protected override string GetDefaultStringRepresentation(object value) {
            string result = base.GetDefaultStringRepresentation(value);
            if(result == BlobDataString)
                return GetCustomBlobDataString(value);
            return result;
        }

        private string GetCustomBlobDataString(object value) {
            // ...  
        }
    }
    ```

    ***

2. Configure the Audit Trail system to use your custom data store. In the application's _Startup.cs_ file, add the following code to the `AddAuditTrailXpo` method call.

    **File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

    # [C#](#tab/tabid-csharp-net6)

    ```csharp
    using DevExpress.Persistent.AuditTrail;
    // ...
    builder.Modules
        .AddAuditTrailXpo(o => {
            o.Events.OnCustomCreateAuditDataStore = context => {
                context.AuditDataStore = new CustomAuditDataStore();
            };
        })
    ```

    ***

## Implement a Custom AuditTrailService

In XAF applications, the Audit Trail system is implemented as a service (`IAuditTrailService`). You can create and register your own implementation of the `IAuditTrailService` as this section describes.

To create a custom `IAuditTrailService`, you can use the [](xref:DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase) type as a base type for your custom implementation or implement the `IAuditTrailService` interface from scratch:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.BaseImpl.AuditTrail.Services;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Options;

public class CustomAuditTrailService : AuditTrailServiceBase {
    private const string unknownUserName = "Unknown";
    private readonly ISecurityStrategyBase securityStrategy;
    private readonly IAuditTrailServiceRoot auditTrailServiceRoot;
    private bool isSetupAuditCalled = false;

    public CustomAuditTrailService(IServiceProvider serviceProvider, IAuditTrailServiceRoot auditTrailServiceRoot, IOptionsSnapshot<AuditTrailOptions> auditTrailServiceOptions) :
        base(serviceProvider, auditTrailServiceRoot, auditTrailServiceOptions.Value) {
        this.securityStrategy = serviceProvider.GetService<ISecurityStrategyBase>();
        this.auditTrailServiceRoot = auditTrailServiceRoot;
    }
    protected override void EnsureSetupAudit() {
        if(!isSetupAuditCalled) {
            isSetupAuditCalled = true;
            auditTrailServiceRoot.SetupAudit(serviceProvider.GetRequiredService<ITypesInfo>(), Options.AuditDataItemPersistentType);
        }
    }
    protected override string GetCurrentUserNameCore() {
        return securityStrategy != null ? securityStrategy.UserName : unknownUserName;
    }
}
```

***

Register your custom `IAuditTrailService` type as a scoped service:

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp-blazor)

```csharp
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MyBlazorApplication>();
            builder.Modules
            // ...
                .AddAuditTrailXpo()
            // ...
        });
        services.AddScoped<IAuditTrailService, CustomAuditTrailService>();
        // ...
    }
//...
}
```

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.Services.AddScoped<IAuditTrailService, CustomAuditTrailService>();
        builder.Modules
        // ...
            .AddAuditTrailXpo()
        // ...
    }
    // ...
}
```

# [C# (Web API Service)](#tab/tabid-csharp-webapi)

```csharp
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddAuditTrailXpoServices();
        services.AddScoped<IAuditTrailService, CustomAuditTrailService>();
        // ...
    }
// ...
}
```

***