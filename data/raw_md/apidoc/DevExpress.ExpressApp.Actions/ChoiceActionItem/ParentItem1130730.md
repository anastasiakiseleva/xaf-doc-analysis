---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItem.ParentItem
name: ParentItem
type: Property
summary: Returns the current ChoiceActionItem's parent item.
syntax:
  content: |-
    [Browsable(false)]
    public ChoiceActionItem ParentItem { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.ChoiceActionItem
    description: A [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) object representing the current Item's parent item.
seealso: []
---
Each ChoiceActionItem can have a collection of ChoiceActionItems, each of which can also have a collection of ChoiceActionItems, and so on. The entire Items collection of a ChoiceAction can contain two or more ChoiceActionItems with the same captions. You can determine an Item by its parent Item. For this purpose, use the **ParentItem** property. Alternatively, use the [ChoiceActionItem.GetItemPath](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.GetItemPath) method.