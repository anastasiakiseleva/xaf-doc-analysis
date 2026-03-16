---
uid: "405447"
title: 'Cross-IDE Template Kit (Windows, macOS)'
---
# Cross-IDE Template Kit (Windows, macOS)

## Visual Studio 2022/2026 Integration (for Windows)
The DevExpress Template Kit allows you to create a new project or project item in just a few steps. The [DevExpress Unified Component Installer](xref:15615) automatically adds this kit as a Visual Studio extension. If you do not use the installer or are working in VS Code or JetBrains Rider, you can install the kit manually.

* [Install the Template Kit on Windows Manually (w/o .NET Installer)](#install-the-template-kit-on-windows-manually-wo-net-installer)
* [Visual Studio Code Integration (for Windows or macOS)](#visual-studio-code-integration-for-windows-or-macos)
* [JetBrains Rider Integration (for Windows or macOS)](#jetbrains-rider-integration-for-windows-or-macos)


DevExpress Template Kit for Visual Studio includes the following template types:

* **Project template** allows you to create XAF-powered projects.
* **Item templates** allow you to add new items to your application, such as business objects, controllers, and templates.

![Template Kit](~/images/template-kit/template-kit-introduction.png)

### Create a New Project

To create a new project, follow the steps below:

1. In Visual Studio, select **File** → **New** → **Project…**
1. In the **Create a new project** window, select **DevExpress <:xx.x:> Template Kit** and click **Next**.

    ![Create a new project window](~/images/template-kit/template-kit-create-a-new-project.png)

1. Specify the project name and location, and click **Create**. 
1. In the invoked Template Kit window, select the **XAF** platform, configure project parameters, and click **CREATE PROJECT**.

    ![Create a new project window](~/images/template-kit/template-kit-create-xaf-project.png)

### Create a New Item

The Template Kit allows you to add the following items in an XAF application:

* EF Core, XPO, and Non-Persistent [Business Objects](xref:113664)
* View and Window [Controllers](xref:112621)
* [Blazor Templates](xref:403450)
* [WinForms Templates](xref:403446)

To create a new item, follow the steps below:

1. Invoke context menu in Solution Explorer. Select **Add | New Item…** or **Add | Class…**

    ![Visual Studio - Solution Explorer Context Menu](~/images/template-kit/template-kit-add-new-item.png)

1. In the opened dialog, select **DevExpress <:xx.x:> Template Kit**, specify the item name, and click **Add**.

    ![Visual Studio - Add New Item Dialog](~/images/template-kit/template-kit-add-new-item-dialog.png)

1. In the **XAF** platform section, select an item to add  and click **ADD ITEM**.

    ![XAF - Select Item Template Dialog](~/images/template-kit/template-kit-add-view-controller.png)

### Install the Template Kit on Windows Manually (w/o .NET Installer)

The **DevExpress Template Kit for Visual Studio** is available as a VSIX extension based on the dotnet CLI. You can install the extension for Visual Studio in the following ways:

* [Use Extension Manager](https://learn.microsoft.com/en-us/visualstudio/ide/finding-and-using-visual-studio-extensions#use-extension-manager).
* Download the extension at the following link: [DevExpress Template Kit for Visual Studio](https://go.devexpress.com/DevExpress_Template_Kit_VisualStudio.aspx). Once ready, [install extensions without using Extension Manager](https://learn.microsoft.com/en-us/visualstudio/ide/finding-and-using-visual-studio-extensions#install-extensions-without-using-extension-manager).

## Visual Studio Code Integration (for Windows or macOS)

In Visual Studio Code, open the **Extensions** tab, find the **DevExpress Template Kit for VS Code**, and click **Install**.

![Template Kit in VS Code](~/images/template-kit/template-kit-vs-code-extension.png)

To run the Template Kit, follow the steps below:

1. Ensure that no folder is open in VS Code. In the **Explorer** tab, click the **New DevExpress Project** button:

    ![New DevExpress Project button](~/images/template-kit/template-kit-vs-code-create-project.png)

1. Specify the project name and press <kbd>Enter</kbd>.
1. Select a project location and click the **Select Folder** button.
1. In the invoked Template Kit window, select the **XAF** platform, configure project parameters, and click **CREATE PROJECT**.

>[!Tip]
> You can use [.NET CLI Integration](xref:404967) to install DevExpress XAF project templates and create XAF ASP.NET Core Blazor, Web API Service, and Windows Forms applications from the console.

## JetBrains Rider Integration (for Windows or macOS)

You can download the **DevExpress Template Kit** plugin for Rider at the following link: [DevExpress Template Kit plugin for Rider](https://go.devexpress.com/DevExpress_Template_Kit_Rider.aspx). Once ready, [install the plugin from disk](https://www.jetbrains.com/help/rider/Managing_Plugins.html#install_plugin_from_disk).

To create a new project, follow the steps below:

1. Click the **New Solution** button.
1. Select **DevExpress Template Kit** in the **Other** category and click **Create**.

    ![Create New Solution window in Rider](~/images/template-kit/template-kit-new-solution-in-rider.png)

1. In the invoked Template Kit window, select the **XAF** platform, configure project parameters, and click **CREATE PROJECT**.

## Build the Project

Install DevExpress component packages to build your project. You can use the [DevExpress Unified Component Installer](xref:15615) that adds a local NuGet feed to your machine.

As an alternative to the installer, you can configure a personal DevExpress NuGet Feed that loads the required packages from the [DevExpress NuGet Gallery](https://nuget.devexpress.com/). To do this, follow the instructions below:

1. [Obtain your NuGet feed URL.](xref:116042)
2. Register the source. You can do this in your IDE or from a CLI:
    
    * [Visual Studio for Windows](xref:116698#visual-studio-for-windows)
    * [JetBrains Rider](xref:116698#jetbrains-rider-macos-windows-linux)
    * [Visual Studio Code](xref:116698#visual-studio-code-vs-code)
    * [CLI](xref:117209)
3. [Register your .NET license key.](xref:405494#online-nuget-feeds-cicd-and-other-installation-methods-windows-macos-linux)