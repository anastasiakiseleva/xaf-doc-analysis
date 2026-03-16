---
uid: DevExpress.ExpressApp.Actions.ParametrizedAction.ValueChanged
name: ValueChanged
type: Event
summary: Occurs after an end-user has typed and submitted a parameter in the Action's editor, and after the [ParametrizedAction.Value](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Value) property has been changed in code.
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler ValueChanged
seealso: []
---
Handle this event to execute custom code in response to a change in the current Parametrized Action's [ParametrizedAction.Value](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Value) property. If you need to respond to the Action's execution, handle the [ParametrizedAction.Execute](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Execute) event, which is raised after the **ValueChanged** event.

> [!NOTE]
> An end-user can submit the typed parameter by pressing ENTER (in WinForms applications) or the button that accompanies the editor. So, do not use this event if you want to execute your code immediately after a value is selected in the editor. In this case, access the editor as described in the [How to: Customize Action Controls](xref:113183) topic.