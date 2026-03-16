---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjects(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty},System.Boolean)
name: GetObjects(Type, CriteriaOperator, IList<SortProperty>, Boolean)
type: Method
summary: Returns a sorted `IList` collection of objects of the specified type, retrieved to the current Object Space and filtered according to the specified criteria.
syntax:
  content: public virtual IList GetObjects(Type objectType, CriteriaOperator criteria, IList<SortProperty> sorting, bool inTransaction)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of the objects to be retrieved.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) which specifies the criteria for object selection.
  - id: sorting
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: An `IList\<`[](xref:DevExpress.Xpo.SortProperty)`>` object that specifies sorting.
  - id: inTransaction
    type: System.Boolean
    description: '`true` if all objects (in the database and retrieved) are processed by the specified criteria; otherwise, `false`. Has effect in XPO only.'
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) collection that contains the persistent objects of the specified type. Only objects that satisfy the specified criteria will be retrieved to this collection.
seealso: []
---
[!include[CRUD_MethodExampleText](~/templates/crud_methodexampletext111240_1163708.md)]

# [C#](#tab/tabid-csharp)

```csharp
IList activeUsers = objectSpace.GetObjects(
    typeof(PermissionPolicyUser), new BinaryOperator("IsActive", true), true);
```
***

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, do not implement the `GetObjects` method. It is implemented in the `BaseObjectSpace` class. To get the specified objects, the `BaseObjectSpace.GetObjects(Type type, CriteriaOperator criteria, bool inTransaction)` method invokes a protected virtual `CreateCollection` method that does nothing and returns `null`. Override the `CreateCollection` method in your descendant.