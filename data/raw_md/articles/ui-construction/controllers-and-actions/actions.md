---
uid: "112622"
seealso: []
title: Actions (Menu Commands)
---
# Actions (Menu Commands)

This article provides general information about Actions:
* [Action Definition](#action-definition)
* [Action Types](#action-types)
* [Action Locations](#action-locations)
* [Action Implementation and Customization](#action-implementation-and-customization)

## Action Definition

Actions are abstract [UI elements](xref:112607) that allow end-users to interact with XAF applications.

In the UI, XAF can display Actions as the following controls:

| Control Name | Control Appearance |
|---|---|
| A toolbar button |![toolbarbutton](~/images/ActionControl-Button.png) |
| A context menu item | ![contextmenuitem](~/images/ActionControl-ContextMenuItem.png) |
| An editor | ![search](~/images/ActionControl-Search.png) |
| A simple button | ![simpleaction](~/images/ActionControl-SimpleAction.png) |
| Other controls | - |

You can access and modify the control associated with an Action in the [ActionBase.CustomizeControl](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) event handler.

## Action Types

XAF Actions can be of different types:
* [](xref:DevExpress.ExpressApp.Actions.SimpleAction)
* [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction)
* [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction)
* [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction)
* [](xref:DevExpress.ExpressApp.Actions.ActionUrl)

You can also [create custom Action types and custom controls](xref:400495#create-custom-action-types-and-custom-controls).

Actions are located in [Action Containers](xref:112610). To access all Actions in an Action Container, use the container's [IActionContainer.Actions](xref:DevExpress.ExpressApp.Templates.IActionContainer.Actions) property.

Actions belong to [Controllers](xref:112621). Use the [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) property to access a Controller's Action collection.

## Action Locations

XAF places Actions in the locations listed below. 

* [Menu: Main Toolbar](xref:400496)
* [Menu: Nested Toolbar](xref:400497)
* [Navigation](xref:400499)
* [Popup Window](xref:400500)
* [Lookup List View](xref:400501)
* [Detail View](xref:400502)
* [Other Menus](xref:400498)

## Action Implementation and Customization

You can customize Actions in your application in two ways:

* [Perform Common Tasks with XAF Actions](xref:400495)
* [Access Actions in Different UI Areas](xref:400494)

You can also [create custom Action types and custom controls](xref:400495#create-custom-action-types-and-custom-controls).
