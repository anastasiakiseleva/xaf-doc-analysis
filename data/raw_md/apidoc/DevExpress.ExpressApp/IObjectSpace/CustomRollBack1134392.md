---
uid: DevExpress.ExpressApp.IObjectSpace.CustomRollBack
name: CustomRollBack
type: Event
summary: Replaces the default process of persistent objects rollback with a custom one.
syntax:
  content: event EventHandler<HandledEventArgs> CustomRollBack
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.RollingBack
- linkId: DevExpress.ExpressApp.IObjectSpace.Reloaded
---
The **CustomRollBack** event is raised as a result of calling the [IObjectSpace.Rollback](xref:DevExpress.ExpressApp.IObjectSpace.Rollback(System.Boolean)) method. Handle this event to provide a custom process for rolling back the current Object Space's persistent objects. Set the handler's **CompletedEventArgs.Handled** parameter to **true** to indicate that the rollback has already been performed. Set the handler's **CompletedEventArgs.IsCompleted** parameter to **true** in the case of a successful rollback; otherwise, set **false**. This value will be returned by the [IObjectSpace.Rollback](xref:DevExpress.ExpressApp.IObjectSpace.Rollback(System.Boolean)) method.

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you should override the **BaseObjectSpace.Reload** method which is called by the [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) method. In this instance, you won't have to raise the **CustomRollBack** event, since it is raised by the **BaseObjectSpace.Rollback** method.