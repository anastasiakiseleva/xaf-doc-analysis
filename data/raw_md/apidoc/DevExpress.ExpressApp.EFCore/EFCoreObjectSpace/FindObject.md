---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
name: FindObject(Type, CriteriaOperator, Boolean)
type: Method
summary: Searches for the first object that matches the specified criteria.
syntax:
  content: public override object FindObject(Type objectType, CriteriaOperator criteria, bool inTransaction)
  parameters:
  - id: objectType
    type: System.Type
    description: A type of an object to be returned.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: Criteria to search for an object.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if the method takes unsaved changes into account; otherwise, **false**.'
  return:
    type: System.Object
    description: The first object that matches the specified criteria. `null` if there is no persistent object that matches the criteria.
seealso: []
---
[!include[FindObject-example](~/templates/FindObject-example.md)]