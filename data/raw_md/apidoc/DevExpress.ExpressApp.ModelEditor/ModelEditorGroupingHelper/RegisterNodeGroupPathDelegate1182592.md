---
uid: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.RegisterNodeGroupPathDelegate(System.Type,System.Func{DevExpress.ExpressApp.Model.IModelNode,System.String[]})
name: RegisterNodeGroupPathDelegate(Type, Func<IModelNode, String[]>)
type: Method
summary: Registers the method used to calculate the Application Model node's group path in the [Model Editor](xref:112582)'s [Nodes Tree](xref:113328).
syntax:
  content: public void RegisterNodeGroupPathDelegate(Type collectionNodeType, Func<IModelNode, string[]> GetNodeGroupPathDelegate)
  parameters:
  - id: collectionNodeType
    type: System.Type
    description: A [](xref:System.Type) object specifying the type of the Application Model node.
  - id: GetNodeGroupPathDelegate
    type: System.Func{DevExpress.ExpressApp.Model.IModelNode,System.String[]}
    description: A delegate used to calculate the Application Model node's group path.
seealso: []
---
You can call the `RegisterNodeGroupPathDelegate` method in the module's constructor implemented in the _MySolution.Module\Module.cs_ file.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ModelEditor;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule () {
        InitializeComponent();
        ModelEditorGroupingHelper.Instance.AllowSplitByGroupLevels = true;
        ModelEditorGroupingHelper.Instance.RegisterNodeGroupPathDelegate(
            typeof(IModelViews), node => CusomGroupPathCalculator(node));
    }
    public string[] CusomGroupPathCalculator(IModelNode node) {
        // ...
    }
    // ...
}
```
***

You can use the [ModelEditorGroupingHelper.SplitGroupPath](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.SplitGroupPath*) helper method in your custom delegate to calculate the group path.

The [](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper) provides two built-in delegates that can be passed to the `RegisterNodeGroupPathDelegate` method:

* [ModelEditorGroupingHelper.DefaultGroupPathCalculator](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.DefaultGroupPathCalculator(System.String,DevExpress.ExpressApp.Model.IModelNode))
* [ModelEditorGroupingHelper.ActionsNodeGroupPathCalculator](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.ActionsNodeGroupPathCalculator(System.String,DevExpress.ExpressApp.Model.IModelNode))