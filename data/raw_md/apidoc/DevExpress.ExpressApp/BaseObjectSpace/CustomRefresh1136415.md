---
uid: DevExpress.ExpressApp.BaseObjectSpace.CustomRefresh
name: CustomRefresh
type: Event
summary: Occurs to replace the default process of refreshing persistent objects with a custom one.
syntax:
  content: public event EventHandler<HandledEventArgs> CustomRefresh
seealso: []
---
The **CustomRefresh** event is raised as a result of calling the [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) method. Handle this event to provide a custom process for refreshing the current Object Space's persistent objects. Set the handler's **CompletedEventArgs.Handled** parameter to **true** to indicate that the refresh operation has already been performed. Set the handler's **CompletedEventArgs.IsCompleted** parameter to **true**, in the case of a successful refresh; otherwise, set it to **false**. This value will be returned by the [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) method.