---
uid: DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper.SplitGroupPath(System.String,DevExpress.ExpressApp.Model.IModelNode,System.Collections.Generic.IList{System.String})
name: SplitGroupPath(String, IModelNode, IList<String>)
type: Method
summary: Splits the specified group name into subgroups.
syntax:
  content: public string[] SplitGroupPath(string fullGroupsName, IModelNode sourceNode, IList<string> customGroupLevels)
  parameters:
  - id: fullGroupsName
    type: System.String
    description: A string which is the group name.
  - id: sourceNode
    type: DevExpress.ExpressApp.Model.IModelNode
    description: An [](xref:DevExpress.ExpressApp.Model.IModelNode) object specifying the Application Model node.
  - id: customGroupLevels
    type: System.Collections.Generic.IList{System.String}
    description: A [List](xref:System.Collections.Generic.List`1)\<[](xref:System.String)> of strings that are used to split the group into subgroups.
  return:
    type: System.String[]
    description: An array of strings that are subgroup names.
seealso: []
---
