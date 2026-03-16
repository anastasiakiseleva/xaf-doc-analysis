---
uid: "404670"
title: 'Convert an Existing Application into a Multi-Tenant Application'
owner: Eugeniy Burmistrov
seealso:
- linkId: "404669"
---

# Convert an Existing Application into a Multi-Tenant Application

Follow the steps below to convert an existing XAF application to a multi-tenant application.

## Install Required Dependencies

Install the following NuGet packages:

SolutionName.Module (the shared module project)
:   **EF Core**: DevExpress.ExpressApp.MultiTenancy.EFCore.v<:xx.x:>  
    **XPO**: DevExpress.ExpressApp.MultiTenancy.XPO.v<:xx.x:>
SolutionName.Blazor.Server (the Blazor application project)
:   **EF Core**: DevExpress.ExpressApp.MultiTenancy.Blazor.EFCore.v<:xx.x:>  
    **XPO**: DevExpress.ExpressApp.MultiTenancy.Blazor.XPO.v<:xx.x:>
SolutionName.Win (the WinForms application project)
:   **EF Core**: DevExpress.ExpressApp.MultiTenancy.Win.EFCore.v<:xx.x:>  
    **XPO**: DevExpress.ExpressApp.MultiTenancy.Win.XPO.v<:xx.x:>
SolutionName.WebApi (the Web API Service project)
:   **EF Core**: DevExpress.ExpressApp.MultiTenancy.WebApi.EFCore.v<:xx.x:>  
    **XPO**: DevExpress.ExpressApp.MultiTenancy.WebApi.Xpo.v<:xx.x:>
SolutionName.MiddleTier (the Middle Tier Security project)
:   **EF Core**: DevExpress.ExpressApp.MultiTenancy.AspNetCore.EFCore.v<:xx.x:>  
    **XPO**: DevExpress.ExpressApp.MultiTenancy.AspNetCore.Xpo.v<:xx.x:>

## Add a Connection String for the Host Database
 
Edit the application's configuration file:

* _appsettings.json_ in Blazor, Web API Service, Middle Tier Security 
* _App.config_ in WinForms

Add a connection string for the [Host Database](xref:404436#glossary) (named `"ConnectionString"` throughout this article).

# [appsettings.json](#tab/json)
```JSON
{
  "ConnectionStrings": {
    "ConnectionString": "Integrated Security=SSPI;Pooling=true;MultipleActiveResultSets=true;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=MySolution_Service",
  },
```
# [app.config](#tab/config)
```XML
<configuration>
  <connectionStrings>
    <add name="ConnectionString" connectionString="Integrated Security=SSPI;MultipleActiveResultSets=True;Data Source=(localdb)\mssqllocaldb;Initial Catalog=MySolution_Service;Application Name=MySolution" providerName="System.Data.SqlClient" />
  </connectionStrings>
</configuration>
```
***

## Enable Multi-Tenancy Mode

In the application's _Startup.cs_ file, add code that enables and configures multi-tenancy mode:

### EF Core

**File:**
* _MySolution.Blazor.Server/Startup.cs_
* _MySolution.Win/Startup.cs_
* _MySolution.WebApi/Startup.cs_
* _MySolution.MiddleTier/Startup.cs_
* _MySolution.Win/Startup.cs_ in Windows Forms applications with Integrated Mode

# [C# (Blazor)](#tab/tabid-csharp-blazor)

```csharp
public class Startup { 
    public void ConfigureServices(IServiceCollection services) {
        services.AddXaf(Configuration, builder => {
            // ...
            builder.AddMultiTenancy() 
                .WithHostDbContext((sp, opt) => {
                    opt.UseConnectionString(Configuration.GetConnectionString("ConnectionString")); 
                })
                .WithTenantResolver<TenantByEmailResolver>(); 
             // ...
        });
    }
} 
```

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.AddMultiTenancy()
            .WithHostDbContext((serviceProvider, options) => { 
                options.UseConnectionString(connectionString);
            }) 
            .WithTenantResolver<TenantByEmailResolver>();
        // ...
    }
}
```

# [C# (Web API Service)](#tab/tabid-csharp-webapi)
```csharp
public class Startup { 
    public void ConfigureServices(IServiceCollection services) {
        services.AddXaf(Configuration, builder => {
            // ...
            builder.AddMultiTenancy() 
                .WithHostDbContext((serviceProvider, options) => {
                    string connectionString = Configuration.GetConnectionString("ConnectionString");
                    options.UseConnectionString(connectionString);
                })
                .WithMultiTenancyModelDifferenceStore()
                .WithTenantResolver<TenantByEmailResolver>();
             // ...
        });
    }
}
```

# [C# (Middle Tier Security)](#tab/tabid-csharp-middletier)
```csharp
public class Startup { 
    public void ConfigureServices(IServiceCollection services) {
        services.AddXaf(Configuration, builder => {
            // ...
            builder.AddMultiTenancy() 
                .WithHostDbContext((serviceProvider, options) => {
                    string connectionString = Configuration.GetConnectionString("ConnectionString");
                    options.UseConnectionString(connectionString);
                })
                .WithMultiTenancyModelDifferenceStore()
                .WithTenantResolver<TenantByEmailResolver>();
             // ...
        });
    }
}
```

# [C# (Windows Forms applications with Integrated Mode)](#tab/tabid-csharp-winformsmiddletier)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.AddMultiTenancy()
            .WithHostDbContext((serviceProvider, options) => { 
                options.UseMiddleTier(serviceProvider.GetRequiredService<ISecurityStrategyBase>());
                options.UseChangeTrackingProxies();
            }, true)
            .WithMultiTenancyModelDifferenceStore()
            .WithTenantResolver<TenantByEmailResolver>();
        // If you register UserType and RoleType on server side only, add them to the options on client side too:
        // builder.Get().PostConfigure<SecurityOptions>(options => {
        //     options.RoleType = typeof(PermissionPolicyRole);
        //     options.UserType = typeof(Module.BusinessObjects.ApplicationUser);
        // });
    }
}
```
***

