---
uid: "404613"
title: "Deploy a XAF ASP.NET Core Application (Blazor Server, Middle Tier Server, or Web API Service) to IIS"
---
# Deploy a XAF ASP.NET Core Application (Blazor Server, Middle Tier Server, or Web API Service) to IIS

This topic explains how to set up and publish an XAF Blazor Server application to an IIS server using the MS SQL database provider. For more information about other deployment approaches for ASP.NET Core and Blazor applications, refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/).

## Prerequisites

* A Windows Server that is configured with the Web Server (IIS) server role and has MS SQL Server installed.

[!include[deployment-tutorial-blazor-demo-app](~/templates/deployment-tutorial-blazor-demo-app.md)]

## Deployment Instructions

### Install the .NET Core Hosting Bundle

Install the .NET Core Hosting Bundle on an IIS server. The bundle includes .NET Core Runtime, .NET Core Library, and ASP.NET Core Module. These features enable you to run ASP.NET Core apps with IIS. You can download the installer from the following page: [Download the .NET Core Hosting Bundle installer](https://dotnet.microsoft.com/permalink/dotnetcore-current-windows-runtime-bundle-installer).

### Create an IIS Site

1. [Enable IIS](https://learn.microsoft.com/en-us/previous-versions/dynamicsnav-2018-developer/How-to--Install-and-Configure-Internet-Information-Services-for-Microsoft-Dynamics-NAV-Web-Client) in **Windows Features**.

1. Enable [WebSockets](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets#enabling-websockets-on-iis) in IIS for deploying Blazor Server or Middle Tier applications.

1. Create a folder that should contain files of a published app (for example, _c:\inetpub\wwwroot\maindemo_).

1. Launch **Internet Information Services (IIS) Manager**. Right-click **Sites** and select **Add Website**.

    ![|DevExpress XAF - Create a Site in IIS](~/images/deployment-tutorial-iis-add-website.png)

1. In the **Add Website** dialog that appears, specify field values and click **OK**.

    * **Site name** -- `maindemo`. 
    * **Physical path** -- _c:\inetpub\wwwroot\maindemo_.
    * Use the **Type** drop-down list to set up **http** and **https** binding configurations. Make sure to select a certificate for the `https` binding configuration (you can create a [self-signed certificate](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis#obtain-a-certificate) for debugging purposes).

        It is not recommended to use top-level wildcard bindings in a production environment (for example, `http://*:80/`
and `http://+:80`). Refer the following links for more information: [Publish an ASP.NET Core app to IIS](https://learn.microsoft.com/en-us/aspnet/core/tutorials/publish-to-iis#create-the-iis-site) and [HTTP Semantics - Host and :authority](https://www.rfc-editor.org/rfc/rfc9110#name-host-and-authority).

    ![DevExpress XAF - Add Website dialog](~/images/deployment-tutorial-iis-add-website-dialog.png)

### Set Up a Connection String

1. Run Visual Studio with administrative privileges and open your Blazor project (the `MainDemo Blazor Server` demo application is used in this example).

1. Specify a [connection string](xref:404290) in the _appsettings.json_ file. For example, you can use the following connection string for MSSQL Server (replace `YourServerName` with the correct value):

    ```JSON
    {
        "ConnectionStrings": {
            "ConnectionString": "Integrated Security=SSPI;Pooling=false;MultipleActiveResultSets=true;Data Source=YourServerName;Initial Catalog=MainDemo.NET.EFCore_v<:xx.x:>;ConnectRetryCount=0;",
            // ...
        },
        // ...
    }
    ```

    In this case, an XAF application uses Windows Authentication to connect to the database.

1. Build your solution and make sure that the application runs correctly in development mode.

1. You may see the following error: `The certificate chain was issued by an authority that is not trusted`. In this case, install a valid CA-signed SSL/TLS certificate on your SQL Server. For testing purposes, you can add a `TrustServerCertificate=True;` option to your connection string (replace `YourServerName` with the correct value):

    ```JSON
    {
        "ConnectionStrings": {
            "ConnectionString": "Integrated Security=SSPI;Pooling=false;MultipleActiveResultSets=true;Data Source=YourServerName;Initial Catalog=MainDemo.NET.EFCore_v<:xx.x:>;ConnectRetryCount=0;TrustServerCertificate=True;",
            // ...
        },
        // ...
    }
    ```

### Publish the Application

1. In **Solution Explorer**, right-click the project name and click **Publish**.

    ![|DevExpress XAF - Publish an Application in IIS](~/images/deployment-tutorial-iis-publish.png)

1. Select **Folder** and click **Next**.

    ![DevExpress XAF - Specify target](~/images/deployment-tutorial-iis-publish-folder.png)

1. In the **Folder location** box, specify a folder you have created (_c:\inetpub\wwroot\maindemo_) and click **Finish**.

    ![DevExpress XAF - Specify a folder location](~/images/deployment-tutorial-iis-publish-folder-location.png)

1. Close the **Publish** wizard.
1. Visual Studio creates a publishing profile for your project. 
1. Click **Publish** next to the created profile.

    ![|DevExpress XAF - Publish an Application in IIS](~/images/deployment-tutorial-iis-publish-profile.png)

1. The **Publish** page with a successful result indicates that the application has been published correctly.

1. Launch the **Command Prompt** and [update a database](xref:113239).

    ```Console
    cd C:\inetpub\wwwroot\maindemo
    dotnet MainDemo.Blazor.Server.dll --updateDatabase --forceUpdate --silent
    ```

### Add IIS AppPool Identities as SQL Server Logons

1. Launch **Microsoft SQL Server Management Studio**. 
1. Connect to your server and create a new login. For this purpose, right-click the **Security** | **Logins** node in Object Explorer and select **New Login** from the ensuing context menu.

    ![|DevExpress XAF - Add IIS AppPool Identities as SQL Server Logons](~/images/deployment-tutorial-iis-sql-server-new-login.png)

1. The **Login - New** dialog appears. On its **General** page, specify the login name (`IIS APPPOOL\maindemo`).

    ![DevExpress XAF - A New Login Name](~/images/deployment-tutorial-iis-new-login-name.png)

1. On the **Server Roles** page, select roles for the created login. For example, you can check **public** and **svsadmin** boxes.

    ![DevExpress XAF - Server Roles for a New Login Name](~/images/deployment-tutorial-iis-new-login-roles.png)

1. On the **User Mapping** page, select your database and set up mappings for it.

    ![DevExpress XAF - User Mapping for a New Login Name](~/images/deployment-tutorial-iis-user-mapping.png)

1. On the **Securables** page, click **Search** and add your SQL Server instance to the page. 

    ![|DevExpress XAF - Add a Securable for a New Login Name](~/images/deployment-tutorial-iis-add-securables.png)

1. Grant the **Connect SQL** permission to the added server and save the login.

    ![DevExpress XAF - Grant a Permission for a New Login Name](~/images/deployment-tutorial-iis-grant-permission.png)

### Run the Published Application

1. Launch **Internet Information Services (IIS) Manager**. Expand the **Sites** node to ensure that the published application is running.

    ![DevExpress XAF - The Published Application is Running](~/images/deployment-tutorial-iis-manager-running-app.png)

1. Click **Browse** to open the application in your browser.

    ![DevExpress XAF - Browse the Published Application](~/images/deployment-tutorial-iis-browse-app.png)

1. The application runs in your default browser.

    ![|DevExpress XAF - Deployed Application](~/images/deployment-tutorial-iis-result.png)

[!include[deployment-tutorial-blazor-disclaimer](~/templates/deployment-tutorial-blazor-disclaimer.md)]

## Troubleshooting

If you encounter problems, refer to the [](xref:113238) or explore logs and stack traces in [Event Viewer](https://learn.microsoft.com/en-us/shows/inside/event-viewer).


## Additional Resources

Refer to the Microsoft documentation for more information about deploying ASP.NET Core and Blazor applications:

* [](xref:403362)
* [Publish an ASP.NET Core app to IIS](https://learn.microsoft.com/en-us/aspnet/core/tutorials/publish-to-iis)
* [Host and deploy server-side Blazor apps](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/server)
