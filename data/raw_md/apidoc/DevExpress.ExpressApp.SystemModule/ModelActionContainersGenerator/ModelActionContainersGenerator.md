---
uid: DevExpress.ExpressApp.SystemModule.ModelActionContainersGenerator
name: ModelActionContainersGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.SystemModule.IModelActionToContainerMapping) node.
syntax:
  content: 'public class ModelActionContainersGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ModelActionContainersGenerator._members
  altText: ModelActionContainersGenerator Members
- linkId: "112810"
- linkId: "112610"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **ActionDesign** | **ActionToContainerMapping** node. 
It collects [IModelAction.Category](xref:DevExpress.ExpressApp.Model.IModelAction.Category) values specified for **ActionDesign** | **Actions** nodes and generates [](xref:DevExpress.ExpressApp.SystemModule.IModelActionContainer) node for each category found. Each **ActionContainer** node contains [](xref:DevExpress.ExpressApp.SystemModule.IModelActionLink) nodes specifying Actions linked to the Action Container.

To customize the content of the **ActionToContainerMapping** node, implement a Generator Updater for this Nodes Generator by inheriting the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) class in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModelNodesGeneratorUpdater<ModelActionContainersGenerator> {
    public override void UpdateNode(ModelNode node) {
        // Cast the 'node' parameter to IModelActionToContainerMapping
        // to access the ActionToContainerMapping node.
    }
}
```
***

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.