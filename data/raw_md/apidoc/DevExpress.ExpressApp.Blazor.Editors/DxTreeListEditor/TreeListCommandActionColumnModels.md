---
uid: DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor.TreeListCommandActionColumnModels
name: TreeListCommandActionColumnModels
type: Property
summary: Stores @DevExpress.Blazor.DxTreeList command column [models](xref:404767).
syntax:
  content: public IList<DxTreeListCommandColumnModel> TreeListCommandActionColumnModels { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.Blazor.Editors.Models.DxTreeListCommandColumnModel}
    description: A set of @DevExpress.Blazor.DxTreeList command column [models](xref:404767).
seealso: []
---
Use this property to customize the `TreeListCommandActionColumnModels` collection:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Blazor.Components.Models;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Editors.ActionControls;
using DevExpress.ExpressApp.Blazor.Editors.Models;

namespace MySolution.Blazor.Server.Controllers;

  public class ColumnsOrderController : ViewController<ListView> {
      protected override void OnViewControlsCreated() {
          base.OnViewControlsCreated();

          if(View.Editor is DxTreeListEditor treeListEditor) {
            // Specify the index of a column
              treeListEditor.TreeListCommandActionColumnModels.FirstOrDefault(c => c.Name == "RecordEdit").VisibleIndex = 3;
          }
      }
  }
```