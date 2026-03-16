---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.RootValue
name: RootValue
type: Property
summary: Specifies the root node.
syntax:
  content: public ITreeNode RootValue { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.General.ITreeNode
    description: An [](xref:DevExpress.Persistent.Base.General.ITreeNode) object which specifies the root node. The default value is _null_.
seealso: []
---
A tree node specified by this property will be considered the root. By default, the **RootValue** is set to _null_, which means that all the nodes that have their [ITreeNode.Parent](xref:DevExpress.Persistent.Base.General.ITreeNode.Parent) property set to _null_ are considered root.