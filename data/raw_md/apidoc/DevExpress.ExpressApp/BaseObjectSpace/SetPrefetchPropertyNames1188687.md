---
uid: DevExpress.ExpressApp.BaseObjectSpace.SetPrefetchPropertyNames(System.Object,System.String[])
name: SetPrefetchPropertyNames(Object, String[])
type: Method
summary: Loads specified delayed properties and child collections in each object of a given list.
syntax:
  content: public virtual void SetPrefetchPropertyNames(object collection, params string[] propertyNames)
  parameters:
  - id: collection
    type: System.Object
    description: An @System.Collections.IEnumerable list of parent objects.
  - id: propertyNames
    type: System.String[]
    description: Properties to load.
seealso: []
---
Before a ListView is displayed, it may actively read properties of underlying data source items to calculate [Conditional Appearance](xref:113286) rules, actions' @DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria, or client-side filters. If filter conditions and appearance rules use [Delayed Properties](xref:2024), call the **SetPrefetchPropertyNames** method before the ListView is opened to pre-load delayed properties and reduce a number of requiests to an underlying data source.

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp;
// ...
public class PreFetchOrdersViewController : ObjectViewController<ListView, Customer> {
    protected override void OnActivated() {
        if(View.CollectionSource.DataAccessMode == CollectionSourceDataAccessMode.Client) {
            ((BaseObjectSpace)ObjectSpace).SetPrefetchPropertyNames(View.CollectionSource.Collection, nameof(Customer.Orders));
        }
    }
}
```
***
