---
uid: "404322"
title: 'How to: Use Multiple Data Models Connected to Different Databases in Entity Framework Core'
---

# How to: Use Multiple Data Models Connected to Different Databases in Entity Framework Core

This article describes how to implement an XAF application with custom Entity Framework DbContexts that work with separate databases. These modules do not depend on each other and thus can be reused in other applications independently.

[!example[How to connect different data models to several databases within a single application with Entity Framework Core](https://github.com/DevExpress-Examples/XAF_how-to-connect-different-data-models-to-several-databases-within-a-single-application)]

This example assumes that you have an XAF application that includes both Windows Forms and ASP.NET Core Blazor projects with standard authentication enabled and the Security System configured in [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core).

## Define Separate Connection Strings

In configuration files for Blazor and WinForms projects, define three separate connection strings: one connection string for a database that stores security data, and two additional connection strings for separate databases used to store application data.

**File:** _SolutionName.Blazor.Server/appsettings.json_, _SolutionName.Win/App.config_
  
  # [ASP.NET Core Blazor](#tab/tabid-blazor)

  ```JSON	
  "ConnectionStrings": {
    "ConnectionString0": "Integrated Security=SSPI;Pooling=false;MultipleActiveResultSets=true;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=DB0_EFCore",
    "ConnectionString1": "Integrated Security=SSPI;Pooling=false;MultipleActiveResultSets=true;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=DB1_EFCore",
    "ConnectionString2": "Integrated Security=SSPI;Pooling=false;MultipleActiveResultSets=true;Data Source=(localdb)\\mssqllocaldb;Initial Catalog=DB2_EFCore",
  }
  ```

  # [Windows Forms](#tab/tabid-winforms)
   
  ```XML
  <connectionStrings>
    <add name="ConnectionString0" 
      connectionString="Integrated Security=SSPI;MultipleActiveResultSets=True;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DB0_EFCore" 
      providerName="System.Data.SqlClient" />
    <add name="ConnectionString1" 
      connectionString="Integrated Security=SSPI;MultipleActiveResultSets=True;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DB1_EFCore" 
      providerName="System.Data.SqlClient" />
    <add name="ConnectionString2" 
      connectionString="Integrated Security=SSPI;MultipleActiveResultSets=True;Data Source=(localdb)\mssqllocaldb;Initial Catalog=DB2_EFCore" 
      providerName="System.Data.SqlClient" />
  </connectionStrings>
  ```
  ***

## Configure the Main Module's DbContext to Store Security Data

In the example project, the main module's DbContext is configured to only store data used by the Security System (users, roles, and login information). The [Template Kit](xref:405447) generates the required code if you enable the Security System. Otherwise, you need to add required persistent classes and configure platform-specific projects as described in the following article: [Use the Security System - Implement Standard Authentication in Code](xref:404204#implement-standard-authentication-in-code).

**File:** _CommonModule/BusinessObjects/CommonModuleDbContext.cs_

  # [C#](#tab/tabid-csharp)

  ```csharp
  public class CommonModuleEFCoreDbContext : DbContext {
    // ...
    public DbSet<PermissionPolicyRole> Roles { get; set; }
    public DbSet<ApplicationUser> Users { get; set; }
    public DbSet<ApplicationUserLoginInfo> UserLoginInfos { get; set; }
    // ...
  }
  ```
  ***

**File:** _SolutionName.Blazor.Server/Startup.cs_, _SolutionName.Win/Startup.cs_
  
  # [ASP.NET Core Blazor](#tab/tabid-blazor)

  ```csharp
  public class Startup {
      // ...
      public void ConfigureServices(IServiceCollection services) {
          services.AddXaf(Configuration, builder => {
              builder.Security
                  .UseIntegratedMode(options => {
                      options.RoleType = typeof(PermissionPolicyRole);
                      options.UserType = typeof(CommonModule.BusinessObjects.ApplicationUser);
                      options.UserLoginInfoType = typeof(CommonModule.BusinessObjects.ApplicationUserLoginInfo);
                  })
              // ...
          });
      }
  }
  ```

  # [Windows Forms](#tab/tabid-winforms)
   
  ```csharp
  public class ApplicationBuilder : IDesignTimeApplicationFactory {
      public static WinApplication BuildApplication(string connectionString) {
          var builder = WinApplication.CreateBuilder();
          // ...
          builder.Security
              .UseIntegratedMode(options => {
                  options.RoleType = typeof(PermissionPolicyRole);
                  options.UserType = typeof(CommonModule.BusinessObjects.ApplicationUser);
                  options.UserLoginInfoType = typeof(CommonModule.BusinessObjects.ApplicationUserLoginInfo);
              })
          // ...
  }
  ```
  ***

## Add Custom Modules to Store Data in Separate Databases 

Use the [Template Kit](xref:405447) to add two new custom XAF modules to an XAF solution as described in the following article: [Create a Custom XAF Module](xref:405523). For each custom module, implement its own DbContext and persistent classes.

Add static methods that configure the Object Space and DbContexts (`SetupObjectSpace()` and `SetupDbContext()`) to all module classes in the solution. Make sure that each module uses its own connection string.

**File:** _ClassLibrary1/XafModule1.cs_, _ClassLibrary2/XafModule2.cs_, _CommonModule/Module.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ApplicationBuilder.Internal;
using Microsoft.Extensions.Configuration;

public class XafModule1 : ModuleBase {
    // ...
    // Specify a separate connection string for each module.
    const string ConnectionStringName = "ConnectionString1"; 

    public static void SetupObjectSpace<TContext>(IObjectSpaceProviderBuilder<TContext> objectSpaceProviderBuilder) 
        where TContext : IXafApplicationBuilder<TContext> {
        string connectionString = ConfigurationManager.ConnectionStrings[ConnectionStringName]?.ConnectionString;
        objectSpaceProviderBuilder.AddSecuredEFCore()
            .WithDbContext<ClassLibrary1EFCoreDbContext>((application, options) => {
                SetupDbContext(options, connectionString),
            }, ServiceLifetime.Transient);
    }
    
    public static void SetupObjectSpace<TContext>(IObjectSpaceProviderServiceBasedBuilder<TContext> 
      objectSpaceProviderBuilder, IConfiguration configuration) 
        where TContext : IXafApplicationBuilder<TContext>, IAccessor<IServiceCollection> {
        string connectionString = configuration.GetConnectionString(ConnectionStringName);
        objectSpaceProviderBuilder.AddSecuredEFCore()
            .WithDbContext<ClassLibrary1EFCoreDbContext>((application, options) => {
                SetupDbContext(options, connectionString),
            }, ServiceLifetime.Transient);
    }

    static void SetupDbContext(DbContextOptionsBuilder options, string connectionString) {
        ArgumentNullException.ThrowIfNull(connectionString);
        options.UseConnectionString(connectionString);
        options.UseObjectSpaceLinkProxies();
    }
}
```
***

Make the following edits to _Startup.cs_ files in your Blazor and WinForms projects:

- Register additional modules as shown in the following code snippet:

  # [C#](#tab/tabid-csharp)

  ```csharp
  public void ConfigureServices(IServiceCollection services) {
      // ...
      services.AddXaf(Configuration, builder => {
          // ...
          builder.Modules 
              .Add<ClassLibrary1.XafModule1>()
              .Add<ClassLibrary2.XafModule2>();
          // ...
      }
  }
  ```
  ***

- Call the `SetupObjectSpace()` static methods for the ClassLibrary1 and ClassLibrary2 modules. ASP.NET Core Blazor and Windows Forms projects require different overloads of this method:

  # [ASP.NET Core Blazor](#tab/tabid-blazor)

  ```csharp	
  public void ConfigureServices(IServiceCollection services) {
      // ...
      services.AddXaf(Configuration, builder => {
          // ...
          ClassLibrary1.XafModule1.SetupObjectSpace(builder.ObjectSpaceProviders, Configuration);
          ClassLibrary2.XafModule2.SetupObjectSpace(builder.ObjectSpaceProviders, Configuration);
          // ...
      }
  }
  ```

  # [Windows Forms](#tab/tabid-winforms)
   
  ```csharp
  public void ConfigureServices(IServiceCollection services) {
      // ...
      services.AddXaf(Configuration, builder => {
          // ...
          ClassLibrary1.XafModule1.SetupObjectSpace(builder.ObjectSpaceProviders);
          ClassLibrary2.XafModule2.SetupObjectSpace(builder.ObjectSpaceProviders);
          // ...
      }
  }
  ```
  ***

  >[!note]
    Business classes linked to different `ObjectSpaceProviders` are considered to be isolated from each other and thus cannot have direct links between them, for example, an association between two classes. Consider using the [How to prevent altering the legacy database schema when creating an XAF application](https://github.com/DevExpress-Examples/xaf-how-to-prevent-altering-the-legacy-database-schema-when-creating-an-xaf-application) or alternative solutions if you need interlinks between classes from different data stores.

