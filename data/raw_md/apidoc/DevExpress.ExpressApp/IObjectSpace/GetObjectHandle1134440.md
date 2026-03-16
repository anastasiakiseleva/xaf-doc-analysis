---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectHandle(System.Object)
name: GetObjectHandle(Object)
type: Method
summary: Returns an object's handle.
syntax:
  content: string GetObjectHandle(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An Object whose handle will be retrieved.
  return:
    type: System.String
    description: A string holding the key property value and type of the specified object, representing the specified object's handle.
seealso: []
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjectHandle** method. It's implemented in the **BaseObjectSpace** class.