---
uid: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.AllowSplitByPoint
name: AllowSplitByPoint
type: Property
summary: Specifies, whether or not the groups are split into subgroups by the dot character in the [Model Editor](xref:112582)'s [Nodes Tree](xref:113328).
syntax:
  content: public bool AllowSplitByPoint { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if groups are split into subgroups by the dot character; otherwise, **false**.'
seealso: []
---
You can change the `AllowSplitByPoint` value in the module's constructor implemented in the _MySolution.Module\Module.cs_ file.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ModelEditor;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule () {
        InitializeComponent();
        ModelEditorGroupingHelper.Instance.AllowSplitByPoint = true;
    }
    // ...
}
```
***