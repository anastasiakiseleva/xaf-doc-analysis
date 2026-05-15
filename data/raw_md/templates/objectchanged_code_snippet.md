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

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp

Public Class MyViewController
    Inherits ObjectViewController(Of ObjectView, Sale)

    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        AddHandler ObjectSpace.ObjectChanged, AddressOf ObjectSpace_ObjectChanged
    End Sub
    Private Sub ObjectSpace_ObjectChanged(ByVal sender As Object, ByVal e As ObjectChangedEventArgs)
        If e.PropertyName = NameOf(Sale.Count) Then
            Dim sale = CType(e.Object, Sale)
            sale.TotalPrice = sale.Count * sale.Price
        End If
    End Sub
    Protected Overrides Sub OnDeactivated()
        MyBase.OnDeactivated()
        RemoveHandler ObjectSpace.ObjectChanged, AddressOf ObjectSpace_ObjectChanged
    End Sub
End Class
```

***

> [!NOTE]
> 
> Business objects must implement the [INotifyPropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged) interface. See this article for details: [The Importance of Property Change Notifications for Automatic UI Updates](xref:117395).

For object changes that cannot be tracked via notification mechanisms exposed by the data layer, the [IObjectSpace.SetModified](xref:DevExpress.ExpressApp.IObjectSpace.SetModified*) method must be called after an object has been changed. This method adds the object passed as the _obj_ parameter to the list of objects to be committed.
