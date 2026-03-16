---
uid: DevExpress.ExpressApp.BaseObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
name: FindObject(Type, CriteriaOperator, Boolean)
type: Method
summary: Searches for the first object of the specified type, matching the specified criteria.
syntax:
  content: public virtual object FindObject(Type objectType, CriteriaOperator criteria, bool inTransaction)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the object to search for.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** descendant which is the criteria to match persistent objects.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if all objects (in the database and retrieved) are processed by the specified criteria; otherwise, **false**. Has effect in XPO only.'
  return:
    type: System.Object
    description: An object which is the first persistent object which matches the specified criteria. `null` if there is no persistent object which matches the criteria.
seealso: []
---
This method does nothing and returns `null`. Override it in the `BaseObjectSpace` class' descendants.