---
uid: DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView
name: ProcessCreatedView
type: Event
summary: Occurs after the [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed) event.
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler<ActionBaseEventArgs> ProcessCreatedView
seealso: []
---
The main entry point of Actions is their **Execute** event. This event is raised when an end-user performs a predefined operation, which is specified in a different way in each Action type. For instance, if you add an Action of the [](xref:DevExpress.ExpressApp.Actions.SimpleAction) type, the **Execute** event is raised when an end-user clicks the button that corresponds to this Action. See the [](xref:DevExpress.ExpressApp.Actions.SimpleAction), [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction), [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction), [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) and [](xref:DevExpress.ExpressApp.Actions.ActionUrl) classes, for details.

Handle the **ProcessCreatedView** event, to perform custom actions with the View created via the **Execute** event handler's [ActionBaseEventArgs.ShowViewParameters](xref:DevExpress.ExpressApp.Actions.ActionBaseEventArgs.ShowViewParameters) parameter. To execute custom code after this View has been shown, handle the [ActionBase.ExecuteCompleted](xref:DevExpress.ExpressApp.Actions.ActionBase.ExecuteCompleted) event.

> [!NOTE]
> A [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) does not raise the **ProcessCreatedView** event. This is because such an Action creates a View before the **Executed** event is raised.