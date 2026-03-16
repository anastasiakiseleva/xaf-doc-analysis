---
uid: "404614"
title: Deploy a XAF ASP.NET Core Application (Blazor Server, Middle Tier Server, or Web API Service) to Azure App Service
---
# Deploy a XAF ASP.NET Core Application (Blazor Server, Middle Tier Server, or Web API Service) to Azure App Service

This topic shows how to publish an XAF ASP.NET Core application (Blazor Server UI, Middle Tier Server, Web API Service) to the [Azure App Service](https://azure.microsoft.com/en-us/products/app-service). For more information about other deployment methods, refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/).

## Prerequisites

* An Azure account with an active subscription.

[!include[deployment-tutorial-blazor-demo-app](~/templates/deployment-tutorial-blazor-demo-app.md)]

## Deployment Instructions

### Add Required Packages (.NET 8+)

Make sure you have the correct drawing engine for your application. If your project targets .NET 8+, add the following packages to your **MainDemo.Blazor.Server** project:

* [DevExpress.Drawing](https://nuget.devexpress.com/packages/DevExpress.Drawing/)
* [DevExpress.Drawing.Skia](https://nuget.devexpress.com/packages/DevExpress.Drawing.Skia) -- For more information on this package, refer to the following topic: [DevExpress.Drawing Graphics Library](xref:404247).

If you are running your application on Linux or macOS and it includes [Reports](xref:113591), [Office](xref:400003) or [Dashboards](xref:117449) modules, additional setup may be required. If you encounter any issues with rendering or exporting documents and dashboards, review the following help topics:

[!include[deployment-non-windows-additional-setup-links](~/templates/deployment-non-windows-additional-setup-links.md)]

### Set Up a Publishing Profile

1. Run Visual Studio with administrative privileges and open your Blazor solution (the `MainDemo Blazor Server` demo application is used in this example).

1. Log into your Microsoft account from Visual Studio.

    ![|DevExpress XAF - Sign In to Azure](~/images/deployment-tutorial-azure-sign-in.png)

1. In **Solution Explorer**, right-click the **MainDemo.Blazor.Server** project name and click **Publish**.

    ![|DevExpress XAF - Publish an Application to Azure](~/images/deployment-tutorial-iis-publish.png)

1. Select **Azure** and click **Next**.

    ![DevExpress XAF - Specify target](~/images/deployment-tutorial-azure-publish-target.png)

1. Select the Azure App Service. In this tutorial, we publish the application to **Azure App Service (Linux)**. Select this item and click **Next**.

    ![DevExpress XAF - Specify a Azure App Service](~/images/deployment-tutorial-azure-publish-specific-target.png)

1. On the **App Service** tab, click **Create new**.

    ![DevExpress XAF - Create a New Azure App Service](~/images/deployment-tutorial-azure-publish-create-new.png)

1. If necessary, change the **Name**, **Resource group**, or **Hosting Plan** values and click **Create**.
1. Select the newly-created service and click **Next**.

    ![DevExpress XAF - A New Azure App Service](~/images/deployment-tutorial-azure-publish-new-service.png)

1. On the **API Management** tab, check the **Skip this step** box and click **Finish**.

    ![DevExpress XAF - A New Azure App Service is Created](~/images/deployment-tutorial-azure-publish-finish.png)

1. Close the **Publish** wizard.

1. Visual Studio creates a publishing profile for your project.

### Connect to an Azure SQL Database

1. Scroll to the bottom of the **Publish Profile Summary** page and click the ellipsis button next to the **SQL Server Database (ConnectionStrings:ConnectionString)** service dependency. Select **Connect** from the ensuing menu.

    ![|DevExpress XAF - Connect to an Azure SQL Database](~/images/deployment-tutorial-azure-connect-to-server-database.png)

1. Select **Azure SQL Database** and click **Next**.

    ![DevExpress XAF - Select a Server Dependency](~/images/deployment-tutorial-azure-select-a-server-dependency.png)

1. Select an existing Azure SQL server or create a new instance. In this tutorial, we click **New** to create a new server.

    ![DevExpress XAF - Create a New Server](~/images/deployment-tutorial-azure-create-new-server.png)

1. Click **New** next to the **Database server** field.

    ![|DevExpress XAF - Create a New Database Server](~/images/deployment-tutorial-azure-new-database-server.png)

1. Specify values for the **Database server name**, **Location**, **Administrator username**, and password fields. Click **OK** to close the dialog.

    ![DevExpress XAF - Credentials for a New Database Server](~/images/deployment-tutorial-azure-new-database-server-credentials.png)

1. Click **Create** in the Azure SQL Database dialog.

1. Select the created database and click **Next**.

    ![DevExpress XAF - Select a Server Dependency](~/images/deployment-tutorial-azure-select-a-service-dependency.png)

1. Specify credentials (**username** and **password**) for database connection. Best practice is to avoid using the same details as the username and password used in step 5. 

    Click **Next**.

    ![DevExpress XAF - Specify Server Credentials](~/images/deployment-tutorial-azure-connection-credentials.png)

1. Clear the **NuGet packages** check box and click **Finish**.

    ![DevExpress XAF - Finish the Server Creation](~/images/deployment-tutorial-azure-uncheck-nuget-packages.png)

1. Close the dialog.

### Choose a Publishing Approach

You can publish your Blazor Server app to the Azure App Service using one of the following options:

Azure SignalR Service (Recommended by Microsoft)
:   This approach requires additional setup in the _MainDemo.Blazor.Server/Startup.cs_ file. Note that the specified step is implemented in the **MainDemo** application by default.

    ```csharp
    public void ConfigureServices(IServiceCollection services) {
        services.AddSingleton(
            typeof(HubConnectionHandler<>),
            typeof(ProxyHubConnectionHandler<>)
    );
    ```

    For more information, refer to the following Microsoft page: [Azure SignalR Service](https://azure.microsoft.com/en-us/products/signalr-service).

Application Request Routing (ARR) Affinity and WebSockets
:   You can enable this functionality in the App Service settings on the Azure Portal. For more information, refer to the following Microsoft topic: [Using the Application Request Routing Module](https://learn.microsoft.com/en-us/iis/extensions/planning-for-arr/using-the-application-request-routing-module).

HTTP Long Polling
:   This approach uses multiple HTTP connections to send and receive data instead of WebSocket connection. In this case, the application displays error messages in the browser console. 

This tutorial describes how to implement the first two approaches. For detailed steps, refer to sections below.

> [!note]
> Middle Tier Server uses Web Socket connection for communicating with Client application. Enable Web Sockets support option for this case as it mentioned below.

#### The "Azure SignalR Service" Publishing Approach

1. Ensure you have performed an [additional setup step](#choose-a-publishing-approach).
1. Scroll to the bottom of the **Publish Profile Summary** page and click the ellipsis button next to the **SignalR** service dependency. Select **Connect** from the ensuing menu.

    ![|DevExpress XAF - Connect to a SingleR Database](~/images/deployment-tutorial-azure-signalr-connect.png)

1. Select an existing SingleR instance or create a new one. In this tutorial, we click **New** to create a new instance.

    ![|DevExpress XAF - Create a New SingleR Instance](~/images/deployment-tutorial-azure-create-new-signalr-instance.png)

1. Specify required field values and click **Create**.

    ![DevExpress XAF - Create a New SingleR Instance](~/images/deployment-tutorial-azure-create-signalr.png)

1. Select the created instance and click **Next**. 
1. Click **Finish** to create the instance.
1. Close the dialog.

#### The "Application Request Routing (ARR) affinity and WebSockets" Publishing Approach

1. Open the [Azure Portal](https://portal.azure.com).
1. Click **App Services**.

    ![|DevExpress XAF - Azure Portal](~/images/deployment-tutorial-azure-portal-app-services.png)

1. Click your App Service name.
1. Switch to the **Configuration** | **General Settings** page. 

    ![|DevExpress XAF - Azure Portal Settings](~/images/deployment-tutorial-azure-portal-settings.png)

1. Enable **WebSockets** and **ARR** settings.
    
    Note that these settings are always enabled for Linux App Services - these settings are enabled by default for the App Service we have created in this tutorial. In this case, the **General Settings** page does not display corresponding settings. For more information, refer to the following Microsoft article: [Azure App Service on Linux FAQ - Web Sockets](https://learn.microsoft.com/en-us/troubleshoot/azure/app-service/faqs-app-service-linux#web-sockets).

### Publish the Application

1. In the **Visual Studio**, click **Publish** next to the created profile.

    ![|DevExpress XAF - Publish an Application to Azure](~/images/deployment-tutorial-azure-publish.png)

1. Once the application is published, update the database (if necessary). Note that these steps (2-3) are not required for this example as our demo application automatically generates a demo database. You would normally need to perform these steps for your custom applications. 

    Open [Azure Portal](https://portal.azure.com) and go your App Service settings. Click **Advanced Tools** and follow the **Go** link.

    ![|DevExpress XAF - Azure Portal Settings](~/images/deployment-tutorial-azure-azure-portal-advanced-tools.png)

1. Switch to the **Bash** tab and launch the application in the database update mode.

    ```Console
    dotnet ~/site/wwwroot/MainDemo.Blazor.Server.dll --updateDatabase --force --silent
    ```
1. Ensure that the application runs correctly in your default browser.

    ![|DevExpress XAF - Publishing Result](~/images/deployment-tutorial-azure-result.png)

[!include[deployment-tutorial-blazor-disclaimer](~/templates/deployment-tutorial-blazor-disclaimer.md)]

## Troubleshooting

If you encounter problems, refer to the [](xref:113238) or review [application logs](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs).


## Additional Resources

Refer to the Microsoft documentation for more information about deploying ASP.NET Core and Blazor applications:

* [Deploy ASP.NET Core apps to Azure App Service](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/)
* [Host and deploy server-side Blazor apps](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/server)
