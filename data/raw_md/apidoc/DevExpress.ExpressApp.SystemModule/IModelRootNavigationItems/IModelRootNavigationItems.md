---
uid: DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems
name: IModelRootNavigationItems
type: Interface
summary: The [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node specifies the navigation structure used by the **ShowNavigationItem** Action.
syntax:
  content: |-
    [ImageName("ModelEditor_Navigation_Items")]
    [ModelNodesGenerator(typeof(NavigationItemNodeGenerator))]
    public interface IModelRootNavigationItems : IModelNode
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems._members
  altText: IModelRootNavigationItems Members
- linkId: "112579"
- linkId: "113198"
---
The **ShowNavigationItem** Action is displayed via the navigation control on the main Window. The navigation control comprises the navigation items. This node defines these items. You can add items by selecting the **Add Item** menu item in the context menu.

You can add child nodes to the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node in code. Use the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) attribute for this purpose.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.SystemModule.NavigationItemNodeGenerator) Nodes Generator.