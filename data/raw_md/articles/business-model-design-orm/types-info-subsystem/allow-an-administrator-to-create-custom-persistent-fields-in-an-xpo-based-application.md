---
uid: "113649"
title: 'Allow an Administrator to Create Custom Persistent Fields in an XPO-Based Application'
---
# Allow an Administrator to Create Custom Persistent Fields in an XPO-Based Application

You can allow an application administrator to create [custom persistent fields](xref:113583) and display the added fields' data in the UI without recompiling the application. In this example, the `SkypeID` field will be added to the `Contact` business object in the **MainDemo** application.

![CustomPersistentFields_Result](~/images/custompersistentfields_result126704.png)

## Prerequisites
Ensure that your application does not contradict the following conditions. Otherwise, creating new persistent fields is impossible at runtime.

* WinForms and ASP.NET Core Blazor applications should be based on the XPO data model.
* The following features should not be used together.
	
	* [SecuredObjectSpaceProvider](xref:DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider) or [XPObjectSpaceProvider](xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider) created using the constructor with the `threadSafe` parameter set to `true` (this parameter enables [](xref:DevExpress.Xpo.ThreadSafeDataLayer)).
	* An Administrator's Model Differences [stored in the database](xref:113698) using the [XafApplication.CreateCustomModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomModelDifferenceStore) event (you can still store the User's differences in the database using the [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) event).
	* [Custom Persistent Fields](xref:113583) declared in the Administrator's Model Differences.
	
	With this configuration, your application loads information on custom persistent fields from the database and then updates the database schema. However, a thread-safe data layer does not support altering the data model after the database connection is established.
* [!include[CustomFields_ServerAppNote](~/templates/customfields_serverappnote111922.md)]

## Setup the Application
Apply the following changes in the application code to allow application administrators to create and display custom persistent field data in the UI.

* Set the static [ModelMemberReadOnlyCalculator.AllowPersistentCustomProperties](xref:DevExpress.ExpressApp.Model.Core.ModelMemberReadOnlyCalculator.AllowPersistentCustomProperties) property to `true` to allow creating persistent fields at runtime. Open the [!include[File_Module](~/templates/file_module11171.md)] file and add the following code to the module's constructor.
	
	```csharp
	DevExpress.ExpressApp.Model.Core.ModelMemberReadOnlyCalculator.AllowPersistentCustomProperties = true;
	```

* Set the [IObjectSpaceProvider.CheckCompatibilityType](xref:DevExpress.ExpressApp.IObjectSpaceProvider.CheckCompatibilityType) property to [CheckCompatibilityType.DatabaseSchema](xref:DevExpress.ExpressApp.CheckCompatibilityType.DatabaseSchema) to catch the database changes and update the database if the schema is modified.
	
	![CheckCompatibilityType](~/images/checkcompatibilitytype120621.png)
* To allow the database schema updates, set the [XafApplication.DatabaseUpdateMode](xref:DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode) property to [DatabaseUpdateMode.UpdateDatabaseAlways](xref:DevExpress.ExpressApp.DatabaseUpdateMode.UpdateDatabaseAlways) or [DatabaseUpdateMode.UpdateOldDatabase](xref:DevExpress.ExpressApp.DatabaseUpdateMode.UpdateOldDatabase).
* [Copy the _DBUpdater.v<:xx.x:>.exe_ and _DBUpdater.v<:xx.x:>.config_ files from the _%PROGRAMFILES%\DevExpress <:xx.x:>\Components\Tools\eXpressAppFramework\DBUpdater\_ folder to the application's installation folder.](#platform/netframework46)

## Implement the Persistent Field and Display It
Follow the steps below to add a custom persistent field at an end-user workstation.

1. Invoke the built-in Model Editor using the **Tools** | **Edit Model** command at runtime or close the application and start the standalone Model Editor by running the _DevExpress.ExpressApp.ModelEditor.v<:xx.x:>.exe_ executable file.
	
	If you use the standalone Model Editor, specify the path to the application configuration file (_MainDemo.Win.exe.config_ for Windows or _MySolution.Blazor.Server.dll_ for Blazor) and click **Open** in the **Open Model** dialog.
	
	![CustomPersistentFields_RunME](~/images/custompersistentfields_runme117509.png)
2. Navigate to the **BO_Model** | **Contact** node in the tree on the left. Right-click the **OwnMembers** child node and choose **Add…** | **Member**.
	
	![CustomPersistentFields_AddMember](~/images/custompersistentfields_addmember117510.png)
3. Set the **Name** property of the newly added node to "SkypeID". Then, set the **IsCalculated** property to "False", **Type** to "System.String", **Size** to "32", and **Caption** to "Skype ID".
	
	![CustomPersistentFields_MemberProperties](~/images/custompersistentfields_memberproperties117511.png)
4. Copy the differences that you have introduced in the administrator's layer using the [Merge Differences](xref:113334) command.
	
	![CustomPersistentFields_Merge](~/images/custompersistentfields_merge117512.png)
5. Save changes using the **Save** button or the <kbd>CTRL</kbd>+<kbd>S</kbd> shortcut and restart the Model Editor.
6. Navigate to the **Views** | **Contact_DetailView** node in the tree on the left. Right-click the **Items** child node and choose **Add…** | **PropertyEditor**.
	
	![CustomPersistentFields_AddEditor1](~/images/custompersistentfields_addeditor1117515.png)
7. Set **PropertyName** and **Id** to "SkypeID".
	
	![CustomPersistentFields_AddEditor2](~/images/custompersistentfields_addeditor2117516.png)
8. Focus the **Layout** node. Right-click the empty space within the form preview displayed on the right and select **Customize Layout**.
	
	![CustomPersistentFields_AddEditor3](~/images/custompersistentfields_addeditor3117526.png)
9. Drag the **Skype ID** item from the invoked **Customization** window to an appropriate position within the form.
	
	![CustomPersistentFields_AddEditor4](~/images/custompersistentfields_addeditor4117527.png)
	
	You can also add the **Skype ID** column to the `Contact` List View using a similar approach (see [List View Columns Customization](xref:113679)).
10. Merge the differences as described at the forth step.
11. Save the changes and close the Model Editor.
12. Update your database schema as described in the [Apply Changes to the Database](#apply-changes-to-the-database) section.
13. Restart the application and open the `Contact` Detail View to see the result demonstrated in the introduction of this topic.

> [!IMPORTANT]
> If the application is installed on multiple PCs and the Administrator's Model Differences are stored in the _Model.xafml_ file, copy it from the application's working folder to each PC. Otherwise, the created field is available only on the workstation where you added it.

## Access a Custom Persistent Field in Code

To access [custom persistent fields](xref:113583) in code, use the solution from the following topic: [Access a Custom Field in Code](xref:113583#access-a-custom-field-in-code)

## Apply Changes to the Database

Launch a command line interpreter, for instance, **Command Prompt**, and run your application with the `-updateDatabase` command. 

# [Console (Blazor)](#tab/tabid-cmd-blazor)
```Console
C:\Users\Public\MyApplication\MySolution.Blazor.Server.exe -updateDatabase -silent -forceUpdate
```
# [Console (WinForms)](#tab/tabid-cmd-win)
```Console
C:\Users\Public\MyApplication\MySolution.Win.exe -updateDatabase -silent -forceUpdate
```
***

For additional information, refer to the following topic: <xref:113239>