---
uid: '400081'
title: Designers Troubleshooting Guide
---
# Designers Troubleshooting Guide

This topic describes how to resolve problems that can occur when you open [Model Editor](xref:112830) or Visual Studio designers. 

## Main Approach

Perform the following steps if you have problems with a designer:

1. Close opened windows with the designers in Visual Studio.

2. Close Visual Studio.

3. Remove the contents of the _bin_ and _obj_ directories in each project and the _.vs_ folder in the solution.

4. [Run Visual Studio as an administrator](https://learn.microsoft.com/en-us/visualstudio/ide/user-permissions-and-visual-studio#run-visual-studio-as-an-administrator).

5. Build your solution and ensure that the build succeeded.

Open the designer again. Refer to the following section if it still throws an error:

## Additional Approaches

### Common Designers Issues

#### A designer throws the "_Dictionary already contains class info_" error.

Solution:
* If you use .NET, use project-to-project references instead of file assembly references for projects in an XAF solution. Microsoft recommends this to manage references in a project and our Model Editor requires [project-to-project references](https://learn.microsoft.com/en-us/visualstudio/ide/managing-references-in-a-project#project-to-project-references) to collect accurate dependency information.

***

#### You receive the "_Package Load Failure_" error when you load a designer. 

Solution: Close Visual Studio and navigate to the folder where its executable (_devenv.exe_) is located: 

* VS 2015: _%ProgramFiles%\Microsoft Visual Studio 14.0\Common7\IDE\_
* VS 2017: _%ProgramFiles%\Microsoft Visual Studio\2017\Professional\Common7\IDE\_
* VS 2019: _%ProgramFiles%\Microsoft Visual Studio\2019\Professional\Common7\IDE\_

After that, execute the following command in the command prompt: 

> devenv /ResetSkipPkgs

It is also possible that extensions do not load because the Visual Studio component's cache is corrupted. Clear the cache as described in the following articles:

* [Clear Visual Studio Component Cache](https://github.com/Codealike/Codealike-KnowledgeBase/blob/main/clear-visual-studio-component-cache.md)
* [Clear MEF Component Cache](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.ClearMEFComponentCache)

### Model Editor Issues

#### Model changes are shown as a plain XML instead of in the designer.

Solution #1: Refer to [the previous solution](#you-receive-the-package-load-failure-error-when-you-load-a-designer). See the following solution if the Model Editor still does not work. 

Solution #2:

Ensure the **DevExpress.ExpressApp.Design.NetCorePackage** extension is enabled. To do this, click the **Extensions** | **Manage extensions** menu item, and in the invoked window, click the **Enable** button (if the extension is disabled). Restart Visual Studio.

![extensions-and-updates-core-package](~/images/extensions-and-updates-core-package-net-core.png)

You can disable this extension when you received the following notification:

![visual-studio-extension-notification](~/images/visual-studio-extension-notification.png)

We recommend that you do not disable DevExpress extensions as this may cause functionality issues.

This extension can be disabled due to a corrupted installation. Refer to the articles below for more information.

* [Extensions get automatically disabled when starting VS 2015](https://github.com/madskristensen/BundlerMinifier/issues/214)
* [Web Essentials disabled on VS 2015 start](https://github.com/madskristensen/WebEssentials2013/issues/1959)

Solution #3: Ensure that the ["Subtype Designer" is added unnecessarily to xml-based files like csproj](https://developercommunity.visualstudio.com/content/problem/204355/subtype-designer-is-added-unnecessarily-to-xml-bas.html) issue is fixed in the version of Visual Studio you use. Otherwise, update your IDE.

***

#### Your Model changes are contained in the XAFML file, but are not applied to an application or higher level modules.

Solution: Ensure that: 
* the _Model.DesignedDiffs.xafml_ file's **Build Action** is set to **EmbeddedResource**;

    ![xafml-build-action](~/images/xafml-build-action.png)

* your changes are not overridden in higher application model layers. For example, if you customized the Model in a platform-agnostic module (_MySolution.Module_), check the _Model.DesignedDiffs.xafml_ or _Model.xafml_ files of your platform-dependent module and project, respectively. 

***

#### You have one of the following issues in a .NET project:
* The Model Editor frame was created, but showed errors inside.
* The Model Editor frame was not created.
* You received **NotImplementedException**.
* You received the "The operation could not be completed" error.

Solution: Follow the steps below to collect diagnostic information and send it to DevExpress Support.

1. Close your Visual Studio, navigate to `%USERPROFILE%\AppData\Roaming\eXpressAppFramework\`, and archive the folder content.
2. If the Model Editor frame was not created or you received **NotImplementedException** or "The operation could not be completed" errors, collect the inner exception message and callstacks using another Visual Studio instance. The following article describes how to do this: [How to obtain a design-time exception call stack](xref:403685#get-exception-call-stack-of-design-time-errors-in-visual-studio). 
3. Create a new Support Center ticket ([https://supportcenter.devexpress.com/ticket/create](https://supportcenter.devexpress.com/ticket/create)) and attach the resulting diagnostic information as well as screenshots showing the exact steps to reproduce, the actual and expected results, your Visual Studio "About" information, and the CSPROJ/VBPROJ of the projects you tested. Optionally, attach a small debuggable sample where this behavior can be reproduced in a stable manner.

### Other Issues

#### You received any other errors. 

Solution: Debug Visual Studio where designers are opened as described in the [How to obtain a design-time exception call stack](xref:403685#get-exception-call-stack-of-design-time-errors-in-visual-studio) KB Article.

***

#### You did not find an appropriate solution in this topic. 

Solution: Close Visual Studio and rerun the DXperience installation in the **Repair** mode. 

> [!Important]
> Do not start Visual Studio until the installation is completed.

If designers still do not work, [submit a support ticket](https://supportcenter.devexpress.com/ticket/create) and attach the [Visual Studio Activity Log](https://devblogs.microsoft.com/visualstudio/troubleshooting-extensions-with-the-activity-log/) and [DevExpress installation log](xref:403007).
