---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectByKey(System.Type,System.Object)
name: GetObjectByKey(Type, Object)
type: Method
summary: Returns the persistent object that has the specified value for its key property.
syntax:
  content: object GetObjectByKey(Type type, object key)
  parameters:
  - id: type
    type: System.Type
    description: A [](xref:System.Type) object which is the type of objects to search for.
  - id: key
    type: System.Object
    description: An object that is the persistent object's key property value.
  return:
    type: System.Object
    description: An object which represents the persistent object with the specified value for its key property.
seealso:
- linkId: DevExpress.Persistent.BaseImpl.BaseObject.Oid
  altText: BaseObject.Oid
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetObjectByKey(System.Type,System.Object)
  altText: EFCoreObjectSpace.GetObjectByKey(Type, Object)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectByKey(System.Type,System.Object)
  altText: XPObjectSpace.GetObjectByKey(Type, Object)
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjectByKey** method. It's implemented in the **BaseObjectSpace** class. The **BaseObjectSpace.GetObjectByKey(Type type, object key)** method returns null, but it is virtual. So, you should override it in your descendant.

To get the key property value, use the [IObjectSpace.GetKeyValue](xref:DevExpress.ExpressApp.IObjectSpace.GetKeyValue(System.Object)) method.