---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjectByKey``1(System.Object)
name: GetObjectByKey<ObjectType>(Object)
type: Method
summary: Returns a persistent object of the type designated by the specified generic type parameter, with the specified value for its key property.
syntax:
  content: public ObjectType GetObjectByKey<ObjectType>(object key)
  parameters:
  - id: key
    type: System.Object
    description: An object that is the persistent object's key property value.
  typeParameters:
  - id: ObjectType
    description: 'The type of the persistent object to retrieve.'
  return:
    type: '{ObjectType}'
    description: A persistent object with the specified value for its key property.
seealso: []
---
To return an object retrieved by the specified key, the `GetObjectByKey\<ObjectType>` method invokes the [BaseObjectSpace.GetObjectByKey](xref:DevExpress.ExpressApp.BaseObjectSpace.GetObjectByKey(System.Type,System.Object)) method, passing the required key as the _key_ parameter. The value returned by the invoked method is cast to the type designated by the specified generic type parameter. Note that the invoked [BaseObjectSpace.GetObjectByKey](xref:DevExpress.ExpressApp.BaseObjectSpace.GetObjectByKey(System.Type,System.Object)) method does nothing and returns `null`. Override it in the `BaseObjectSpace` class' descendants.