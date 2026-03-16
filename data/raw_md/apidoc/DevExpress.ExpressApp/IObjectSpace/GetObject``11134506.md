---
uid: DevExpress.ExpressApp.IObjectSpace.GetObject``1(``0)
name: GetObject<ObjectType>(ObjectType)
type: Method
summary: Gets an object similar to the specified object from another Object Space, to the current Object Space. The returned object is cast by the type designated by the specified generic type parameter.
syntax:
  content: ObjectType GetObject<ObjectType>(ObjectType obj)
  parameters:
  - id: obj
    type: '{ObjectType}'
    description: An object that represents a template object from another Object Space.
  typeParameters:
  - id: ObjectType
    description: ''
  return:
    type: '{ObjectType}'
    description: An object retrieved from the database to the current Object Space and cast by the specified type.
seealso: []
---
Use this method to check whether a particular persistent object belongs to the current Object Space. If the object passed as the parameter belongs to another Object Space, this method retrieves the same object from the database via the current Object Space.

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObject\<ObjectType>** method. It's implemented in the **BaseObjectSpace** class. The **BaseObjectSpace.GetObject\<ObjectType>(ObjectType objectFromDifferentObjectSpace)** method calls the **BaseObjectSpace.GetObject(Object objectFromDifferentObjectSpace)** method, which returns null. The latter method is virtual. So, you should override it in your descendant.