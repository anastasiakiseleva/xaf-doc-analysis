---
uid: "113232"
seealso:
- linkId: "113033"
- linkId: "113238"
title: Xcopy Deployment of a Windows Forms Application
---
# Xcopy Deployment of a Windows Forms Application

In this lesson, you will learn how to deploy a Windows Forms XAF application using the Xcopy Deployment method. This method is named after the **xcopy** command-line utility, which copies files from one location to another. With this method, you copy the application files from the Developer Workstation to a location accessible to end-users.  
Instead of the **xcopy** utility, you can use Windows Explorer or another file manager to copy files. However, in certain cases, the command-line utility may be more convenient than graphical user interface (GUI) tools. To learn more about the **xcopy** command capabilities, refer to the [xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy) document.

Perform the following steps at the Developer Workstation to prepare the Windows Forms application for Xcopy Deployment.

* Open the _MySolution_ solution in Visual Studio. In the Solution Explorer, expand the _MySolution.Win\References_ folder. Select assemblies whose names start with _"DevExpress"_. If you use Entity Framework, third-party controls or modules, select their assemblies as well. In the Properties window, set the **CopyLocal** property to **True**.
	
	![Deployment_Tutorial_0010](~/images/deployment_tutorial_0010116453.png)
	
	Repeat this step for all module projects that are referenced in the application project (e.g. _MySolution.Module_ and _MySolution.Module.Win_ if exists).
* Change the Active Solution Configuration from **Debug** to **Release**.
	
	![Deployment_Tutorial_0020](~/images/deployment_tutorial_0020116454.png)
* Build and run the Windows Forms application.
* Check to make sure that the application performs correctly and close it.
* Ensure that the _MySolution\MySolution.Win\bin\Release_ folder contains application files.
	
	![Deployment_Tutorial_0025](~/images/deployment_tutorial_0025116455.png)

Now, the Windows Forms application is ready for Xcopy Deployment.

Perform the following steps at an End-User Workstation or at a Terminal Server.

* Ensure that an appropriate version of .NET is installed.
* Create an application folder. For instance, it can be _C:\Program Files\MySolution_. Copy the _MySolution\MySolution.Win\Bin\Release_ folder contents from the Developer Workstation to the newly created directory via the network or using removable media.
	
	![Deployment_Tutorial_0030](~/images/deployment_tutorial_0030116458.png)
	
	As a Windows Forms application project may have references to several module projects (e.g. MySolution.Module.Win and MySolution.Module), then it is required to deploy referenced assembles of these modules. Copy required assemblies from output folders of module projects (i.e. _MySolution\MySolution.Module.Win\Bin\Release_ and _MySolution\MySolution.Module\Bin\Release_). You can skip overwriting files that are copied already.
* If the application is [localized](xref:112595), and [pre-built satellite assemblies](xref:113301) are used in it, do the following.
	
	1. Create a subfolder in the application folder. The subfolder name should be the language culture code (for instance, "de" for the German language).
	2. Copy the required satellite assemblies to the subfolder.
	3. Check to make sure that the target language is added to the application configuration file (_MySolution.Win.exe.config_)
		
		# [XML](#tab/tabid-xml)
		
		```XML
		<appSettings>
		    <!-- ... -->
		    <add key="Languages" value="en;de" />
		    <!-- ... -->
		</appSettings>
		```
		
		***
		
		The supported languages are specified via the **Languages** key. This key value consists of supported language codes, separated by semicolons.
	
	If there are several localization languages, repeat these steps for each language.
* Create a desktop shortcut to the _C:\Program Files\MySolution\MySolution.Win.exe_ file. Name it _MySolution_.
* Run the application by double-clicking the _MySolution.Win.exe_ file or its shortcut. If the following error message stating that an assembly is missing is displayed, then the reported assembly was not copied to the _Release_ folder from the Developer Workstation Global Assembly Cache (GAC).
	
	![Deployment_Tutorial_0040](~/images/deployment_tutorial_0040116459.png)
	
	To resolve this error, copy the required assembly to the application folder on the target computer. There are two locations on the Developer Workstation where you can get the required assembly.
	
	* _[!include[PathToXafDlls](~/templates/path-to-xaf-dlls.md)]_
	* _[!include[PathToDxInstallation](~/templates/path-to-installation.md)]Bin_
	
	> [!NOTE]
	> You can register the required assembly in the [Global Assembly Cache](https://learn.microsoft.com/en-us/dotnet/framework/app-domains/gac), instead of copying it to the application folder.
	
	Run the application once again, and determine if there is another missing assembly. Copy it from the Developer Workstation. Repeat the process until there are no error messages concerning missing assemblies.
	
	Note that an error message may look like the following.
	
	![Deployment_Tutorial_0050](~/images/deployment_tutorial_0050116460.png)
	
	The cause of this error is also a missing assembly, but it is not clear which assembly is missing. To find out which assembly it is, open the application log file. This is a text file located in the application folder or in the user's application data folder, and has the most recent modification time. Find the text matching the error message and analyze what happened before the error.
	
	![Deployment_Tutorial_0060](~/images/deployment_tutorial_0060116461.png)
	
	As you can see in the image, in this instance the application was trying to load an assembly when the error occurred. So, it should be copied from the Developer Workstation.
	
	> [!NOTE]
	> Only run-time assemblies from the Developer Workstation are required. Ensure that you do not accidentally copy design-time assemblies or XML files that are named identically to the run-time assemblies.
* Finally, the application will display the following message.
	
	![Deployment_Tutorial_0065](~/images/deployment_tutorial_0065116462.png)
	
	It means that all assembly requirements are satisfied and the application now requires a proper connection string in its configuration file, as well as access to its database. The [Set Up the Database Connection](xref:113236) lesson describes how to resolve this issue.

> [!NOTE]
> If you experience problems performing any steps of this lesson, refer to the [Deployment Troubleshooting Guide](xref:113238) lesson.

Copy the _C:\Program Files\MySolution_ folder and the _MySolution_ desktop shortcut to each of the remaining End-User Workstations, if necessary. If you are deploying a Windows Forms application to the Terminal Server, follow the steps from the [Connect Clients to the Terminal Server](xref:113244) lesson.

Now your application needs a connection to a database to run properly. Proceed to the [Set Up the Database Connection](xref:113236) lesson to learn how to do it. To familiarize yourself with alternative deployment methods, take one of the following lessons.

* [Publish Wizard Deployment of a Windows Forms Application](xref:113234)
* [Setup Project Deployment of a Windows Forms Application](xref:113235)
