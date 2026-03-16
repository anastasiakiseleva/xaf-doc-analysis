---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
name: FindObject(Type, CriteriaOperator, Boolean)
type: Method
summary: Searches for the first object that matches the specified criteria and of the specified type. This method takes uncommitted changes into account.
syntax:
  content: public override object FindObject(Type objectType, CriteriaOperator criteria, bool inTransaction)
  parameters:
  - id: objectType
    type: System.Type
    description: A type of objects this method searches.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: Criteria to search for an object.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if the method takes unsaved changes into account; otherwise, **false**.'
  return:
    type: System.Object
    description: The first object that matches the specified criteria. `null` if there is no object that matches the criteria and belongs to the current Object Space.
seealso: []
---
[!include[FindObject-example](~/templates/FindObject-example.md)]
