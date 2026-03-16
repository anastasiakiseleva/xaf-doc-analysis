---
uid: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.AllowSplitByGroupLevels
name: AllowSplitByGroupLevels
type: Property
summary: Specifies, whether or not the groups are split into subgroups using the [ModelEditorGroupingHelper.GroupLevels](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.GroupLevels) list in the [Model Editor](xref:112582)'s [Nodes Tree](xref:113328).
syntax:
  content: public bool AllowSplitByGroupLevels { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if groups are split into subgroups using the predefined list; otherwise, **false**.'
seealso: []
---
You can change the `AllowSplitByGroupLevels` value in the module's constructor implemented in the _MySolution.Module\Module.cs_ file:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ModelEditor;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule () {
        InitializeComponent();
        ModelEditorGroupingHelper.Instance.AllowSplitByGroupLevels = true;
    }
    // ...
}
```
***

The **`AllowSplitByGroupLevels`** property allows splitting for all nodes. To enable or disable splitting for a specific node type, use the [ModelEditorGroupingHelper.SplitByGroupLevels](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.SplitByGroupLevels(System.Type,System.Boolean)) method instead.