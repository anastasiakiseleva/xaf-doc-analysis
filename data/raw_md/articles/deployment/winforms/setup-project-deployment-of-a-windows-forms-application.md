---
uid: "113235"
seealso:
- linkId: "113033"
- linkId: "113238"
title: Setup Project Deployment of a Windows Forms Application
---
# Setup Project Deployment of a Windows Forms Application

In this lesson, you will learn how to deploy a Windows Forms XAF application using the Setup Project method. You will create a simple installer for the application.

> [!NOTE]
> The **Setup Project** template is no longer included by default with the latest Visual Studio versions. You can download this template from Visual Studio Gallery: [Microsoft Visual Studio 2015 Installer Projects](https://marketplace.visualstudio.com/items?itemName=VisualStudioClient.MicrosoftVisualStudio2015InstallerProjects).

Perform the following steps at the Developer Workstation.

* Right-click the **Solution** item in the **Solution Explorer**. Choose **Add** | **New Project…** in the context menu. In the invoked **Add New Project** dialog window, locate the **Other Project Types** | **Setup and Deployment** node in the **Project types** section. Choose **Setup Project** in the **Templates** section. Enter the required Setup project name. For instance, call it _MySolution.Win.Setup_. Click **OK**.
	
	![Deployment_Tutorial_2010](~/images/deployment_tutorial_2010116481.png)
* Right-click the newly created _MySolution.Win.Setup_ project in the Solution Explorer. In the invoked context menu, choose **Add** | **Project Output…**.
	
	![Deployment_Tutorial_2020](~/images/deployment_tutorial_2020116482.png)
* The **Add Project Output Group** dialog will be invoked. In the **Project** dropdown list, select the Windows Forms application project (e.g. _MySolution.Win_). In the output type list, choose "Primary output" and "Content Files" simultaneously. In the **Configuration** drop-down list, select the Release configuration. Click **OK**. All the dependent assemblies will be added to the Setup project.
	
	![Deployment_Tutorial_2030](~/images/deployment_tutorial_2030116483.png)
* Specify the Setup project properties via the **Properties** window. Set the **Author** property to your name. Set the **Manufacturer** to your company name. Set the **ProductName** to **MySolution**. Set the **RemovePreviousVersions** to **True**. Set the **Title** to **MySolution Setup**.
	
	![Deployment_Tutorial_2040](~/images/deployment_tutorial_2040116484.png)
* Right-click the _MySolution.Win.Setup_ project in the Solution Explorer. In the invoked context menu, choose **View** | **File System**.
	
	![Deployment_Tutorial_2045](~/images/deployment_tutorial_2045116485.png)
* Select the **User's Desktop** item. Right-click the blank space to the right. In the invoked context menu, choose **Create New Shortcut**.
	
	![Deployment_Tutorial_2050](~/images/deployment_tutorial_2050116486.png)
* In the invoked **Select Item in Project** dialog, double-click the **Application Folder** to expand its content. Double-click the **Primary output from MySolution.Win (Active)** item to set it as the shortcut target.
	
	![Deployment_Tutorial_2055](~/images/deployment_tutorial_2055116624.png)
* In the shortcut Properties window, set the **Name** to MySolution.
	
	![Deployment_Tutorial_2060](~/images/deployment_tutorial_2060116487.png)
* If your application is [localized](xref:112595) and uses the [pre-built satellite assemblies](xref:113301), the satellite assemblies should be deployed with the application. So right-click the **Application Folder** item in the **File System** pane and choose **Add** | **Folder**. Set the  name of the new folder to the language culture code (for instance, "de" for the German language). Add the required satellite assemblies to this folder (right-click the folder and choose **Add** | **File…**).
	
	Additionally, the satellite assemblies with your custom localizations made within modules, should be added. Right-click the **Application Folder** item in the **File System** pane and choose **Add** | **Project Output…**. The **Add Project Output Group** dialog will be invoked. In the **Project** dropdown list, select the module project (e.g. _MySolution.Module_). In the output type list, choose "Localized resources". In the **Configuration** drop-down list, select the Release configuration. Click **OK**. All the dependent assemblies will be added to the Setup project. Analogously, add the required localized resources from the platform-specific module.
* Build the _MySolution.Win.Setup_ project.
	
	![Deployment_Tutorial_2070](~/images/deployment_tutorial_2070116488.png)
* After the successful build, check that the _setup.exe_ and _MySolution.Win.Setup.msi_ files exist in the _MySolution\MySolution.Win.Setup\Release_ folder. Copy these files to a location accessible by end-users (e.g. a shared network folder or removable media).

Perform the following steps at each End-User Workstation or at the Terminal Server.

* Ensure that an appropriate version of .NET is installed.
* Launch the _setup.exe_ file as a user with administrative privileges. In the invoked **Open File - Security Warning** dialog, click **Run**.
	
	![Deployment_Tutorial_3010](~/images/deployment_tutorial_3010116489.png)
* In the invoked **MySolution Setup Wizard** click **Next** .
	
	![Deployment_Tutorial_3020](~/images/deployment_tutorial_3020116490.png)
* Select the installation folder, e.g. _C:\Program Files\MySolution_. To install the application for all local users, click **Everyone**. Click **Next**.
	
	![Deployment_Tutorial_3030](~/images/deployment_tutorial_3030116491.png)
* In the invoked confirmation dialog, click **Next**.
	
	![Deployment_Tutorial_3040](~/images/deployment_tutorial_3040116492.png)
* Wait until the installation process finishes.
	
	![Deployment_Tutorial_3050](~/images/deployment_tutorial_3050116493.png)
* Check that the _C:\Program Files\MySolution_ folder contains the application files, and there is a _MySolution_ shortcut located on the Desktop.
* Run the application. If the application displays the following message, it requires a proper connection string in the configuration file, and database accessibility. The [Set Up the Database Connection](xref:113236) lesson describes this issue.
	
	![Deployment_Tutorial_0065](~/images/deployment_tutorial_0065116462.png)

> [!NOTE]
> You can uninstall the Windows Forms application via the **Programs and Features** (**Add or Remove Programs** in Windows XP) Control Panel applet.

If you are deploying your Windows Forms application to the Terminal Server, follow the steps from [Connect Clients to the Terminal Server](xref:113244) lesson, to learn how to provide end-users with access to the application.

Now your application needs a connection to database to run properly. Proceed to the [Set Up the Database Connection](xref:113236) lesson, to learn how to do it. To familiarize yourself with alternative deployment methods, take one of the following lessons.

* [Xcopy Deployment of a Windows Forms Application](xref:113232)
* [Publish Wizard Deployment of a Windows Forms Application](xref:113234)