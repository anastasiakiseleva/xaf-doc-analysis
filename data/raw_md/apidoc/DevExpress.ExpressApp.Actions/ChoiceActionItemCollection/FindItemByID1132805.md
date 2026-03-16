---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItemCollection.FindItemByID(System.String)
name: FindItemByID(String)
type: Method
summary: Returns the item with the specified identifier. Does not search over the child items of the collection's items.
syntax:
  content: public ChoiceActionItem FindItemByID(string itemId)
  parameters:
  - id: itemId
    type: System.String
    description: A string value that specifies the identifier of the Action Item to be found.
  return:
    type: DevExpress.ExpressApp.Actions.ChoiceActionItem
    description: A [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) object with the specified identifier, contained in the **ChoiceActionItemCollection**.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItemCollection.Find*
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItemCollection.FindItemByID(System.String)
---
Generally, you do not need to use this method. Use the [ChoiceActionItemCollection.Find](xref:DevExpress.ExpressApp.Actions.ChoiceActionItemCollection.Find*) method overload which takes an _itemId_ parameter, instead.