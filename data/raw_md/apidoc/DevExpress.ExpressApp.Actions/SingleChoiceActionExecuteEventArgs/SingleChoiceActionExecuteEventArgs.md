---
uid: DevExpress.ExpressApp.Actions.SingleChoiceActionExecuteEventArgs
name: SingleChoiceActionExecuteEventArgs
type: Class
summary: Represents arguments passed to a Single Choice Action's [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event.
syntax:
  content: 'public class SingleChoiceActionExecuteEventArgs : SimpleActionExecuteEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Actions.SingleChoiceActionExecuteEventArgs._members
  altText: SingleChoiceActionExecuteEventArgs Members
---
The **SingleChoiceActionExecuteEventArgs** class declares the [SingleChoiceActionExecuteEventArgs.SelectedChoiceActionItem](xref:DevExpress.ExpressApp.Actions.SingleChoiceActionExecuteEventArgs.SelectedChoiceActionItem) property specific to the [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event. You can handle this event to execute custom code when clicking an item in the Single Choice Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection.

This class is inherited from the [](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs) class. Use the inherited [SimpleActionExecuteEventArgs.CurrentObject](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.CurrentObject) and [SimpleActionExecuteEventArgs.SelectedObjects](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.SelectedObjects) properties to access the current and selected objects of the [View](xref:112611) for which the Action is activated.