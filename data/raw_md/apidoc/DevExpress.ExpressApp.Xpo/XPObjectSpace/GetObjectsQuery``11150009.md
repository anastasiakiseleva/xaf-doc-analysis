---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectsQuery``1(System.Boolean)
name: GetObjectsQuery<T>(Boolean)
type: Method
summary: Gets a queryable data structure that provides functionality to evaluate queries against a specific business object type.
syntax:
  content: public override IQueryable<T> GetObjectsQuery<T>(bool inTransaction)
  parameters:
  - id: inTransaction
    type: System.Boolean
    description: '**true**, if querying a data store for objects includes all in-memory changes into query results; otherwise, **false**.'
  typeParameters:
  - id: T
    description: ''
  return:
    type: System.Linq.IQueryable{{T}}
    description: An [](xref:System.Linq.IQueryable`1) object that provides functionality to evaluate queries against a specific business object type.
seealso: []
---
