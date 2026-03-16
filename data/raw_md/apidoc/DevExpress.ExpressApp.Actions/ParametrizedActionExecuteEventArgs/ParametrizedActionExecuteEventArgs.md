---
uid: DevExpress.ExpressApp.Actions.ParametrizedActionExecuteEventArgs
name: ParametrizedActionExecuteEventArgs
type: Class
summary: Represents arguments passed to a Parametrized Action's [ParametrizedAction.Execute](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Execute) event.
syntax:
  content: 'public class ParametrizedActionExecuteEventArgs : SimpleActionExecuteEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Actions.ParametrizedActionExecuteEventArgs._members
  altText: ParametrizedActionExecuteEventArgs Members
---
The **ParametrizedActionExecuteEventArgs** class declares the [ParametrizedActionExecuteEventArgs.ParameterCurrentValue](xref:DevExpress.ExpressApp.Actions.ParametrizedActionExecuteEventArgs.ParameterCurrentValue) property specific to the [ParametrizedAction.Execute](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Execute) event. You can handle this event to execute custom code when entering a value to the Single Choice Action's control.

This class is inherited from the [](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs) class. Use the inherited [SimpleActionExecuteEventArgs.CurrentObject](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.CurrentObject) and [SimpleActionExecuteEventArgs.SelectedObjects](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.SelectedObjects) properties to access the current and selected objects of the View for which the Action is activated.