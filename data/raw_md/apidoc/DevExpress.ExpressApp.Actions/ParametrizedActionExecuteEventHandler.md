---
uid: DevExpress.ExpressApp.Actions.ParametrizedActionExecuteEventHandler
name: ParametrizedActionExecuteEventHandler
type: Delegate
summary: Represents a method that will handle the [ParametrizedAction.Execute](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Execute) event.
syntax:
  content: public delegate void ParametrizedActionExecuteEventHandler(object sender, ParametrizedActionExecuteEventArgs e);
  parameters:
  - id: sender
    type: System.Object
    description: ''
  - id: e
    type: DevExpress.ExpressApp.Actions.ParametrizedActionExecuteEventArgs
    description: ''
seealso: []
---
When creating a **ParametrizedActionExecuteEventHandler** delegate, you identify the method that will handle the corresponding event. To associate an event with your event handler, add a delegate instance to this event. The event handler is called whenever the event occurs unless you remove the delegate. For more information on event handler delegates, see [Handling and Raising Events](https://learn.microsoft.com/en-us/dotnet/standard/events/).
