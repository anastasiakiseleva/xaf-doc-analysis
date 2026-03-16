---
uid: DevExpress.ExpressApp.SystemModule.ModelListViewFiltersGenerator
name: ModelListViewFiltersGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilters) node.
syntax:
  content: 'public class ModelListViewFiltersGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ModelListViewFiltersGenerator._members
  altText: ModelListViewFiltersGenerator Members
- linkId: "112810"
- linkId: "112998"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **View** | **ListView** | **Filters** node. Collects filters specified for the current List View's business class via the [](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute) attributes. Creates the [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilterItem) for each filter.

To customize the content of the **AppearanceRules** node, implement a Generator Updater for this Nodes Generator by inheriting the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) class in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModelNodesGeneratorUpdater<ModelListViewFiltersGenerator> {
    public override void UpdateNode(ModelNode node) {
        // Cast the 'node' parameter to IModelListViewFilters
        // to access the Filters node.
    }
}
```
***

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method. The complete example of implementing a Generator Updater for this Nodes Generator is provided in the [Filters Application Model Node](xref:112992) topic.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.