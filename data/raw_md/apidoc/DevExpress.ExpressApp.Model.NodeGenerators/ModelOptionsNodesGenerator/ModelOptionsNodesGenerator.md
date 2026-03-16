---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelOptionsNodesGenerator
name: ModelOptionsNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelOptions) node.
syntax:
  content: |-
    [Browsable(false)]
    public class ModelOptionsNodesGenerator : ModelNodesGeneratorBase
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelOptionsNodesGenerator._members
  altText: ModelOptionsNodesGenerator Members
- linkId: "112810"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant that implements an empty **GenerateNodesCore** method, so it generates nothing. However, as it is attached to the **Options** node, you can implement a Generator Updater for this Generator, and customize the **Options** node.

[!include[<Options><ModelOptionsNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.