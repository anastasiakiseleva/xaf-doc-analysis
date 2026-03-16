---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewLayoutNodesGenerator
name: ModelDetailViewLayoutNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelViewLayout) node.
syntax:
  content: 'public class ModelDetailViewLayoutNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewLayoutNodesGenerator._members
  altText: ModelDetailViewLayoutNodesGenerator Members
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **Views** | **View** | **Layout** node. It creates the layout structure of the current View. The rules of generating a default layout are described in the [View Items Layout Customization](xref:112817) topic.

[!include[<Layout><ModelDetailViewLayoutNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method. The complete example of implementing a Generator Updater for this Node Generator is available in the [How to: Implement a View Item](xref:405483) topic.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.