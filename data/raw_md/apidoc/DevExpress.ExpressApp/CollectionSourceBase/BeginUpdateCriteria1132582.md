---
uid: DevExpress.ExpressApp.CollectionSourceBase.BeginUpdateCriteria
name: BeginUpdateCriteria()
type: Method
summary: Begins update of the Collection Source's collection criteria. The criteria will not be applied to the collection until the update is complete.
syntax:
  content: public void BeginUpdateCriteria()
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase.EndUpdateCriteria
---
Generally, the `BeginUpdateCriteria`/[](xref:DevExpress.ExpressApp.CollectionSourceBase.EndUpdateCriteria) methods should be used when you need to perform several modifications of the Collection Source's collection [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria). After you call the `BeginUpdateCriteria` method, you can change the criteria as required. The criteria will not be applied to the Collection Source's collection until you call the @DevExpress.ExpressApp.CollectionSourceBase.EndUpdateCriteria method. The following code snippet illustrates this:

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
