---
uid: "404449"
title: Get Started with Web API Service
seealso:
- linkId: "403401"
- linkId: "403561"
---

# Get Started with Web API Service

We ship the Web API Service as a part of the DevExpress Unified Component Installer. You can use the DevExpress [Template Kit](xref:405447) to create new solutions in a configuration that meets your requirements. This article describes steps that you should follow to prepare your development environment so you can start your new project with the Web API Service.

Also see the [FAQ](xref:403394#faq) to find answers to some of the questions that you may have as you explore the Web API Service's functionality.

## Prerequisites

To install and use the Web API Service, ensure that the following software is installed on your development machine:

- [Visual Studio 2022 v17.0+](https://visualstudio.microsoft.com/vs/)
- [.NET SDK 6.0+](https://dotnet.microsoft.com/en-us/download/dotnet)

We also require one of the following licenses to be registered in your account at [devexpress.com](https://www.devexpress.com/):

- [DevExpress Universal Subscription](https://www.devexpress.com/subscriptions/universal.xml) or [Free 30-day trial of DevExpress .NET products](https://www.devexpress.com/products/try/)
- [Free .NET App Security & Web API Offer from DevExpress](https://www.devexpress.com/products/net/application_framework/security-web-api-service.xml)

The free offer includes the basic functions of our Web API Service (including the [Template Kit](xref:405447)). To register your free copy today, please visit our offer page: [.NET App Security & Web API – Free Offer from DevExpress](https://www.devexpress.com/security-api-free/).

Watch the following video for information on how to register our free .NET App Security & Web API Service offer and install the required tools on your development machine:

> [!video https://www.youtube.com/embed/T7y4gwc1n4w]

## Install DevExpress Products and Use the Template Kit to Start a new Project (Recommended)

1. Download your copy of the DevExpress Unified Component Installer. Log in to your account at [devexpress.com](https://www.devexpress.com), navigate to the [Download Manager](https://www.devexpress.com/ClientCenter/DownloadManager/) page, and click the download link for the _Unified Component Installer_. 

    ![Download Unified Component Installer](~/images/component-installer-download.png)

2. Run the installer, make sure that the **.NET APP Security & Web API Service** option is checked on the product selection page, and proceed through the installation process.

    ![Unified Component Installer](~/images/component-installer-web-api.png)

3. Run the DevExpress [Template Kit](xref:405447) from the Visual Studio _Create a new project_ dialog and select the XAF platform. In the **Blazor / Web API Service Options** section, specify whether to host the Web API Service as part of a Blazor Server project or as a standalone ASP.NET Core project. Specify other project options and click **Create Project**. 

    See the following topic for detailed information on how to use the [Template Kit](xref:405447) to configure and create a new Web API solution: [](xref:403401).

    ![Template Kit - Enable Web API Service](~/images/template-kit/template-kit-security-standard-906.png)

## Register the DevExpress NuGet Gallery Remote Feed (Advanced)

DevExpress NuGet Gallery is a remote NuGet feed that hosts DevExpress libraries in a centralized manner. This remote feed complements the local installation with the following additional benefits:

- With the remote NuGet feed, you do not need to update your installation of DevExpress controls to get the latest versions of packages available with your license. You can just use the NuGet Package Manager or .NET CLI to update the packages in your solution.

- If you only want to use a subset of DevExpress libraries in your project (for example, the XAF Security System) and do not require the Template Kit to generate a solution, you can install the required NuGet packages from the remote feed and add the required boilerplate code manually. The following example solution covers this usage scenario: [Role-based Access Control, Permission Management, and OData / Web / REST API Services for Entity Framework and XPO ORM - Blazor Server App](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/23.1.1%2B/EFCore/ASP.NetCore/Blazor.ServerSide)

    > [!TIP]
    > If you choose to use one of our example solutions on GitHub as a starting point for your new project, you do not need the local installation. The required packages will be restored from the remote feed.

Follow the steps below to obtain and register your personalized NuGet feed URL.

1. Go to [https://nuget.devexpress.com/](https://nuget.devexpress.com/) and click _"Obtain Feed URL"_.

    ![Obtain Feed URL](~/images/register-nuget-obtain-url.png)

2. You will be navigated to the feed URL that contains your personal key. Click _"Copy to Clipboard"_.

    ![Copy Feed URL](~/images/register-nuget-copy-url.png)

3. To register the feed URL, open the Visual Studio _Options_ dialog, navigate to the _NuGet Package Manager_ | _Package Sources_ view and click the `+` button. Select the added entry and paste the feed URL into the _Source_ input field.

    ![Register NuGet in Visual Studio](~/images/register-nuget-vs-options.png)
