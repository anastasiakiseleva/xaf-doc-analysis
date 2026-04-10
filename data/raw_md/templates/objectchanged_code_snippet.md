The following code snippet updates the `TotalPrice` property of a `Sale` object when the `Count` property changes.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;

public class MyViewController : ObjectViewController<ObjectView, Sale> {
    protected override void OnActivated() {
        base.OnActivated();
        ObjectSpace.ObjectChanged += ObjectSpace_ObjectChanged;
    }

    private void ObjectSpace_ObjectChanged(object sender, ObjectChangedEventArgs e) {
        if (e.PropertyName == nameof(Sale.Count)) {
            Sale sale = (Sale)e.Object;
            sale.TotalPrice = sale.Count * sale.Price;
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        ObjectSpace.ObjectChanged -= ObjectSpace_ObjectChanged;
    }
}
```
***

> [!NOTE]
> 
> Business objects must implement the [INotifyPropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged) interface. See this article for details: [The Importance of Property Change Notifications for Automatic UI Updates](xref:117395).

For object changes that cannot be tracked via notification mechanisms exposed by the data layer, the [IObjectSpace.SetModified](xref:DevExpress.ExpressApp.IObjectSpace.SetModified*) method must be called after an object has been changed. This method adds the object passed as the _obj_ parameter to the list of objects to be committed.
