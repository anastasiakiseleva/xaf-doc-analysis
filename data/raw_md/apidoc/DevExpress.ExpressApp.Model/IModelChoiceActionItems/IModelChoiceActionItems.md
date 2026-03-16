---
uid: DevExpress.ExpressApp.Model.IModelChoiceActionItems
name: IModelChoiceActionItems
type: Interface
summary: Displays a collection of Choice Action Items in the Application Model that corresponds to items in the Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelChoiceActionItemsNodesGenerator))]
    public interface IModelChoiceActionItems : IModelNode, IModelList<IModelChoiceActionItem>, IList<IModelChoiceActionItem>, ICollection<IModelChoiceActionItem>, IEnumerable<IModelChoiceActionItem>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelChoiceActionItems._members
  altText: IModelChoiceActionItems Members
- linkId: "112579"
- linkId: "112580"
---
This node is available when the parent node is an Action of the [SingleChoiceAction](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) type. Only items added in the Controller's constructor are loaded to the Application Model.

This interface is a part of the [Application Model infrastructure](xref:112580). Usually, you do not need to implement this interface.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelChoiceActionItemsNodesGenerator) Nodes Generator.