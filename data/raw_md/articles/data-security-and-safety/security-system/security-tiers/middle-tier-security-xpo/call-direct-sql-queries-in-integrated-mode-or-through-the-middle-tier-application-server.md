---
uid: "118741"
seealso: []
title: 'Execute Direct SQL Queries in Integrated Mode and with XPO Middle Tier Security'
owner: Ekaterina Kiseleva
---

# Execute Direct SQL Queries in Integrated Mode and with XPO Middle Tier Security

You cannot execute [Direct SQL Queries](xref:8914) and [Stored Procedures](xref:8919) in [Integrated Mode](xref:113436) of the [Security System](xref:113366), or when the [Middle Tier Application Server](xref:113439) is used. The "_Transferring requests via ICommandChannel is prohibited within the security engine_" exception occurs when you execute the corresponding methods of the [](xref:DevExpress.Xpo.Session).

> [!NOTE]
> Do not use this approach to handle a database update when the application version changes. Instead, use the protected methods of the [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) class.

## Enable Direct SQL Queries 

### In Integrated Mode

To enable direct queries and stored procedure execution in these configurations, set the `SecuredXPObjectSpaceProviderOptions.AllowICommandChannelDoWithSecurityContext` property to `true` in application startup code that registers the XPO Object Space Provider:

**File**: _MySolution.Blazor.Server/Startup.cs._, _MySolution.Win/Startup.cs_, _MySolution.WebAPI/Startup.cs_

# [C# (Blazor)](#tab/tabid-csharp-blazor)

```csharp{14}
public void ConfigureServices(IServiceCollection services) {-+
    services.AddXaf(Configuration, builder => {
        // ...
        builder.ObjectSpaceProviders
            .AddSecuredXpo((serviceProvider, options) => {
                string connectionString = null;
                if(Configuration.GetConnectionString("ConnectionString") != null) {
                    connectionString = Configuration.GetConnectionString("ConnectionString");
                }
                ArgumentNullException.ThrowIfNull(connectionString);
                options.ConnectionString = connectionString;
                options.ThreadSafe = true;
                options.UseSharedDataStoreProvider = true;
                options.AllowICommandChannelDoWithSecurityContext = true;
            })
        // ...
    });
    // ...
}
```	

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp{5}
public static WinApplication BuildApplication(string connectionString) {
    builder.ObjectSpaceProviders
        .AddSecuredXpo((application, options) => {
            options.ConnectionString = connectionString;
            options.AllowICommandChannelDoWithSecurityContext = true; ;
        })
    // ...
}
```

# [C# (Web API Service)](#tab/tabid-csharp-webapi)

```csharp{14}
public void ConfigureServices(IServiceCollection services) {
    services.AddXafWebApi(builder => {
        // ...
        builder.ObjectSpaceProviders
            .AddSecuredXpo((serviceProvider, options) => {
                string connectionString = null;
                if(Configuration.GetConnectionString("ConnectionString") != null) {
                    connectionString = Configuration.GetConnectionString("ConnectionString");
                }
                ArgumentNullException.ThrowIfNull(connectionString);
                options.ConnectionString = connectionString;
                options.ThreadSafe = true;
                options.UseSharedDataStoreProvider = true;
                options.AllowICommandChannelDoWithSecurityContext = true;
            })
        // ...
    });
    // ...
}   
```

***

### In the Middle-Tier Server

To enable direct queries and stored procedure execution, set the `AllowICommandChannelDoWithSecurityContext` property to `true` in the _Startup.cs_ file in the Middle Tier Security project as follows:

**File**: _MySolution.MiddleTier/Startup.cs._

# [C#](#tab/tabid-csharp1)
 
```csharp{7}
public void ConfigureServices(IServiceCollection services) {
    // ...
    services.AddXafMiddleTier(Configuration, builder => {
        builder.ConfigureDataServer(options => {
            options.UseConnectionString(Configuration.GetConnectionString("ConnectionString"));
            options.UseDataStorePool(true);
            options.AllowICommandChannelDoWithSecurityContext(true);
        });
        // ...
    });
}   
```
***

## Run Direct SQL Queries

After you enable the direct SQL queries, you can [access the Object Space](xref:113707), cast it to the [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace) type, get the [](xref:DevExpress.Xpo.Session) object using the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) property, and call [Session.ExecuteQuery](xref:DevExpress.Xpo.Session.ExecuteQuery*), [Session.ExecuteSproc](xref:DevExpress.Xpo.Session.ExecuteSproc(System.String,DevExpress.Data.Filtering.OperandValue[])), or other suitable methods.
