---
uid: DevExpress.ExpressApp.Actions.ChoiceActionBase.BehaviorChanged
name: BehaviorChanged
type: Event
summary: Occurs when the [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase) Action behavior is modified.
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler<ChoiceActionBehaviorChangedEventArgs> BehaviorChanged
seealso: []
---
The **BehaviorChanged** event is invoked as the result of executing the setters of the following properties:

* [ChoiceActionBase.ImageMode](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ImageMode)
* [ChoiceActionBase.DefaultItemMode](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.DefaultItemMode)
* [ChoiceActionBase.ShowItemsOnClick](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ShowItemsOnClick)

The event is invoked only if the new value differs from the previous one.

Handle this event to implement a custom logic to be executed when the Action's behavior is changed.