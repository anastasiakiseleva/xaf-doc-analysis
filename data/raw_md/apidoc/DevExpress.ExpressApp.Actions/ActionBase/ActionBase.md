---
uid: DevExpress.ExpressApp.Actions.ActionBase
name: ActionBase
type: Class
summary: The base class for [Actions](xref:112622).
syntax:
  content: 'public abstract class ActionBase : Component, ISupportUpdate, ISupportClientScripts, ISecuredAction'
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase._members
  altText: ActionBase Members
---
Actions are abstract UI elements that allow you to perform specific operations in response to an end-user's manipulations (see the [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event definition). Actions are contained within [Controllers](xref:112621) in their [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) lists. An Action's presence in a particular [Window (Frame)](xref:112608) depends on whether the corresponding Controller is active in it. Note that you can also specify the availability context for individual Actions via their properties.

The [](xref:DevExpress.ExpressApp.Actions.ActionBase) class is the base class for all Action types. This class provides events, properties and methods that support the common Action behavior. They are:

* The [ActionBase.Executing](xref:DevExpress.ExpressApp.Actions.ActionBase.Executing) and [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed) events are used to execute custom code before and after executing an Action.
* The [ActionBase.Controller](xref:DevExpress.ExpressApp.Actions.ActionBase.Controller) property provides access to the parent Controller.
* The [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) and [ActionBase.Changed](xref:DevExpress.ExpressApp.Actions.ActionBase.Changed) members provide the Action activation mechanism.
* The [ActionBase.TargetObjectType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType), [ActionBase.TargetViewId](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewId), [ActionBase.TargetViewNesting](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewNesting) [ActionBase.TargetViewType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewType), [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria), [ActionBase.TargetObjectsCriteriaMode](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteriaMode) and [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) properties specify conditions for Action activation (these conditions are checked only for Actions from View Controllers).
* The [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) and [ActionBase.Changed](xref:DevExpress.ExpressApp.Actions.ActionBase.Changed) members represent mechanisms for making an Action enabled/disabled.

The **XAF** supplies several Action types derived from the **Action** class: [](xref:DevExpress.ExpressApp.Actions.SimpleAction), [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction), [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction), [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) and [](xref:DevExpress.ExpressApp.Actions.ActionUrl). Each of these types has a different purpose. For details, see the descriptions of these classes and the [Actions](xref:112622) topic.

To add an Action to a Controller, use on of the approaches described in the following topic: [](xref:400495). Information specified for an Action in the Controller's Designer or the Controller's constructor in code is loaded to the [Application Model](xref:112580). You can view all the Actions that will be created in your application. To do this, invoke the Model Editor and navigate to the **ActionDesign** | **Actions** node. Information on Actions is represented by properties of the **Action** child nodes. These properties can be initially set to default values or the values that you specified in the Controller's constructor or in the Controller's Designer. You can modify these values if the properties are not read-only.

Actions of the **SimpleAction** and **PopupWindowShowAction** types can be also added via the [](xref:DevExpress.Persistent.Base.ActionAttribute) attribute. Refer to the [How to: Create an Action Using the Action Attribute](xref:112619) topic to see an example.

In this documentation, built-in Actions are referred to by their identifiers specified by [ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id) property. To find out what caption is assigned to a particular Action, use the Model Editor.

## Execute Actions Programmatically

[!include[<* "Related GitHub Examples" section of the [SimpleAction.DoExecute](xref:DevExpress.ExpressApp.Actions.SimpleAction.DoExecute) topic.><* "Related GitHub Examples" section of the [ParametrizedAction.DoExecute(Object)](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.DoExecute(System.Object)) topic.>](~/templates/execute-actions-programmatically.md)]
