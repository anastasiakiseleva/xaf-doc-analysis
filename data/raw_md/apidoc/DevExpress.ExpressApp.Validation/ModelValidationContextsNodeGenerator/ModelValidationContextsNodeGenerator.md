---
uid: DevExpress.ExpressApp.Validation.ModelValidationContextsNodeGenerator
name: ModelValidationContextsNodeGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Validation.IModelValidationContexts) node.
syntax:
  content: 'public class ModelValidationContextsNodeGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Validation.ModelValidationContextsNodeGenerator._members
  altText: ModelValidationContextsNodeGenerator Members
- linkId: "112810"
- linkId: "113008"
- linkId: "113251"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **Validation** | **Contexts** node. It uses [IRuleBaseProperties.TargetContextIDs](xref:DevExpress.Persistent.Validation.IRuleBaseProperties.TargetContextIDs) values from the **Validation** | **Rules** | **Rule** nodes to collect Validation Contexts, and adds an [](xref:DevExpress.ExpressApp.Validation.IModelValidationContext) node for each Context.

To customize the content of the **Contexts** node, implement a Generator Updater for this Nodes Generator by inheriting the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) class in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModelNodesGeneratorUpdater<ModelValidationContextsNodeGenerator> {
    public override void UpdateNode(ModelNode node) {
        // Cast the 'node' parameter to IModelValidationContexts
        // to access the Contexts node.
    }
}
```
***

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.