---
uid: DevExpress.ExpressApp.Actions.ActionBase.Executed
name: Executed
type: Event
summary: Occurs after executing an [Action](xref:112622).
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler<ActionBaseEventArgs> Executed
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView
- linkId: DevExpress.ExpressApp.Actions.ActionBase.ExecuteCompleted
- linkId: "403731"
---
The main entry point of Actions is their **Execute** event. This event is raised when an end-user performs a predefined operation, which is specified in a different way in each Action type. For instance, if you add an Action of the [](xref:DevExpress.ExpressApp.Actions.SimpleAction) type, the **Execute** event is raised when an end-user clicks the button that corresponds to this Action. See the [](xref:DevExpress.ExpressApp.Actions.SimpleAction), [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction), [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction), [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) and [](xref:DevExpress.ExpressApp.Actions.ActionUrl) classes, for details.

The **Executed** event is raised after the **Execute** event. Generally, you do not need to handle it, because the **Execute** event is appropriate for most tasks.