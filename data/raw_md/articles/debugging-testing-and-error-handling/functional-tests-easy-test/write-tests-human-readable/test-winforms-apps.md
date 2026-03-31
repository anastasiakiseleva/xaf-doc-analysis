---
uid: "403492"
title: Integrate EasyTest into XAF WinForms Applications
---
# Integrate EasyTest into XAF WinForms Applications

## Overview

This topic describes how to integrate EasyTest functional testing into your XAF WinForms application.


> [!TIP]
> 
> The [Template Kit](xref:405447) creates new applications that already have integrated EasyTest components. The wizard does the following:
> 
> - Adds the `EasyTest` solution configuration.
> 
>     ![EasyTest solution configuration](~/images/easytest-solution-configuration.png)
> - Adds all necessary code to allow you to run tests in the `EasyTest` solution configuration.
> - Adds the _FunctionalTests_ folder with a configuration file (_config.xml_) and a sample test (_sample.ets_) to the platform-independent _YourApplicationName.Module_.
 
If your application already has EasyTest integrated, go to the [Next Steps](#next-steps) section.

## Configuration

Typically, the EasyTest configuration file (_config.xml_) is stored in the  _FunctionalTests_ folder in a [platform-agnostic module](xref:118045) (_MySolution.Module_).

**Requirement:** Install the `DevExpress.ExpressApp.EasyTest.WinAdapter` NuGet package to your `YourApplicationName.Win` project.

The following code snippet demonstrates a sample [configuration file](xref:113209). You can edit it according to your project environment.

# [Xml](#tab/tabid-xml)
```XML
<?xml version="1.0" encoding="utf-8" ?>
<Options xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <Applications>
        <!-- Win -->
        <Application
            Name="MySolutionWin"
            FileName="[WinAppBin]\MySolution.Win.exe"
            AdapterFileName="[WinAdapterFileName]"
            CommunicationPort="4100"/>
    </Applications>
    <TestDatabases>
        <Database xsi:type="TestMSSQLDatabase" Server="(localdb)\mssqllocaldb" DBName="MySolutionEasyTest"/>
    </TestDatabases>

    <Aliases>
        <Alias Name="WinAppBin" Value="[ConfigPath]\..\MySolutionWin.Win\Bin\EasyTest" />
        <Alias Name="WinAdapterFileName" Value="[WinAppBin]\DevExpress.ExpressApp.EasyTest.WinAdapter.v<:xx.x:>.dll" />
    </Aliases>
</Options>
```
***


### Configuration Options

| Attribute | Description |
|---|---|
| **Name** | Specifies the name of the **Application** element. This name is used to differentiate between different applications. The **Application** [command](xref:113208) takes this name as the parameter. |
| **FileName** | Specifies the fully qualified name of the application's executable file. You can use the built-in **[ConfigPath]** alias to specify a path relative to the _Config.xml_ file location. |
| **Arguments** | Optional. Specifies the command-line arguments passed to the application when it is started. |
| **AdapterFileName** | (For **.NET 8+** projects) The path to the WinForms EasyTest adapter. To use the standard adapter, specify the following path: _%ProgramW6432%\DevExpress <:xx.x:>\\Components\Bin\NetCore\DevExpress.ExpressApp.EasyTest.WinAdapter.v<:xx.x:>.dll_ | 
| **CommunicationPort** | Specifies the communication port number that will be used by EasyTest when testing the application. |


## Run EasyTest in the Debug Configuration

The following steps describe the modifications required to support EasyTest in the **Debug** solution configuration.


Note that after updating the solution in this way, EasyTest will use the database connection strings specified in the application projects' configuration files. As such, you may want to back up the databases used by the applications before running any tests.

In a Windows Forms application project, the following methods must be updated:

1. The **DatabaseVersionMismatch** method in the _WinApplication.cs_ (_WinApplication.vb_) file.
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    private void MySolutionWindowsFormsApplication_DatabaseVersionMismatch(
        object sender, DevExpress.ExpressApp.DatabaseVersionMismatchEventArgs e) {
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
2. The **Main** method in the _Program.cs_ (_Program.vb_) file.
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    static void Main() {
    #if DEBUG
        DevExpress.ExpressApp.Win.EasyTest.EasyTestRemotingRegistration.Register();
    #endif
    //....
    }
    ```
    ***

3. In the *App.config* file, add the following keys to **\<appSettings>**:

    # [XML](#tab/tabid-xml)

    ```XML
    <?xml version="1.0"?>
    <configuration>
    <!-- ... -->
        <appSettings>
        <!-- ... -->
            <add key="EasyTestTraceLevel" value="4"/> 
            <add key="EasyTestLogFileName" value="TestExecutor.log" />
        </appSettings>
    </configuration>
    ```
    ***

4. EasyTest listens to the default **4100** port. To use another port, specify the **EasyTestCommunicationPort** key value in the application configuration file (_App.config_). The custom port must match the port specified in the [EasyTest Config.xml configuration file](xref:113209).
    
    # [XML](#tab/tabid-xml)
    
    ```XML
    <appSettings>
        <!-- Specify a custom port -->
        <add key="EasyTestCommunicationPort" value="15923"/>
        <!-- ... -->
    </appSettings>
    ```
    
    ***


## Remove EasyTest

You can remove all EasyTest components from your application. In this case, delete the following:

* The **FunctionalTests** folder.
* The **DevExpress.ExpressApp.EasyTest.WinAdapter** assembly reference (or NuGet package) from the Windows Forms application project.
* The `EASYTEST` conditions from the Windows Forms application project's _Program.cs_ (_Program.vb_) and _WinApplication.cs_ (_WinApplication.vb_) files.



## Next Steps

- [Test an Action](xref:113218)
- [EasyTest Script Reference](xref:113208)
- [Run Tests](xref:113210)
