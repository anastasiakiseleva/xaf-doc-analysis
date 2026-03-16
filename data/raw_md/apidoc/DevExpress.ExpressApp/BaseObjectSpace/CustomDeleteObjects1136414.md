---
uid: DevExpress.ExpressApp.BaseObjectSpace.CustomDeleteObjects
name: CustomDeleteObjects
type: Event
summary: Occurs to replace the default process of deleting persistent objects with a custom one.
syntax:
  content: public event EventHandler<CustomDeleteObjectsEventArgs> CustomDeleteObjects
seealso: []
---
The **CustomDeleteObjects** event is raised as a result of calling the [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*) method. Handle this event to provide a custom process for deleting persistent objects. Use the handler's **CustomDeleteObjectsEventArgs.Objects** parameter to get the objects to be deleted. Set the handler's **CompletedEventArgs.Handled** parameter to **true**, to indicate that the delete operation has already been performed.

As an alternative to this event, you can override the **DeleteCore** method in the **BaseObjectSpace** class' descendant.