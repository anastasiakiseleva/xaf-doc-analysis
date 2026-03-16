---
uid: DevExpress.Persistent.Base.General.ITreeNode.Children
name: Children
type: Property
summary: Provides access to the current node's child nodes.
syntax:
  content: IBindingList Children { get; }
  parameters: []
  return:
    type: System.ComponentModel.IBindingList
    description: A [](xref:System.ComponentModel.IBindingList) object that represents the current node's child nodes.
seealso: []
---
The child nodes are the nodes that have their [ITreeNode.Parent](xref:DevExpress.Persistent.Base.General.ITreeNode.Parent) property pointing to the current node.