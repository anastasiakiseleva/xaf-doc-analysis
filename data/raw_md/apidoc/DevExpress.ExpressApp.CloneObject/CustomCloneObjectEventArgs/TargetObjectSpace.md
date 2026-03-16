---
uid: DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.TargetObjectSpace
name: TargetObjectSpace
type: Property
summary: Specifies the Object Space of the target object.
syntax:
  content: public IObjectSpace TargetObjectSpace { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: The Object Space of the target object.
seealso: []
---
The `TargetObjectSpace` property returns `null`. You should initialize it in case the cloned object is assigned to the [CustomCloneObjectEventArgs.ClonedObject](xref:DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.ClonedObject) property.

Use the [CustomCloneObjectEventArgs.CreateDefaultTargetObjectSpace](xref:DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.CreateDefaultTargetObjectSpace) method to obtain a default Object Space for the current context or use the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method to create a new Object Space instance.