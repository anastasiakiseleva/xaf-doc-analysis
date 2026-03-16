---
uid: DevExpress.ExpressApp.BaseObjectSpace.CreateObject``1
name: CreateObject<ObjectType>()
type: Method
summary: Creates an object of the type designated by the specified generic type parameter.
syntax:
  content: public ObjectType CreateObject<ObjectType>()
  typeParameters:
  - id: ObjectType
    description: ''
  return:
    type: '{ObjectType}'
    description: A created object of the specified type.
seealso: []
---
This method calls a protected virtual method, **CreateObjectCore**, which must be overridden in the **BaseObjectSpace** class descendants. After an object of the specified type is created, the [BaseObjectSpace.SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*) method is called so that the object is saved to the database during the next changes commit (see [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges)).

Use this method to create objects in [Controllers](xref:112621). In a regular business class, create objects directly via their constructor.