---
uid: "113239"
title: Production Database and Application Updates
seealso:
- linkId: "113238"
---
# Production Database and Application Updates

This topic describes how to update an application deployed on a user machine or on an application server.

## Update an ASP.NET Core Blazor Application

### Update a Database

1. Launch a command line interpreter, for instance, **Command Prompt**. 
1. Run your application with the `-updateDatabase` command.
    You can use the following additional parameters:
    * `-silent` initiates a silent update without direct user interaction.
    * `-forceUpdate` forces a schema update on each run.
1. Follow the on-screen instructions.

    # [Console (Windows)](#tab/tabid-cmd-win)
    ```Console
    C:\Users\Public\MyApplication\SolutionName.Blazor.Server.exe -updateDatabase -silent -forceUpdate
    ```

    # [Console (Linux or MacOS)](#tab/tabid-cmd-mac)
    ```Console
    dotnet MyApplication/SolutionName.Blazor.ServerSide.dll -updateDatabase -silent -forceUpdate
    ```
    ***

![Update a database for an ASP.NET Core Blazor application](~/images/update-a-database-cli.png)

Run the application to ensure the update was successful.

### Update Application Files

To update an application, you can use the same technique as when you deployed it: [Deploy ASP.NET Core Blazor Server Apps to Azure, Linux with Nginx or Windows with IIS](https://community.devexpress.com/blogs/xaf/archive/2020/10/19/xaf-deploy-asp-net-core-blazor-server-apps-to-azure-linux-with-nginx-or-windows-with-iis.aspx).

## Update a Windows Forms Application

### Update a Database

1. Launch a command line interpreter, for instance, **Command Prompt**. 
1. Run your application with the `-updateDatabase` command.
    You can use the following additional parameters:
    * `-silent` initiates a silent update without direct user interaction.
    * `-forceUpdate` forces a schema update on each run.
1. Follow the on-screen instructions.

# [Console](#tab/tabid-cmd-win1)
```Console
C:\Users\Public\MyApplication\SolutionName.Win.exe -updateDatabase -silent -forceUpdate
```
***

Run the application to ensure that the update was successful.

### Update Application Files

To update an application, you can use the same technique as when you deployed it:
* [Xcopy Method](xref:113232)
* [Setup Project Method](xref:113235)
* [Update ClickOnce applications](https://learn.microsoft.com/en-us/visualstudio/deployment/clickonce-security-and-deployment#update-clickonce-applications)

> [!NOTE]
> Do not overwrite user _SolutionName.Win.dll.config_ or _Model.User.xafml_ files when you update an application. 

### Update Application Files Automatically (Application Updater Utility)

Use this technique to automate the update process at multiple workstations.

#### Prerequisites

Ensure that applications on end-user workstations and the new application you want to deploy meet the following conditions:

1. The [XafApplication.CheckCompatibilityType](xref:DevExpress.ExpressApp.XafApplication.CheckCompatibilityType) property is set to `ModuleInfo`.
2. `NonPersistentObjectSpaceProvider` is not the first registered Provider in your application. XAF uses the first registered Object Space Provider while an application updates.

[!include[checkcompatibilitytype-moduleinfo](~/templates/checkcompatibilitytype-moduleinfo.md)]

#### Enable Auto Update

1. Choose a file server in the end-user network. On this server, create a shared folder that stores newer application versions (for example, the _SolutionNameUpdateSource_ folder). 
2. Ensure that all end users have a _read_ permission to this folder and do not have a _write_ permission.
3. On all end-user workstations, open the _SolutionName.Win.dll.config_ file, and set the `NewVersionServer` key to the [UNC path](https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats#unc-paths) to this folder:

	# [XML](#tab/tabid-xml)
	
	```XML
	<?xml version="1.0" encoding="utf-8"?>
    <configuration>
	  <!-- ... -->
	  <appSettings>
	    <!-- ... -->
	    <add key="NewVersionServer" value="\\FILESERVER\SolutionNameUpdateSource\" />
      </appSettings>
	</configuration>  
	```
	
	***
	
4. Copy WinForms application folder contents from the end-user workstation to the _SolutionNameUpdateSource_ shared folder.  
The UNC path to the application executable should be "_\\FILESERVER\SolutionNameUpdateSource\MySolition.Win.exe_".
5. Copy the following files from the developer workstation to the _SolutionNameUpdateSource_ shared folder:
    - _%PROGRAMFILES%\DevExpress <:xx.x:>\Components\Tools\eXpressAppFrameworkNetCore\Application Updater\DevExpress.ExpressApp.Updater.exe_
    - _%PROGRAMFILES%\DevExpress <:xx.x:>\Components\Tools\eXpressAppFrameworkNetCore\Application Updater\DevExpress.ExpressApp.Updater.runtimeconfig.json_
    - _%PROGRAMFILES%\DevExpress <:xx.x:>\Components\Tools\eXpressAppFrameworkNetCore\Application Updater\DevExpress.ExpressApp.Updater.dll_

   The UNC path to these files should be "_\\FILESERVER\SolutionNameUpdateSource\\<file name\>_".
6. When you run the WinForms application at an end-user workstation that was not updated, the following Updater progress bar is shown:
	
	![Deployment_Tutorial_0260](~/images/deployment_tutorial_0260116474.png)
	
	If one of the error messages below is displayed instead, ensure the following:
	* the UNC path in the configuration file is correct;
	* the shared folder is readable;
	* the shared folder contains the _DevExpress.ExpressApp.Updater.exe_ file.
	
	![Deployment_Tutorial_0240](~/images/deployment_tutorial_0240116475.png)
	
	The application restarts automatically after an update.

To deploy a new application version, follow the steps below:

1. Replace the files located in the _SolutionNameUpdateSource_ shared folder with new application files.
2. Update the database version as described in the [Update Database](#update-a-database) section.

When a user launches the WinForms application, it is instantly updated. The update process cannot be initiated if the database is not updated, even if the _SolutionNameUpdateSource_ folder contains a new version of the application.

> [!NOTE]
> * The _SolutionNameUpdateSource_ folder should only store new application files. Do not store other files in this folder. Otherwise, they will be copied to each end-user workstation.
> * If you want to change Updater utility behavior, change and recompile its sources. Updater tool sources are in the following folder: _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp.Tools\DevExpress.ExpressApp.Updater_. For example, you can configure the Updater tool to download files from a remote web server instead of using a shared folder in a local network.

## Update Database on Microsoft Azure

For a Blazor application, in the Azure CLI, run the application with the `-updateDatabase -silent` key.

## Update Database in Multi-Tenant Application

### Using –updateDatabase Switch for Blazor and WinForms Apps

The functionality to automatically update the database with the `--updateDatabase` key has a limitation in multi-tenant applications. Only the host database can be updated, as the specific tenant database is identified only after user login. These tools cannot be used to create or update database structure or data in tenant databases.

These tools can be useful for the following actions in a multi-tenant application:

* Initially create the host database (if you need to create a database before the first application launch).
* Update data in the host database (for instance, create new tenants or administrator users for the host database).
 
### How to Use ModuleUpdater to Update Database in Multi-Tenant Applications

Since a multi-tenant application works with multiple databases of different structures, `ModuleUpdater` runs in the application in the following cases:

* When logging into the host interface
* When logging into a tenant interface for the first time

It is essential to consider whether the update applies to a tenant database or the host database.

The XAF [Template Kit](xref:405447) generates projects with DevExpress.ExpressApp.MultiTenancy.ITenantProvider.TenantId and @DevExpress.ExpressApp.MultiTenancy.ITenantProvider.TenantName properties to identify the current tenant. These properties return `null` when the host database is being updated.

The following code sample outlines the recommended structure of the updater class in multi-tenant applications:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.MultiTenancy;
using DevExpress.ExpressApp.Updating;
using Microsoft.Extensions.DependencyInjection;

namespace SolutionName.Module.DatabaseUpdate;
public class Updater :ModuleUpdater {
    public Updater(IObjectSpace objectSpace, Version currentDBVersion) :
          base(objectSpace, currentDBVersion) {
    }
    public override void UpdateDatabaseAfterUpdateSchema() {
        base.UpdateDatabaseAfterUpdateSchema();

        if (TenantName == null) {
            // Update data in the host database
        } else {
            // Update data in tenant databases
            if (TenantName == "company1.com") {
                // Update data in the company1.com tenant database
            }
        }
        // Update data in any database—host or tenant
    }

    // Returns the current tenant identifier or `null` if the application runs in Host User Interface mode
    Guid? TenantId {
        get { return ObjectSpace.ServiceProvider.GetRequiredService<ITenantProvider>().TenantId; }
    }

    // Returns the current tenant name or `null` if the application runs in Host User Interface mode
    string TenantName {
        get { return ObjectSpace.ServiceProvider.GetRequiredService<ITenantProvider>().TenantName; }
    }
}
```

#### Register Predefined Dashboards in a Multi-Tenant Application

In a multi-tenant application, the host database cannot store Dashboards Module data. When you register a predefined dashboard in the Module Updater, call the [DashboardsModule.AddDashboardData\<T>](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.AddDashboardData``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String)) method only if a tenant database is being updated. You can implement `ModuleUpdater` as described in the previous section.

Refer to the following help topic for more information about predefined Dashboards: <xref:117453>.

#### Register Predefined Reports in a Multi-Tenant Application

In a multi-tenant application, the host database cannot store Reports Module data. When you register a predefined report in the Module Updater, run the Reports Module Updater only if a tenant database is being updated. You can implement `ModuleUpdater` as follows:

```csharp
public override IEnumerable<ModuleUpdater> GetModuleUpdaters(IObjectSpace objectSpace, Version versionFromDB) {
 
    // Adds Module Updaters required to update tenant and host databases
    ModuleUpdater updater = new DatabaseUpdate.Updater(objectSpace, versionFromDB);
    var updaters = new List<ModuleUpdater>() { updater };
 
    // Returns the current tenant identifier or `null` if the application runs in Host User Interface mode
    Guid? tenantId = objectSpace.ServiceProvider.GetRequiredService<ITenantProvider>().TenantId;
 
    // Adds Updaters that are required for tenant databases only
    if (tenantId != null) {
        PredefinedReportsUpdater predefinedReportsUpdater =
            new PredefinedReportsUpdater(Application, objectSpace, versionFromDB);
        predefinedReportsUpdater.AddPredefinedReport<XtraReport1>("Report Name", typeof(ApplicationUser));
        updaters.Add(predefinedReportsUpdater);
    }
    return updaters;
}
```

Refer to the following help topic for more information about predefined Reports: <xref:113645>.

## Update Database in Middle Tier Security Application

1. Launch a command line interpreter, for instance, **Command Prompt**. 
1. Run the application with the `-updateDatabase` command.
    You can use the following additional parameters:
    * `-silent` initiates a silent update without direct user interaction.
    * `-forceUpdate` forces a schema update on each run.
1. Follow the on-screen instructions.

    ```Console
    C:\Users\Public\MyApplication\SolutionName.MiddleTier.exe -updateDatabase -silent -forceUpdate
    ```

1. Run the application to ensure the update was successful.

## Important Notes

* If you encounter issues with your application update, refer to the following help topic: [Deployment Troubleshooting Guide](xref:113238).

* To prevent a module from updating the database, specify a fixed version of this module's assembly (for example, _1.0.0.0_). Version synchronization of your WinForms and ASP.NET Core Blazor modules may be forced. The default build and revision numbers are specified with the asterisk (*), and Visual Studio automatically increments these numbers (see [AssemblyVersionAttribute](xref:System.Reflection.AssemblyVersionAttribute)). This leads to a database version mismatch on each module update.

## How Database is Updated in Debug Mode

The DevExpress [Template Kit](xref:405447) configures new XAF applications so that a database is created when running the application for the first time, and updated when the application's version grows. At startup, XAF checks if the database version is older than the application's version. 

The kit adds the @DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch event handler in new Blazor, Web API, and WinForms projects to keep the application and database versions synchronized. 

# [SolutionName.Blazor.Server\BlazorApplication.cs](#tab/tabid-Blazor)
```csharp
public class SolutionNameBlazorApplication : BlazorApplication {
    public SolutionNameBlazorApplication() {
       DatabaseVersionMismatch += SolutionNameBlazorApplication_DatabaseVersionMismatch;
       // ...
    }
    void SolutionNameBlazorApplication_DatabaseVersionMismatch(object sender, DatabaseVersionMismatchEventArgs e) {
       e.Updater.Update();
       e.Handled = true;
       // ...
    }
}
```
# [SolutionName.WebApi\Startup.cs](#tab/tabid-WebAPI)
```csharp
public class Startup {
   public void ConfigureServices(IServiceCollection services) {
      services.AddXafWebApi(builder => {
            builder.AddBuildStep(application => {
               // ...
               if(System.Diagnostics.Debugger.IsAttached && application.CheckCompatibilityType == CheckCompatibilityType.DatabaseSchema) {
                  application.DatabaseUpdateMode = DatabaseUpdateMode.UpdateDatabaseAlways;
                  application.DatabaseVersionMismatch += (s, e) => {
                        e.Updater.Update();
                        e.Handled = true;
                  };
               }
            });
         // ...
      }
    )}
} 

```
# [SolutionName.Win\WinApplication.cs](#tab/tabid-WinForms)

```csharp
public class SolutionNameWindowsFormsApplication : WinApplication {
   public SolutionNameWindowsFormsApplication() {
      DatabaseVersionMismatch += SolutionNameWindowsFormsApplication_DatabaseVersionMismatch;
      // ...
   }
   void SolutionNameWindowsFormsApplication_DatabaseVersionMismatch(object sender, DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs e) {
      e.Updater.Update();
      e.Handled = true;
      // ...
   }
}
```
***

If the application includes the [Middle Tier Server](xref:113439) application, the compatibility check must be performed server side. In this case, the kit adds the @DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch event handler in the Middle Tier Security application. Client applications (Blazor, Web API, and WinForms) throw an exception when the `DatabaseVersionMismatch` event occurs.

# [MiddleTier](#tab/tabid-middletier)

```csharp
// File: SolutionName.MiddleTier\Startup.cs
builder.AddBuildStep(application => {
   application.CheckCompatibilityType = DevExpress.ExpressApp.CheckCompatibilityType.DatabaseSchema;
   if (application.CheckCompatibilityType == CheckCompatibilityType.DatabaseSchema) {
      application.DatabaseUpdateMode = DatabaseUpdateMode.UpdateDatabaseAlways;
      application.DatabaseVersionMismatch += (s, e) => {
            e.Updater.Update();
            e.Handled = true;
      };
   }
   //...
})
```
***

You can use the @DevExpress.ExpressApp.XafApplication.CustomCheckCompatibility event to implement your own custom check of the application and database compatibility, update the database, or perform other actions.

### Database Update Settings

@DevExpress.ExpressApp.XafApplication.CheckCompatibilityType
:   Specifies whether XAF ensures that the database schema matches the business model or that the database version matches the application version.
@DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode
:   Specifies when the application database should be updated: at every application run, when its version is older than the application version, or never (manually).
@DevExpress.ExpressApp.IObjectSpaceProvider.SchemaUpdateMode
:   Allows you to disable database updates for a particular Object Space.

