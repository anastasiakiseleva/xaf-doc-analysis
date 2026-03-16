---
uid: DevExpress.ExpressApp.CompositeObjectSpace.GetObjectsQuery``1(System.Boolean)
name: GetObjectsQuery<T>(Boolean)
type: Method
summary: Gets a queryable data structure that provides functionality to evaluate queries against the specified business object type.
syntax:
  content: public override IQueryable<T> GetObjectsQuery<T>(bool inTransaction = false)
  parameters:
  - id: inTransaction
    type: System.Boolean
    defaultValue: "False"
    description: '**true** if the method takes unsaved changes into account; otherwise, **false**.'
  typeParameters:
  - id: T
    description: A business object type for that this method returns the queryable data structure.
  return:
    type: System.Linq.IQueryable{{T}}
    description: An [](xref:System.Linq.IQueryable`1) object that provides functionality to evaluate queries against a specific business object type.
seealso: []
---
