---
uid: "404449"
title: Get Started with Web API Service
seealso:
- linkId: "403401"
- linkId: "403561"
---

# Get Started with Web API Service

We ship the Web API Service as a part of the [DevExpress Unified Component Installer](xref:15615). You can use the DevExpress [Template Kit](xref:405447) to create new solutions in a configuration that meets your requirements. This article describes steps that you should follow to prepare your development environment so you can start your new project with the Web API Service.

Also see the [FAQ](xref:403394#faq) to find answers to some of the questions that you may have as you explore the Web API Service's functionality.

## Prerequisites

To install and use the Web API Service, ensure that the following software is installed on your development machine:

- [Visual Studio 2022 v17.0+](https://visualstudio.microsoft.com/vs/)
- [.NET SDK 8.0+](https://dotnet.microsoft.com/en-us/download/dotnet)

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
