---
uid: "113484"
seealso:
- linkId: "112818"
title: Determine an Action's Controller and Identifier
---
# Determine an Action's Controller and Identifier

If you wish to customize an [Action](xref:112622) provided by XAF (or a third-party module), you should know which [Controller](xref:112621) provides this Action. When the Controller is known, you can [override it](xref:112676) or access it using the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method, and handle the required events. In certain cases, you may also require an Action's identifier (e.g., to create a [Conditional Appearance](xref:113286) rule). This topic describes how to determine the Controller that hosts a particular Action and how to get the Action identifier.

## Determine a Controller and Identifier at Runtime
When you execute an Action in your application, the Action information is displayed in the Visual Studio [Output Window](https://learn.microsoft.com/en-us/visualstudio/ide/reference/output-window) (and also is appended to the [log file](xref:112575)).

```
04.09.14 11:57:49.966	Execute action
04.09.14 11:57:49.968		Type: DevExpress.ExpressApp.Actions.SingleChoiceAction
04.09.14 11:57:49.970		ID: ChooseSkin
04.09.14 11:57:49.972		Category: Appearance
04.09.14 11:57:49.974		Controller.Name: DevExpress.ExpressApp.Win.SystemModule.ChooseSkinController
04.09.14 11:57:49.975		Context.Name: Contact
04.09.14 11:57:49.976		Context.IsRoot: True
04.09.14 11:57:49.978		Context.SelectedObjects.Count: 0
04.09.14 11:57:49.980		Context.CurrentObject: <not specified>
04.09.14 11:57:49.983		SelectedItem: Visual Studio 2013 Blue
04.09.14 11:57:50.377	Action 'ChooseSkin' done
```

Here, the **Controller.Name** value is the name of the executed Action's Controller and the **ID** value is the Action's identifier.

## Determine a Controller at Design Time
If you know the Action's identifier, you can determine the Action's Controller in the [Model Editor](xref:112582) using the [IModelAction.Controller](xref:DevExpress.ExpressApp.Model.IModelAction.Controller) property of the [!include[Node_Action](~/templates/node_action111373.md)] node. In the Model Editor, Action identifiers (see [ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id)) are used as **Action** node captions, instead of captions visible in the UI. Thus, to easily locate an Action is the Model Editor, you must know its identifier.

![IModelAction.Controller](~/images/imodelaction.controller117534.png)

If the identifier is unknown, use the [IModelAction.Caption](xref:DevExpress.ExpressApp.Model.IModelAction.Caption) property that specifies the Action caption visible to users to check if this is the Action you are looking for.

## Actions Added via the Action Attribute
Actions defined via the [](xref:DevExpress.Persistent.Base.ActionAttribute) are generated at runtime by the **ObjectMethodActionsViewController**. Identifiers of these Actions are formed using the following pattern:

``<business_class_short_name>.<action_method_name>``

If the Action method takes a parameter, then the method parameter type name is also appended.

``<business_class_short_name>.<action_method_name>.<parameter_type_short_name>``

For instance, to access an Action declared in the **Task** business class via the **MarkCompleted** method, use the following code:

[!include[controller_actions_dictionary_example](~/templates/controller_actions_dictionary_example.md)]

To access an Action declared in the **Task** business class via the **Postpone** method taking the **PostponeParametersObject** type parameter, use the following code:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Actions;
// ...
ObjectMethodActionsViewController controller = Frame.GetController<ObjectMethodActionsViewController>();
if (controller != null) {
    PopupWindowShowAction postponeAction = controller.Actions["Task.Postpone.PostponeParametersObject"] as PopupWindowShowAction;
    // ...
}
```
***

## Help Topics that List Built-in Controllers and their Actions
You can search through the [Built-in Controllers and Actions](xref:113016) section of this documentation to find the required Action and its Controller.

> [!NOTE]
> You can also search an Action by its identifier or caption in XAF sources which are installed to _[!include[PathToXafInstallation](~/templates/path-to-installation.md)]Sources\_ by default.
