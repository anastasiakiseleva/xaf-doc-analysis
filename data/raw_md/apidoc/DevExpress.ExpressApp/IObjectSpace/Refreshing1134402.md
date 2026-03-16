---
uid: DevExpress.ExpressApp.IObjectSpace.Refreshing
name: Refreshing
type: Event
summary: Occurs before refreshing the current Object Space's persistent objects.
syntax:
  content: event EventHandler<CancelEventArgs> Refreshing
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.CustomRefresh
- linkId: DevExpress.ExpressApp.IObjectSpace.Reloaded
---
The **Refreshing** event is raised before updating persistent objects as a result of calling the [IObjectSpace.Refresh](xref:DevExpress.ExpressApp.IObjectSpace.Refresh) method. Handle this event to prevent objects refresh. For this purpose, set the handler's **CancelEventArgs.Cancel** parameter to **true**. By default, this parameter is set to **false**.

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you should override the **BaseObjectSpace.Reload** method which is called by the [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) method. In this instance, you won't have to raise the **Refreshing** event, since it is raised by the **BaseObjectSpace.Refresh** method.