---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ImageSourceNodesGenerator
name: ImageSourceNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelImageSources) node.
syntax:
  content: 'public class ImageSourceNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ImageSourceNodesGenerator._members
  altText: ImageSourceNodesGenerator Members
- linkId: "112810"
- linkId: "404209"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates the following child nodes of the **ImageSources** node:
* the "Images" [](xref:DevExpress.ExpressApp.Model.IModelFileImageSource) node
* the [](xref:DevExpress.ExpressApp.Model.IModelAssemblyResourceImageSource) nodes for each referenced module assembly
* the "DevExpress.Images.v<:xx.x:>" @DevExpress.ExpressApp.Model.IModelDevExpressImagesAssemblyImageSource node for the _DevExpress.Images.v<:xx.x:>_ assembly

[!include[<ImageSources><ImageSourceNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.