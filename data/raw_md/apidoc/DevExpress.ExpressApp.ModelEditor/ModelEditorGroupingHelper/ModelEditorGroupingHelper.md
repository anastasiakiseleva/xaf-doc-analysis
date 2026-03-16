---
uid: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper
name: ModelEditorGroupingHelper
type: Class
summary: Contains helper methods and properties that you can use to replace or customize the default grouping mechanism in the [Model Editor](xref:112582)'s [Nodes Tree](xref:113328).
syntax:
  content: public class ModelEditorGroupingHelper
seealso:
- linkId: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper._members
  altText: ModelEditorGroupingHelper Members
---
The following example demonstrates how to group [](xref:DevExpress.ExpressApp.Validation.IModelValidationRules) child nodes by a target type's full name. 
1. In the module's constructor implemented in the _MySolution.Module\Module.cs_ file, access the `ModelEditorGroupingHelper` instance (see [ModelEditorGroupingHelper.Instance](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.Instance)) and call its [RegisterNodeGroupPathDelegate](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.RegisterNodeGroupPathDelegate(System.Type,System.Func{DevExpress.ExpressApp.Model.IModelNode,System.String[]})). Pass the type of a node you want to regroup (`IModelValidationRules`) and a delegate with grouping logic (`GroupPathCalculatorByNamespace`) to this delegate. 
    > [!IMPORTANT]
    > Do not customize `ModelEditorGroupingHelper` in multiple modules in the solution to avoid design-time issues in the Model Editor.
2. In the `GroupPathCalculatorByNamespace` method, return a string array where each array item is a group in the Node Tree. 
3. Create an array with the @DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.UnspecifiedGroupName constant value and return it for nodes whose group path cannot be calculated for the current model node.

**File**: _MySolution.Module\Module.cs._

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp; 
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.ModelEditor; 
using DevExpress.ExpressApp.Model.Core;
using DevExpress.ExpressApp.Validation;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        InitializeComponent();
        ModelEditorGroupingHelper.Instance.RegisterNodeGroupPathDelegate(
        typeof(IModelValidationRules), node => GroupPathCalculatorByNamespace("TargetType.FullName", node));
    }
    private static string[] EmptyGroupName = new string[] { ModelEditorGroupingHelper.UnspecifiedGroupName };
    public string[] GroupPathCalculatorByNamespace(string propertyName, IModelNode modelNode) {
        object propertyValue = ModelEditorGroupingHelper.Instance.GetPropertyValue(propertyName, modelNode);
        if(propertyValue != null) {
            string typeName = propertyValue.ToString();
            if(!string.IsNullOrEmpty(typeName)) {
                int lastPointIndex = typeName.LastIndexOf('.');
                if(lastPointIndex > 0) {
                    return new string[] {
                        typeName.Substring(0, lastPointIndex),
                        typeName.Substring(lastPointIndex + 1)
                    };
                }
                else {
                    return new string[] { typeName };
                }
            }
        }
        return EmptyGroupName;
    }
    // ...
}
```
***

The following image demonstrates the grouped **Validation** | **Rules** nodes:

![ModelEditorGroupingHelper](~/images/modeleditorgroupinghelper131163.png)

You can apply the same grouping mechanism to other model nodes. The following example demonstrates how to register the `GroupPathCalculatorByNamespace` mechanism for the @DevExpress.ExpressApp.Model.IModelViews node in addition to @DevExpress.ExpressApp.Validation.IModelValidationRules.

**File**: _MySolution.Module\Module.cs_

# [C#](#tab/tabid-csharp)

```csharp{14-17}
using DevExpress.ExpressApp; 
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.ModelEditor; 
using DevExpress.ExpressApp.Model.Core;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        InitializeComponent();
        ModelEditorGroupingHelper.Instance.RegisterNodeGroupPathDelegate(
            typeof(IModelValidationRules), 
            node => GroupPathCalculatorByNamespace("TargetType.FullName", node)
        );
        ModelEditorGroupingHelper.Instance.RegisterNodeGroupPathDelegate(
            typeof(IModelViews), 
            node => GroupPathCalculatorByNamespace("ModelClass.Name", node)
        );
    }
    // ...
}
```
***

The following image demonstrates the grouped **Views** nodes:

![ModelEditorGroupingHelper](~/images/modeleditorgroupinghelper131163_2.png)

> [!Note]
> XAF uses the same mechanism to group the **Validation** | **Rules** and **Views** nodes. 