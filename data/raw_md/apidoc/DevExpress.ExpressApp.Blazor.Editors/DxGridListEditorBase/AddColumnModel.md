---
uid: DevExpress.ExpressApp.Blazor.Editors.DxGridListEditorBase.AddColumnModel(DevExpress.ExpressApp.Blazor.Editors.Models.DxDataColumnBaseModel)
name: AddColumnModel(DxDataColumnBaseModel)
type: Method
summary: Adds an unbound column to the @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.
syntax:
  content: public void AddColumnModel(DxDataColumnBaseModel dataColumnModel)
  parameters:
  - id: dataColumnModel
    type: DevExpress.ExpressApp.Blazor.Editors.Models.DxDataColumnBaseModel
    description: The [Component Model](xref:404767) that allows you to configure column properties such as the field name, caption, visibility, sorting, and format.
seealso: []
---

The following code snippet adds two columns to the Grid: 

- `Total` - specifies the `UnboundExpression` property to calculate values. 
- `Result`- uses the `UnboundColumnData` event handler to obtain data (see the next code snippet).

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
            //Add an unbound column
            editor.AddColumnModel(
                new DxGridDataColumnModel() {
                    FieldName = "Total",
                    Caption = "Total",
                    Visible = true,
                    VisibleIndex = 5,
                    UnboundType = GridUnboundColumnType.Integer,
                    UnboundExpression = "Number1 + Number2 + Number3"
                }
            );
            editor.AddColumnModel(
                new DxGridDataColumnModel() {
                    FieldName = "Result",
                    Caption = "Result",
                    Visible = true,
                    VisibleIndex = 6,
                    UnboundType = GridUnboundColumnType.String,
                }
            );
        }
        base.OnViewControlsCreated();
    }
}
```

The following code handles the `UnboundColumnData` event to supply values to the `Result` column based on `Total` column values:

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
            // Obtain an unbound column by field name
            editor.GridModel.UnboundColumnData = (args) => {
                if(args.FieldName == "Result") {
                    var total = (int)args.GetRowValue("Total");
                    if(total > 0)
                        args.Value = "Positive";
                    else if(total == 0)
                        args.Value = "Zero";
                    else
                        args.Value = "Negative";
                }
            };
        }
        base.OnViewControlsCreated();
    }
}
```