### XPO

**File:**
* _MySolution.Blazor.Server/Startup.cs_
* _MySolution.Win/Startup.cs_
* _MySolution.WebApi/Startup.cs_
* _MySolution.MiddleTier/Startup.cs_
* _MySolution.Win/Startup.cs_ in Windows Forms applications with Integrated Mode

# [C# (Blazor)](#tab/tabid-csharp-blazor)

```csharp
public class Startup {
    public void ConfigureServices(IServiceCollection services) {
        services.AddXaf(Configuration, builder => {
            // ...
            builder.AddMultiTenancy()
                .WithHostDatabaseConnectionString(Configuration.GetConnectionString("ConnectionString"))
                .WithTenantResolver<TenantByEmailResolver>();
            // ...
        });
    }
} 
```

# [C# (WinForms)](#tab/tabid-csharp-winforms)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.AddMultiTenancy()
            .WithHostDatabaseConnectionString(connectionString)
            .WithTenantResolver<TenantByEmailResolver>();
        // ...
    }
}
```

# [C# (Web API Service)](#tab/tabid-csharp-webapi)
```csharp
public class Startup {
    public void ConfigureServices(IServiceCollection services) {
        services.AddXaf(Configuration, builder => {
            // ...
            builder.AddMultiTenancy()
                // In Web API Service and Windows Forms with Middle Tier Security projects, XAF creates and checks the database only once at setup.
                // If you need to check compatibility for each tenant's database, add this method:
                //.WithTenantDatabaseUpdater()
                .WithHostDatabaseConnectionString(Configuration.GetConnectionString("ConnectionString"))
                .WithMultiTenancyModelDifferenceStore()
                .WithTenantResolver<TenantByEmailResolver>();
            // ...
        });
    }
} 
```

# [C# (Middle Tier Security)](#tab/tabid-csharp-middletier)
```csharp
public class Startup {
    public void ConfigureServices(IServiceCollection services) {
        services.AddXaf(Configuration, builder => {
            // ...
            builder.AddMultiTenancy()
                // In Web API Service and Windows Forms with Middle Tier Security projects, XAF creates and checks the database only once at setup.
                // If you need to check compatibility for each tenant's database, add this method:
                //.WithTenantDatabaseUpdater()
                .WithHostDatabaseConnectionString(Configuration.GetConnectionString("ConnectionString"))
                .WithMultiTenancyModelDifferenceStore()
                .WithTenantResolver<TenantByEmailResolver>();
            // ...
        });
    }
} 
```

# [C# (Windows Forms applications with Integrated Mode)](#tab/tabid-csharp-winformsmiddletier)

```csharp
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.AddMultiTenancy(true)
            .WithMultiTenancyModelDifferenceStore()
            .WithTenantResolver<TenantByEmailResolver>();
        // If you register UserType and RoleType on server side only, add them to the options on client side too:
        // builder.Get().PostConfigure<SecurityOptions>(options => {
        //     options.RoleType = typeof(PermissionPolicyRole);
        //     options.UserType = typeof(Module.BusinessObjects.ApplicationUser);
        // });
        // ...
    }
}
```
***

## Modify Code that Configures ObjectSpaceProviders

In a multi-tenant application, the connection string for a database that stores tenant data is not static and changes based on the current tenant. To accommodate for this, make the following changes to methods that configure the application's [ObjectSpaceProviders](xref:DevExpress.ExpressApp.IObjectSpaceProvider):

- Use the @DevExpress.ExpressApp.MultiTenancy.IConnectionStringProvider service to obtain the connection string instead of assigning the connection string as a static value.
- In a WinForms application that uses EF Core, specify an additional parameter for created ObjectSpaceProviders: `serviceLifeTime = ServiceLifeTime.Transient`.

Below is an example of modified code used to configure `ObjectSpaceProviders` in a multi-tenant application.

**File:** _MySolution.Blazor.Server/Startup.cs_ (_MySolution.Win/Startup.cs_)

# [C# (EF Core)](#tab/tabid-csharp-efcore)

```csharp{4,7}
.AddSecuredEFCore(options => options.PreFetchReferenceProperties())
    .WithDbContext<SolutionEFCoreDbContext>((application, options) => {
        string connectionString = application.ServiceProvider.GetRequiredService<IConnectionStringProvider>().GetConnectionString();
        options.UseConnectionString(connectionString);
        options.UseObjectSpaceLinkProxies();
    }, ServiceLifetime.Transient)
