---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelControllersNodesGenerator
name: ModelControllersNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelControllers) node.
syntax:
  content: 'public class ModelControllersNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelControllersNodesGenerator._members
  altText: ModelControllersNodesGenerator Members
- linkId: "112810"
- linkId: "112621"
- linkId: "112622"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **ActionDesign** | **Controllers** node. It adds an [](xref:DevExpress.ExpressApp.Model.IModelViewController), [](xref:DevExpress.ExpressApp.Model.IModelWindowController) or [](xref:DevExpress.ExpressApp.Model.IModelController) node for each registered Controller, depending on the Controller type. Adds the [](xref:DevExpress.ExpressApp.Model.IModelControllerActions) child node for Controllers exposing a non-empty [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) Actions list.

[!include[<Controllers><ModelControllersNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.