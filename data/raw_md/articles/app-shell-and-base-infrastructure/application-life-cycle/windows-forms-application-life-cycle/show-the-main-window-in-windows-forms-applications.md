---
uid: "113118"
seealso: []
title: Show the Main Window in Windows Forms Applications
owner: Ekaterina Kiseleva
---
# Show the Main Window in Windows Forms Applications

This topic details the steps performed after an end-user has been authorized, until the moment the main window is shown to the end-user. The main window, as any other window in XAF applications, is defined by two objects: a control called [Template](xref:112609) and an abstract entity called [Window](xref:112608). A Window, in contrast to a Template, does not contain information on what controls must be located on it. Windows only include the information concerning their functions in the **XAF** applications.  In this topic, you will learn how a Window and Template objects are created and associated to present the main window.

## Create a Window
![MainWindowWin1](~/images/mainwindowwin1116118.png)

{|
|-

! Stage
! Ways to Interfere
|-

| Before creating an instance of the [](xref:DevExpress.ExpressApp.Window) class, all [Controllers](xref:112621) listed in the [Application Model](xref:112580)'s **ActionDesign** | **Controllers** node are created.
| Subscribe to the [Controller.AfterConstruction](xref:DevExpress.ExpressApp.Controller.AfterConstruction) event to set up a Controller's properties. For instance, you can specify the conditions to be satisfied for the Controller's activation.
|-

| Then, a Window is created and all the Controllers are registered in this Window. This means that their [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window) property is set to the current Window object.
| Subscribe to the [Controller.FrameAssigned](xref:DevExpress.ExpressApp.Controller.FrameAssigned) event to access the Controller's Window (see [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window)) and perform the required actions with it. For instance, in the event handler, you can subscribe to the event that is raised before the Controller is activated.
|-

| The Controllers that represent the [](xref:DevExpress.ExpressApp.WindowController) class' descendants are activated one after another.
| To activate a Window Controller for the main Window only, set its [WindowController.TargetWindowType](xref:DevExpress.ExpressApp.WindowController.TargetWindowType) property to **Main** or **Any**.

Override a Controller's **WindowChanging** method to cancel the activation. Add an item to the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection passing **false** as the item's _value_.

Subscribe to the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event. This is the main entry to perform the required functionality using a Controller.
|}

## Assign a Template to the Window
![MainWindowWin2](~/images/mainwindowwin2116119.png)

{|
|-

! Stage
! Ways to Interfere
|-

| To be visualized, the Window creates a [Template](xref:112609), a control (e.g. a form) that supports the XAF architecture. To create a Template, a **Frame Template Factory** is used. It creates the Template that is appropriate in the Window's context (see [Frame.Context](xref:DevExpress.ExpressApp.Frame.Context)). The main Window is created in the "ApplicationWindow" context. The **DefaultFrameTemplateFactory**, which is used by default to create Templates, creates the built-in Main Form Template in the "ApplicationWindow" context.
| Subscribe to the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event of your [](xref:DevExpress.ExpressApp.Win.WinApplication) object, to create a custom Template in the "ApplicationWindow" context. To get the current context in which a Template is created, use the event handler's _Context_ parameter. To see an example, refer to the [Template Customization](xref:112696) and [How to: Create a Custom WinForms Ribbon Template](xref:112618) topics.

Use a custom **Frame Template Factory** to create custom Templates. Register the required **Frame Template Factory** in a module where the custom Templates are implemented. In this instance, the module should be added to an application to use the custom Templates. For details, refer to the [How to: Distribute Custom Templates with Modules](xref:113047) topic.
|-

| When a Template is created, all its [Action Containers](xref:112610) are created as well. Action Containers are the controls that display [Actions](xref:112622). Main Form Templates contain the following Action Containers: About, Tools, File, ObjectsCreation, Print, Export, Exit, RecordEdit, RecordsNavigation, ViewsHistoryNavigation, FiltersSearch, Filters, View, Options, navigation, Diagnostic, ViewsNavigation. The Navigation Action Container represents the **NavBarControl**. The other Action Containers represent **BarLinkContainerExItem**, some of which create toolbar items for their Actions, and others create menu items.
| Subscribe to the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) event of your WinApplication object. To customize the Template that is created for the main Window, use the event handler's _Context_ parameter. It must be set to [TemplateContext.ApplicationWindow](xref:DevExpress.ExpressApp.TemplateContext.ApplicationWindow). To see an example, refer to the [Template Customization](xref:112696) topic.
|-

