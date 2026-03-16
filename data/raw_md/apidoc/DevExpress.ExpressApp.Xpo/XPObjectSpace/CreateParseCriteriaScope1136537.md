---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateParseCriteriaScope
name: CreateParseCriteriaScope()
type: Method
summary: Used when parsing a CriteriaOperator represented by a string and containing persistent objects.
syntax:
  content: public override IDisposable CreateParseCriteriaScope()
  return:
    type: System.IDisposable
    description: An **IDisposable** object used to restore persistent objects from a serialized string.
seealso: []
---
Use this method when you need to parse a CriteriaOperator from a string and you expect that it contains references to persistent objects.

# [C#](#tab/tabid-csharp)

```csharp
CriteriaOperator criteria;
using(IDisposable scope = objectSpace.CreateParseCriteriaScope()) {
  criteria = CriteriaOperator.Parse(filterString);
}
```
***

Persistent objects are serialized as a part of a CriteriaOperator in a special format and a 'scope' object is necessary to restore objects from a serialized string.