---
uid: "112818"
seealso: []
title: Determine Why an Action, Controller or Editor is Inactive
---
# Determine Why an Action, Controller or Editor is Inactive

When building an application, you may need to determine why an [Action](xref:112622) or [Controller](xref:112621) is not active (visible) in a particular [Window](xref:112608). An Action may be deactivated or disabled for various reasons: [Security System](xref:113366) permissions, the current [View](xref:112611) is read-only, an inconvenient object type of the current View, and other specific parameters. The current View may also be made read-only for different reasons. A thorough debugging may be required to ascertain the actual reason.  For this purpose, the **XAF** provides the **Diagnostic Info** Action. This Action shows a window with information on all Controllers and Actions loaded to the [Application Model](xref:112580) for the current View, and [validation rules](xref:113008) applied to the View. You can use this information to find issues and fix them. This topic explains how to add the **Diagnostic Info** Action to your application and use it to get this information.

* [Enable the DiagnosticInfo Action](#enable-the-diagnosticinfo-action)
* [Analyze the DiagnosticInfo Action Output](#analyze-the-diagnosticinfo-action-output)
* [DiagnosticInfo Reference](#diagnosticinfo-reference)
* [Custom Diagnostic Information on Actions](#custom-diagnostic-information-on-actions)

## Enable the DiagnosticInfo Action

To add the **Diagnostic Info** Action to the UI, follow the steps below:

1. Open the configuration file of your application's project. The name of the file depends on the UI framework:

    * WinForms -- _App.config_
    * ASP.NET Core Blazor -- _appsettings.Development.json_

2. Locate `EnableDiagnosticActions` key and set its value to `True` to add the **Diagnostic Info** Action to the Application Model and show the Action in the UI.

   For WinForms:

    # [XML](#tab/tabid-xml)

    ```XML
    <add key="EnableDiagnosticActions" value="True" />
    ```

    ***

   For ASP.NET Core Blazor:

    # [JSON](#tab/tabid-json)
    
    ```JSON
    {
      //...
      "DevExpress": {
        "ExpressApp": {
          "EnableDiagnosticActions": true
        }
      }
    }
    ```
    ***

The **Diagnostic Info** Action is implemented in the `DevExpress.ExpressApp.SystemModule.DiagnosticInfoController` and belongs to the **Diagnostic** Action Container. The images below show the **Diagnostic Info** Action's location on different templates.

WinForms

:   ![DiagnosticInfo_Action](~/images/diagnosticinfo_action_win115605.png)

ASP.NET Core Blazor

:   ![DiagnosticInfo_Action_Blazor](~/images/diagnosticinfo_action_blazor.png)

The **Diagnostic Info** Action is a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction). When you click this Action's item, you invoke a dialog window with the **DiagnosticInfoObject_DetailView** Detail View. The `DiagnosticInfoObject.AsText` property contains information in XML format.

![DiagnosticInfo_Window](~/images/diagnosticinfo_window115606.png)

## Analyze the DiagnosticInfo Action Output

Follow the steps below to determine why an Action is disabled.

1. Determine the identifier of an Action you want to debug. If the Action is implemented in your code, use the [ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id) value. Otherwise, refer to the [Determine an Action's Controller and Identifier](xref:113484) topic for instructions on how to get the identifier of a [built-in](xref:113016) or third-party Action.
2. Click **Diagnostic** | **Actions Info** and search for the Action identifier in the output XML.
3. Look at the XML element that describes the target Action and its Controller. For instance:
	
   # [XML](#tab/tabid-xml1)

	 ```XML
	 <Controller Name="OpenObjectController" FullName="DevExpress.ExpressApp.Win.SystemModule.OpenObjectController" Active="True">
	   <ActiveList>
	 	 <Item Key="View is assigned" Value="True" />
	 	 <Item Key="View type is ObjectView" Value="True" />
		 <Item Key="PropertyEditor has ObjectSpace" Value="True" />
	   </ActiveList>
	   <Actions>
		 <Action ID="OpenObject" Caption="Open Related Record" TypeName="SimpleAction" Category="OpenObject" Active="False" Enabled="True" AdditionalInfo="">
		   <ActiveList>
			 <Item Key="Controller active" Value="True" />
			 <Item Key="HasReadPermissionToTargetType" Value="True" />
			 <Item Key="DataViewMode" Value="False" />
		   </ActiveList>
		 </Action>
	   </Actions>
	 </Controller>
	 ```

   ***

4. If the `Active` or `Enabled` attributes for the **Controller** or **Action** element return `False`, look at each individual item under the nested `ActiveList` and `EnabledList` elements. The `Key` attribute of each property briefly describes why the Action or Controller is active or not. A superposition of all Value attributes for these nested items forms the resulting **Active** or **Enabled** value for the parent Action or its Controller.

## DiagnosticInfo Reference
When you select the **Actions Info** item, the invoked window displays the following information:

{|
|-

! Section
! Definition
|-

| Template
| Specifies the current Window's context name and Template's type name.
|-

| Template | DefaultActionContainer
| Specifies the name of the current Template's default Action Container (see  [IFrameTemplate.DefaultContainer](xref:DevExpress.ExpressApp.Templates.IFrameTemplate.DefaultContainer)).
|-

| Template | DefaultActionContainer | Actions
| Lists the Actions registered in the default Action Container (see [IActionContainer.Actions](xref:DevExpress.ExpressApp.Templates.IActionContainer.Actions)).
|-

| Template | DefaultActionContainer | Actions | Action
| Specifies an Action's ID (see [ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id)).
|-

| Template | ActionContainers
| Lists the current Template's Action Containers.
|-

| Template | ActionContainers | Container
| Specifies an Action Container's name.
|-

| Template | ActionContainers | Container | Actions
| Lists the Actions registered in the current Action Container (see [IActionContainer.Actions](xref:DevExpress.ExpressApp.Templates.IActionContainer.Actions)).
|-

| Template | ActionContainers | Container | Actions | Action
| Specifies an Action's ID (see [ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id)).
|-

| Controllers
| Lists all Controllers loaded to the Application Model.
|-

| Controllers | Controller
| Specifies a Controller's name and the Active state (see [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active)).
|-

| Controllers | Controller | ActiveList
| Allows you to compare the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection items' state with the expected state.
|-

| Controllers | Controller | ActiveList | Item
| Specifies the key and value of an item from the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) list.
|-

| Controllers | Controller | Actions
| Lists the Actions contained in the current Controller (see [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions)).
|-

| Controllers | Controller | Actions | Action
| Specifies the following Action details.

* ID ([ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id))
* Caption ([ActionBase.Caption](xref:DevExpress.ExpressApp.Actions.ActionBase.Caption))
* TypeName
* Category (see [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category))
* Active state (see [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active))
* Enabled state (see [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled))
* Additional info specified by the Action's [ActionBase.DiagnosticInfo](xref:DevExpress.ExpressApp.Actions.ActionBase.DiagnosticInfo) property (see below)
|-

| Controllers | Controller | Actions | Action | ActiveList
| Allows you to compare the [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) collection items' state with an expected state.
|-

| Controllers | Controller | Actions | Action | ActiveList | Item
| Specifies the key and value of an item from the [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active)list.
|-

| Controllers | Controller | Actions | Action | EnabledList
| Allows you to compare the [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) collection items' state with the expected state.
|-

| Controllers | Controller | Actions | Action | EnabledList | Item
| Specifies the key and value of an item from the [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) list.
|-

| Controllers | Controller | Actions | Action | Items (for Actions of the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) type)
| Lists items contained in the [ChoiceActionItem.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Items) collection.
|-

| Controllers | Controller | Actions | Action | Items | Item (for Actions of the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) type)
| Describes an item: its caption, Active and Enabled states. If the item has a collection of nested items (see [ChoiceActionItem.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Items)), they are also listed and described.
|-

| Controllers | Controller | Actions | Action | Items | Item | ActiveList (for Actions of the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) type)
| Allows you to compare the [ChoiceActionItem.Active](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Active) collection items state with the expected state.
|-

| Controllers | Controller | Actions | Action | Items | Item | ActiveList | Item (for Actions of the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) type)
| Specifies the key and value of an item from the [ChoiceActionItem.Active](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Active) list.
|-

