---
uid: "113577"
seealso: []
title: Getting Started
---
# Getting Started

## [Video Tutorials & Overview](xref:404219)

Browse video content from our MVPs and evangelists to get a better understanding of XAF usage and functionality.

## [Basic .NET WinForms & Blazor Tutorial (Project Manager)](xref:401943)

The Simple Project Manager demo shows how to use XAF to build an ASP.NET Core Blazor and Windows Forms project management application. XAF facilitates getting started because it ships with a rich set of typical line-of-business functionality packed into built-in modules.

## [In-Depth .NET WinForms & Blazor UI (Employee Manager)](xref:402125)

For more information about XAF features, follow this comprehensive tutorial. It describes how to implement the MainDemo application that ships with XAF (the Blazor version is also available [online](https://demos.devexpress.com/XAF/BlazorMainDemo/)). This tutorial explains how to design a complex business model, extend the default functionality, customize the user interface, use extra modules that ship with XAF, and set up the security system.

 ## [.NET REST Backend / Web API Service](xref:404218)

This tutorial contains step-by-step instructions on how to create an application with the Backend Web API Service.
 
It also introduces our 1-Click Solution for CRUD REST API Services with ASP.NET Core, OData, Swagger, Entity Framework Core, or XPO ORM. The Web API Service generates URLs (endpoints) that allow you to perform CRUD operations from non-XAF UI applications such as .NET MAUI, JavaScript, or Blazor clients.

## [.NET WinForms & Blazor Outlook-Inspired Demo (Multi-Tenancy/SaaS-ready)](xref:404669)

This application serves as the central data management hub for the fictitious company, overseeing various business entities such as Employees, Products, Orders, Quotes, Customers, and Stores. It includes Blazor & WinForms projects powered by the DevExpress [Multi-Tenancy Module](xref:404436).

![Outlook-Inspired Demo Overview](~/images/xaf-outlook-inspired-app-overview.png)

### Demo Source Code

The **OutlookInspiredDemo** solution source code is installed as part of the XAF package and typically located in the following directory:   _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\Components\XAF\OutlookInspiredDemo.NET.EFCore\CS\_.

### Run the Application from the Demo Center

You can run the **OutlookInspiredDemo** application from the Demo Center as follows: 

1. Open the Demo Center. Select **Cross-Platform .NET APP IU** and click the **Outlook Inspired App** block.

   ![Demo Center](~/images/xaf-demo-center-outlook-inspired-app.png)

When first launching the application, log in with the **Admin** account and a blank password to access the Host User Interface, where you can manage tenants. The application creates two tenants: **company1.com** and **company2.com**. You can view the tenant list in the Host User Interface List View.

After the Host Database is initialized, you can log in to the Tenant User Interface using one of the following Tenant Administrator accounts: **Admin@company1.com** or **Admin@company2.com** and a blank password. A Tenant Administrator has full access to all data stored in the Tenant Database, but no access to other Tenant data. Users and permissions are managed for each tenant independently.

The application also creates users with restricted access in each tenant, such as **clarkm@company1.com**.

> [!NOTE]
> We recommend that you use **Entity Framework Core** for data access in all new projects. For additional information, refer to the following topic: <xref:404186>.

## Employee Management Demo (XPO/EF Core)

This demo allows you to store contacts, tasks, events, reports and other related data. It includes reusable XAF modules such Reports, Office, Scheduler, View Variants, PivotChart, AuditTrail, FileAttachments. The EF Core Blazor version is available [online](https://demos.devexpress.com/XAF/BlazorMainDemo/).

### Demo Source Code

The **Main Demo** solution source code is installed as part of the XAF package and typically located in the following directories:

* **MainDemo.NET.EFCore:** _[!include[](~/templates/path-to-main-demo-ef-core.md)]\CS\_
* **MainDemo.NET.XPO:** _[!include[](~/templates/path-to-all-xaf-demos.md)]\MainDemo.NET.XPO\CS\_

## Feature Center Demo (XPO)

This demo has been designed to help you quickly get acquainted with the eXpressAppFramework and start using it effectively. If you are new to the eXpressApp Framework, you can get a glimpse of various features offered by XAF. Each individual demo shows off some particular XAF feature and comes with a description of that functionality. If you are a seasoned XAF developer, this demo can prove valuable to you too. You can refer to this demo's source code to see how some specific behavior can be implemented.

The Blazor version is available [online](https://demos.devexpress.com/XAF/featurecenter).

### Demo Source Code

The **FeatureCenter.NET.XPO** solution source code is installed as part of the XAF package and typically located in the following directory: _[!include[](~/templates/path-to-feature-center.md)]\CS\_.


