---
uid: DevExpress.ExpressApp.IObjectSpace.RollingBack
name: RollingBack
type: Event
summary: Occurs before rolling back the changes made to the current Object Space's persistent objects.
syntax:
  content: event EventHandler<CancelEventArgs> RollingBack
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.CustomRollBack
- linkId: DevExpress.ExpressApp.IObjectSpace.Reloaded
---
The **RollingBack** event is raised before updating persistent objects as a result of calling the [IObjectSpace.Rollback](xref:DevExpress.ExpressApp.IObjectSpace.Rollback(System.Boolean)) method. Handle this event to prevent objects from rolling back. For this purpose, set the handler's **CancelEventArgs.Cancel** parameter to **true**. By default, this parameter is set to **false**.

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you should override the **BaseObjectSpace.Reload** method which is called by the [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) method. In this instance, you won't have to raise the **RollingBack** event, since it is raised by the **BaseObjectSpace.Rollback** method.