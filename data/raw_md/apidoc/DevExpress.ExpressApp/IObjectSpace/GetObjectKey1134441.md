---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectKey(System.Type,System.String)
name: GetObjectKey(Type, String)
type: Method
summary: Converts the key property value string representation into its actual type.
syntax:
  content: object GetObjectKey(Type objectType, string objectKeyString)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the object whose key property value is to be converted.
  - id: objectKeyString
    type: System.String
    description: A string that is the key property value to be converted.
  return:
    type: System.Object
    description: An object that is the value of the specified type object's key property.
seealso:
- linkId: DevExpress.Persistent.BaseImpl.BaseObject.Oid
- linkId: DevExpress.ExpressApp.BaseObjectSpace.GetObjectKey(System.Type,System.String)
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjectKey** method. It's implemented in the **BaseObjectSpace** class. The **BaseObjectSpace.GetObjectKey** method returns null, but it is virtual. So, you should override it in your descendant.