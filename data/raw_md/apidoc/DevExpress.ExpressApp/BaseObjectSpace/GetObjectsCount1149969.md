---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjectsCount(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: GetObjectsCount(Type, CriteriaOperator)
type: Method
summary: Returns the number of objects specified.
syntax:
  content: public virtual int GetObjectsCount(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object that identifies the type of objects against which the calculation will be performed.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: The [](xref:DevExpress.Data.Filtering.CriteriaOperator) that specifies the criteria for object selection in the database.
  return:
    type: System.Int32
    description: An integer value that is the count of persistent objects that satisfy the specified criteria.
seealso: []
---
This method is intended to calculate the number of persistent objects in the database. For instance, this method is used before retrieving objects for the Lookup Property Editor. If there are more than the specified value, the Find editor is available.