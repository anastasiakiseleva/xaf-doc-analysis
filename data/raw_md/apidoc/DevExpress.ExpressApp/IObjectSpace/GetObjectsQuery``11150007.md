---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectsQuery``1(System.Boolean)
name: GetObjectsQuery<T>(Boolean)
type: Method
summary: Gets a queryable data structure that provides functionality to evaluate queries against a specific business object type.
syntax:
  content: IQueryable<T> GetObjectsQuery<T>(bool inTransaction = false)
  parameters:
  - id: inTransaction
    type: System.Boolean
    defaultValue: "False"
    description: '**true**, if querying a data store for objects includes all in-memory changes into query results; otherwise, **false**. Has effect in XPO only.'
  typeParameters:
  - id: T
    description: ''
  return:
    type: System.Linq.IQueryable{{T}}
    description: An [](xref:System.Linq.IQueryable`1) object that provides functionality to evaluate queries against a specific business object type.
seealso: []
---
You can use the following code to query data in EF Core and XPO applications:

# [C#](#tab/tabid-csharp)

```csharp
IQueryable<Payment> query = objectSpace.GetObjectsQuery<Payment>(true);
object obj = query.Where(p => p.Hours == 4).FirstOrDefault();
```
***

The **GetObjectsQuery\<T>** method has implementations in [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace), [](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace), and [](xref:DevExpress.ExpressApp.NonPersistentObjectSpace) classes:

* [XPObjectSpace.GetObjectsQuery\<T>](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectsQuery``1(System.Boolean))
* [EFCoreObjectSpace.GetObjectsQuery\<T>](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetObjectsQuery``1(System.Boolean))
* [NonPersistentObjectSpace.GetObjectsQuery\<T>](xref:DevExpress.ExpressApp.NonPersistentObjectSpace.GetObjectsQuery``1(System.Boolean))