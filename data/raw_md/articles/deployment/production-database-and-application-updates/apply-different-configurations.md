---
uid: "112693"
seealso: []
title: Apply Different Configurations for Development and Production
---
# Apply Different Configurations for Development and Production

XAF generates configuration files for ASP.NET Core Blazor/Web API Service (_appsettings.json_) and WinForms (_App.config_) applications. These files contain information that an application reads at runtime such as database connection strings, modules list, paths to important folders, and so on. In Windows Forms applications, some configuration parameters can be different for different application solution modes (Debug or Release). For example, the `UserModelDiffsLocation` and `TraceLogLocation` parameters must be set to the `ApplicationDataFolder` value if you use the the **ClickOnce** technique to manage the application life cycle, but you have to modify configuration files each time an application is built in another mode. You can also create configuration files for each possible application solution mode, and copy it to the application project when needed. However, both these approaches are inconvenient. This topic shows two different approaches and which configuration files to use for each scenario.

## Specify a Configuration File via the Project Properties Window
Via  this approach, you can create various configurations and use them as needed. For instance, a Windows Forms application can have the following configuration files:

* **App.Debug.config** 
	
	Used when debugging the application.
* **App.Release.config**
	
	Used to build a release version.
* **App.ClickOnceLocal.config**
	
	Used when testing the application installation.
* **App.ClickOnce.config**
	
	Used for application deployment.

> [!NOTE]
> All configuration files must be called in the following manner: App.\<_ConfigurationName_>.config.

Place all of these configuration files in the same folder. To specify which file must be used, do the following:

* In the **Solution Explorer**, right-click the Application project name and click **Properties**.
* Select the **BuildEvents** tab in the Project Properties window.
* In the **Pre-build events command line** box, insert the following:
	xcopy "$(ProjectDir)App.$(ConfigurationName).config" "$(ProjectDir)App.config" /Y /R
* Save the project.

## Use Conditional Compilation
Via this approach, you can define two application configurations: Debug and Release. Use the **DEBUG** constant within the **#If...Then...#Else** directive to override configuration parameters when debugging an application. The following code demonstrates how to get the connection string specified by the ConnectionStringForDebug setting, when debugging the application:

# [C#](#tab/tabid-csharp)

```csharp
string connectionString = 
   ConfigurationManager.ConnectionStrings["ConnectionStringForDevelopment"].ConnectionString;
#if DEBUG
   string connectionString = 
      ConfigurationManager.ConnectionStrings["ConnectionStringForDebug"].ConnectionString;
#endif
```

***

In the code above, the connection string is specified by the ConnectionStringForDevelopment setting of the configuration file when the application is compiled in **Release** mode, and by the ConnectionStringForDebug setting when the application is compiled in **Debug** mode. To specify **Release** or **Debug** mode, use the **Define DEBUG constant** checkbox in the **Build** tab of the application project's **Project Properties** window. If this checkbox is selected, the application is compiled in **Debug** mode.

# [](#platform/netframework46)

> [!NOTE]
> The [DBUpdater](xref:113239#how-database-is-updated-in-debug-mode) updates the database if the connection string is specified by the `ConnectionString` setting in the configuration file. If you use another name for this setting, the `DBUpdater` does not work.

***