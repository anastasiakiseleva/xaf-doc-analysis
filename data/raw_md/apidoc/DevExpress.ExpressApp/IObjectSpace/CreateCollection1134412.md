---
uid: DevExpress.ExpressApp.IObjectSpace.CreateCollection(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: CreateCollection(Type, CriteriaOperator)
type: Method
summary: Creates and initializes a collection of objects of the specified type, filtered according to the specified criteria.
syntax:
  content: IList CreateCollection(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of persistent objects to include in the collection.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: The [](xref:DevExpress.Data.Filtering.CriteriaOperator) that specifies a criteria for object selection in a data store.
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) collection that includes the persistent objects of the specified type. In addition, only objects that satisfy the specified criteria will be retrieved to this collection.
seealso: []
---
Use this method to create a collection of objects of the specified type, filtered according to the specified criteria. The newly created collection will use the current Object Space to load and save persistent objects.

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you should override a virtual protected **BaseObjectSpace.CreateCollection** method which is called by the [BaseObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.BaseObjectSpace.CreateCollection*) method.