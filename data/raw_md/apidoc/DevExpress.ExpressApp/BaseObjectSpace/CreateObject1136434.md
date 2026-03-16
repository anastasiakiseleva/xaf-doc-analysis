---
uid: DevExpress.ExpressApp.BaseObjectSpace.CreateObject(System.Type)
name: CreateObject(Type)
type: Method
summary: Creates an object of the specified type.
syntax:
  content: public virtual object CreateObject(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the object to be created.
  return:
    type: System.Object
    description: A created object of the specified type.
seealso: []
---
This method calls a protected virtual method, **CreateObjectCore**, which must be overridden in the **BaseObjectSpace** class descendants. After an object of the specified type is created, the [BaseObjectSpace.SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*) method is called so that the created object is marked as modified, and therefore, is saved to the database during the next changes commit (see [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges)).

Use this method to create objects in [Controllers](xref:112621). In a regular business class, create objects directly via their constructor.