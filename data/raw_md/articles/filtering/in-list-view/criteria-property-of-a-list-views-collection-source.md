---
uid: "112988"
seealso: []
title: Criteria Property of a List View's Collection Source
owner: Ekaterina Kiseleva
---
# Criteria Property of a List View's Collection Source

The [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria) property of a List View's [ListView.CollectionSource](xref:DevExpress.ExpressApp.ListView.CollectionSource) allows you to filter the List View at data source level. This means that only objects that satisfy the specified criteria are retrieved from the database. This topic explains how to use this approach if you need to apply a filter which does not change at runtime or design time.

Do the following to access the `Criteria` property of a List View's CollectionSource:

1. Create a [View Controller](xref:112621).
2. Override the Controller's `OnActivated` method to access the current [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) object.
3. Use the List View's [ListView.CollectionSource](xref:DevExpress.ExpressApp.ListView.CollectionSource) to retrieve the required objects from the data store.
4. Add your filter to the [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria) filter collection.

The following code demonstrates how to show only objects whose `FullName` begins with an "A" in Person List Views:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.Data.Filtering;
using DevExpress.Persistent.BaseImpl;
// ...
public class FilterPersonListViewController : ObjectViewController<ListView, Person> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CollectionSource.Criteria["Filter1"] = CriteriaOperator.Parse("StartsWith([FullName], 'A')");
    }
}
```
***

This approach can be applied to any List View that you can define in code. In the code above, all List Views that display `Person` type objects are filtered.

[!include[](~/templates/criteria_sessionmixingexception111409.md)]

> [!NOTE]
> * [!include[](~/templates/collectionsourcecriterianested111748.md)]
> * [!include[](~/templates/collectionsourcetreelist111750.md)]
