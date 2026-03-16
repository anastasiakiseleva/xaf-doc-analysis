---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowAction.DoExecute(DevExpress.ExpressApp.Window)
name: DoExecute(Window)
type: Method
summary: Raises the [ActionBase.Executing](xref:DevExpress.ExpressApp.Actions.ActionBase.Executing), [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute), [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed), [ActionBase.ProcessCreatedView](xref:DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView) and [ActionBase.ExecuteCompleted](xref:DevExpress.ExpressApp.Actions.ActionBase.ExecuteCompleted) events one after another, and determines whether to close a Pop-up Window Show Action's pop-up Window.
syntax:
  content: public bool DoExecute(Window window)
  parameters:
  - id: window
    type: DevExpress.ExpressApp.Window
    description: A [](xref:DevExpress.ExpressApp.Window) object that represents the current Pop-up Window Show Action's pop-up Window.
  return:
    type: System.Boolean
    description: "**true** if the current Pop-up Window Show Action's pop-up Window must be closed; otherwise, **false**."
seealso: []
---
[!include[<* "Related GitHub Examples" section of the [SimpleAction.DoExecute](xref:DevExpress.ExpressApp.Actions.SimpleAction.DoExecute) topic.><* "Related GitHub Examples" section of the [ParametrizedAction.DoExecute(Object)](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.DoExecute(System.Object)) topic.>](~/templates/execute-actions-programmatically.md)]