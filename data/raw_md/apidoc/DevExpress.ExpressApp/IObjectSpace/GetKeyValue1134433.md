---
uid: DevExpress.ExpressApp.IObjectSpace.GetKeyValue(System.Object)
name: GetKeyValue(Object)
type: Method
summary: Returns the key property's value of the specified persistent object.
syntax:
  content: object GetKeyValue(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object whose key property's value is requested.
  return:
    type: System.Object
    description: An object which is the value of the specified object's key property.
seealso:
- linkId: DevExpress.Persistent.BaseImpl.BaseObject.Oid
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetKeyValue** method. It's implemented in the **BaseObjectSpace** class.