---
uid: DevExpress.ExpressApp.Actions.ActionBase.ExecuteCompleted
name: ExecuteCompleted
type: Event
summary: Occurs after all actions implemented in the `Execute`, [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed) and [ActionBase.ProcessCreatedView](xref:DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView) event handlers have been performed.
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler<ActionBaseEventArgs> ExecuteCompleted
seealso: []
---
The main entry point of Actions is their `Execute` event. This event is raised when an end-user performs a predefined operation, which is specified in a different way in each Action type. For instance, if you add an Action of the [](xref:DevExpress.ExpressApp.Actions.SimpleAction) type, the `Execute` event is raised when an end-user clicks the button that corresponds to this Action. See the [](xref:DevExpress.ExpressApp.Actions.SimpleAction), [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction), [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction), [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) and [](xref:DevExpress.ExpressApp.Actions.ActionUrl) classes, for details.

Handle the `ExecuteCompleted` event, to execute custom code after the Action execution has been completed.

> [!NOTE]
> In an Action's `Execute` event handler, you can specify a View to be shown after executing the code implemented in this handler. For this purpose, specify the handler's [ActionBaseEventArgs.ShowViewParameters](xref:DevExpress.ExpressApp.Actions.ActionBaseEventArgs.ShowViewParameters) parameter. To access this View before it is shown, handle the [ActionBase.ProcessCreatedView](xref:DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView) event. To access the View shown, handle the `ExecuteCompleted` event and use the handler's [ActionBaseEventArgs.ShowViewParameters](xref:DevExpress.ExpressApp.Actions.ActionBaseEventArgs.ShowViewParameters) parameter. If a View has not been initialized in the `Execute` or [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed) event handler, the `ExecuteCompleted` event handler's `ShowViewParameters` parameter returns `null`.