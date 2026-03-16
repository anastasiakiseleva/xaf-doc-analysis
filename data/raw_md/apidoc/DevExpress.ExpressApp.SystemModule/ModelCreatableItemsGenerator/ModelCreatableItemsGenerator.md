---
uid: DevExpress.ExpressApp.SystemModule.ModelCreatableItemsGenerator
name: ModelCreatableItemsGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems) node.
syntax:
  content: 'public class ModelCreatableItemsGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ModelCreatableItemsGenerator._members
  altText: ModelCreatableItemsGenerator Members
- linkId: "112810"
- linkId: DevExpress.Persistent.Base.CreatableItemAttribute
- linkId: DevExpress.Persistent.Base.DefaultClassOptionsAttribute
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **CreatableItems** node. It adds an [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItem) node for each business class having the [IModelClass.IsCreatableItem](xref:DevExpress.ExpressApp.Model.IModelClass.IsCreatableItem) property set to **True**.

To customize the content of the **CreatableItems** node, implement a Generator Updater for this Nodes Generator by inheriting the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) class in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModelNodesGeneratorUpdater<ModelCreatableItemsGenerator> {
    public override void UpdateNode(ModelNode node) {
        // Cast the 'node' parameter to IModelCreatableItems
        // to access the CreatableItems node.
    }
}
```
***

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.