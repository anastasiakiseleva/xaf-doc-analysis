---
uid: '115638'
seealso: []
title: Security Permissions Caching
owner: Ekaterina Kiseleva
---
# Security Permissions Caching

This topic describes how to specify the way an application with `SecurityStrategyComplex` caches permissions.

## General Information

The Security System uses Security Adapters to process and cache security permission requests. Each Security Adapter has the corresponding Security Adapter Provider used internally to register the Adapter. The following assemblies contain platform-dependent Adapters and their Providers:

{|
|-
! Platform
! Assembly
|-

| XPO
| _DevExpress.ExpressApp.Security.Xpo[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_ 
|-

| Entity Framework Core
| _DevExpress.EntityFrameworkCore.Security[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_
|}

These assemblies contain the `RegisterXPOAdapterProviders`, `RegisterEFAdapterProviders`, and `RegisterEFCoreAdapterProviders` methods that extend the @DevExpress.ExpressApp.Security.SecurityStrategy class. Use these methods to enable/disable Security Adapters instead of accessing them directly. 

> [!NOTE] 
> You do not need to call the `RegisterEFCoreAdapterProviders` method because @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 calls this method automatically.

## Enable the Security Adapter

The [Template Kit](xref:405447) adds the following platform-dependent code to enable the Security Adapter in new XAF projects.

### WinForms Applications

Call `Register***AdapterProviders` in the application's builder.

```csharp{8-9}
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                // ...
                // XPO
                options.Events.OnSecurityStrategyCreated += securityStrategy => {
                    ((SecurityStrategy)securityStrategy).RegisterXPOAdapterProviders();
                };
            })
        // ...
    }
}
```

### ASP.NET Core Blazor Applications

Call `Register***AdapterProviders` in the `Startup.ConfigureServices` method.

```csharp{9-10}
public class Startup {
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            // ...
            builder.Security
                .UseIntegratedMode(options => {
                    // ...
                    // XPO
                    options.Events.OnSecurityStrategyCreated += securityStrategy => {
                        ((SecurityStrategy)securityStrategy).RegisterXPOAdapterProviders();

                    };
                })
        });
    }

    // ...
}
```

## Set the Permissions Reload Mode

To specify how Security Adapters reload security permissions, set the `SecurityStrategyComplex`'s @DevExpress.ExpressApp.Security.SecurityStrategy.PermissionsReloadMode property to a [](xref:DevExpress.ExpressApp.Security.PermissionsReloadMode) enumeration value. The default mode is `NoCache`. In this mode, the cache is created for each [](xref:DevExpress.Xpo.Session) (in XPO) and [DBContext](xref:Microsoft.EntityFrameworkCore.DbContext) (in EF Core). 

Switch to the **CacheOnFirstAccess** mode to eagerly load permissions from the database in a single SQL query and cache them when secured data is accessed for the first time. The application then uses the cached permissions until a user logs out.

This mode allows you to reduce the number of database requests in an application that works with secured data.

## Limitations

The [XAF Web API Service](xref:403394) is stateless and does not support security permission caching. Under this setup, the `SecurityStrategy.PermissionsReloadMode` property set to `PermissionsReloadMode.CacheOnFirstAccess` has no effect.
