You can customize the `TreeListEditor` and `CategorizedListEditor` List Editors or the `TreeList` control exposed via the List Editor's [ListEditor.Control](xref:DevExpress.ExpressApp.Editors.ListEditor.Control) property.

To access a List Editor in code, create a [View Controller](xref:112621) and handle its [ViewController.ViewControlsCreated](xref:DevExpress.ExpressApp.ViewController.ViewControlsCreated) event or override the `OnViewControlsCreated` protected method.

### Access DxTreeListEditor (ASP.NET Core Blazor)

# [C#](#tab/tabid-csharp)

[!include[dxtreelisteditor-access](~/templates/dxtreelisteditor-access.md)]

***

### Access TreeListEditor (Windows Forms)

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.TreeListEditors.Win;
using DevExpress.XtraTreeList;
using DevExpress.Persistent.Base.General;

namespace YourSolutionName.Win.Controllers;

public partial class TreeListController : ViewController {
    public TreeListController() {            
        TargetViewType = ViewType.ListView;
        TargetObjectType = typeof(ITreeNode);         
    }
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        ListView view = (ListView)View;
        TreeListEditor listEditor = (TreeListEditor)view.Editor;
        TreeList treeList = listEditor.TreeList;
        // Access the TreeList object here.           
    }
}
```
***

### Access CategorizedListEditor (Windows Forms)

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.TreeListEditors.Win;
using DevExpress.XtraTreeList;
using DevExpress.Persistent.Base.General;

namespace YourSolutionName.Win.Controllers;

public partial class CategorizedListController : ViewController {
    public CategorizedListController() {            
        TargetViewType = ViewType.ListView;
        TargetObjectType = typeof(ICategorizedItem);         
    }
    protected override void OnViewControlsCreated() {
        ListView view = (ListView)View;
        CategorizedListEditor listEditor = (CategorizedListEditor)view.Editor;
        ListView categoriesListView = listEditor.CategoriesListView;
        TreeListEditor treeListEditor = (TreeListEditor)categoriesListView.Editor;
        TreeList treeList = treeListEditor.TreeList;
        // Implement the required changes here.    
    }
}
```
***