.AddNonPersistent();
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp{3,5}
builder.ObjectSpaceProviders
    .AddSecuredXpo((application, options) => {
        string connectionString = application.ServiceProvider.GetRequiredService<IConnectionStringProvider>().GetConnectionString();
        options.ConnectionString = connectionString;
        // ...
    })
```
***
## Modify the Module Updater Code

A multi-tenant application works with multiple databases that have separate purposes and store separate data sets. Consequently, code that updates a database must take into account what tenant is currently active and whether or not the application runs in Host User Interface mode. In most cases, you need to follow the rules below when you modify the Module Updater Code to use it in a multi-tenant application.

- When you update the Host Database, do not create any business objects used in [Tenant Databases](xref:404436#glossary).
- When you update the Host Database, do not create user accounts with roles other than the Administrators role.
- When you update a Tenant Database, specify user logins in the format from which the format can be determined. For more information, see: [Tenant Resolvers](xref:404667#tenant-resolvers).

To determine the configuration in which the application currently runs, you can use the following custom properties in your [ModuleUpdater](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) descendant:

**File:** _MySolution.Module/DatabaseUpdate/Updater.cs_

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModuleUpdater {
    // Returns the current tenant's unique identifier.
    // If `null`, the application runs in Host User Interface mode.
    Guid? TenantId {
        get {
            return ObjectSpace.ServiceProvider?.GetService<ITenantProvider>()?.TenantId;
        }
    }

    // Returns the current tenant's name.
    // If `null`, the application runs in Host User Interface mode.
    string TenantName {
        get {
            return ObjectSpace.ServiceProvider?.GetService<ITenantProvider>()?.TenantName;
        }
    }
}
```
***

The code sample below demonstrates how you can modify the [UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method implementation to use it in a multi-tenant application:

**File:** _MySolution.Module/DatabaseUpdate/Updater.cs_

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModuleUpdater {
    public override void UpdateDatabaseAfterUpdateSchema() {
        base.UpdateDatabaseAfterUpdateSchema();
        if (TenantId != null) {
            // Code that updates Tenant Databases
            if(TenantName == "company1.com") {
                // Code that updates the database for the tenant `company1.com`
            }
            // ...
        } else {
            // Code that updates the Host Database
            // ...
        }
    }
    // ...
}
```
***
