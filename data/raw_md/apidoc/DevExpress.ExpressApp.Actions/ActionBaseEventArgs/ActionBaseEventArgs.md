---
uid: DevExpress.ExpressApp.Actions.ActionBaseEventArgs
name: ActionBaseEventArgs
type: Class
summary: Represents the base class for arguments passed to [Action](xref:112622) execution handling events.
syntax:
  content: 'public class ActionBaseEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBaseEventArgs._members
  altText: ActionBaseEventArgs Members
- linkId: DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView
---
The **ActionBaseEventArgs** class declares properties specific to the **Execute**, [ActionBase.Executed](xref:DevExpress.ExpressApp.Actions.ActionBase.Executed), [ActionBase.ProcessCreatedView](xref:DevExpress.ExpressApp.Actions.ActionBase.ProcessCreatedView) and [ActionBase.ExecuteCompleted](xref:DevExpress.ExpressApp.Actions.ActionBase.ExecuteCompleted) events designed to execute custom code when executing an Action.

This class has the [](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs) descendant which declares additional properties specific to the [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event.