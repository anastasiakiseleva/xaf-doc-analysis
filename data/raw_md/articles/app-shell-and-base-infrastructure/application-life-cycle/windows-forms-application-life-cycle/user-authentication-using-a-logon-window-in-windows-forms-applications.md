---
uid: "113117"
seealso: []
title: User Authentication using a Logon Window in Windows Forms Applications
---
# User Authentication using a Logon Window in Windows Forms Applications

This topic details the steps performed from the time the [](xref:DevExpress.ExpressApp.Win.WinApplication) object has been created and initialized, until the moment an end user has been authenticated to the application. There are two built-in Authentication Strategies in XAF. The [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authenticates end users with the information typed in the logon window. The [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) does not require the logon window to be displayed. It takes the required information from the system's active directory. This topic details how end users are authenticated when the built-in **AuthenticationStandard** strategy is used. To learn what steps are taken when the built-in **AuthenticationActiveDirectory** strategy is used, refer to the [User Authentication Without a Logon Window in Windows Forms Applications](xref:113124) topic. You can customize the **AuthenticationActiveDirectory**, so that a logon window is displayed and the information typed in it is used for authentication. In this instance, read this topic to learn how the logon window is displayed.

## Create a Logon View
{|
|-

! Stage Description
! Ways to Interfere
|-

| A Detail View is created by the information stored in the [Application Model](xref:112580)'s **Views** | **\<LogonParameters_class_name>_DetailView** node. This Detail View represents a newly created object of the type that is specified by the **LogonParametersType** property of the security's Authentication object. The object's properties are initialized by the values that were typed the last time the application was run. These values were saved to the Application Model's **Logon** node after a user had been authenticated.
| If you require that custom information is requested in the logon window, specify a custom **LogonParameters** class. For this purpose, before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method is called in your **Program.Main** method, set the **LogonParametersType** property of the Authentication object that is used by the Security System. If your **LogonParameters** demand a custom authentication technique, implement an Authentication class, deriving it from the [](xref:DevExpress.ExpressApp.Security.AuthenticationBase) class. In this instance, you should assign an instance of your class to the **Application.Security.Authentication** property.

By default, an object of the specified LogonParameters type is created, using a custom [Object Space](xref:113707) which stores an object in memory and does not connect to the database. If you need to access the database to represent a custom LogonParameters object in the logon window, create an Object Space of the [](xref:DevExpress.ExpressApp.IObjectSpace) type. To do this, handle the [XafApplication.CreateCustomLogonWindowObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonWindowObjectSpace) event in your application.

By default, the values specified by an authenticated user are saved to the **SettingsStorageOnString** store, so that they can be read the next time the application is run. This store saves the credentials to the _LogonParameters_ file. You can implement a custom store by inheriting from the **SettingsStorage** class. To use this store instead of the default, handle the [XafApplication.CreateCustomLogonParameterStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonParameterStore) event.

You can access the LogonParameters object before and after the values that were saved when the application was run the last time, are assigned. For this purpose, handle the [XafApplication.LastLogonParametersReading](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersReading) and [XafApplication.LastLogonParametersRead](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersRead) events, respectively. Alternatively, you can override the **XafApplication.ReadLastLogonParametersCore** method, to implement a custom technique for reading these values.

You can customize the Detail View representing the LogonParameters object. For this purpose, use the **Views** | **\<LogonParameters_class_name>_DetailView** node in the [Model Editor](xref:112582). For instance, you can change the View Items layout or perform [localization](xref:112595).
|}

## Create a Logon Window
![MainWindowWin1](~/images/mainwindowwin1116118.png)

{|
|-

! Stage Description
! Ways to Interfere
|-

| Before creating an instance of the [](xref:DevExpress.ExpressApp.Window) class, the required Controllers are created.
| If you need to add custom buttons to the logon window, or customize the behavior of the default ones, implement a custom [Dialog Controller](xref:112805) by inheriting from the **LogonController** Dialog Controller. Note that the default [Template](xref:112609) that visualizes the logon window contains the **ButtonsContainer** [Action Container](xref:112610) only. So, you are limited in the types of the Actions you can add to the Controller (see [Add Actions to a Popup Window](xref:112804)). To replace the default LogonController, override the **CreateLogonController** method in your WinApplication descendant.

By default, only the Controllers that are sufficient for the logon window are created. You can create extra Controllers. To do this, handle the [XafApplication.CreateCustomLogonWindowControllers](xref:DevExpress.ExpressApp.XafApplication.CreateCustomLogonWindowControllers) event in your WinApplication class. Return a list of created Controllers.

Subscribe to the [Controller.AfterConstruction](xref:DevExpress.ExpressApp.Controller.AfterConstruction) event, to set up a Controller's properties. For instance, you can specify the conditions to be satisfied for the Controller's activation.
|-

| Then, a Window is created and all the created Controllers are registered in it. This means that their [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window) property is set to the current Window object.
| Subscribe to the [Controller.FrameAssigned](xref:DevExpress.ExpressApp.Controller.FrameAssigned) event, to access a Controller's Window (see [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window)) and perform the required actions with it. For instance, in the event handler, you can subscribe to the event that is raised before the Controller is activated.
|-

| The Controllers that represent the [](xref:DevExpress.ExpressApp.WindowController) class' descendants are activated sequentially.
| To activate a Window Controller for the Logon Window only, add an item to the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection. As the item's _value_, pass an expression that is set to **true** when the current Window contains the LogonController.

Override a Controller's **WindowChanging** method to cancel the activation. Add an item to the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection, passing **false** as the item's _value_.

Subscribe to the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event. This is the main entry to perform the required functionality using a Controller.
|}

## Assign a Template to the Window
![LogonWindowWin2](~/images/logonwindowwin2116127.png)

{|
|-

! Stage Description
! Ways to Interfere
|-

| To be visualized, the Logon Window creates a [Template](xref:112609), a control (e.g. a form) that supports the XAF architecture. To create a Template, a **Frame Template Factory** is used. It creates the Template that is appropriate in the Window's context (see [Frame.Context](xref:DevExpress.ExpressApp.Frame.Context)). The Logon Window is created in the "PopupWindow" context. The **DefaultFrameTemplateFactory**, which is used by default to create Templates, creates the built-in **PopupForm** Template in the "PopupWindow" context.
| Subscribe to the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event of your WinApplication object, to create a custom Template in the "PopupWindow" context. To get the current context in which a Template is created, use the event handler's _Context_ parameter. To see an example, refer to the [Template Customization](xref:112696) and [How to: Create a Custom WinForms Ribbon Template](xref:112618) topics.

Use a custom **Frame Template Factory** to create custom Templates. Register the required **Frame Template Factory** in a module where the custom Templates are implemented. In this instance, the module should be added to an application to use the custom Templates. For details, refer to the [How to: Distribute Custom Templates with Modules](xref:113047) topic.
|-

| When a Template is created, all its [Action Containers](xref:112610) are created as well. Action Containers are the controls that display [Actions](xref:112622). The **PopupForm** Template contains the **PopupActions** Buttons Action Container. This Container represents Actions via a button. For details, refer to the [Add Actions to a Popup Window](xref:112804) topic.
| Subscribe to the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) event of your WinApplication object. To customize the Template that is created for the Logon Window, use the event handler's _Context_ parameter. It must be set to [TemplateContext.PopupWindow](xref:DevExpress.ExpressApp.TemplateContext.PopupWindow). To see an example, refer to the [Template Customization](xref:112696) topic.
|-

| The created Template is assigned to the [Window.Template](xref:DevExpress.ExpressApp.Window.Template) property.
| 
|}

