---
uid: DevExpress.ExpressApp.CollectionSourceBase.EndUpdateCriteria
name: EndUpdateCriteria()
type: Method
summary: Ends update of the Collection Source's collection criteria and applies it.
syntax:
  content: public void EndUpdateCriteria()
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.BeginUpdateCriteria
---
Generally, the [](xref:DevExpress.ExpressApp.CollectionSourceBase.BeginUpdateCriteria)/`EndUpdateCriteria` methods should be used when you need to perform several modifications of the Collection Source's collection [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria). After you call the @DevExpress.ExpressApp.CollectionSourceBase.BeginUpdateCriteria method, you can change the criteria as required. The criteria will not be applied to the Collection Source's collection until you call the `EndUpdateCriteria` method. The following code snippet illustrates this:

# [C#](#tab/tabid-csharp)

```csharp
//...
collectionSource.BeginUpdateCriteria();
collectionSource.Criteria["1"] = CriteriaOperator.Parse("...");
collectionSource.Criteria["2"] = CriteriaOperator.Parse("...");
collectionSource.EndUpdateCriteria();
//...
```
***
