---
uid: DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.ClonedObject
name: ClonedObject
type: Property
summary: The target object of the cloning process.
syntax:
  content: public object ClonedObject { get; set; }
  parameters: []
  return:
    type: System.Object
    description: The target object of the cloning process.
seealso: []
---
To clone an object manually, assign the cloned object to the `ClonedObject` property and initialize the [CustomCloneObjectEventArgs.TargetObjectSpace](xref:DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.TargetObjectSpace) property.