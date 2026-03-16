---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItem.IsHierarchical
name: IsHierarchical()
type: Method
summary: Checks whether the [ChoiceActionItem.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Items) collection exposed by the current [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) has a tree-like structure.
syntax:
  content: public bool IsHierarchical()
  return:
    type: System.Boolean
    description: '**true** if there are Items containing other Items; otherwise **false**.'
seealso: []
---
The **IsHierarchical** method iterates through the Items collection exposed by the current Item (represented by the [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItemCollection) class), and detects if there are child Items.