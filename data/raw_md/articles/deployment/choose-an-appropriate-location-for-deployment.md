---
uid: "113240"
seealso:
- linkId: "113244"
title: Choose an Appropriate Location for Deployment (Windows Forms)
---
# Choose an Appropriate Location for Deployment (Windows Forms)
<!--TODO: rewrite for Winforms and Blazor or IDK -->

This lesson explains how to choose the best location for deploying your Windows Forms application in a production environment.

> [!NOTE]
> The XAF Blazor server application can also be deployed to non-Windows platforms (Linux, Docker, etc.). See topics from the [Deployment - ASP.NET Core Blazor](xref:403362) help section for details.

There are two approaches to providing network users with access to a Windows Forms application:

* Deploy the application to each End-User Workstation.
* Deploy the application to a Terminal Server.

Each approach has its advantages and disadvantages.

## Deploy a Windows Forms Application to Each End-User Workstation
The most common way to deploy a Windows Forms application is to install it on each End-User Workstation. The application files are placed in a folder at each End-User Workstation. For instance, it can be the _C:\Program Files\MySolution_ folder. The following image illustrates the MySolution application installed and running at an End-User Workstation.

![Deployment_Tutorial_0001](~/images/deployment_tutorial_0001116478.png)

This approach requires the application to be deployed to each End-User Workstation. If a workstation goes out of order and an end-user has to use another PC, the application must be redeployed. Each workstation must satisfy the hardware requirements and have Microsoft Windows with an appropriate .NET version installed.

## Deploy a Windows Forms Application to a Terminal Server
If the end-user network has a Terminal Server, you can install your Windows Forms application on it. For instance, it can be a server running Microsoft Windows Server 2008. The server should have the Terminal Services role installed. The following image illustrates the MySolution application running in a remote desktop session.

![Deployment_Tutorial_0002](~/images/deployment_tutorial_0002116479.png)

This method does not require you to deploy the application to each End-User Workstation. End-users can use the application from any workstation. The only two requirements are the capability to run a remote desktop client and network access to the Terminal Server where the application is deployed. Hardware requirements for End-User Workstations are very low - so-called "thin clients" (diskless workstations which boot from the network), inexpensive netbooks or nettops can be used. End-users can use the application remotely via the Internet. Software requirements are also more liberal - every operating system (OS) which has a remote desktop client can be used - GNU/Linux, MacOS, etc. The following image illustrates the MySolution application running in a remote desktop session launched at a non-Windows workstation.

![Deployment_Tutorial_0003](~/images/deployment_tutorial_0003116480.png)

However, there are certain drawbacks associated with this method. First, if the Terminal Server fails, all users will lose access to the application. 
Second, the Terminal Server hardware requirements are also significant. Additionally, the Terminal Server must have a sufficient number of terminal server client licenses.

> [!NOTE]
> It is unsafe to expose the Terminal Server to a public network directly - use Virtual Private Network (VPN) technology to secure remote desktop connections. To reduce network load, the Terminal and Database Servers can be located on the same server.

## Summary
### It is recommended to deploy your Windows Forms application to each End-User Workstation if:

* end users have no Terminal Server;
* it is not required to access the Windows Forms Application remotely;
* end-users work in a homogeneous network - every End-User Workstation has Microsoft Windows installed.
* end-users have workstations with sufficient performance.

### It is recommended to deploy your Windows Forms application to a Terminal Server if:

* end-users have a fast and reliable Terminal Server;
* it is required to access the Windows Forms Application remotely;
* end-users work in a heterogeneous network - various platforms are used (Microsoft Windows, GNU/Linux, Apple MacOS, etc.);
* end-users have low-performance or even diskless workstations (thin clients, netbooks, nettops etc.).

You can combine the deployment approaches described in this topic. The following diagram illustrates one of the possible scenarios.

![Deployment_Tutorial_0000](~/images/deployment_tutorial_0000116467.png)

Here, a Windows Forms application is deployed to the Terminal Server as well as to a group of End-User Workstations. The Terminal Server is accessible from the local network and via Internet. Remote connections are protected by the firewall. The application database is located at the Database Server.

The following step-by-step lessons demonstrate how to deploy an XAF application using different methods.
Choose the most suitable method, and apply it.

* [Xcopy Deployment of a Windows Forms Application](xref:113232)
* [Publish Wizard Deployment of a Windows Forms Application](xref:113234)
* [Setup Project Deployment of a Windows Forms Application](xref:113235)
