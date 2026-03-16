---
uid: DevExpress.ExpressApp.Blazor.Editors.DxGridListEditorBase.RemoveColumnModel(DevExpress.ExpressApp.Blazor.Editors.Models.DxDataColumnBaseModel)
name: RemoveColumnModel(DxDataColumnBaseModel)
type: Method
summary: Removes an unbound column from the @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.
syntax:
  content: public void RemoveColumnModel(DxDataColumnBaseModel dataColumnModel)
  parameters:
  - id: dataColumnModel
    type: DevExpress.ExpressApp.Blazor.Editors.Models.DxDataColumnBaseModel
    description: The [Component Model](xref:404767) that identifies the column to be deleted.
seealso: []
---

The following code snippet removes an unbound column from the Grid:

```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp;
using MySolutionName.Module.BusinessObjects;
using DevExpress.ExpressApp.Blazor.Editors.Models;

namespace MySolutionName.Blazor.Server.Controllers;
public class UnboundColumnController : ObjectViewController<ListView, TestObjects> {
    protected override void OnViewControlsCreated() {
        if (View.Editor is DxGridListEditor editor) {
            // Remove an unbound column
            var columnToRemove = (DxGridColumnWrapper)editor.Columns.FirstOrDefault(u => u.PropertyName == "property name");
            if (columnToRemove != null) {
                editor.RemoveColumnModel(columnToRemove.DxGridDataColumnModel);
            }
        }
        base.OnViewControlsCreated();
    }
}
```