---
uid: DevExpress.ExpressApp.BaseObjectSpace.CreateCollection(System.Type)
name: CreateCollection(Type)
type: Method
summary: Creates and initializes a collection of objects of the specified type.
syntax:
  content: public IList CreateCollection(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of objects to include in the collection.
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) collection that includes objects of the specified type.
seealso: []
---
Use this method to create a collection of objects of the specified type. This method calls a protected virtual method, **CreateCollection**, which must be overridden in the **BaseObjectSpace** class descendants.

The newly created collection will use the current Object Space to load and save persistent objects.