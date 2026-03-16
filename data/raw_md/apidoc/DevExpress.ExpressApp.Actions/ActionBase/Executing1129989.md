---
uid: DevExpress.ExpressApp.Actions.ActionBase.Executing
name: Executing
type: Event
summary: Occurs before an end-user performs the operation that leads to raising an [Action](xref:112622)'s **Execute** event.
syntax:
  content: |-
    [Browsable(false)]
    public event CancelEventHandler Executing
seealso: []
---
The main entry point of Actions is their **Execute** event. This event is raised when an end-user performs a predefined operation, specified in different ways for each Action type. For instance, if you add an Action of the [](xref:DevExpress.ExpressApp.Actions.SimpleAction) type, the **Execute** event is raised when an end-user clicks the button that corresponds to this Action. See the [](xref:DevExpress.ExpressApp.Actions.SimpleAction), [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction), [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction), [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) and [](xref:DevExpress.ExpressApp.Actions.ActionUrl) classes, for details.

Handle the **Executing** event to cancel execution of the current Action. For this purpose, set the handler's **CancelEventHandler.Cancel** parameter to **true**. In this instance, the [ActionBase.ExecuteCanceled](xref:DevExpress.ExpressApp.Actions.ActionBase.ExecuteCanceled) event will be raised.