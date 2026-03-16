---
uid: DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.CreateDefaultTargetObjectSpace
name: CreateDefaultTargetObjectSpace()
type: Method
summary: Returns an Object Space for the [CustomCloneObjectEventArgs.ClonedObject](xref:DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.ClonedObject).
syntax:
  content: public IObjectSpace CreateDefaultTargetObjectSpace()
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) Object Space for the cloned object.
seealso: []
---
Depending on the current View properties and context, the `CreateDefaultTargetObjectSpace` method creates a nested Object Space, creates a new Object Space, or returns an existing Object Space. For more information, refer to the following topic: [CustomCloneObjectEventArgs.TargetObjectSpace](xref:DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.TargetObjectSpace).