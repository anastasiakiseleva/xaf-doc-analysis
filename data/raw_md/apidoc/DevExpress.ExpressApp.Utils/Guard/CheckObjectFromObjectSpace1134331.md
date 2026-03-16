---
uid: DevExpress.ExpressApp.Utils.Guard.CheckObjectFromObjectSpace(DevExpress.ExpressApp.IObjectSpace,System.Object)
name: CheckObjectFromObjectSpace(IObjectSpace, Object)
type: Method
summary: Ensures that a specific object belongs to a particular Object Space.
syntax:
  content: public static void CheckObjectFromObjectSpace(IObjectSpace objectSpace, object obj)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the Object Space against which the specified object is checked.
  - id: obj
    type: System.Object
    description: An object to check.
seealso: []
---
If the specified object does not belong to the specified Object Space, an exception is thrown.