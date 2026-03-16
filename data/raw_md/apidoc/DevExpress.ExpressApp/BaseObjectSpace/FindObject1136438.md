---
uid: DevExpress.ExpressApp.BaseObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: FindObject(Type, CriteriaOperator)
type: Method
summary: Searches for the first object of the specified type, matching the specified criteria.
syntax:
  content: public object FindObject(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the object to search for.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** descendant which is the criteria to match persistent objects.
  return:
    type: System.Object
    description: An object which is the first persistent object which matches the specified criteria. `null` if there is no persistent object which matches the criteria.
seealso: []
---
To find the specified object, this method invokes a public virtual **FindObject** method that does nothing and returns null. So, the details on how the objects are searched depend on how the **FindObject** virtual method is overridden in a particular descendant of the **BaseObjectSpace** class.