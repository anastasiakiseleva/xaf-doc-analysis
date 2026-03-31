---
uid: "113360"
seealso:
- linkId: "118741"
title: Run the XPO Application Server as a Windows Service
---
# Run the XPO Application Server as a Windows Service

> [!IMPORTANT]
> [!include[Wizard_Note](~/templates/wizard_note111144.md)]

In a production environment, it is convenient to set up and run the XAF Application Server as a [Windows Service](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/introduction-to-windows-service-applications). This topic describes how to convert the Console Application Server implemented in the [Middle Tier Security](xref:113439) topic to a Windows Service. While debugging, use the Console Application Server. Convert it to a Windows Service before final deployment. Ensure that the Console Application Server operates with no errors before conversion.

## Add the Windows Service Application Server Project
Although the Middle Tier application server can be implemented as a regular Windows Service, XAF provides a project template to simplify this task. So to add a Windows Service application server project to your solution, do the following:

* Right-click the solution in the **Solution Explorer**.
* In the invoked context menu, choose **Add** | **New Project…**.
* Choose the **DevExpress v<:xx.x:> XAF Template Gallery** template.
* Specify the project name (for example, MySolutionApplicationServer) and click **OK**.
* Select the **Application Server Project** in the Solution Wizard and click **Next**.
* Choose the **Windows Service** as the **Middle Tier Server Type** and click **Finish**.

As a result, the **MySolutionApplicationServer** project will be created from the template.

## Copy the Server Configuration from the Console Application Server Project
Copy the **ServerApplication.ApplicationName** property and **ServerApplication.Modules** collection initializations from the _ServerApplication.cs_ file located in the Console Application Server project to the _ApplicationServerService.cs_ file.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security.ClientServer.Wcf;
using DevExpress.ExpressApp.Xpo;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
// … 
public partial class ApplicationServerService : System.ServiceProcess.ServiceBase {
    // … 
    protected override void OnStart(string[] args) {
        string connectionString = ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString;
        ValueManager.ValueManagerType = typeof(MultiThreadValueManager<>).GetGenericTypeDefinition();
        ServerApplication serverApplication = new ServerApplication();
        serverApplication.ApplicationName = "DxSampleService";
        serverApplication.Modules.BeginInit();
        serverApplication.Modules.Add(new MySolutionWindowsFormsModule());
        serverApplication.Modules.Add(new MySolutionAspNetModule());
        serverApplication.Modules.EndInit();
        //...
    }
    //...
}
```

***

Do not forget to add required references to your module projects (for example, **MySolution.Module**, **MySolution.Module.Win**, and **MySolution.Module.Web**). Right-click the newly created Application Server project and choose **Add reference…**. In the invoked dialog, switch to the **Projects** tab, select the module projects, and click **OK**.

The Windows Service Application Server is configured to use the WCF client connection type, `ApplicationUser` user type (derived from [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser)), [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRole) role type, and [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authentication type. If your settings for the Console Application Server differ, copy the corresponding code to the _MySolutionService.cs_ file. Below is an example for WCF (the **OnStart** and **OnStop** methods of the **MySolutionService** class are modified).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security.ClientServer.Wcf;
using DevExpress.ExpressApp.Xpo;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
// … 
public partial class ApplicationServerService : System.ServiceProcess.ServiceBase {
    // … 
    protected override void OnStart(string[] args) {
        //...
        serverApplication.CheckCompatibilityType = CheckCompatibilityType.DatabaseSchema;
        serverApplication.CreateCustomObjectSpaceProvider += (s, e) => 
            e.ObjectSpaceProvider = new XPObjectSpaceProvider(connectionString);
        serverApplication.ConnectionString = connectionString;
        serverApplication.Setup();
        serverApplication.CheckCompatibility();
        serverApplication.Dispose(); 
        Func dataServerSecurityProvider = () =>
            new SecurityStrategyComplex(typeof(ApplicationUser), typeof(PermissionPolicyRole), new AuthenticationStandard());
        serviceHost = new WcfXafServiceHost(connectionString, dataServerSecurityProvider);
        string serviceEndPoint = @"net.tcp://localhost:1451/DataServer";
        serviceHost.AddServiceEndpoint(typeof(IWcfXafDataServer), WcfDataServerHelper.CreateNetTcpBinding(), serviceEndPoint);
        serviceHost.Open();
    }
    protected override void OnStop() {
        serviceHost.Close();
    }
}
```

***

A reference to the _System.ServiceModel.dll_ assembly is required when using WCF. To connect the application server to a database provider, specify the connection string in the configuration file (_App.config_) located in the application server project, or explicitly set it to the **connectionString** variable in the code above.

## Install and Run the Windows Service Application Server
Do the following to install and run the application server service:

* Build the application server project.
* Run **Visual Studio Command Prompt** (from the Windows Start menu).
* Type "installutil _path_to_service_executable_" and press ENTER.
* Type "net start _service_name_". You can see the service name in the previous step in the **installutil** output. The service name can be configured in a designer invoked for the _ProjectInstaller.cs_ file (change the [ServiceInstaller.ServiceName](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceinstaller.servicename#System_ServiceProcess_ServiceInstaller_ServiceName) value).

To stop the service, type "net stop _service_name_". To uninstall it, type "installutil _path_to_service_executable_ /u". Do not forget to stop the service each time you need to rebuild the application server project. Otherwise, Visual Studio will not be able to replace the service executable with the new one.

> [!NOTE]
> If you experience any difficulties with these steps, refer to the MSDN topics listed below.
> 
> * [How to: Specify the Security Context for Services](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-specify-the-security-context-for-services)
> * [How to: Install and Uninstall Services](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-install-and-uninstall-services)
> * [How to: Start Services](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-start-services)
> * [How to: Debug Windows Service Applications](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-debug-windows-service-applications)

## Windows Service Troubleshooting
If the service could not be started with the **net start** command, start the Event Viewer application and open the **Application** log to determine the issue.

![DebugAppServer](~/images/debugappserver117088.png)

If this does not help, refer to the MSDN topics listed below.

* [How to: Specify the Security Context for Services](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-specify-the-security-context-for-services)
* [How to: Install and Uninstall Services](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-install-and-uninstall-services)
* [How to: Start Services](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-start-services)
* [How to: Debug Windows Service Applications](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-debug-windows-service-applications)
