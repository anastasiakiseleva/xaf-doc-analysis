---
uid: DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomCloneObject
name: CustomCloneObject
type: Event
summary: Occurs before the default cloning process begins.
syntax:
  content: public event EventHandler<CustomCloneObjectEventArgs> CustomCloneObject
seealso: []
---
When you handle this event and the handler's `ClonedObject` parameter is initialized, the object passed via this parameter becomes the target object of the cloning process. Otherwise, XAF performs default cloning.

Handle this event to implement custom cloning logic. Pass the custom cloned object via the handler's `ClonedObject` parameter. Pass the target object's Object Space via the `TargetObjectSpace` parameter.

To manually clone a source object, handle this event and assign a custom cloned object to the [CustomCloneObjectEventArgs.ClonedObject](xref:DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.ClonedObject)  parameter. If the event is not handled or the `ClonedObject` parameter is `null`, XAF performs the default cloning is performed.

The [CustomCloneObjectEventArgs.TargetObjectSpace](xref:DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.TargetObjectSpace) parameter refers to an [](xref:DevExpress.ExpressApp.IObjectSpace) object. Initialize the `TargetObjectSpace` property to use custom Object Space type object to clone an object.

> [!NOTE]
> XAF raises an exception when you pass the handler's `ClonedObject` parameter if the `TargetObjectSpace` parameter is `null`.

You can implement a custom `DevExpress.Persistent.Base.Cloner` class descendant to customize the cloning process and then call its `CloneTo` method in the `CustomCloneObject` event handler.

The following snippet overrides the `Cloner.CopyMemberValue` method to skip association properties during cloning.

[!include[customcloneobjectcodesnippet](~/templates/customcloneobjectcodesnippet.md)]