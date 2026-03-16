---
uid: DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.GridCommandActionColumnModels
name: GridCommandActionColumnModels
type: Property
summary: Provides access to a set of `DxGrid` command column [models](xref:404767).
syntax:
  content: public IList<DxGridCommandColumnModel> GridCommandActionColumnModels { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.Blazor.Editors.Models.DxGridCommandColumnModel}
    description: A collection of `DxGrid` command column models.
seealso: []
---
Use this property to customize the `GridCommandActionColumnModels` collection:

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

          if(View.Editor is DxGridListEditor gridListEditor) {
              gridListEditor.GridCommandActionColumnModels.FirstOrDefault(c => c.Name == "RecordEdit").VisibleIndex = 3;
          }
      }
  }
```