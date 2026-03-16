---
uid: DevExpress.ExpressApp.IObjectSpace.CreateObject``1
name: CreateObject<ObjectType>()
type: Method
summary: Creates an object of the type designated by the specified generic type parameter.
syntax:
  content: ObjectType CreateObject<ObjectType>()
  typeParameters:
  - id: ObjectType
    description: ''
  return:
    type: '{ObjectType}'
    description: A created object of the specified type.
seealso:
- linkId: "113711"
---

[!include[](~/templates/objectspace_createobject.md)]

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to override the **CreateObject\<ObjectType>** method entirely. The [BaseObjectSpace.CreateObject\<ObjectType>](xref:DevExpress.ExpressApp.BaseObjectSpace.CreateObject``1) method invokes a protected virtual **BaseObjectSpace.CreateObjectCore** method and then sets the returned object modified by calling the [BaseObjectSpace.SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*) method for it. So, you should only override the **CreateObjectCore** method.

The created object will be saved to the database when calling the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method.