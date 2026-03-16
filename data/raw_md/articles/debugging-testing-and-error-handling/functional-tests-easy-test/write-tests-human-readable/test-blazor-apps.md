---
uid: "403393"
title: 'Integrate EasyTest into XAF Blazor UI Applications'
owner: Alexey Kazakov
---
# Integrate EasyTest into XAF Blazor UI Applications

## Overview

XAF can run functional tests for Blazor UI applications based on the [Selenium](https://www.selenium.dev/documentation/) driver to interact with a browser.

EasyTest for Blazor supports the following browsers:

- Google Chrome
- Microsoft Edge

This topic describes how to integrate EasyTest functional testing into your XAF Blazor application.

## Prerequisites

Configure your working machine as described below:

1. [Install browser drivers](https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/).

    - For Google Chrome: download "chromedriver.exe" from <https://developer.chrome.com/docs/chromedriver/downloads>. 
    - For Microsoft Edge: download "msedgedriver.exe" from <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH>.
 
    Selenium requires a path to the downloaded driver. You can specify a path to the driver in any of the following ways:
    - Add a folder with the driver to the system's PATH variable.
    - Specify a path to the driver in EasyTest's [configuration](#configuration) file.

        # [Xml](#tab/tabid-xml)
        ```XML
        <Application ... WebDriverPath="C:\WebDriverPath" />
        ```
        ***
2. Install the `DevExpress.ExpressApp.EasyTest.BlazorAdapter` package to your `YourApplicationName.Blazor.Server` project.

> [!TIP]
> 
> The [Template Kit](xref:405447) creates new applications that already have integrated EasyTest components. The wizard does the following:
> 
> - Adds the `EasyTest` solution configuration.
> 
>     ![EasyTest solution configuration](~/images/easytest-solution-configuration.png)
> - Adds all the necessary code to allow you run tests in the `EasyTest` solution configuration.
> - Adds the _FunctionalTests_ folder with a configuration file (_config.xml_) and a sample test (_sample.ets_) to the platform-independent _YourApplicationName.Module_ module.
> Installs the `DevExpress.ExpressApp.EasyTest.BlazorAdapter` package to your `YourApplicationName.Blazor.Server` project (only for the `EasyTest` solution configuration).



## Configuration

The code below demonstrates a sample [configuration file](xref:113209). You can edit it according to your project environment.

# [Xml](#tab/tabid-xml)
```XML
<?xml version="1.0" encoding="utf-8" ?> 
<Options xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> 
    <Applications> 
        <!-- Blazor --> 
        <Application 
            Name="DXApplication1Blazor" 
            Url="http://localhost:4030" 
            PhysicalPath="[BlazorAppPath]" 
            AdapterFileName="[BlazorAdapterAssemblyPath]" 
            Configuration="EasyTest" 
            IgnoreCase="true"/> 
    </Applications> 

    <TestDatabases> 
            <Database xsi:type="TestMSSQLDatabase" Server="(localdb)\mssqllocaldb" DBName="DXApplication1EasyTest"/> 
    </TestDatabases> 

    <Aliases> 
        <Alias Name="BlazorAppPath" Value="[ConfigPath]\..\..\DXApplication1.Blazor.Server" /> 
        <Alias Name="BlazorAdapterAssemblyPath" Value="[BlazorAppPath]\bin\EasyTest\net8.0\DevExpress.ExpressApp.EasyTest.BlazorAdapter.v21.2.dll" /> 
    </Aliases> 
</Options> 
```
***

### Configuration Options

| Attribute | Description |
|---|---|
| **Name** | Specifies the name of the **Application** element. This name is used to differentiate between different applications. The **Application** [command](xref:113208) takes this name as the parameter. |
| **Url** | The application's web address. |
| **PhysicalPath** | A path to the folder that contains the application. You can use the built-in **[ConfigPath]** alias to specify a path to the _Config.xml_ file. |
| **AdapterFileName** | Specifies a path to the Blazor EasyTest adapter. This is an EasyTest assembly that contains platform-specific functionality. The attribute contains the adapter's assembly filename, assembly version, culture, and public key. |
| **IgnoreCase** | Specifies whether the test ignores a letter case when referring to UI element names, captions, or tags. |
| **Configuration** | Specifies the configuration to use when running tests.|
| **WebDriverPath** | Specifies a path to a folder that stores a web driver executable. |
| **Browser** | Specifies a web browser to use for running tests. Available values: `Chrome`, `Edge` (the default value).

### Aliases

| Alias | Description |
|---|---|
| **BlazorAppPath** | A path to a Blazor application. |
| **BlazorAdapterAssemblyPath** | A path to the Blazor EasyTest adapter. This path typically points to a project's build results. Reference the `DevExpress.ExpressApp.EasyTest.BlazorAdapter` adapter and it becomes available in the project's build results. In new applications created by the [Template Kit](xref:405447), the adapter is already referenced in the project and this option is set to a folder with the build results.|


##  Run EasyTest in the Debug Configuration

The following steps describe the modifications required to support EasyTest in the **Debug** solution configuration.

Note that after updating the solution in this way, EasyTest will use the database connection strings specified in the application projects' configuration files. As such, you may want to back up the databases used by the applications before running any tests.

In a Blazor application project, update the `DatabaseVersionMismatch` method in _BlazorApplication.cs_:

# [C#](#tab/tabid-csharp1)
 
```csharp
private void MyBlazorApplication_DatabaseVersionMismatch(object sender, DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs e) { 
#if DEBUG 
    e.Updater.Update(); 
    e.Handled = true; 
#else 
    if (System.Diagnostics.Debugger.IsAttached) { 
        //... 
    } 
    else { 
        //... 
    } 
#endif 
} 
```
 
***


## Run Tests

Use the [TestExecutor Utility](xref:113210) to run tests.

# [Console](#tab/tabid-console)

```Console
cd %ProgramFiles%\DevExpress <:xx.x:>\Components\Tools\eXpressAppFrameworkNetCore\EasyTest

TestExecutor.v<:xx.x:>.exe C:\PathToTest\sample.ets
```
***

## Remove EasyTest

You can remove all EasyTest components from your application. In this case, delete the following:

* The **FunctionalTests** folder.
* The **DevExpress.ExpressApp.EasyTest.BlazorAdapter** package from Blazor applications.
* The `EASYTEST` conditions from the Blazor application project's _BlazorApplication.cs_ file.


## Next Steps

- [Test an Action](xref:113218)
- [EasyTest Script Reference](xref:113208)