---
uid: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.Instance
name: Instance
type: Property
summary: Gets the existing [](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper) instance.
syntax:
  content: public static ModelEditorGroupingHelper Instance { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper
    description: An [](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper) object.
seealso: []
---
Use the `Instance` property to access the API provided by the [](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper) class. This property is _static_. You can use it in the module's constructor implemented in the _MySolution.Module\Module.cs_ file.

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