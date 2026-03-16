---
uid: "403709"
seealso:
- linkId: "113103"
- linkId: "112728"
title: 'Ways to Hide or Disable an Action (Button, Menu Command)'
owner: Eugenia Simonova
---
# Ways to Hide or Disable an Action (Button, Menu Command)

You can hide or disable an [Action](xref:112622). If an Action (button) is disabled, it is grayed out. The table below shows different Action states. 

{|
|-
! Description
! Image 
|-

|-
| The _Clear tasks_ Action is active.
| ![The Clear tasks Action is active.](~/images/active-action.png)
|-

|-
| The _Clear tasks_ Action is disabled.
| ![The Clear tasks Action is disabled.](~/images/disable-action.png)
|-

|The _Clear tasks_ Action is hidden.
| ![The Clear tasks Action is hidden.](~/images/hide-action.png)
|}

XAF allows you to change the state of custom and built-in Actions. The following topic describes how to identify built-in Actions: [Determine an Action's Controller and Identifier](xref:113484).
## Ways to Disable an Action

You can utilize the following techniques to disable an Action (button, menu item):

* Use the @DevExpress.ExpressApp.Actions.ActionBase.Enabled property. See the following topic for examples: [Deactivate (Hide) an Action in Code](xref:112728).

* Specify the [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) and [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) properties. When conditions specified in these properties are not met, an Action is disabled. Refer to the property descriptions for additional information.

* Use the [Conditional Appearance](xref:113286) module. You can enable and disable Actions based on the specified rules (for example, disable an Action based on business object properties). Refer to the following topic for more information: [Declare Conditional Appearance Rules in Code](xref:113371). See the rule with the **ActionState** ID in the **Examples** section.

## Ways to Hide an Action

You can utilize the following techniques to hide an Action (button, menu item):

* Use the @DevExpress.ExpressApp.Actions.ActionBase.Active property. See the following topic for examples: [Deactivate (Hide) an Action in Code](xref:112728).

* Specify the [ActionBase.TargetObjectType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType), [ActionBase.TargetViewType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewType), [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType), and [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType) properties. Refer to the following topic for details: [Define the Scope of Controllers and Actions](xref:113103).

* Use the [Conditional Appearance](xref:113286) module. You can show and hide Actions based on the specified rules (for example, hide an Action based on business object properties). Refer to the following topic for more information: [Declare Conditional Appearance Rules in Code](xref:113371). See the rule with the **ActionState** ID in the Examples section.

* Use the [Security System](xref:113366). You can define the _Read_, _Write_, _Create_, _Delete_, and _Navigate_ permissions for business classes, objects, and members. Built-in Controllers display Actions according to these permissions. For example, the **Delete** Action is disabled if a user does not have permission to delete the selected objects. 
    
    You can manually specify permissions for custom and system Actions. Refer to the following link for more information: [Action Permissions](xref:404633#action-permissions).
    
    It is also possible to set permissions for custom Actions in code. For more information, refer to the following topics:
    * [](xref:403824)
    * [](xref:113472)

* Specify the [IModelView.AllowNew](xref:DevExpress.ExpressApp.Model.IModelView.AllowNew), [IModelView.AllowDelete](xref:DevExpress.ExpressApp.Model.IModelView.AllowDelete), [IModelView.AllowEdit](xref:DevExpress.ExpressApp.Model.IModelView.AllowEdit), and [IModelCommonMemberViewItem.AllowClear](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.AllowClear) properties in the Application Model. These properties define allowed operations with business objects in a View.
* Use the [](xref:DevExpress.ExpressApp.SystemModule.IModelHiddenActions) node that allows you to hide an Action from a specific View in the [Model Editor](xref:112582).
