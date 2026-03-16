---
uid: "112575"
title: Log Files
owner: Eugenia Simonova
seealso:
  - linkId: "112818"
  - linkId: "112576"
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/logging/
    altText: 'Logging in .NET Core and ASP.NET Core'
---
# Log Files

XAF writes information about runtime errors and exceptions to log files. Log files also record all system and user operations during application runtime. XAF uses two types of log files -- runtime and design-time.

If a problem occurs, you can use log files to find the cause. You can also send the log file to our [Support Center](https://supportcenter.devexpress.com) to get assistance from DevExpress support engineers.

For a number of log files, you can control the level of detail, change the file location, or add custom information.

The XAF trace mechanism relies on standard .NET logging APIs from @System.Diagnostics and related namespaces. The `DevExpress.Persistent.Base.Tracing` class is a wrapper around the standard [trace listeners](https://learn.microsoft.com/en-us/dotnet/framework/debug-trace-profile/trace-listeners). The `DevExpress.Persistent.Base.Tracing` class uses the @System.Diagnostics.TextWriterTraceListener class to write all application events to a log file. Refer to the following topic for more information on how to customize the default trace mechanism: [](xref:112576).

> [!TIP]
> Use the `DevExpress.Persistent.Base.Tracing.LogSensitiveData` property to control sensitive data logging. For more information, refer to the following breaking change ticket: [Core - Sensitive data is removed from log files](https://supportcenter.devexpress.com/ticket/details/t1182871/core-sensitive-data-is-removed-from-log-files).

## Default Log File Names and Locations 

### Log Files Generated at Runtime

The default log file name is _eXpressAppFramework.log_. The table below contains the default location for log files generated at runtime.

| Platform | The Default Log File Location |
|---|---|
| WinForms | A folder with the executable file. |
| ASP.NET Core Blazor | A folder with the executable file. |

### Log Files Generated for Designers

The XAF application creates log files for the [Model Editor](xref:112830).

#### Model Editor (All Platforms)

* \<_SolutionName_>.Module\\Model.DesignedDiffs.log 
* \<_SolutionName_>.Win\\Model.log
* \<_SolutionName_>.Blazor.Server\\Model.log

#### Model Editor

All files in the _%USERPROFILE%\AppData\Roaming\eXpressAppFramework\_ folder.

### Log File Generated in Azure

XAF applications deployed to the Azure App Service generate a log file with the _eXpressAppFramework.log_ name. Follow the steps below to find this file:

1. Open the [Azure portal](https://portal.azure.com/). On the **App Services** page, select your application service and click **Development Tools** | **App Service Editor (Preview)**:

    ![Azure Portal Development Tools](~/images/logs_azure_development_tools.png)

2. Click **Go -->** and navigate to the **WWWROOT** section:

    ![Azure Portal App Service Editor](~/images/logs_azure_app_service_editor.png)

## Change the Log File Location and Name

### Use the TraceLogLocation Attribute to Change the Location in WinForms

WinForms and application configuration files use the `TraceLogLocation` attribute to specify the log file location.

**File:** _MySolution.Win\App.config_

# [XML](#tab/tabid-xml)

```XML{4}
<configuration>
    <appSettings>
        <!-- ... -->
        <add key="TraceLogLocation" value="ApplicationFolder"/>
        <!-- ... -->
    </appSettings>
</configuration>
```
***

The `TraceLogLocation` values are as follows:

| Value | Description |
|---|---|
| `ApplicationFolder` | XAF stores the log file in the application folder. Windows Forms applications save the log file to the folder with the executable file. Ensure that the system account used to run the application has write permission to this folder. |
| `CurrentUserApplicationDataFolder` | XAF saves the log file to the current user _ApplicationData_ folder. You can use this option only in Windows Forms applications.|
| `None` | Logging is disabled. Use this value in the production environment since XAF does not support log rotation.|

### Use the LogName Property to Change the Name and Location (.NET)

You can change the default log file name in code before XAF Application object creation. Set the `Tracing.LogName` property to a new file name. The _.log_ extension is added automatically.

#### WinForms

**File**: _MySolution.Win\Program.cs_
# [C#](#tab/tabid-csharp)

```csharp{4}
static class Program {
    // ...
    static void Main() {
        Tracing.LogName = "CustomLogFile";
        // ...
        MySolutionWindowsFormsApplication winApplication = 
            new MySolutionWindowsFormsApplication();
        //...
```
***

#### ASP.NET Core Blazor and Web API

**File**: _MySolution.Blazor.Server\Program.cs_, _MySolution.WebApi\Program.cs_

# [C#](#tab/tabid-cs)
```csharp{5}
namespace MySolution.Blazor.Server {
    public class Program : IDesignTimeApplicationFactory {
        // ...
        public static int Main(string[] args) {
            Tracing.LogName = "CustomLogFile";
            // ...
            IHost host = CreateHostBuilder(args).Build();
            //...
        }
    }
}
```
***

You can also change the file location in the `Tracing.LogName` property. This property accepts the following values:

* A relative path to the log file. For example, _Logs\CustomLogFile_.
* An absolute path to the log file. For example, _C:\\Logs\\CustomLogFile_.

If the specified location is not accessible, XAF does not create the log file.

> [!NOTE]
> If XAF tries to write to a log file that is in use, a new log file is created and its name has the GUID prefix. Set a custom log file name for each application to avoid prefixes.

## Change the Log File Detail Level

You can control how detailed log file information is. Use numbers to specify five different detail levels in WinForms projects. Utilize the [LogLevel](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.loglevel) enumeration to set the log detail level in ASP.NET Core Blazor and Web API applications.

| Level |Blazor and Web API Level| Description |
|---|---|---|
| 0 |`LogLevel.None`| Logging is disabled. |
| 1 |`LogLevel.Critical`, `LogLevel.Error`| The log file records only errors. |
| 2 |`LogLevel.Warning`| The log file records errors and warning messages. |
| 3 |`LogLevel.Information`| In addition to the levels mentioned above, the log file records system and user operations. |
| 4 |`LogLevel.Debug`, `LogLevel.Trace`| Use this level to create the most detailed log files. All Security System loggers (Permission Processors, Middle Tier loggers, security rule loggers) are enabled in this mode. |

> [!NOTE]
> We recommend log file detail levels 3 and 4 for debugging purposes only because logging reduces performance.

### WinForms

Edit `<appSettings>` tag content in the _App.config_ file.

**File:** _MySolution.Win\App.config_

# [XML](#tab/tabid-xml)

```XML{5}
<configuration>
<!-- ... -->
    <appSettings>
    <!-- ... -->
        <add key="eXpressAppFrameworkTraceLevel" value="4"/>
    </appSettings>
</configuration>
```

***

### ASP.NET Core Blazor and Web API

You can specify different log detail levels for different namespaces in the _appsettings.json_ file. The following code sets the `Debug` log detail level for the `DevExpress.ExpressApp` namespace:

**File:** _MySolution.Blazor.Server\appsettings.json (appsettings.Development.json), MySolution.WebApi\appsettings.json (appsettings.Development.json)_

# [JSON](#tab/tabid-json)
```JSON{7}
// ...
"Logging": {
  "LogLevel": {
    "Default": "Information",
    "Microsoft": "Warning",
    "Microsoft.Hosting.Lifetime": "Information",
    "DevExpress.ExpressApp": "Debug"
  }
},
// ...  
```

***

## Add Custom Information to Log Files

You can write diagnostic information to a log file. Use static methods from the `DevExpress.Persistent.Base.Tracing` class for this purpose. See the following topic for details: [Add Custom Log Entries and Customize the Default Tracer Behavior](xref:112576).

## Log XPO SQL Queries

For more information on how to log SQL queries in applications that use XPO, refer to the following topic: [](xref:403928).

## Disable Logging

### Use the TraceLogLocation Attribute in WinForms

Set the `TraceLogLocation` attribute to `None` to disable logging.

**File:** _MySolution.Win\App.config_
# [XML](#tab/tabid-xml)

```XML{4}
<configuration>
    <appSettings>
        <!-- ... -->
        <add key="TraceLogLocation" value="None"/>
        <!-- ... -->
    </appSettings>
</configuration>
```
***

### Use the \<appSettings> Tag in WinForms Applications

Set the [log file detail level](#change-the-log-file-detail-level) to `0` to disable logging. Use the following content within the `<appSettings>` tag:

**File:** _MySolution.Win\App.config_

# [XML](#tab/tabid-xml)

```XML{5}
<configuration>
<!-- ... -->
    <appSettings>
    <!-- ... -->
        <add key="eXpressAppFrameworkTraceLevel" value="0"/>
    </appSettings>
</configuration>
```
***

### ASP.NET Core Blazor and Web API

 Set the log level to `None` in the _appsettings.json_ file for the `DevExpress.ExpressApp` namespace to disable logging:

**File:** _MySolution.Blazor.Server\appsettings.json (appsettings.Development.json), MySolution.WebApi\appsettings.json (appsettings.Development.json)_

# [JSON](#tab/tabid-json)
```JSON{6}
// ...
"Logging": {
    "Default": "Information",
    "Microsoft": "Warning",
    "Microsoft.Hosting.Lifetime": "Information",
    "DevExpress.ExpressApp": "None"
},
// ...  
```
***
