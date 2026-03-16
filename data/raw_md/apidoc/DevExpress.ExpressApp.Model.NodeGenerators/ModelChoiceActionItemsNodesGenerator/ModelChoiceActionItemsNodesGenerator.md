---
uid: DevExpress.ExpressApp.Model.NodeGenerators.ModelChoiceActionItemsNodesGenerator
name: ModelChoiceActionItemsNodesGenerator
type: Class
summary: A [Nodes Generator](xref:112810) that generates the content of the [](xref:DevExpress.ExpressApp.Model.IModelChoiceActionItems) node.
syntax:
  content: 'public class ModelChoiceActionItemsNodesGenerator : ModelNodesGeneratorBase'
seealso:
- linkId: DevExpress.ExpressApp.Model.NodeGenerators.ModelChoiceActionItemsNodesGenerator._members
  altText: ModelChoiceActionItemsNodesGenerator Members
- linkId: "112810"
- linkId: "112622"
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionBase
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItem
---
This class is a [](xref:DevExpress.ExpressApp.Model.ModelNodesGeneratorBase) descendant, that generates child nodes of the [!include[Node_Action](~/templates/node_action111373.md)] | **ChoiceActionItems** nodes. It adds [](xref:DevExpress.ExpressApp.Model.IModelChoiceActionItem) nodes that represent items of the Choice Action.

[!include[<ChoiceActionItems><ModelChoiceActionItemsNodesGenerator>](~/templates/nodegenerator-example.md)]

The Generator Updater above should be registered within the overridden [ModuleBase.AddGeneratorUpdaters](xref:DevExpress.ExpressApp.ModuleBase.AddGeneratorUpdaters(DevExpress.ExpressApp.Model.Core.ModelNodesGeneratorUpdaters)) method.

For a complete list of available Nodes Generators, refer to the [Built-in Nodes Generators](xref:113316) topic.