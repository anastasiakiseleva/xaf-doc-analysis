---
uid: "113238"
seealso:
- linkId: "112691"
- linkId: "402148"
title: Deployment Troubleshooting Guide
owner: Ekaterina Kiseleva
---
# Deployment Troubleshooting Guide

This topic lists common deployment issues and ways to resolve them when the application runs as intended on the Developer Workstation.

## ASP.NET Core Blazor-Specific Issues

### The “An attempt to load the "DevExpress.Drawing.v<:xx.x:>.Skia.dll" assembly failed.” error occurs on Linux and MacOS platforms.

Issue Description:

An application displays the following error message on Linux or MacOS:

_An attempt to load the "DevExpress.Drawing.v<:xx.x:>.Skia.dll" assembly failed._

Solution:

The `DevExpress.Drawing.Skia` assembly is a part of the [DevExpress.Drawing.Skia](https://nuget.devexpress.com/packages/DevExpress.Drawing.Skia) NuGet package. In .NET 8+, the `DevExpress.Drawing` library uses the [SkiaSharp](https://www.nuget.org/packages/SkiaSharp/) drawing engine for Office API and Reports modules. To resolve this error, install the `DevExpress.Drawing.Skia` NuGet package to your **MySolutionName.Blazor.Server** project.

Refer to the following topic for details: [](xref:404247).

***

### The “System.PlatformNotSupportedException: System.Drawing.Common is not supported on this platform.” error occurs on Linux and MacOS platforms.

Issue Description:

An application displays the following error message on Linux or MacOS:

_System.PlatformNotSupportedException: System.Drawing.Common is not supported on this platform._

Solution:

Make sure that your project does not reference the `System.Drawing.Common` library v.7+. You also need to upgrade to the latest DevExpress component version that does not contain direct `System.Drawing` API calls.

***

### Problems with documents rendering or exporting when using Reports module, Office module, or Dashboards module on Linux and MacOS platforms.

Issue Description:

An application with the [Reports](xref:113591), [Office](xref:400003), or [Dashboards](xref:117449) module renders or exports documents incorrectly when deployed on Linux or MacOS. 

Solution:

Ensure that all required libraries and packages are installed. Refer to the following topics for more information: 

[!include[deployment-non-windows-additional-setup-links](~/templates/deployment-non-windows-additional-setup-links.md)]

***

### The “Could not find 'xaf.focusViewItem' ('xaf' was undefined).” error occurs.

Issue Description:

An application displays the following error message:

_Could not find 'xaf.focusViewItem' ('xaf' was undefined)._

Solution:

This error can occur if the application is being run with an incorrect working directory or from outside of its location. For example: 

` dotnet C:\Some\Path\MySolutionName.NET.EFCore\CS\MySolutionName.Blazor.Server\bin\Debug\net7.0\MySolutionName.Blazor.Server.dll ` 

To resolve the issue, make sure that you run the application from its working directory:

`dotnet MySolutionName.Blazor.Server.dll` 

For more information, refer to the following Microsoft topic: [ASP.NET Core Blazor static files](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/static-files).

***

### A deployed application loses styles or displays other scripting errors in production.

Problem Description:

An application loses styles applied to its elements or displays style-related scripting errors. 

Solution:

This happens when a Blazor application cannot load scripts and styles from the _content/DevExpress.Blazor_ folder. This folder stores [static web assets](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/static-files) (see also the `UseStaticFiles` call in _Startup.cs_). This problem usually occurs in Linux-based or Docker-based deployments due to DevExpress assemblies that are incorrectly integrated into a project. You need to use NuGet package references instead of assembly references because our NuGet packages contain all the required static web assets in their _staticwebassets_ folder (e.g., _C:\Program Files\DevExpress <:xx.x:>\Components\Offline Packages\devexpress.blazor\\<:xx.x.x:>\staticwebassets_).

***

### The "The application cannot connect to the specified database, because the database doesn't exist, its version is older than that of the application, or its schema does not match the ORM data model structure." error occurs.

Issue Description:

An application displays one of the following error messages:

* _The application cannot connect to the specified database, because the database doesn't exist, its version is older than that of the application, or its schema does not match the ORM data model structure._

* _Login failed for `UserName`. User name or password is incorrect._

Solution:

Initialize the database and populate it with initial data.

#### Applications Deployed to Azure

For applications deployed to Azure, follow the steps below:

1. Open the [Azure Portal](https://portal.azure.com).
1. Click **App Services**.

    ![|DevExpress XAF - Azure Portal](~/images/deployment-tutorial-azure-portal-app-services.png)

1. Click your App Service name.

1. Click **Advanced Tools** and follow the **Go** link.

    ![|DevExpress XAF - Azure Portal Settings](~/images/deployment-tutorial-azure-azure-portal-advanced-tools.png)

1. Switch to the **Bash** tab and launch the application in the database update mode.

    ```Console
    dotnet ~/site/wwwroot/MainDemo.Blazor.Server.dll --updateDatabase --force --silent
    ```

#### Other Applications

In common cases, to initialize a database, run the application in database update mode:

` dotnet MySolutionName.Blazor.Server.dll --updateDatabase --forceUpdate –silent`

Make sure that this mode is available in the configuration in which the application was built (`Debug` or `Release`). If you changed the schema of the existing database, use [EF Core migrations](xref:405418#ef-core-migrations).


***

### The "Could not copy `PackagePath` to `AnotherPackagePath`. Exceeded retry count of 10. Failed." error occurs.

Problem Description:

An application displays the following error message:

_Could not copy `PackagePath` to `AnotherPackagePath`. Exceeded retry count of 10. Failed._

Solution:

This problem usually occurs because the file path is too long. To solve this, move the folder containing your application closer to the root of your drive.

***

## Windows Forms Specific Problems

### The "application failed to initialize properly" error message is displayed

Issue Description:

Windows displays an **Application Error** window with the following text.

_The application failed to initialize properly (0xc0000135). Click OK to terminate the application._

Solution:

This may happen if you try to launch an XAF Windows Forms application at the workstation with Windows XP or an older Windows version installed. These systems do not have .NET installed by default. Download and install the correct version of .NET from the [Microsoft Download Center](https://www.microsoft.com/en-us/download/details.aspx?id=17851).

***

### The "could not load file or assembly" error message is displayed

Issue Description:

When loading, the application displays the following error message:

![Deployment_Tutorial_0040](~/images/deployment_tutorial_0040116459.png)

_Could not load file or assembly 'DevExpress.XtraTreeList.v9.2, Version=9.2.8.0, Culture=neutral, PublicKeyToken=b88d1754d700e49a' or one of its dependencies. The system cannot find the file specified._

Assembly name, version, etc., may be different.

The assembly mentioned in the error message is missing from the application folder. Copy it from the Developer Workstation. It is usually located in the _[!include[PathToXafDlls](~/templates/path-to-xaf-dlls.md)]_ folder.

**See also:** [Xcopy Deployment of a Windows Forms Application](xref:113232) | [How the Runtime Locates Assemblies](https://learn.microsoft.com/en-us/dotnet/framework/deployment/how-the-runtime-locates-assemblies) | [Fuslogvw.exe (Assembly Binding Log Viewer)](https://learn.microsoft.com/en-us/dotnet/framework/tools/fuslogvw-exe-assembly-binding-log-viewer)

***

### An error message containing insufficient information is displayed

Issue Description:

When loading, the application displays an error message that appears as follows:

![Deployment_Tutorial_0050](~/images/deployment_tutorial_0050116460.png)

_Exception occurs while loading schema from DevExpress.ExpressApp.Win.SystemModule.SystemWindowsFormsModule
The type initializer for 'DevExpress.ExpressApp.Win.SystemModule.DefaultSkinListGenerator' threw an exception._

The details of the message may be different. Generally, the message does not contain enough information on how to resolve the error.

Solution:

To find the cause of the error, open the application log file. The log file is a text file located in the application folder or in the user's application data folder, and has the most recent modification time. Find the text matching the error message and analyze what happened before the error occurred. For instance, this error can be caused by a missing assembly. For details, see the next item.

**See also:** [Xcopy Deployment of a Windows Forms Application](xref:113232) | [Log Files](xref:112575)

***

### Resolve the 'DevExpress.Assembly.Name.vXX.X' assembly Exception thrown: 'System.IO.FileNotFoundException'

Issue Description:

The following text is written to the application log before a warning occurs:

![Deployment_Tutorial_0060](~/images/deployment_tutorial_0060116461.png)

_10.03.22 12:35:36.750 Resolve the 'DevExpress.Assembly.Name.vXX.X' assembly
Exception thrown: 'System.IO.FileNotFoundException' in mscorlib.dll_

An assembly name and version may be different.

Solution:

Outdated records in the XPObjectType table cause these warnings. Use one of the following options to avoid them:

* Ignore these diagnostic messages since they are non-critical.

* Change the assembly name in the AssemblyName column of the [XPObjectType](xref:2632#inheritance-mapping-and-object-polymorphism) table in the database to point to the latest application version. For example, change the assembly name from _DevExpress.Persistent.BaseImpl.v10.1_ to _DevExpress.Persistent.BaseImpl.Xpo.v21.2_.

* Override the @DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseBeforeUpdateSchema method and call UpdateXPObjectType for all required classes. See the following topic for details: [How to: Handle Renamings and Deletions of Business Classes and their Properties](xref:113254), [XPO - Old business class assemblies may be loaded from the application folder or GAC, and may cause side effects in .NET Framework apps (due to outdated XPObjectType records)](https://supportcenter.devexpress.com/ticket/details/t451078/xpo-old-business-class-assemblies-may-be-loaded-from-the-application-folder-or-gac-and).

**See also:** [Xcopy Deployment of a Windows Forms Application](xref:113232) | [Log Files](xref:112575)

***

### Logged errors are not available, although the application fails to start

Issue Description:

The application log file does not contain errors or you cannot find the log file, although the application fails to start; and it is not possible to determine exactly what happens from the displayed error message.

Solution:

Check that logging is enabled in the application configuration file. This is the _\<Application_Name>.Win.exe.config_ XML file located in the application folder. Open this file in a text editor and check that the **TraceLogLocation** key in the **appSettings** section is not set to **None**.

Check that the user account that you use to start the application has the appropriate permissions to write to the log file. For instance, Windows Vista does not allow non-administrative users to write anything to _Program Files_ subfolders. To resolve this issue, you can do one of the following:

* Grant write permissions to a user.
* Run the application as an administrator.
* Open the configuration file and set the **TraceLogLocation** key in the **appSettings** section to **CurrentUserApplicationDataFolder** (each user has permission to write to their application data folder).
	
	# [XML](#tab/tabid-xml)
	
	```XML
	<appSettings>
	    <!-- ... -->
	    <add key="TraceLogLocation" value="CurrentUserApplicationDataFolder"/>
	    <!-- ... -->
	</appSettings>
	```
	
	***

> [!NOTE]
> The default location of the application data folder varies in different Windows versions.

**See also:** [Log Files](xref:112575) | [Application Configuration Files](https://learn.microsoft.com/en-us/windows/desktop/SbsCs/application-configuration-files)

***

### Cannot store individual customizations in a multi-user environment

Issue Description:

A Windows Forms application is installed on a Terminal Server and multiple users use it simultaneously, or it is installed on an End-User Workstation with multiple local logins enabled. User customizations interfere with each other, making individual customizations impossible.

Solution:

Open the configuration file and set the **UserModelDiffsLocation** key in the **appSettings** section to **CurrentUserApplicationDataFolder**.

# [XML](#tab/tabid-xml)

```XML
<appSettings>
    <!-- ... -->
    <add key="UserModelDiffsLocation" value="CurrentUserApplicationDataFolder"/>
    <!-- ... -->
</appSettings>
```

***

This allows each user to store individual customizations.

Another solution is provided in the [How to: Store the Application Model Differences in the Database](xref:113698) topic.

**See also:** [Application Configuration Files](https://learn.microsoft.com/en-us/windows/desktop/SbsCs/application-configuration-files)

***

### "Unable to save customization information" error is displayed on exit

Issue Description:

A Windows Forms application launches and runs normally, however the following error message is displayed on exit.

![DTG_01](~/images/dtg_01116651.png)

_Unable to save customization information_.

Solution:

Check that the user account used to start the application has appropriate permissions to write to the _Model.User.xafml_ file. This file location is specified by the **UserModelDiffsLocation** key in the application configuration file. By default, the _Model.User.xafml_ file is located in the application folder. Typically, non-administrative users have no permission to write anything to _Program Files_ subfolders. To resolve this issue, you can do one of the following:

* grant write permissions to a user;
* open the configuration file and set the **UserModelDiffsLocation** key in the **appSettings** section to **CurrentUserApplicationDataFolder** (each user has permission to write to their application data folder).

**See also:** [Application Configuration Files](https://learn.microsoft.com/en-us/windows/desktop/SbsCs/application-configuration-files)

***

### The LogonParameters file is inaccessible

Issue Description:

The following error is displayed after clicking the **Log On** button.

_Access to the path 'C:\Program Files\MySolution\LogonParameters' is denied._

Solution:

Check that the user account used to start the application has appropriate permissions to write to the _LogonParameters_ file. This file is used to save the logon parameters (user name by default), and is located together with the _Model.User.xafml_ file. The location is specified by the **UserModelDiffsLocation** key in the application configuration file. By default, the _LogonParameters_ file is located in the application folder. Typically, non-administrative users do not have permission to write anything to _Program Files_ subfolders. To resolve this issue, you can do one of the following:

* Grant write permission to a user.
* Open the configuration file and set the **UserModelDiffsLocation** key in the **appSettings** section to **CurrentUserApplicationDataFolder** (each user has permission to write to their application data folder).

**See also:** [Application Configuration Files](https://learn.microsoft.com/en-us/windows/desktop/SbsCs/application-configuration-files)

***

### The application cannot find the Updater executable

Issue Description:

When loading, the application displays the following error message.

![DTG_03](~/images/dtg_03116653.png)

_Could not find file '\\FILESERVER\MySolutionUpdateSource

\DevExpress.ExpressApp.Updater.exe'._

Solution:

The database was updated and an automatic update was initiated. The **NewVersionServer** value in the application configuration file is not empty. However, the Updater utility was not found. Check that the _DevExpress.ExpressApp.Updater.exe_ file exists in the update source folder. You can get this file from the Developer Workstation (this file path is _[!include[PathToXafTools](~/templates/path-to-xaf-tools.md)]\DBUpdater\DBUpdater.v<:xx.x:>.exe_). Check that the **NewVersionServer** value is correct.

**See also:**[Application Update](xref:113239) | [Application Configuration Files](https://learn.microsoft.com/en-us/windows/desktop/SbsCs/application-configuration-files)

***

### The '1113' error occurs

Issue Description:

When loading, the application displays the following error message.

![DTG_02](~/images/dtg_02116652.png)

_An error with number 1113 has occurred.
Error message: Cannot run the application. The database version is newer than the application version, but the server with the new application version is not found. Ask the administrator to check that the configuration file contains a correct path to the new application version._

Solution:

The database was updated and an automatic update was initiated. The **NewVersionServer** value in the application configuration file is not empty. However, the update source folder cannot be accessed. Ensure that the **NewVersionServer** key value is correct and that the shared folder referenced by it is accessible.

**See also:** [Application Update](xref:113239) | [Application Configuration Files](https://learn.microsoft.com/en-us/windows/desktop/SbsCs/application-configuration-files)

***

### "Cannot create temporary file" error message is displayed

Issue Description:

When loading, the application displays the following error message.

![DTG_08](~/images/dtg_08116943.png)

_Cannot compile generated code. Please inspect generated code using this exception's SourceCode property. 
The following errors occurred: (0,0): Cannot create temporary file 'c:\Program Files\MySolution\CSC27CD.tmp' -- Access is denied._

Solution:

Starting with version v2011 vol 1, XAF can dynamically create assemblies at run time to cache the structure of Application Model used in the application (see [XAF – Core & Performance Improvements](https://community.devexpress.com/blogs/xaf/archive/2011/04/28/xaf-core-amp-performance-improvements-coming-in-v2011-vol1.aspx)). This can be done, for instance, to store the [Application Model Structure](xref:112580). By default, your application will try to create temporary files in the folder it is installed. If the application is not allowed to write to this folder, you will see an error message. To solve the issue, you can specify exact cache file names that the application will be allowed to create and modify. This is done by overriding [](xref:DevExpress.ExpressApp.XafApplication)'s protected **GetDcAssemblyFilePath**, **GetModelAssemblyFilePath** and **GetModulesVersionInfoFilePath** methods. Alternatively, you can override these methods to return `null` to specify that caching should be disabled.

_WinApplication.cs_

# [C#](#tab/tabid-csharp)

```csharp
public partial class MySolutionWindowsFormsApplication : WinApplication {
    //...
    protected override string GetDcAssemblyFilePath() {
        return null;
    }
    protected override string GetModelAssemblyFilePath() {
        return null;
    }
    protected override string GetModulesVersionInfoFilePath() {
        return null;
    }
}
```
***

**See also:** [Application Model Structure](xref:112580)

***

### User customizations are lost after updating the ClickOnce deployment

Issue Description:

A Windows Forms application is deployed using [Publish Wizard Deployment of a Windows Forms Application](xref:113234). User customizations are lost each time the application is updated.

Solution:

The solution is the same as for the [Cannot store individual customizations in a multi-user environment](#cannot-store-individual-customizations-in-a-multi-user-environment) issue.

***

## Platform-Independent Problems

### Numerous assemblies are missing

Issue Description:

After deploying an application with Xcopy, you find numerous assemblies missing from the Windows Forms application folder.

Solution:

Open the application solution at the Developer Workstation and check that you have correctly followed all the pre-deployment steps from the [Xcopy Deployment of a Windows Forms Application](xref:113232) lesson.

> [!NOTE]
> Use the [Assembly Deployment Tool](xref:17237) to analyze your project and obtain the list of assemblies you should deploy. Compare the assemblies the tool identifies to the redistributable assemblies list available in the [End User License Agreement](xref:2218) (EULA).


***

### "The application cannot connect to the specified database" error is displayed

Issue Description:

The following error message is displayed when you run the application.

![Deployment_Tutorial_1080](~/images/deployment_tutorial_1080116466.png) ![Deployment_Tutorial_0065](~/images/deployment_tutorial_0065116462.png)

_The application cannot connect to the specified database, because the latter does not exist or its version is older than that of the application.
The automatic update is disabled, because the application was started without debugging.
You should start the application under Visual Studio, or modify the source code of the 'DatabaseVersionMismatch' event handler to enable an automatic database update, or manually create a database using the 'DBUpdater' tool._

Solution:

To find out what is wrong with the application database, use the **DBUpdater** tool. If the **DBUpdater** reports an error, check if it is described later in this topic.

**See also:** [Set Up the Database Connection](xref:113236)

***

### The '1111' error occurs when running the application or DBUpdater (or the application’s -updateDatabase CLI command)

Issue Description:

The following error message is displayed when running the application, or **DBUpdater** tool, or `-updateDatabase` CLI command.

![DTG_04](~/images/dtg_04116654.png)

_An error with number 1111 has occurred.
Error message: The database version is greater than the application version. The application needs to be updated. Please contact your system administrator or download a new version.
Additional information: the local version 1.0.3603.18312 of module 'MySolutionModule' is smaller than version 1.0.3603.21783 in the database._

Solution:

One possible reason for a version mismatch is that you restored the database from the Developer Workstation backup and did not update the application. Another possible reason is that you updated the database from another End-User Workstation running a more recent application version. In both cases, you need to update your application.

**See also:** [Application Update](xref:113239)

***

### The application cannot connect to the database, although the DBUpdater (or the application's -updateDatabase CLI command) reports no error

Issue Description:

The following error message is displayed when you run the application.

![DTG_05](~/images/dtg_05116655.png)

_An error has occurred connecting to database. Please contact your system administrator._

At the same time, the **DBUpdater** tool (or the application's -updateDatabase CLI command) reports no error.

Solution:

A possible reason is that the application does not have sufficient permissions to access the application database. Confirm that the account used to connect to the Database Server is provided with proper permissions or ask the database administrator to do it. Another solution is to switch to an account having proper permissions.

**See also:** [Set Up the Database Connection](xref:113236)

***

### The DBUpdater reports that the database does not exist

Issue Description:

The **DBUpdater** reports:

![Deployment_Tutorial_0070](~/images/deployment_tutorial_0070116468.png)

_The database does not exist. It will be created now._

_..._

_Database update completed successfully._

Solution:

This behavior is normal when creating an initial database. The database mentioned in the connection string was absent and the **DBUpdater** created it. Restore the database from a backup if you need specific data in the created database or check the connection string - you may be connecting to a different database.

**See also:** [Set Up the Database Connection](xref:113236)

***

### The DBUpdater reports the '1110' error

Issue Description:

The following error message is displayed when running the **DBUpdater** tool.

![Deployment_Tutorial_0071](~/images/deployment_tutorial_0071116470.png)

_An error with number 1110 has occurred.
Error message: The database is an older version than the application. The database
needs to be updated._

Solution:

* The database is empty. Press ENTER and the **DBUpdater** will populate it with initial data.
* The application was updated, so the database must be updated as well. Press ENTER and the **DBUpdater** will fix this issue.

**See also:** [Application Update](xref:113239)

***

### The DBUpdater (or the application's -updateDatabase CLI command) cannot update the database as it cannot connect to the database server

Issue Description:

The following error message is displayed when running the **DBUpdater** tool or `-updateDatabase` CLI command.

![DTG_06](~/images/dtg_06116656.png)

_The database cannot be updated: An error has occurred while establishing a connection to the server._

Solution:

The possible reasons are:

* network failure;
* incorrect connection string;
* Database Server is not running;
* Database Server does not allow remote connections.

Ask the Database Server administrator for assistance if required.

**See also:** [Set Up the Database Connection](xref:113236)

***

### The DBUpdater (or the application's -updateDatabase CLI command) cannot update the database due to invalid credentials

Issue Description:

The following error message is displayed when running the **DBUpdater** tool or `-updateDatabase` CLI command.

![DTG_07](~/images/dtg_07116657.png)

_The database cannot be updated: Login failed for the user 'username'._

Solution:

The possible reasons are:

* incorrect connection string (a mistyped user ID);
* Database Server does not allow 'username' user to connect to a specified database.

Check that the account used to connect to the database has the proper permissions. Ask the Database Server administrator for assistance, if required.

**See also:** [Set Up the Database Connection](xref:113236)

***

### Performance issues when working with a large amount of data

Issue Description:

List Views with thousands of records load too slowly.

Solution:

* Set the [IModelOptions.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelOptions.DataAccessMode) option to `Server`, `ServerView`, `InstantFeedback`, or `InstantFeedbackView`. When [Server, ServerView, InstantFeedback, or InstantFeedbackView](xref:118450) mode is enabled in an XAF application, only visible records are retrieved from the server (50 records instead of thousands).
* XPO uses [GCRecord](xref:2632) in queries by default, and XAF sorts records by the [IModelClass.DefaultProperty](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultProperty) property. You need to create indexes for these columns, run your application, and trace the sent queries with the help of the [XPO Profiler](xref:10646) to check the _where_ and _order_ clauses, and add other necessary indexes.

**See also:** [CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode) | [Webinar: Profiling an XAF application with XPO Profiler](https://community.devexpress.com/blogs/xpo/archive/2011/08/18/webinar-profiling-a-xaf-application-with-xpo-profiler.aspx) | [Connect the XPO Profiler to a .NET Core application](xref:401638)

***

### The "An attempt was made to load a program with an incorrect format" error occurs when starting the DBUpdater or standalone Model Editor tool on an x64 system

Issue Description:

The DBUpdater or Model Editor tool states that it cannot load your application's assembly or executable; for example:

``Developer Express Inc (R) ExpressApp Framework Database Updater.``

``Version: <:xx.x.x:>.0``

``Copyright (C) Developer Express Inc 2012. All rights reserved.``

``Silent mode OFF``

``The database can't be updated:``

``Could not load file or assembly 'c:\Program Files\MySolution\MySolution.Win.exe' or one of its dependencies.``

``An attempt was made to load a program with an incorrect format.``

Solution:

To fix this issue, do one of the following:

* Reconfigure DBUpdater and Model Editor executable headers using [CorFlags.exe (CorFlags Conversion Tool)](https://learn.microsoft.com/en-us/dotnet/framework/tools/corflags-exe-corflags-conversion-tool).
	
	``CorFlags.exe "%PROGRAMFILES%\DevExpress <:xx.x:>\Components\Tools\eXpressAppFramework\DBUpdater\DBUpdater.v<:xx.x:>.exe" /32Bit+ /Force``

	``CorFlags.exe "%PROGRAMFILES%\DevExpress <:xx.x:>\Components\Tools\eXpressAppFramework\Model Editor\DevExpress.ExpressApp.ModelEditor.v<:xx.x:>.exe" /32Bit+ /Force``

* Change you application's configuration to 'Any CPU', recompile, and redeploy it.
* Recompile the DBUpdater and Model Editor utility against x64 (sources are located in the _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\DevExpress.ExpressApp.Tools\_ folder, by default).

See the [BadImageFormatException Class](https://learn.microsoft.com/en-us/dotnet/api/system.badimageformatexception) article in MSDN for the full list of scenarios or situations where this error can occur.

***

If this document does not contain sufficient information on how to resolve your issue, feel free to contact Developer Express support engineers at the [Support Center](https://supportcenter.devexpress.com).
