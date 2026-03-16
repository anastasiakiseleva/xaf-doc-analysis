---
uid: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.GroupLevels
name: GroupLevels
type: Property
summary: Gets the predefined list of strings that are used to split groups into subgroups in the [Model Editor](xref:112582)'s [Nodes Tree](xref:113328) when the [ModelEditorGroupingHelper.AllowSplitByGroupLevels](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.AllowSplitByGroupLevels) property is set to **true**.
syntax:
  content: public List<string> GroupLevels { get; }
  parameters: []
  return:
    type: System.Collections.Generic.List{System.String}
    description: A [List](xref:System.Collections.Generic.List`1)\<[](xref:System.String)> of strings that are used to split groups into subgroups.
seealso: []
---
By default, the `GroupLevels` list includes:

``"DevExpress"``

``"ExpressApp.Win"``

``"ExpressApp.Web"``

``"ExpressApp"``

``"SystemModule"``

``"Persistent"``

``"BaseImpl"``

``"ReportsV2"``

``"Reports"``

``"Security"``

``"Validation"``

``"FileAttachments"``

``"Notifications"``

``"PivotGrid"``

``"Scheduler"``

``"TreeListEditors"``

``"Xpo"``

``"DC"``

``"EF"``

You can add more values to this list to provide grouping for your custom nodes, using the following code in the module's constructor implemented in the _MySolution.Module\Module.cs_ file.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ModelEditor;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule () {
        InitializeComponent();
        ModelEditorGroupingHelper.Instance.AllowSplitByGroupLevels = true;
        ModelEditorGroupingHelper.Instance.GroupLevels.Add("MySolution.Module.BusinessObjects.Planning");
        ModelEditorGroupingHelper.Instance.GroupLevels.Add("MySolution.Module.BusinessObjects.Marketing");
    }
    // ...
}
```
***

You can also use one of the [ModelEditorGroupingHelper.SplitGroupPath](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.SplitGroupPath*) method overloads to split group paths in your custom delegate registered using the [ModelEditorGroupingHelper.RegisterNodeGroupPathDelegate](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.RegisterNodeGroupPathDelegate(System.Type,System.Func{DevExpress.ExpressApp.Model.IModelNode,System.String[]})) method.