| Controllers | Controller | Actions | Action | Items | Item | EnabledList (for Actions of the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) type)
| Allows you to compare the [ChoiceActionItem.Enabled](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Enabled) collection items' state with the expected state.
|-

| Controllers | Controller | Actions | Action | Items | Item | EnabledList | Item (for Actions of the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) type)
| Specifies the key and value of an item from the [ChoiceActionItem.Enabled](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Enabled) list.
|}

The information presented in the invoked window when the **View Info** item is selected includes the following:

{|
|-

! Section
! Definition
|-

| DetailView
| Describes the current View. Writes values of the following properties.

* [View.Id](xref:DevExpress.ExpressApp.View.Id)
* [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)
* [View.AllowNew](xref:DevExpress.ExpressApp.View.AllowNew)
* [View.AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit)
* [View.AllowDelete](xref:DevExpress.ExpressApp.View.AllowDelete)
|-

| DetailView | AllowNewList
| Allows you to compare the [View.AllowNew](xref:DevExpress.ExpressApp.View.AllowNew) collection items' state with the expected state.
|-

| DetailView | AllowNewList | Item
| Specifies the key and value of an item from the [View.AllowNew](xref:DevExpress.ExpressApp.View.AllowNew) list.
|-

| DetailView | AllowEditList
| Allows you to compare the [View.AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit) collection items' state with the expected state.
|-

| DetailView | AllowEditList | Item
| Specifies the key and value of an item from the [View.AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit) list.
|-

| DetailView | AllowDeleteList
| Allows you to compare the [View.AllowDelete](xref:DevExpress.ExpressApp.View.AllowDelete) collection items' state with the expected state.
|-

| DetailView | AllowDeleteList | Item
| Specifies the key and value of an item from the [View.AllowDelete](xref:DevExpress.ExpressApp.View.AllowDelete) list.
|-

| DetailView | PropertyEditors
| Lists the Property Editors contained in the current View.
|-

| DetailView | PropertyEditors | PropertyEditor
| Describes a Property Editor:

* Type
* [PropertyEditor.Caption](xref:DevExpress.ExpressApp.Editors.PropertyEditor.Caption)
* [PropertyEditor.PropertyName](xref:DevExpress.ExpressApp.Editors.PropertyEditor.PropertyName)
* [PropertyEditor.AllowEdit](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit)
|-

| DetailView | PropertyEditors | PropertyEditor | AllowEditList
| Allows you to compare the [PropertyEditor.AllowEdit](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit) collection items' state with the expected state.
|-

| DetailView | PropertyEditors | PropertyEditor | AllowEditList | Item
| Specifies the key and value of an item from the [PropertyEditor.AllowEdit](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit) list.
|-

| ListView
| Describes the current List View. Writes values of the following properties:

* [View.Id](xref:DevExpress.ExpressApp.View.Id)
* [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)
* [View.AllowNew](xref:DevExpress.ExpressApp.View.AllowNew)
* [View.AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit)
* [View.AllowDelete](xref:DevExpress.ExpressApp.View.AllowDelete)
|-

| ListView | AllowNewList
| Allows you to compare the [View.AllowNew](xref:DevExpress.ExpressApp.View.AllowNew) collection items' state with the expected state.
|-

| ListView | AllowNewList | Item
| Specifies the key and value of an item from the [View.AllowNew](xref:DevExpress.ExpressApp.View.AllowNew) list.
|-

| ListView | AllowEditList
| Allows you to compare the [View.AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit) collection items' state with the expected state.
|-

| ListView | AllowEditList | Item
| Specifies the key and value of an item from the [View.AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit) list.
|-

| ListView | AllowDeleteList
| Allows you to compare the [View.AllowDelete](xref:DevExpress.ExpressApp.View.AllowDelete) collection items' state with an expected state.
|-

| ListView | AllowDeleteList | Item
| Specifies the key and value of an item from the [View.AllowDelete](xref:DevExpress.ExpressApp.View.AllowDelete) list.
|-

| ListView | ListEditor
| Describes the current List View's Editor (see [](xref:DevExpress.ExpressApp.Editors.ListEditor)). Writes values of the following properties.

* Type
* [ListEditor.Name](xref:DevExpress.ExpressApp.Editors.ListEditor.Name)
* [ListEditor.AllowEdit](xref:DevExpress.ExpressApp.Editors.ListEditor.AllowEdit)
|}

