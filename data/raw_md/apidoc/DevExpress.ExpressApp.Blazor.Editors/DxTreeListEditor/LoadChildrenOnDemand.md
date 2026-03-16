---
uid: DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor.LoadChildrenOnDemand
name: LoadChildrenOnDemand
type: Property
summary: Specifies whether @DevExpress.Blazor.DxTreeList should render child nodes only when users expand their parent.
syntax:
  content: public bool LoadChildrenOnDemand { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if you want to render the rows for child nodes on-demand; otherwise, `false`.'
seealso: []
---
When you use @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor to display a tree of `ITreeNode` objects, XAF renders child nodes on-demand when users expand their parent nodes for the first time. To render all node rows during control initialization, set the `LoadChildrenOnDemand` property to `false`.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

namespace MySolution.Blazor.Server.Controllers;

public class LoadChildrenOnDemandController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        if (View.Editor is DxTreeListEditor editor) { 
            editor.LoadChildrenOnDemand = false; 
        }
    }
}
```

> [!NOTE]
> This functionality has certain limitations. For more information, refer to the following topic: [Blazor.DxTreeList.ChildrenLoadingOnDemand](xref:DevExpress.Blazor.DxTreeList.ChildrenLoadingOnDemand#limitations).