---
uid: '401253'
title: Migration to .NET from .NET Framework in v25.2+
seealso:
- linkType: HRef
  linkId: https://dotnet.microsoft.com/en-us/platform/modernize
  altText: Modernize .NET apps effortlessly with GitHub Copilot
- linkType: HRef
  linkId: https://techcommunity.microsoft.com/blog/appsonazureblog/start-your-cloud-journey-with-azure-app-service/3804037
  altText: Start Your Cloud Journey with Azure App Service
- linkType: HRef
  linkId: https://www.youtube.com/playlist?list=PLdo4fOcmZ0oWiK8r9OkJM3MUUL7_bOT9z
  altText: Migrating from ASP.NET to ASP.NET Core tutorial playlist on YouTube
- linkType: HRef
  linkId: https://github.com/Azure/reliable-web-app-pattern-dotnet
  altText: Reliable web app pattern for .NET on GitHub
---
# Migration to .NET from .NET Framework in v25.2+

XAF v25.2 introduces many changes. Before upgrading, you need to make specific changes to your application in v25.1. The migration process has several steps: you can use the **XafApiConverter** tool to automate some tasks and simplify the update, but manual code review and adjustments are still required.

## Prerequisites

Ensure that the following components are installed on your machine:

* [DevExpress Universal Subscription](https://www.devexpress.com/Subscriptions/Universal.xml) v25.1 and v25.2 or [DevExpress NuGet feed](xref:116042). 
* [.NET 8+ SDK and runtime](https://dotnet.microsoft.com/en-us/download/dotnet)
* [Visual Studio 2022](https://visualstudio.microsoft.com/)

## What Has Changed in XAF v25.2

The major changes are listed below. For the complete list of removed APIs, refer to the following knowledge base article: [XAF - Legacy .NET Framework (WinForms and ASP.NET WebForms) APIs, .NET-based API/Modules, and Security System have been removed from distribution](https://supportcenter.devexpress.com/ticket/details/t1312589/xaf-legacy-net-framework-winforms-and-asp-net-webforms-apis-net-based-api-modules).

* End of .NET Framework support
* End of Entity Framework 6 (EF6) support
* The following modules have been removed from XAF:
    * Maps (DevExpress.ExpressApp.Maps.Web)
    * KPI (DevExpress.ExpressApp.Kpi)
    * Script Recorder (DevExpress.ExpressApp.ScriptRecorder)
    * Pivot Chart (DevExpress.ExpressApp.PivotChart.Web)
    * Workflow (DevExpress.ExpressApp.Workflow)
* Security System, which includes built-in user and role types other than `PermissionPolicyUser` and `PermissionPolicyRole` or the legacy SHA-512 password hashing algorithm has been deprecated
* Built-in business classes have been removed

## The New DevExpress Cross-IDE Template Kit

The legacy Solution Wizard no longer allows you to create new XAF project and item templates. Instead, use the new DevExpress Template Kit that is now automatically added as a Visual Studio extension by our [Unified Component Installer](xref:15615).

* To access the **DevExpress Template Kit** for project templates, select **File** → **New** → **Project…** in Visual Studio 2022+.
* To access the **DevExpress Template Kit** for item templates, invoke the context menu in Solution Explorer and select **Add** | **New Item…**

For additional information, refer to the following help topic: [Template Kit](xref:405447).

![DevExpress Template Kit](~/images/template-kit/template-kit-create-a-new-project.png)

> [!NOTE]
> The new Template Kit also supports Rider and VS Code.

## The XafApiConverter Tool

We developed a tool designed for those migrating an XAF application to v25.2+. It automates the following routine migration tasks:

* Updates legacy security APIs.
* Removes .NET Framework APIs, and legacy .NET-based APIs and modules.
* Converts an application from .NET Framework to .NET.

You can find the tool source code in the following GitHub repository: [XafApiConverter](https://github.com/DevExpress-Examples/XafMigrationTools/tree/25.2.3%2B/XafApiConverter). Refer to the repository description for additional information about the **XafApiConverter** tool.

## Upgrade Scenarios

See the following help topics for information on the corresponding upgrade scenarios:

* <xref:405693>
* <xref:405736>
* <xref:401264>