---
uid: DevExpress.ExpressApp.BaseObjectSpace.CustomRollBack
name: CustomRollBack
type: Event
summary: Occurs to replace the default process of persistent objects rollback with a custom one.
syntax:
  content: public event EventHandler<HandledEventArgs> CustomRollBack
seealso: []
---
The **CustomRollBack** event is raised as a result of calling the [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) method. Handle this event to provide a custom process of rolling back the current Object Space's persistent objects. Set the handler's **CompletedEventArgs.Handled** parameter to **true**, to indicate that the rollback has already been performed. Set the handler's **CompletedEventArgs.IsCompleted** parameter to **true** in the case of a successful rollback; otherwise, set **false**. This value will be returned by the [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) method.