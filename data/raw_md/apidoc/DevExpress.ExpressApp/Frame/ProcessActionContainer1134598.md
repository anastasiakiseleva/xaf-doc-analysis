---
uid: DevExpress.ExpressApp.Frame.ProcessActionContainer
name: ProcessActionContainer
type: Event
summary: Occurs when the [Action Containers](xref:112610) displayed in the current [](xref:DevExpress.ExpressApp.Frame) are changed.
syntax:
  content: public event EventHandler<ProcessActionContainerEventArgs> ProcessActionContainer
seealso: []
---
Handle the `ProcessActionContainer` event to customize Action Containers. This event fires when you execute the [Frame.SetView](xref:DevExpress.ExpressApp.Frame.SetView*) and [Frame.SetTemplate](xref:DevExpress.ExpressApp.Frame.SetTemplate(DevExpress.ExpressApp.Templates.IFrameTemplate)) methods. If the Frame is [nested](xref:DevExpress.ExpressApp.NestedFrame), the event also fires when Action Containers are registered and unregistered.

To customize an Action's control, use the [](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl) event.
