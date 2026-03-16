---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObject``1(``0)
name: GetObject<ObjectType>(ObjectType)
type: Method
summary: Retrieves an object from another Object Space to the current Object Space. The returned object is cast by the type designated by the specified generic type parameter.
syntax:
  content: public ObjectType GetObject<ObjectType>(ObjectType obj)
  parameters:
  - id: obj
    type: '{ObjectType}'
    description: An object that represents a template object from another Object Space.
  typeParameters:
  - id: ObjectType
    description: 'The type to which the retrieved object is cast.'
  return:
    type: '{ObjectType}'
    description: An object retrieved from the database by the current Object Space and cast by the specified type.
seealso: []
---
To return an object retrieved by the current Object Space, the `GetObject\<ObjectType>` method invokes the [BaseObjectSpace.GetObject](xref:DevExpress.ExpressApp.BaseObjectSpace.GetObject(System.Object)) method passing the specified object as the _objectFormDifferentObjectSpace_ parameter. The value returned by the invoked method is cast to the type designated by the specified generic type parameter. Note that the invoked [BaseObjectSpace.GetObject](xref:DevExpress.ExpressApp.BaseObjectSpace.GetObject(System.Object)) method does nothing and returns `null`. Override it in the `BaseObjectSpace` class' descendants.