---
uid: DevExpress.ExpressApp.IObjectSpace.CustomRefresh
name: CustomRefresh
type: Event
summary: Replace the default processes of refreshing persistent objects with a custom one.
syntax:
  content: event EventHandler<HandledEventArgs> CustomRefresh
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.Refreshing
- linkId: DevExpress.ExpressApp.IObjectSpace.Reloaded
---
The **CustomRefresh** event is raised as a result of calling the [IObjectSpace.Refresh](xref:DevExpress.ExpressApp.IObjectSpace.Refresh) method. Handle this event to provide a custom process for refreshing the current Object Space's persistent objects. Set the handler's **CompletedEventArgs.Handled** parameter to **true** to indicate that the refresh operation has been already performed. Set the handler's **CompletedEventArgs.IsCompleted** parameter to **true** in the case of a successful refresh; otherwise, set **false**. This value will be returned by the [IObjectSpace.Refresh](xref:DevExpress.ExpressApp.IObjectSpace.Refresh) method.

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you should override the **BaseObjectSpace.Reload** method which is called by the [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) method. In this instance, you won't have to raise the **CustomRefresh** event, since it is raised by the **BaseObjectSpace.Refresh** method.