| The created Template is assigned to the [Window.Template](xref:DevExpress.ExpressApp.Window.Template) property.
| 
|}

## Create Controls for Actions
![MainWindowWin3](~/images/mainwindowwin3116120.png)

| Stage | Ways to Interfere |
|---|---|
| The Window's **TemplateChanged** event is raised. This event is handled by the **FillActionContainersController**, which is already activated, since it represents a Window Controller. The **TemplateChanged** event handler registers Actions in the Action Containers of the Window's Template. Each Action is registered in the Action Container to which it is mapped in the Application Model's **ActionDesign** \| **ActionToContainerMapping** node. The Action Containers create controls for their Actions. | Subscribe to the [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) event to access the Window's Template and its Action Containers. To do this, use a Window Controller's [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event. To see an example, refer to the [How to: Access the Navigation Control](xref:112617) topic. |

## Set the Template's Settings
![MainWindowWin4](~/images/mainwindowwin4116121.png)

{|
|-

! Stage
! Ways to Interfere
|-

| The Template's [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method is called to apply the settings that are specified by an end-user the last time the application was run.
| By default, the Template's settings are saved to the [Application Model](xref:112580)'s **Templates** | **Template** node. You can save them to another Application Model node. For this purpose, override the **GetTemplateCustomizationModel** method in your WinApplication class and return the required node in it.

You can save the Template's setting in another store. To do this, implement a custom Template overriding the methods exposed by the [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) interface.
|-

| The Template is shown.
| 
|}

## Assign a View to the Window
![MainWindowWin5](~/images/mainwindowwin5116122.png)

| Stage | Ways to Interfere |
|---|---|
| The [ShowNavigationItemController.ShowNavigationItemAction](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction) is executed as if an item is selected in the navbar. This forces the creation of the View associated with the "selected" item. | To imitate the selection of a particular item in the navigation control, inherit from the **ShowNavigationItemController** and override its **GetStartupNavigationItem** method. In this method, return the required item from the **ShowNavigationItem** Action's Items collection. |
| The created View is assigned to the current Window. | Subscribe to the [Frame.ViewChanging](xref:DevExpress.ExpressApp.Frame.ViewChanging) event. You can do this in a Window Controller's [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler, or in a View Controller's [Controller.FrameAssigned](xref:DevExpress.ExpressApp.Controller.FrameAssigned) event handler. |

## View Controllers are Activated
![MainWindowWin6](~/images/mainwindowwin6116123.png)

{|
|-

! Stage
! Ways to Interfere
|-

| View Controllers from the Window's [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection are activated.
| You can manage the activation of a View Controller using the following properties: [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType), [ViewController.TargetViewNesting](xref:DevExpress.ExpressApp.ViewController.TargetViewNesting), [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType) and [ViewController.TargetViewId](xref:DevExpress.ExpressApp.ViewController.TargetViewId).

Override a Controller's **ViewChanging** method to cancel the activation. Add an item to the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection passing **false** as the item's _value_.

Subscribe to the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event. This is the main entry to perform the required functionality using a Controller.
|}

## Assign the Window's View to the Template
![MainWindowWin7](~/images/mainwindowwin7116124.png)

| Stage | Ways to Interfere |
|---|---|
| The View is assigned to the current Window's Template. This forces the creation of the View's control (see [View.CreateControls](xref:DevExpress.ExpressApp.View.CreateControls)). This control is added to the Template's ViewSite. | Handle the [View.ControlsCreating](xref:DevExpress.ExpressApp.View.ControlsCreating) and [View.ControlsCreated](xref:DevExpress.ExpressApp.View.ControlsCreated) events to perform custom actions before and after the controls that represent the View in a UI are created. |
