---
uid: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.SplitByGroupLevels(System.Type,System.Boolean)
name: SplitByGroupLevels(Type, Boolean)
type: Method
summary: Enables or disables splitting groups into subgroups using the [ModelEditorGroupingHelper.GroupLevels](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.GroupLevels) list for a specific Application Model node type.
syntax:
  content: public void SplitByGroupLevels(Type collectionNodeType, bool allowSplit)
  parameters:
  - id: collectionNodeType
    type: System.Type
    description: A [](xref:System.Type) object specifying the type of the Application Model node.
  - id: allowSplit
    type: System.Boolean
    description: '**true**, if  splitting groups to subgroups is allowed for _collectionNodeType_ nodes; otherwise, **false**.'
seealso: []
---
To enable or disable splitting for all nodes at once, use the [ModelEditorGroupingHelper.AllowSplitByGroupLevels](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.AllowSplitByGroupLevels) property instead of this method.