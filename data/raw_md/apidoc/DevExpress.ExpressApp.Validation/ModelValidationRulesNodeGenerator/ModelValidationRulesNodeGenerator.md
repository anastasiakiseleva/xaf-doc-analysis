---
uid: DevExpress.ExpressApp.Validation.ModelValidationRulesNodeGenerator
name: ModelValidationRulesNodeGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Validation.IModelValidationRules) node.
syntax:
  content: 'public class ModelValidationRulesNodeGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Validation.ModelValidationRulesNodeGenerator._members
  altText: ModelValidationRulesNodeGenerator Members
- linkId: "112810"
- linkId: "113008"
- linkId: "113251"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **Validation** | **Rules** node. Collects Validation Rules specified in code and adds corresponding [](xref:DevExpress.ExpressApp.Validation.IModelRuleBase) nodes.

To customize the content of the **Rules** node, implement a Generator Updater for this Nodes Generator by inheriting the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) class in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModelNodesGeneratorUpdater<ModelValidationRulesNodeGenerator> {
    public override void UpdateNode(ModelNode node) {
        // Cast the 'node' parameter to IModelValidationRules
        // to access the Rules node.
    }
}
```
***

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.