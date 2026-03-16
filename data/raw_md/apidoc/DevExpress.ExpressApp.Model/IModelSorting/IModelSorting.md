---
uid: DevExpress.ExpressApp.Model.IModelSorting
name: IModelSorting
type: Interface
summary: The **Sorting** node provides access to the sort settings applied to the collection of the [List View](xref:112611)'s Collection Source.
syntax:
  content: 'public interface IModelSorting : IModelNode, IModelList<IModelSortProperty>, IList<IModelSortProperty>, ICollection<IModelSortProperty>, IEnumerable<IModelSortProperty>, IEnumerable'
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelSorting._members
  altText: IModelSorting Members
- linkId: "112579"
- linkId: "112580"
- linkId: DevExpress.ExpressApp.CollectionSource
- linkId: DevExpress.ExpressApp.ListView.CollectionSource
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

> [!IMPORTANT]
> Sorting, specified in the **IModelSorting** node is applied to the underlying data source. It may be overridden by sorting specified for the bound control (see [IModelColumn.SortOrder](xref:DevExpress.ExpressApp.Model.IModelColumn.SortOrder)).

The **IModelSorting** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelSortProperty) nodes. You can add **SortProperty** child nodes to specify sorting applied to the collection of the List View's Collection Source. For instance, this setting has effect when the [IModelListView.TopReturnedObjects](xref:DevExpress.ExpressApp.Model.IModelListView.TopReturnedObjects) property is specified.

Settings specified in the **IModelSorting** node have no effect in List Views where the [](xref:DevExpress.ExpressApp.PropertyCollectionSource) is used. Nested List Views of [collection properties](xref:113568) and lookup List Views of properties decorated with the [DataSourceProperty](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) attribute use this Collection Source. In the **PropertyCollectionSource** class, the [CollectionSourceBase.CanApplySorting](xref:DevExpress.ExpressApp.CollectionSourceBase.CanApplySorting) default value is set to **false** to avoid overriding the sorting specified in a collection property getter accidentally. To change the **CanApplySorting** value to **true**,  use the following View Controller:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
public class MyViewController : ViewController<ListView> {
    public MyViewController() {
        this.TargetObjectType = typeof(MyBusinessObject);
        this.TargetViewNesting = DevExpress.ExpressApp.Nesting.Nested;
    }
    protected override void OnActivated() {
        base.OnActivated();
        this.View.CollectionSource.CanApplySorting = true;
    }
}
```
***