## Create Controls for Actions
![LogonWindowWin3](~/images/logonwindowwin3116128.png)

| Stage Description | Ways to Interfere |
|---|---|
| The Window's **TemplateChanged** event is raised. This event is handled by the **FillActionContainersController**, which is already activated, since it represents a Window Controller. The **TemplateChanged** event handler registers Actions in the Action Containers of the Window's Template. Each Action is registered in the Action Container to which it is mapped in the Application Model's **ActionDesign** \| **ActionToContainerMapping** node. The Action Containers create controls for their Actions. | Subscribe to the [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) event to access the Logon Window's Template and its Action Containers. To do this, use a Window Controller's [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event. To see an example, refer to the [How to: Access the Navigation Control](xref:112617) topic. |

## Assign the View to the Window
![LogonWindowWin5](~/images/logonwindowwin5116129.png)

| Stage Description | Ways to Interfere |
|---|---|
| The created View is assigned to the Logon Window. | Subscribe to the [Frame.ViewChanging](xref:DevExpress.ExpressApp.Frame.ViewChanging) or [Frame.ViewChanged](xref:DevExpress.ExpressApp.Frame.ViewChanged) event. You can do this in a Widow Controller's [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler, or in a View Controller's [Controller.FrameAssigned](xref:DevExpress.ExpressApp.Controller.FrameAssigned) event handler. |

## View Controllers are Activated
![LogonWindowWin6](~/images/logonwindowwin6116130.png)

{|
|-

! Stage Description
! Ways to Interfere
|-

| View Controllers from the Logon Window's [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection are activated.
| You can manage the activation of a View Controller using the following properties: [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType), [ViewController.TargetViewNesting](xref:DevExpress.ExpressApp.ViewController.TargetViewNesting), [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType) and [ViewController.TargetViewId](xref:DevExpress.ExpressApp.ViewController.TargetViewId).

Override a Controller's **ViewChanging** method to cancel the activation. Add an item to the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection, passing **false** as the item's _value_.

Subscribe to the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event. This is the main entry to perform the required functionality using a Controller.
|}

