---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjects(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: GetObjects(Type, CriteriaOperator)
type: Method
summary: Returns an **IList** collection of objects of the specified type, retrieved to the current Object Space and filtered according to the specified criteria.
syntax:
  content: public IList GetObjects(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of the objects to be retrieved.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** which specifies the criteria for object selection.
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) collection that contains the persistent objects of the specified type. Only objects that satisfy the specified criteria will be retrieved to this collection.
seealso: []
---
To get the specified objects, this method invokes a protected virtual **CreateCollection** method that does nothing and returns null. So, the details on how the objects are retrieved depend on how the **CreateCollection** method is overridden in a particular descendant of the **BaseObjectSpace** class.