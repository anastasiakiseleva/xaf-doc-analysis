A persistent object used in Collection Source's Criteria does not reload when the [Object Space](xref:113707) is refreshed, which raises the [](xref:DevExpress.Xpo.Exceptions.SessionMixingException) exception. To avoid this, use a persistent object's key property instead of the object itself.

# [C#](#tab/tabid-csharp)
```csharp
View.CollectionSource.Criteria["Filter1"] = CriteriaOperator.Parse("Manager.Oid = ?", ObjectSpace.GetKeyValue(manager));
```
***
