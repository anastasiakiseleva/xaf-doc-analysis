---
uid: DevExpress.ExpressApp.IObjectSpace.CreateCollection(System.Type)
name: CreateCollection(Type)
type: Method
summary: Creates and initializes a collection of objects of the specified type.
syntax:
  content: IList CreateCollection(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of persistent objects to include in the collection.
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) collection that includes objects of the specified type.
seealso: []
---
Use this method to create a collection of objects of the specified type. The newly created collection will use the current Object Space to load and save persistent objects.

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you should override a virtual protected **BaseObjectSpace.CreateCollection** method which is called by the [BaseObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.BaseObjectSpace.CreateCollection*) method.