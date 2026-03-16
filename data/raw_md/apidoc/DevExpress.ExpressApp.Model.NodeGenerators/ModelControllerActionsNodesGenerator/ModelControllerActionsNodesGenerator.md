---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelControllerActionsNodesGenerator
name: ModelControllerActionsNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelControllerActions) node.
syntax:
  content: 'public class ModelControllerActionsNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelControllerActionsNodesGenerator._members
  altText: ModelControllerActionsNodesGenerator Members
- linkId: "112810"
- linkId: "112621"
- linkId: "112622"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **ActionDesign** | **Controllers** | **Controller** | **Actions** nodes. It collects Actions of the current Controller from the [](xref:DevExpress.ExpressApp.Model.IModelActions) node.

[!include[<Actions><ModelControllerActionsNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.