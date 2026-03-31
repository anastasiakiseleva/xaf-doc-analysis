---
uid: "112691"
seealso: []
title: Deployment
---
# Deployment

In addition to building XAF business applications, you should be familiar with appropriate methods for deploying and updating these applications. For this purpose, you may need to use configuration settings that differ from the ones applied for such application compilation modes as debugging, testing, etc. Topics in this help section will explain how to modify configuration files easily, and describes approaches to deploy XAF applications.

> [!NOTE]
>
> Single-file deployment and executable option ([`<PublishSingleFile>`](https://docs.microsoft.com/en-us/dotnet/core/deploying/single-file)) is not supported in ASP.NET Core Blazor, WinForms, and Web API applications.

## Deployment Tutorial -- Overview

The aim of these topics is to deploy an XAF application in a production environment. It is assumed that you have already reviewed the [In-Depth .NET WinForms & Blazor UI (Employee Manager)](xref:402125). In this section, you will learn how to deploy the application you developed. Most of the lessons in this section refer to the simple application (called _MySolution_) you developed in the previous lessons in the XAF Tutorial. Microsoft SQL Server is used as the database management system (DBMS). However, you can use any XAF application, such as the demo application that ships with XAF, or your custom application. You can also use any DBMS supported by XAF.

> [!NOTE]
> Use the [Assembly Deployment Tool](xref:17237) to analyze your project and obtain the list of assemblies you should deploy. Compare the assemblies the tool identifies to the redistributable assemblies list available in the [End User License Agreement](xref:2218) (EULA).

In a typical production environment, there are a number of computers playing various roles. Throughout this tutorial we use the following naming conventions:

* **Developer Workstation** - a PC with Microsoft Visual Studio and XAF installed. For instance, it can be your own workstation.
* **End-User Workstation** - one or more PCs with neither Microsoft Visual Studio nor XAF installed. Your aim is to deploy the XAF application to these workstations.
* **Database Server** - a server in which a DBMS is installed. Generally, End-User Workstations must have network access to this server.
* **Web Server** - a server in which Microsoft Internet Information Services (IIS) are installed. This server must have network access to the Database Server and be accessible from the end user's local network or via the Internet, if required.
* **Terminal Server** - a server in which Microsoft Terminal Services are installed. This server must have network access to the Database Server and be accessible from the end user's local network or via the Internet, if required.

> [!NOTE]
> The Database, Web and Terminal Servers may be physically located on the same server.

## Deployment Tutorial -- Lessons

* [Choose an Appropriate Location for Deployment](xref:113240)
	
	This lesson helps you to decide where to deploy your Windows Forms application (to each End-User Workstation or to a Terminal Server).

* Deploy an XAF ASP.NET Core Blazor UI, Middle Tier Server, and Web API Service Applications

	* [Deploy a XAF ASP.NET Core Application to IIS](xref:404613)
	* [Deploy a XAF ASP.NET Core Application to Azure App Service](xref:404614)
	* [Deploy a XAF ASP.NET Core Application to Linux with Nginx](xref:404717)
	
* Deploy an XAF WinForms Applications

	* [](xref:113232)
	* [](xref:113234)
	* [](xref:113235)
	
* [](xref:113236)
	
	Instructions on how to connect your application to a Database Server and create the initial database. Information on how to resolve database and application version mismatches is also included.
* [](xref:113237)
	
	An introduction to database security. This lesson shows how to grant access to an application database only to your XAF application users.
* [](xref:113244)
	
	Instructions on how to connect remote desktop clients to the Terminal Server with the Windows Forms application installed.
* [](xref:113239)
	
	You will learn how to update your application.

If you do not have access to a real production environment but still want to perform this tutorial for training purposes, you can use the DBMS and Web Server installed in the Developer Workstation. In this case, we recommend that you create a virtual LAN using virtualization software so that you can perform all of the steps described in the tutorial.

To begin, refer to the [Choose an Appropriate Location for Deployment](xref:113240) topic.

## Troubleshooting Guide

If you run into an issue when deploying an XAF application, take a look at the [Deployment Troubleshooting Guide](xref:113238) help topic. The topic provides a list of common deployment problems and ways of resolving them.

## General Deployment Information

The following topics provide general information on XAF applications deployment.

* [](xref:112693)
* [](xref:113239)
* [](xref:113033)
* [](xref:403362)

## Community Content
* [Deploying XAF to Windows Azure](https://community.devexpress.com/blogs/xaf/archive/2011/05/26/deploying-xaf-on-windows-azure.aspx)
