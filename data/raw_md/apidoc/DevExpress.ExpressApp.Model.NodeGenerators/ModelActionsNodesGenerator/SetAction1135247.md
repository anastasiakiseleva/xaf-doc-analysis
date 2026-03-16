---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelActionsNodesGenerator.SetAction(DevExpress.ExpressApp.Model.IModelAction,DevExpress.ExpressApp.Actions.ActionBase)
name: SetAction(IModelAction, ActionBase)
type: Method
summary: Associates the [](xref:DevExpress.ExpressApp.Model.IModelAction) node with the specified [Action](xref:112622) .
syntax:
  content: public static void SetAction(IModelAction modelAction, ActionBase action)
  parameters:
  - id: modelAction
    type: DevExpress.ExpressApp.Model.IModelAction
    description: An **IModelAction** node which represents the Action settings.
  - id: action
    type: DevExpress.ExpressApp.Actions.ActionBase
    description: An [](xref:DevExpress.ExpressApp.Actions.ActionBase) Action to be associated with the specified **IModelAction** node.
seealso: []
---
Additionally, this method updates the [IModelAction.Caption](xref:DevExpress.ExpressApp.Model.IModelAction.Caption) property with the [ActionBase.Caption](xref:DevExpress.ExpressApp.Actions.ActionBase.Caption) value.