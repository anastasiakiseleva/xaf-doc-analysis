---
uid: "113244"
seealso:
- linkId: "113238"
  linkId: "405538"
  altText: DevExpress WinForms Troubleshooting - Application Performance
title: Connect Clients to the Terminal Server   
---
# Connect Clients to the Terminal Server

In this lesson, you will learn how to connect remote desktop clients to the Terminal Server where your Windows Forms application is deployed. It is assumed that the Terminal Server is up and running. Otherwise, refer to the Windows Server documentation to learn more about the Terminal Services role. Skip this lesson if you are not deploying a Windows Forms application to the Terminal Server, and refer to the [Application Update](xref:113239) lesson to learn how to update the application.

Perform the following steps at one of the End-User Workstations.

* Run the **Remote Desktop Connection** program. Typically, it is located in the **All Programs** | **Accessories** menu. It can also be launched from the Command Prompt via the **mstsc** command. In the **Remote Desktop Connection** window, click **Options**.
	
	![Deployment_Tutorial_9010](~/images/deployment_tutorial_9010116494.png)
* In the **General** tab, specify the Terminal Server name or its IP address.
	
	![Deployment_Tutorial_9020](~/images/deployment_tutorial_9020116495.png)
* In the **Display** tab, specify the desired remote desktop size and color depth.
	
	![Deployment_Tutorial_9030](~/images/deployment_tutorial_9030116496.png)
* In the **Programs** tab, specify the path to your application executable in the Terminal Server file system.
	
	![Deployment_Tutorial_9040](~/images/deployment_tutorial_9040116497.png)
* Go back to the **General** tab and click **Save As…**. Set **Desktop** as the folder and _MySolution_ as the file name. Click **Save**, and close the **Remote Desktop Connection** window.
* Double-click the newly created _MySolution.rdp_ file located on the Desktop. In the invoked **Windows Security** window, enter the credentials valid at the Terminal Server and click **OK**. The Remote Desktop Client will perform the connection to the Terminal Server. The Windows Forms application will be launched in a Remote Desktop session.
	
	![Deployment_Tutorial_9050](~/images/deployment_tutorial_9050116498.png)
	
	The remote Windows Forms application functionality is exactly the same as the local Windows Forms application functionality.
	
	> [!NOTE]
	> The application launched in a Remote Desktop session prints documents to printers available on the Terminal Server, and saves files to the Terminal Server file system. To make a local printer and the file system available, additional configuration is required. Check out the **Local Resources** tab in the **Remote Desktop Connection** window.

Copy the _MySolution.rdp_ file to each of the remaining End-User Workstations.

> [!NOTE]
> If there are branded thin clients to be connected to the Terminal Server, refer to their installation manual. If there are non-Windows workstations to be connected, refer to their OS documentation to find out how to connect them to a Windows terminal server. Most Unix-like systems have the **rdesktop** command-line utility for this purpose. The following command initiates a remote desktop connection to **MyTerminalServer** as the **Sam** user, sets remote desktop resolution to **800x600** and color depth to **24** bits:
>
> ``rdesktop MyTerminalServer -u Sam -g 800x600 -a 24``

Proceed to the [Application Update](xref:113239) lesson to learn how to update the application.
