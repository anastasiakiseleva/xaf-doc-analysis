---
uid: DevExpress.ExpressApp.Actions.ActionBase.ExecuteCanceled
name: ExecuteCanceled
type: Event
summary: Occurs after execution of the [Action](xref:112622) has been cancelled.
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler<ActionBaseEventArgs> ExecuteCanceled
seealso: []
---
You can cancel execution of an Action by handling the [ActionBase.Executing](xref:DevExpress.ExpressApp.Actions.ActionBase.Executing) event and setting the **CancelEventHandler.Cancel** parameter to **true**. In this instance, the **ExecuteCanceled** event is raised.

Generally, you do not need to handle the **ExecuteCanceled** event.