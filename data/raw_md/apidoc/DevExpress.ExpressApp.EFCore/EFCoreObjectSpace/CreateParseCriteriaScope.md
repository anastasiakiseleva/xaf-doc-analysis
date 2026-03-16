---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.CreateParseCriteriaScope
name: CreateParseCriteriaScope()
type: Method
summary: Used to parse a @DevExpress.Data.Filtering.CriteriaOperator from a string that contains references to persistent objects.
syntax:
  content: public override IDisposable CreateParseCriteriaScope()
  return:
    type: System.IDisposable
    description: An **IDisposable** object used to restore persistent objects from a serialized string.
seealso: []
---
The following example shows how to use this method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp.EFCore;
// ... 
CriteriaOperator criteria;
using(IDisposable scope = objectSpace.CreateParseCriteriaScope()) {
  criteria = CriteriaOperator.Parse(filterString);
}
```
***