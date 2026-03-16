---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewItemsNodesGenerator
name: ModelDetailViewItemsNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelViewItems) node.
syntax:
  content: 'public sealed class ModelDetailViewItemsNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewItemsNodesGenerator._members
  altText: ModelDetailViewItemsNodesGenerator Members
- linkId: "112810"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **Views** | **View** | **Items** node. If the parent **View** node is [](xref:DevExpress.ExpressApp.Model.IModelObjectView), it adds [](xref:DevExpress.ExpressApp.Model.IModelPropertyEditor) nodes for members of the current object that should be visible. 
Separate **PropertyEditor** nodes are generated for aggregated objects' members, if this option is enabled via the [](xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute) attribute.

[!include[<Items><ModelDetailViewItemsNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method. The complete example of implementing a Generator Updater for this Node Generator is available in the [How to: Implement a View Item](xref:405483) topic.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.