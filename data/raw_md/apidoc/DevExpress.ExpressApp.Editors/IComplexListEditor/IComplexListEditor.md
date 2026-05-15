---
uid: DevExpress.ExpressApp.Editors.IComplexListEditor
name: IComplexListEditor
type: Interface
summary: Declares members implemented by a [List Editor](xref:113189) to support receiving information on the application and Collection Source of the List View that uses the List Editor.
syntax:
  content: public interface IComplexListEditor
seealso:
- linkId: DevExpress.ExpressApp.Editors.IComplexListEditor._members
  altText: IComplexListEditor Members
- linkId: DevExpress.ExpressApp.XafApplication
- linkId: DevExpress.ExpressApp.CollectionSourceBase
- linkId: DevExpress.ExpressApp.CollectionSourceBase.ObjectSpace
- linkId: DevExpress.ExpressApp.Editors.IComplexViewItem
---
In certain scenarios, a List Editor may require access to the application or the Collection Source of the List View that uses the List Editor. To get this information, the List Editor can implement the **IComplexListEditor** interface. This interface exposes a single [IComplexListEditor.Setup](xref:DevExpress.ExpressApp.Editors.IComplexListEditor.Setup(DevExpress.ExpressApp.CollectionSourceBase,DevExpress.ExpressApp.XafApplication)) method that passes this information to the List Editor.

When implementing a custom List Editor, support this interface if the List Editor requires information on the application and Collection Source to function properly.

Here is an example of how to implement **IComplexListEditor** in a [](xref:DevExpress.ExpressApp.Editors.ListEditor) descendant.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
// ...
public class CustomListEditor : ListEditor, IComplexListEditor {
    private CollectionSourceBase collectionSource;
    private XafApplication application;
    #region IComplexListEditor Members
    public void Setup(CollectionSourceBase collectionSource, 
XafApplication application) {
        this.collectionSource = collectionSource;
        this.application = application;
    }
    #endregion
    // Example:
    protected override object CreateControlsCore() {
        IList objectsCollection = collectionSource.List;
        // ...
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Editors
'...
Public Class CustomListEditor
    Inherits ListEditor
    Implements IComplexListEditor

    Private collectionSource As CollectionSourceBase
    Private application As XafApplication
    #Region "IComplexListEditor Members"
        Public Sub Setup(ByVal collectionSource As CollectionSourceBase, _
ByVal application As XafApplication) Implements IComplexListEditor.Setup
            Me.collectionSource = collectionSource
            Me.application = application
        End Sub
    #End Region
    ' Example:
    Protected Overrides Function CreateControlsCore() As Object
        Dim objectsCollection As IList = collectionSource.List
        ' ...
    End Function
End Class
```

***
