---
uid: DevExpress.ExpressApp.SystemModule.NavigationItemNodeGenerator
name: NavigationItemNodeGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems) node.
syntax:
  content: 'public class NavigationItemNodeGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.NavigationItemNodeGenerator._members
  altText: NavigationItemNodeGenerator Members
- linkId: "112810"
- linkId: "113198"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node. Adds [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) nodes for business classes that have the [IModelClassNavigation.IsNavigationItem](xref:DevExpress.ExpressApp.SystemModule.IModelClassNavigation.IsNavigationItem) property set to **true** in the corresponding **BOModel** | **_\<Class\>_** node.

To customize the content of the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node, implement a Generator Updater for this Nodes Generator by inheriting the [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorUpdater`1) class in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
public class Updater : ModelNodesGeneratorUpdater<NavigationItemNodeGenerator> {
    public override void UpdateNode(ModelNode node) {
        // Cast the 'node' parameter to IModelRootNavigationItems
        // to access the NavigationItems node.
    }
}
```
***

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.