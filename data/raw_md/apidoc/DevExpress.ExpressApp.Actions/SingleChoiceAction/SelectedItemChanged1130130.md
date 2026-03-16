---
uid: DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItemChanged
name: SelectedItemChanged
type: Event
summary: Occurs when a Single Choice Action's item is changed by an end-user.
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler SelectedItemChanged
seealso: []
---
Handle this event, to execute custom code in response to manual changing of the current Single Choice Action's [SingleChoiceAction.SelectedItem](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItem) property. If you need to respond to the [SingleChoiceAction.SelectedItem](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItem) property change performed by an end-user, handle the [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event.