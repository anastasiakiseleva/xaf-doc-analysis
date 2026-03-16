---
uid: '400495'
seealso: []
title: Perform Common Tasks With XAF Actions
owner: Vera Ulitina
---
# Perform Common Tasks With XAF Actions

This article describes the most common tasks with XAF [Actions](xref:112622). 

* [Use Action Settings](#use-action-settings)
* [Add an Action to a Controller](#add-an-action-to-a-controller)
* [Add an Action by applying the Action attribute to a business class method](#add-an-action-by-applying-the-action-attribute-to-a-business-class-method)
* [Customize an Action in the Application Model](#customize-an-action-in-the-application-model)
* [Customize an Action in code](#customize-an-action-in-code)
* [Create custom Action types and custom controls](#create-custom-action-types-and-custom-controls)
* [Troubleshoot Actions](#troubleshoot-actions)
* [Execute Actions Programmatically](#execute-actions-programmatically)

## Add an Action to a Controller

If you require an [Action](xref:112622) that applies to multiple business objects and takes user input, add this Action to a [Controller](xref:112621).

* [](xref:402155)
* [](xref:402158)
* [](xref:402159)

You can also add an Action to a Controller in code.

[!include[](~/templates/add-action.md)]

After you add an Action to a Controller, you can use the Designer to customize the Action.

[!include[Localization-Overview-Intro](~/templates/coderush-templates-actions-controllers.md)]

## Add an Action by Applying the Action Attribute to a Business Class Method

If you require an [Action](xref:112622) that applies to one business object and uses the business object's parameters, apply the Action attribute to the business class's method as shown below: 

* [Getting Started: Add a Simple Action Using an Attribute (.NET)](xref:402156)
* [How to: Create an Action Using the Action Attribute](xref:112619)

Use the Action attribute only for simple scenarios similar to those described in the articles. For greater flexibility, you can [add an Action to a Controller](#add-an-action-to-a-controller).

## Use Action Settings

The base class for all Action types is the [](xref:DevExpress.ExpressApp.Actions.ActionBase) class. This class exposes events, properties, and methods that support the common [Action](xref:112622) behavior.

**Events**

* The [ActionBase.Executing](xref:DevExpress.ExpressApp.Actions.ActionBase.Executing) and [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed) events occur when an end user performs a specified action: clicks a button, selects an item in a combo box, etc.

**Properties**

* [ActionBase.Controller](xref:DevExpress.ExpressApp.Actions.ActionBase.Controller) provides access to the parent Controller.
* [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) determines the Action's active/inactive state and visibility.
* [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) determines an Action's enabled/displayed state. A Disabled Action is visible in the UI, but is grayed out.
* [ActionBase.TargetViewType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewType), [ActionBase.TargetViewNesting](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewNesting), [ActionBase.TargetViewId](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewId), [ActionBase.TargetObjectType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType), [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria), [ActionBase.TargetObjectsCriteriaMode](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteriaMode) and [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) specify conditions for Action activation.
* [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) specifies an Action's category. The category determines the Action's placement in an Action Container.
* [ActionBase.ConfirmationMessage](xref:DevExpress.ExpressApp.Actions.ActionBase.ConfirmationMessage) specifies the confirmation message displayed when an end user executes an Action.
* [ActionBase.Caption](xref:DevExpress.ExpressApp.Actions.ActionBase.Caption) specifies the Action's caption.


> [!TIP]
> Access the [ActionBase](xref:DevExpress.ExpressApp.Actions.ActionBase) class's members page for a complete list of available API.
## Customize an Action in the Application Model

Information on [Actions](xref:112622) is available in the Application Model's **ActionDesign** node.

* [](xref:402145)
* [](xref:402146)
* [](xref:112816)


## Customize an Action in Code

You can access [Actions](xref:112622) and customize them in code.

* [](xref:112676)
* [](xref:113183)
* [](xref:112728)
* [](xref:112815)

## Create Custom Action Types and Custom Controls

In XAF, you can create custom [Action](xref:112622) types and custom controls. See the examples below:

* [Create a custom Action type with a custom control (BarCheckItem) associated with it](https://github.com/DevExpress-Examples/xaf-win-custom-action-with-custom-action-control)

## Troubleshoot Actions

See the articles below to learn how to diagnose and fix the most frequently encountered problems.

* [](xref:112818)
* [](xref:113103)
* [](xref:113484)
* [ActionBase.DiagnosticInfo](xref:DevExpress.ExpressApp.Actions.ActionBase.DiagnosticInfo)

## Execute Actions Programmatically

[!include[<* "Related GitHub Examples" section of the [SimpleAction.DoExecute](xref:DevExpress.ExpressApp.Actions.SimpleAction.DoExecute) topic.><* "Related GitHub Examples" section of the [ParametrizedAction.DoExecute(Object)](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.DoExecute(System.Object)) topic.>](~/templates/execute-actions-programmatically.md)]
