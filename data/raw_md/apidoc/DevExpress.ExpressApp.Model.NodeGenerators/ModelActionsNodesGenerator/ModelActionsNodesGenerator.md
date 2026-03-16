---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelActionsNodesGenerator
name: ModelActionsNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelActions) node.
syntax:
  content: 'public class ModelActionsNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelActionsNodesGenerator._members
  altText: ModelActionsNodesGenerator Members
- linkId: "112810"
- linkId: "112621"
- linkId: "112622"
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the **ActionDesign** | **Actions** node. It collects Controllers from the **Controllers** node, and gets their owned Actions via the [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) property. It adds [](xref:DevExpress.ExpressApp.Model.IModelAction) nodes that represent found actions. An [](xref:DevExpress.ExpressApp.Model.IModelChoiceActionItems) child node is additionally created for [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase) Actions.

[!include[<Actions><ModelActionsNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.