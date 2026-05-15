The following code snippet reloads the parent Detail View when one of the child objects is reloaded.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using YourSolutionName.Module.BusinessObjects;

namespace YourSolutionName.Module.Controllers {
    public class MyViewController : ObjectViewController<DetailView, Parent> {
        protected override void OnActivated() {
            base.OnActivated();
            ObjectSpace.ObjectReloaded += ObjectSpace_ObjectReloaded;
        }
        private void ObjectSpace_ObjectReloaded(object sender, ObjectManipulatingEventArgs e) {
            Child child = e.Object as Child;
            if (child != null && ReferenceEquals(child.Parent, View.CurrentObject)) {
                View.Refresh();
            }
        }
        protected override void OnDeactivated() {
            ObjectSpace.ObjectReloaded -= ObjectSpace_ObjectReloaded;
            base.OnDeactivated();
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)
```vb
Imports DevExpress.ExpressApp
Imports YourSolutionName.Module.BusinessObjects

Namespace YourSolutionName.Module.Controllers
    Public Class MyViewController
        Inherits ObjectViewController(Of DetailView, Parent)

        Protected Overrides Sub OnActivated()
            MyBase.OnActivated()
            AddHandler ObjectSpace.ObjectReloaded, AddressOf ObjectSpace_ObjectReloaded
        End Sub

        Private Sub ObjectSpace_ObjectReloaded(ByVal sender As Object, ByVal e As ObjectManipulatingEventArgs)
            Dim child As Child = TryCast(e.Object, Child)

            If child IsNot Nothing AndAlso ReferenceEquals(child.Parent, View.CurrentObject) Then
                View.Refresh()
            End If
        End Sub

        Protected Overrides Sub OnDeactivated()
            RemoveHandler ObjectSpace.ObjectReloaded, AddressOf ObjectSpace_ObjectReloaded
            MyBase.OnDeactivated()
        End Sub
    End Class
End Namespace
```
***