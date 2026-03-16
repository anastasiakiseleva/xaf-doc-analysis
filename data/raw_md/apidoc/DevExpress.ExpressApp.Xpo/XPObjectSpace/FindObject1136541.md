---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
name: FindObject(Type, CriteriaOperator, Boolean)
type: Method
summary: Searches for the first object which matches the specified criteria.
syntax:
  content: public override object FindObject(Type objectType, CriteriaOperator criteria, bool inTransaction)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which is the type of objects to search for.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A **DevExpress.Data.Filtering.CriteriaOperator** descendant which is the criteria for matching persistent objects.
  - id: inTransaction
    type: System.Boolean
    description: '**true** if all objects (in the database and retrieved) are processed by the specified criteria; otherwise, **false**.'
  return:
    type: System.Object
    description: An object which is the first persistent object which matches the specified criteria. `null` if there is no persistent object which matches the criteria.
seealso: []
---
This method searches for an object, both if the specified object type is a class and if the specified object type is an interface.

Persistent objects that are marked for deletion are not included in the search.

[!include[FindObject-example](~/templates/FindObject-example.md)]
