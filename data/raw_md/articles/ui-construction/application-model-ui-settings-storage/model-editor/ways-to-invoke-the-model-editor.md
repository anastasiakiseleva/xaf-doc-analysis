---
uid: "113326"
seealso: []
title: Ways to Invoke the Model Editor
owner: Ekaterina Kiseleva
---
# Ways to Invoke the Model Editor

The [Model Editor](xref:112582) can be used:

At design time (in Visual Studio by a developer)
:   The Model Editor invoked at design time is a window pane in Visual Studio.
At runtime (by application users and administrators)
:   The Model Editor invoked by users and administrators is a form. 
    
The elements and capabilities in both instances are primarily the same. 

This topic describes how to invoke the Model Editor in different scenarios.

## Invoke the Model Editor in Visual Studio at Design Time
In the Solution Explorer, double-click the _Model.xafml_ or _Model.DesignedDiffs.xafml_ file in the XAF solution's project (module or application project).

![Tutorial_BMD_Lesson4_1](~/images/tutorial_bmd_lesson4_1115428.png)

Alternatively, you can right-click the project and choose **Open Model Editor** in the context menu.

![ModelEditor_Invoke](~/images/modeleditor_invoke116598.png)

Visual Studio invokes the Model Editor in a window pane.

![ModelEditorDesign](~/images/modeleditordesign115654.png)
 
The model editor pane contains the following elements:
- [nodes tree](xref:113328)
- [property grid](xref:113329)
- [search pane](xref:113331) (optional)

To switch focus between UI elements, press the <kbd>TAB</kbd> key.

You can see a description and type of a selected node/property at the bottom of the window pane.

The Model Editor displays different information for different projects. This information is collected from the modules that are added to the project for which you invoked the Model Editor. If the project is a module itself, the information about it is loaded as well.

Everything you change in the Model Editor is saved to the _Model.xafml_ or _Model.DesignedDiffs.xafml_ file, depending on whether the changes were made in an application project or in a module. Changes are displayed in bold in the Model Editor.

To view the underlying XML code, right-click the XAFML file and choose **View code**. These changes are superimposed on previous values loaded to the Application Model. Values specified in the Model Editor for the application project are the Application Model's final values. They are used when starting the application.

For details, refer to the following topic: [Application Model Basics](xref:112580).

##  Use Actions to Invoke the Model Editor At RunTime

When the **Edit Model** or **Administrative** [permission](xref:113366) is granted to the current user, the **Tools** category of the WinForms application's root window shows the **EditModel** and **ViewInModel** Actions. These Actions are available if the [Security System](xref:113366) is not enabled.

### The Edit Model Action

Use the **EditModel** Action (or the <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F1</kbd> shortcut) to invoke the Model Editor window.

![ToolsEditModel](~/images/toolseditmodel115347.png)

![|ModelEditor_Runtime|](~/images/modeleditor_runtime115655.png)

### The View in Model Action

Use the **ViewInModel** Action (or the <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F2</kbd> shortcut) to invoke the Model Editor window with the selected View node item.

![View in Model Action](~/images/view-in-model-action-model-editor.png)

![The Model Editor with the selected node](~/images/view-in-model-action-model-editor-1.png)

You can also utilize Action items to open the Model Editor with the selected Class or Validation nodes.

![View in Model Action items](~/images/view-in-model-action-items.png)

## User Model Difference Storage

At runtime, the Model Editor contains complete information that includes recent changes made in the UI. When a user makes changes in the UI or in the Model Editor, they are saved to the _Model.User.xafml_ file. This file is located in the folder with the application executable file. Set the `UserModelDiffsLocation` configuration key to `CurrentUserApplicationDataFolder` to place this file in a user's _ApplicationData_ folder.

**File:** _MySolution.Win\App.config_
# [XML](#tab/tabid-xml)

```XML
<appSettings>
    <add key="UserModelDiffsLocation" value="CurrentUserApplicationDataFolder"/>
</appSettings>
```
***

You can also store user settings in the database. For additional information, refer to the following topic: [Model Difference Storages](xref:403527).

## Deploy and Run the Standalone Model Editor

The application administrator can run the Model Editor as a standalone utility on Windows. The administrator can edit a model of the deployed ASP.NET Core Blazor application or deployed Windows Forms application with the **EditModel** Action disabled.

### On .NET

To use the standalone Model Editor:
1. Copy the _%PROGRAMFILES%\DevExpress <:xx.x:>\Components\Tools\eXpressAppFrameworkNetCore\Model Editor_ folder from the developer workstation to a workstation or a server where the XAF application is deployed. 
2. Copy all assemblies required by your XAF application (deployed together with the executable).

After you invoke the standalone Model Editor, use the **Open Model** dialog to specify the Application Model to edit. This dialog is initially open. To re-invoke it later, click the **Open Model** button on the [toolbar](xref:113327).

![ModelEditor_OpenModel](~/images/modeleditor_openmodel_core.png)

### Open and Edit Application Model

To edit the Application Model of the deployed application, you should specify:
- configuration file name (Windows Forms)
- _MySolution.Blazor.Server.dll_ file (ASP.NET Core Blazor)

An option to choose an assembly file and model differences path allows you to edit the model of a specific module outside of Visual Studio.

You can also use command-line parameters to specify an Application Model to open. The standalone Model Editor has the following command-line syntax:

``DevExpress.ExpressApp.ModelEditor.v<:xx.x:>.exe appConfigFile | moduleAssemblyFile diffsPath | /?``

> [!NOTE]
>
> The Windows Forms application configuration file is:
> - _\<Application_Name>.Win.dll.config_
>
> The ASP.NET Core Blazor application does not include a configuration file. Specify the _moduleAssemblyFile_ and _diffsPath_ parameters instead of _appConfigFile_.

{|
|-

! Parameter
! Description
|-

| _appConfigFile_
| Specifies an XAF application configuration file. Pass this parameter to edit the Application Model of a deployed XAF application (Windows Forms).

_Example:_

``DevExpress.ExpressApp.ModelEditor.v<:xx.x:>.exe d:\MySolution\MySolution.Win\bin\Release\MySolution.Win.dll.config``
|-

| _moduleAssemblyFile_
| Specifies an XAF module's assembly file (DLL). Pass this parameter followed by the _diffsPath_ parameter to edit the Application Model of an XAF module.

_Example:_

``DevExpress.ExpressApp.ModelEditor.v<:xx.x:>.exe``

``d:\Projects\MySolution\MySolution.Module\Bin\Debug\MySolution.Module.dll``

``d:\Projects\MySolution\MySolution.Module``
|-

| _diffsPath_
| This parameter specifies a model differences folder, and is required when the first parameter specifies an assembly. Typically, you should pass a module project's folder that contains a _Model.DesignedDiffs.xafml_ file to modify.
|-

| _/?_
| Displays a help message on how to use the above parameters.
|}

The Model Editor will be displayed as a form.

![ModelEditor_CMD](~/images/modeleditor_cmd116531.png)

Alternatively, you can right-click the configuration file in Windows Explorer and click the **Open With…** menu item to choose the Model Editor executable.

To edit the Application Model of an XAF module, type the Model Editor executable full path in the command prompt and pass the assembly file and the differences folder as parameters (see the table above).
