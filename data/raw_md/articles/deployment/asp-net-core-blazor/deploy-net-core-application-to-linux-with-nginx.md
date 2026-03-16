---
uid: "404717"
title: Deploy a XAF ASP.NET Core Application (Blazor Server, Middle Tier Server, or Web API Service) to Linux with Nginx
---
# Deploy a XAF ASP.NET Core Application (Blazor Server, Middle Tier Server, or Web API Service) to Linux with Nginx

This topic describes how to set up and publish an XAF Blazor Server UI application to Ubuntu, Red Hat Enterprise (RHEL), and SUSE Linux Enterprise Server machines with Nginx reverse proxy.

The [Template Kit](xref:405447) uses Microsoft SQL Server as the default database provider option. This examples changes that default option to PostgreSQL (simply as a customization example). For more information on how to switch database providers, refer to the following topic: [](xref:404290).

## Prerequisites

# [Ubuntu](#tab/tabid-ubuntu)

* Access to [Ubuntu](https://ubuntu.com/). Use its standard user account with `sudo` privileges.

[!include[deployment-tutorial-linux-common-prerequisites](~/templates/deployment-tutorial-linux-common-prerequisites.md)]

# [Red Hat Enterprise Linux](#tab/tabid-red-hat)

* Access to [Red Hat Enterprise (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) v8.0 or later. Use its standard user account with `sudo` privileges.

[!include[deployment-tutorial-linux-common-prerequisites](~/templates/deployment-tutorial-linux-common-prerequisites.md)]

# [SUSE Linux Enterprise Server](#tab/tabid-suse)

* Access to [SUSE Linux Enterprise Server (SLES)](https://www.suse.com/products/server/) v12 or v15. Use its standard user account with `sudo` privileges.

[!include[deployment-tutorial-linux-common-prerequisites](~/templates/deployment-tutorial-linux-common-prerequisites.md)]

***

## Deployment Instructions

### Install Required Libraries and Packages

1. Install the following font libraries. These libraries allow the application to measure text to correctly render documents and export them to PDF.

    # [Ubuntu](#tab/tabid-ubuntu)

    ```Console
    sudo apt-get install -y libc6 libicu-dev libfontconfig1
    ```

    # [Red Hat Enterprise Linux](#tab/tabid-red-hat)

    ```Console
    sudo yum install -y glibc-devel libicu fontconfig
    ```

    # [SUSE Linux Enterprise Server](#tab/tabid-suse)

    ```Console
    sudo zypper install -y libicu fontconfig
    ```

    ***

1. Install the `ttf-mscorefonts-installer` package that adds Microsoft `TrueType` core fonts to your system. (Installed fonts include Arial, Times New Roman, Courier New, and others.)

    # [Ubuntu](#tab/tabid-ubuntu)

    ```Console
    sudo apt-get install ttf-mscorefonts-installer
    ```

    # [Red Hat Enterprise Linux](#tab/tabid-red-hat)

    ```Console
    sudo rpm -i https://downloads.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6-1.noarch.rpm
    ```

    # [SUSE Linux Enterprise Server](#tab/tabid-suse)

    ```Console
    sudo zypper install -y ttf-mscorefonts-installer
    ```

    ***
    
1. Install the package below to render JPEG images in PDF files (you can install any other package that implements `libjpeg` API v6.2 or v8.0.).

    # [Ubuntu](#tab/tabid-ubuntu)

    ```Console
    sudo apt install -y libjpeg-turbo8
    ```

    # [Red Hat Enterprise Linux](#tab/tabid-red-hat)

    ```Console
    sudo yum install -y libjpeg-turbo
    ```

    # [SUSE Linux Enterprise Server](#tab/tabid-suse)

    ```Console
    sudo zypper install -y libjpeg8
    ```

    ***

1. Make sure an appropriate drawing engine is available. Add the following packages to your **MainDemo.Blazor.Server** project:

    * [DevExpress.Drawing](https://nuget.devexpress.com/packages/DevExpress.Drawing/)
    * [DevExpress.Drawing.Skia](https://nuget.devexpress.com/packages/DevExpress.Drawing.Skia) -- For more information on this package, refer to the following topic: [DevExpress.Drawing Graphics Library](xref:404247).

### Set Up Forwarded Header Middleware

Since requests are forwarded through a reverse proxy, use [Forwarded Headers Middleware](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer#forwarded-headers). It updates `Request.Scheme` with the `X-Forwarded-Proto` header so that redirect URIs and other security policies work correctly.

Forwarded Headers Middleware should run before any other middleware. This order ensures that other middleware can consume header values for processing. To run Forwarded Headers Middleware after diagnostic and error handling middleware, see [Forwarded Headers Middleware order](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer#fhmo). 

To set up this middleware, call the `UseForwardedHeaders` method from your project's _Startup.cs_ file before calling any other middleware. Within this call, configure the middleware to forward `X-Forwarded-For` and `X-Forwarded-Proto` headers.

# [MainDemo.Blazor.Server/Startup.cs](#tab/blazor)
```csharp{2,10-12}
//...
using Microsoft.AspNetCore.HttpOverrides;

namespace MainDemo.Blazor.Server;

public class Startup {
    //...
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env) {
        //...
        app.UseForwardedHeaders(new ForwardedHeadersOptions {
            ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto
        });
        //...
    }
}
```
***

### Set Up the Database and Connection String

To use PostgreSQL database provider, follow the steps below:

1. Install the [Npgsql.EntityFrameworkCore.PostgreSQL](https://www.nuget.org/packages/Npgsql.EntityFrameworkCore.PostgreSQL) package to both **MainDemo.Module** and **MainDemo.Blazor.Server** projects. Make sure that this package's version matches the version of the [EntityFrameworkCore](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore) package you have installed.

1. Change the application connection string.

     # [MainDemo.Blazor.Server/appsettings.json](#tab/blazor)
    ```JSON
    "ConnectionStrings": {
        "ConnectionString": "EFCoreProvider=PostgreSql;Host=localhost;Database=maindemo;Username=testuser;Password=Qwerty1_",
        ...
    },
    ...  
    ```
    ***

1. If you use [migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/), update the `MainDemoDesignTimeDbContextFactory.ConnectionString` property as follows:

     # [MainDemo.Module/BusinessObjects/MainDemoDbContext.cs](#tab/blazor)
    ```csharp
    public class MainDemoDesignTimeDbContextFactory : DesignTimeDbContextFactory<MainDemoDbContext> {
        protected override string ConnectionString  => 
            "EFCoreProvider=PostgreSql;Host=localhost;Database=maindemo;Username=testuser;Password=Qwerty1_";
    }
    ```
    ***

You may see an error message that says "_Cannot write DateTime with Kind=Unspecified to PostgreSQL type 'timestamp with time zone'_". If this happens, set `DateTimeKind` to `UTC` for each DateTime property or add the following line to the `Program.Main()` method.

# [MainDemo.Blazor.Server/Program.cs](#tab/blazor)
```csharp{6}
namespace MainDemo.Blazor.Server;

public class Program : IDesignTimeApplicationFactory {
    public static int Main(string[] args) {
        //...
        AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);
        //...
    }
}
```
***

Refer the following topic for details: [Date and Time Handling](https://github.com/npgsql/doc/blob/main/conceptual/Npgsql/types/datetime.md/).

### Publish and Copy the Application

1. Make sure that the DevExpress NuGet source URL is registered in your source list. Use the following link to locate this URL: [Your DevExpress NuGet Feed URL](https://nuget.devexpress.com/#feed-url). We also recommend that you use the NuGet v3 source URL.

    The command below adds `DevExpressNuget` to your source list.

    ```Console
    dotnet nuget add source -n DevExpressNuget https://nuget.devexpress.com/{your-feed-authorization-key}/api/v3/index.json 
    ```

1. Execute the [dotnet publish](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish) command from the development environment to package an application into a directory that can be run on the server.

    ```Console
    dotnet publish --configuration Release
    ```

1. Copy your application to the server using a tool that is integrated into the organization's workflow (for example, `SCP`, `SFTP`).  It is common to store web applications in the `var` directory (for example, `var/www/MainDemo.Blazor.Server`).

1. Check that the application works correctly. To do this, run the application from the command line.

    ```Console
    dotnet MainDemo.Blazor.Server.dll.
    ```
    
    Run the application locally under Linux. Open a browser and navigate to `http://<serveraddress>:<port>`. Check that the application works correctly.

    ![|DevExpress XAF - Publishing Result](~/images/deployment-tutorial-azure-result.png)

1. If the application database exists and does not require any updates, your XAF Blazor application is ready to use.

    If the database is not ready, you will see a [database version mismatch error](xref:113238#the-the-application-cannot-connect-to-the-specified-database-because-the-database-doesnt-exist-its-version-is-older-than-that-of-the-application-or-its-schema-does-not-match-the-orm-data-model-structure-error-occurs) in the console. Such an error indicates that the database either does not exist yet or needs to be updated (based on your latest changes to the data model and XAF modules). To resolve the error, start the application in database update mode.

    ```Console
    dotnet MainDemo.Blazor.Server.dll --updateDatabase --forceUpdate –silent
    ```

### Configure Nginx

1. Install Nginx. To do this, you can use the following instructions:

    * [Debian/Ubuntu](https://docs.nginx.com) 
    * [RHEL](https://nginx.org/en/linux_packages.html#RHEL)
    * [SLES](https://nginx.org/en/linux_packages.html#SLES)

1. As Nginx has just been installed, explicitly start it.

    ```Console
    sudo service nginx start
    ```

1. Configure Nginx as a reverse proxy to forward HTTP requests to your ASP.NET Core application.

    Open the following file: _/etc/nginx/sites-available/default_. For example, run the command below to open it in the **nano** text editor.

    ```Console
    sudo nano /etc/nginx/sites-available/default 
    ```

    Replace the file's content with the following code.

    # [Web API Service](#tab/tabid-webapi)

    ```Console
    server {
            listen 80;
            server_name localhost;

            location / {
                    return 301 https://$host$request_uri;
            }
    }

    server {
            listen 443 ssl http2;
            server_name localhost;

            ssl_certificate     /etc/ssl/certs/nginx-selfsigned.crt;
            ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;

            location / {
                    proxy_pass         http://localhost:5000;
                    proxy_http_version 1.1;
                    proxy_set_header   Host $host;
                    proxy_set_header   X-Real-IP $remote_addr;
                    proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header   X-Forwarded-Proto $scheme;

            # Disable proxy buffering for APIs (responses stream immediately)
                    proxy_buffering off;
            }
    }
    ```
    
    # [Middle Tier Server or Blazor Server Application](#tab/tabid-razor)

    ```console
    server {
            listen 80;
            server_name localhost;

            location / {
                    return 301 https://$host$request_uri;
            }
    }

    server {
            listen 443 ssl http2;
            server_name localhost;

            ssl_certificate     /etc/ssl/certs/nginx-selfsigned.crt;
            ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;

            location / {
                    proxy_pass         http://localhost:5000;
                    proxy_http_version 1.1;
                    proxy_set_header   Host $host;
                    proxy_set_header   X-Real-IP $remote_addr;
                    proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header   X-Forwarded-Proto $scheme;

                    proxy_set_header   Upgrade $http_upgrade;
                    proxy_set_header   Connection "Upgrade";
                    proxy_cache_bypass $http_upgrade;

                    proxy_buffering off;
                    proxy_read_timeout 100s;
            }
    }
    ```
    ***


1. In the configuration snippet above, Nginx accepts public HTTPS traffic on ports `80` and `443` and redirects unsecured HTTP traffic to an encrypted HTTPS connection. Nginx forwards matching requests to Kestrel at `http://127.0.0.1`. 

1. Specify the path to the certificate file and associated key. For example, you can generate a self-signed certificate file for testing purposes. For more information, refer to the following tutorial: [How To Create a Self-Signed SSL Certificate for Nginx in Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-16-04).

1. Run the following command to check that configuration file syntax is correct.

    ```Console
    sudo nginx –t
    ```

1. Run the command below to apply the new configuration to Nginx.

    ```Console
    sudo nginx -s reload
    ```

1. Navigate to the application directory and run the application. 

    ```Console
    dotnet MainDemo.Blazor.Server.dll.
    ```

1. Navigate to `https://<your_host_name>` in a browser to check that Nginx is working correctly with the application.

### Monitor the Application

1. Nginx cannot manage Kestrel application processes. You can use [systemd](https://systemd.io/) to create a service file that starts and monitors the underlying web application. 

1. Create a service definition file.

    ```Console
    sudo nano /etc/systemd/system/kestrel-maindemo.service
    ```

    The following service file example starts and monitors the `MainDemo.Blazor.Server` application.

    ```Console
    [Unit]

    Description=XAF Blazor App running on Linux

    [Service]

    WorkingDirectory=/var/www/MainDemo.Blazor.Server
    ExecStart=/usr/bin/dotnet /var/www/MainDemo.Blazor.Server/MainDemo.Blazor.Server.dll
    Restart=always

    # Restart service after 10 seconds if the dotnet service crashes:

    RestartSec=10
    KillSignal=SIGINT
    SyslogIdentifier=dotnet-example
    User=www-data
    Environment=ASPNETCORE_ENVIRONMENT=Development
    Environment=DOTNET_PRINT_TELEMETRY_MESSAGE=false

    [Install]

    WantedBy=multi-user.target
    ```

1. The example above uses the `/usr/bin/dotnet` command to start the application. You can change this option if the `dotnet` runtime location is different, or if you have published your application with the `--self-contained` argument. For example:

    ```Console
    ExecStart=/var/www/MainDemo.Blazor.Server/MainDemo.Blazor.Server
    ```

   Make sure that the value of the `WorkingDirectory` option is correct. Otherwise, you may see the following error: "_Could not find 'xaf.focusViewItem' ('xaf' was undefined)_".

    The `User` option specifies a user that manages the service. This user (`www-data` in this example) must exist and have proper ownership of application files.

1. Save the file and enable the service.

    ```Console
    sudo systemctl enable kestrel-maindemo.service
    ```

1. Start the service.

    ```Console
    sudo systemctl start kestrel-maindemo.service
    ```

1. Verify that the service is running.

    ```Console
    sudo systemctl status kestrel-maindemo.service
    ```

    ![DevExpress XAF - The Service Is Running](~/images/deployment-tutorial-linux-service-is-running.png)

[!include[deployment-tutorial-blazor-disclaimer](~/templates/deployment-tutorial-blazor-disclaimer.md)]

## Troubleshooting

If you encounter problems, refer to the following topic: [](xref:113238).

## Additional Resources

Refer to the Microsoft documentation for more information about deploying ASP.NET Core and Blazor applications:

* [Host ASP.NET Core on Linux with Nginx](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx)
* [Host and deploy ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/)
* [Host and deploy server-side Blazor apps](https://learn.microsoft.com/en-us/aspnet/core/blazor/host-and-deploy/server)
