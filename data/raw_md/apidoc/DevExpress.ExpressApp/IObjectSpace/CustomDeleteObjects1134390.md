---
uid: DevExpress.ExpressApp.IObjectSpace.CustomDeleteObjects
name: CustomDeleteObjects
type: Event
summary: The [IObjectSpace.Delete](xref:DevExpress.ExpressApp.IObjectSpace.Delete*) method raises the `CustomDeleteObjects` event. Handle this event to replace the default persistent object deletion logic with custom logic.
syntax:
  content: event EventHandler<CustomDeleteObjectsEventArgs> CustomDeleteObjects
seealso: []
---
Use the handler's `CustomDeleteObjectsEventArgs.Objects` parameter to obtain the objects to be deleted. Set the handler's `CompletedEventArgs.Handled` parameter to `true` to indicate the delete operation is completed.

[!include[](~/templates/CustomDeleteObjects-codesnippet.md)]

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class descendant, you can override the `BaseObjectSpace.DeleteCore` method instead of handling the `CustomDeleteObjects` event. The [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*) method calls the `BaseObjectSpace.DeleteCore` method and raises the `CustomDeleteObjects` event. This means you can implement custom deletion logic in any of these places. For more information, refer to the [IObjectSpace.Delete](xref:DevExpress.ExpressApp.IObjectSpace.Delete*) method description.