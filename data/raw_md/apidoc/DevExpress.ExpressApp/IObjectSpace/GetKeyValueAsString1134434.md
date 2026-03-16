---
uid: DevExpress.ExpressApp.IObjectSpace.GetKeyValueAsString(System.Object)
name: GetKeyValueAsString(Object)
type: Method
summary: Returns the key property's value of the specified object, converted to a string representation.
syntax:
  content: string GetKeyValueAsString(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object whose key property value is requested.
  return:
    type: System.String
    description: A string which is the value of the specified object's key property.
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.GetKeyValue(System.Object)
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetKeyValueAsString** method. It's implemented in the **BaseObjectSpace** class. The **BaseObjectSpace.GetKeyValueAsString** method returns null, but it is virtual. So, you should override it in your descendant.