## Assign the Window's View to the Template
![LogonWindowWin7](~/images/logonwindowwin7116131.png)

{|
|-

! Stage Description
! Ways to Interfere
|-

| The View is assigned to the current Window's Template. This forces the creation of the View's control (see [View.CreateControls](xref:DevExpress.ExpressApp.View.CreateControls)). This control is added to the Template's ViewSite.
| Handle the [View.ControlsCreating](xref:DevExpress.ExpressApp.View.ControlsCreating) and [View.ControlsCreated](xref:DevExpress.ExpressApp.View.ControlsCreated) events to perform custom actions before and after the controls that represent the View in a UI are created.
|-

| The Template's [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method is called to apply the settings that are specified by an end user the last time the application was run.
| By default, the Template's settings are saved to the [Application Model](xref:112580)'s **Templates** | **Template** node. You can save them to another Application Model node. For this purpose, override the **GetTemplateCustomizationModel** method in your WinApplication class and return the required node in it.

You can save the Template's settings in another store. To do this, implement a custom Template, overriding the methods exposed by the [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) interface.
|-

| The Template is shown.
| 
|}

## Authentication
{|
|-

! Stage Description
! Ways to Interfere
|-

| To start the authentication process, an Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace))  is created to check whether a record, defining the user who is logging on, exists in the application database. Before accessing the database, the compatibility of the module versions in the database and their actual versions are checked. If the versions in the database are greater than the actual ones, an exception is raised, requiring that you increase your application's version. If lower, the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event is raised. By default, this event is handled in XAF solutions. The event handler calls the Database Updater's **Update** method, which updates the database to the required version. However, this method is called when the application is run in debug mode. In release mode, an exception is raised (you can see the entire code in your application).
| Before the authenticating process is started, you can access the LogonParameters object, modified by the user who is logging on. For this purpose, handle the [XafApplication.LoggingOn](xref:DevExpress.ExpressApp.XafApplication.LoggingOn) event.

You can perform a custom process of checking the database and application compatibility. For this purpose, handle the [XafApplication.CustomCheckCompatibility](xref:DevExpress.ExpressApp.XafApplication.CustomCheckCompatibility) event. In this instance, you should raise the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event in this code as well, to update the database when required.

If you do not need the scenario implemented in the [XafApplication.DatabaseVersionMismatch](xref:DevExpress.ExpressApp.XafApplication.DatabaseVersionMismatch) event handler, generated automatically in your application, write a custom event handler. For instance, you can implement a custom **DatabaseUpdater** class and call its **Update** method in the **DatabaseVersionMismatch** event handler.

Use the [XafApplication.DatabaseUpdateMode](xref:DevExpress.ExpressApp.XafApplication.DatabaseUpdateMode) property to set the required behavior for the updating database mechanism. For instance, you can set the **UpdateDatabaseAlways** value so that the database's version is updated each time the application runs.
|-

| Authentication is accomplished after an end user clicks **Log In** in the logon window. When the **AuthenticationStandard** strategy is used, users whose name and password typed in the logon window coincide with the corresponding records in the database are authenticated.
| If the default authentication performed by a built-in Authentication class does not satisfy your requirements, implement a custom class. For instance, inherit from one of the built-in authentication classes: **AuthenticationStandard** or **AuthenticationActiveDirectory**. Alternatively, inherit from the base **AuthenticationBase** class. In your class, override the **Authenticate** method. It returns the user object that is found in the database with the credentials specified by the end user who is logging on. To use a custom authentication instead of a default authentication, assign an instance of your class to the **Application.Security.Authentication** property.

You can access the LogonParameters object before its property values are saved to a store. For this purpose, handle the [XafApplication.LastLogonParametersWriting](xref:DevExpress.ExpressApp.XafApplication.LastLogonParametersWriting) event. Alternatively, you can override the **XafApplication.WriteLastLogonParametersCore** method, to implement a custom technique for saving the credentials.

To create a custom User Model Differences Store, handle the [XafApplication.CreateCustomUserModelDifferenceStore](xref:DevExpress.ExpressApp.XafApplication.CreateCustomUserModelDifferenceStore) event. The default Store saves and loads user differences from the Model.User.xafml file. To learn how to implement a custom store, refer to the [](xref:113698) document.
|-

| The system gives end users three attempts to log on to the application. After the third attempt, a user-friendly exception is raised.
| To change the three attempt scenario, override the **Logon** method in your WinApplication class' descendant.
|-

| The Application Model's layer with end user customizations, stored in the _Model.User.xafml_ file is created. This file stores end user customizations to the application, created during the previous application runs.
| To access the LogonParameters object or perform custom actions after the logging on procedure has completed, handle the [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) event.
|}