---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectByKey``1(System.Object)
name: GetObjectByKey<ObjectType>(Object)
type: Method
summary: Returns a persistent object of the type designated by the specified generic type parameter, with the specified value for its key property.
syntax:
  content: ObjectType GetObjectByKey<ObjectType>(object key)
  parameters:
  - id: key
    type: System.Object
    description: An object that represents the persistent object's key property value.
  typeParameters:
  - id: ObjectType
    description: ''
  return:
    type: '{ObjectType}'
    description: A persistent object with the specified value for its key property.
seealso:
- linkId: DevExpress.Persistent.BaseImpl.BaseObject.Oid
---
When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjectByKey\<ObjectType>** method. It's implemented in the **BaseObjectSpace** class. The **BaseObjectSpace.GetObjectByKey\<ObjectType>(object key)** method calls the **BaseObjectSpace.GetObjectByKey(Type type, object key)** method which returns null. The latter method is virtual. So, you should override it in your descendant.

To get the key property value, use the [IObjectSpace.GetKeyValue](xref:DevExpress.ExpressApp.IObjectSpace.GetKeyValue(System.Object)) method.