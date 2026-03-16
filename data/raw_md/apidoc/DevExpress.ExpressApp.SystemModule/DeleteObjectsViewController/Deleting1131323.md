---
uid: DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.Deleting
name: Deleting
type: Event
summary: Occurs before deleting objects.
syntax:
  content: public event EventHandler<DeletingEventArgs> Deleting
seealso: []
---
Handle this event to customize the list of objects to be deleted by the [DeleteObjectsViewController.DeleteAction](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.DeleteAction). By default, this list contains objects that are selected in the current View (see [View.SelectedObjects](xref:DevExpress.ExpressApp.View.SelectedObjects)). To change this list, use the event handler's **DeletingEventArgs.Objects** parameter.