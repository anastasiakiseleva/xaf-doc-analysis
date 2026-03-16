---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventHandler
name: PopupWindowShowActionExecuteEventHandler
type: Delegate
summary: Represents a method that will handle the [PopupWindowShowAction.Execute](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute) event.
syntax:
  content: public delegate void PopupWindowShowActionExecuteEventHandler(object sender, PopupWindowShowActionExecuteEventArgs e);
  parameters:
  - id: sender
    type: System.Object
    description: ''
  - id: e
    type: DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs
    description: ''
seealso: []
---
When creating a **PopupWindowShowActionExecuteEventHandler** delegate, you identify the method that will handle the corresponding event. To associate an event with your event handler, add a delegate instance to this event. The event handler is called whenever the event occurs unless you remove the delegate. For more information on event handler delegates, see [Handling and Raising Events](https://learn.microsoft.com/en-us/dotnet/standard/events/).
