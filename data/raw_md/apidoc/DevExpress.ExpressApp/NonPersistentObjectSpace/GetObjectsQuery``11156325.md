---
uid: DevExpress.ExpressApp.NonPersistentObjectSpace.GetObjectsQuery``1(System.Boolean)
name: GetObjectsQuery<T>(Boolean)
type: Method
summary: Gets a queryable data structure that provides functionality to evaluate queries against a specific business object type.
syntax:
  content: public override IQueryable<T> GetObjectsQuery<T>(bool inTransaction = false)
  parameters:
  - id: inTransaction
    type: System.Boolean
    defaultValue: "False"
    description: This parameter has no effect in [](xref:DevExpress.ExpressApp.NonPersistentObjectSpace). It is added only to provide compatibility with [IObjectSpace.GetObjectsQuery\<T>](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsQuery``1(System.Boolean)).
  typeParameters:
  - id: T
    description: ''
  return:
    type: System.Linq.IQueryable{{T}}
    description: An [](xref:System.Linq.IQueryable`1) object that provides functionality to evaluate queries against a specific business object type.
seealso: []
---
If the @DevExpress.ExpressApp.NonPersistentObjectSpace.CustomGetObjectsQuery event is handled and its *Queryable* argument is not empty, **GetObjectsQuery\<T>** casts the *Queryable* query to [](xref:System.Linq.IQueryable`1) and returns the result. Otherwise, the **GetObjectsQuery\<T>** method casts the collection of objects created in the [NonPersistentObjectSpace.ObjectsGetting](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.ObjectsGetting) event to [](xref:System.Linq.IQueryable`1) and returns the result.