The information presented in the window invoked when the **Rules Info** item is selected includes the following.

| Section | Definition |
|---|---|
| Rules | Lists all validation rules registered in the Application Model. |

## Custom Diagnostic Information on Actions

You can supply custom diagnostic information on an Action. To do this, use the [ActionBase.DiagnosticInfo](xref:DevExpress.ExpressApp.Actions.ActionBase.DiagnosticInfo) property. Its value will be assigned to the **AdditionalInfo** item within the Controllers | Controller | Actions | Action section. In the following code, the **DiagnosticInfo** property is specified for the **SetPriorityAction** from the **SetPriorityController**, which is implemented in the MainDemo (see [](xref:402159)):

# [C#](#tab/tabid-csharp)

```csharp
public partial class SetPriorityController : ViewController {
   //...
   private void SetPriorityController_AfterConstruction(object sender, EventArgs e) {
      SetPriorityAction.DiagnosticInfo += "\r\n" + "Hello!";
   }
   // ...
}
```
***

The diagnostic info snippet below demonstrates the state of the **SetPriorityController** and its **SetPriorityAction** when a Contact is displayed in the main Window.

# [XML](#tab/tabid-xml1)

```XML
<Controller Name="SetPriorityController" 
            FullName="MainDemo.Module.SetPriorityController" Active="True">
  <ActiveList>
    <Item Key="View is assigned" Value="True" />
    <Item Key="Activating is allowed" Value="True" />
    <Item Key="!ViewChanging.Cancel" Value="True" />
  </ActiveList>
  <Actions>
    <Action ID="SetPriorityAction" TypeName="SingleChoiceAction" 
         Category="RecordEdit" Active="False" Enabled="True" AdditionalInfo="Hello!">
      <ActiveList>
        <Item Key="EmptyItems" Value="True" />
        <Item Key="Controller active" Value="True" />
        <Item Key="ObjectType" Value="False" />
        <Item Key="HideActionsViewController" Value="True" />
      </ActiveList>
      <EnabledList>
        <Item Key="EmptyItems" Value="True" />
        <Item Key="ByContext_RequireMultipleObjects" Value="True" />
      </EnabledList>
    </Action>
  </Actions>
</Controller>
```

***

The **SetPriorityAction** is activated in the main Window when a Task is displayed and the diagnostic information above confirms that this Action is currently deactivated.
