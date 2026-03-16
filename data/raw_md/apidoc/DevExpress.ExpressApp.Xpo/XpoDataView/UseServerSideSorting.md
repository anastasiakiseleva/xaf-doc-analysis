---
uid: DevExpress.ExpressApp.Xpo.XpoDataView.UseServerSideSorting
name: UseServerSideSorting
type: Field
summary: Indicates that the sort operation is executed on the server side before the result set is trimmed according to the **TopReturnedObjects** property.
syntax:
  content: public bool UseServerSideSorting
  return:
    type: System.Boolean
    description: "**true** if the sort operation is executed on the server side; **false** if the sort operation is executed on the client side. The default value equals the @DevExpress.ExpressApp.Xpo.XpoDataView.DefaultUseServerSideSorting static field's value."
seealso: []
---
You can specify the **UseServerSideSorting** field in a List View [Controller](xref:112621) as demonstrated below:
# [C#](#tab/tabid-csharp)

```csharp{9}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Xpo;
// ...
public class CustomizeListViewController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        var xpoDataView = View.CollectionSource.Collection as XpoDataView;
        if (xpoDataView != null) {
            xpoDataView.UseServerSideSorting = false;
        }
    }
}
```
***

If you want to specify this option globally for all List Views, use the static @DevExpress.ExpressApp.Xpo.XpoDataView.DefaultUseServerSideSorting field instead.

> [!Note]
> With server-side sorting, you can use only persistent and aliased properties in the @DevExpress.ExpressApp.XafDataView.Sorting criteria. With client-side sorting, you can also use column names.