---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItem.GetItemPath
name: GetItemPath()
type: Method
summary: Returns a full path from the current Item to the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection's first-level parent Item.
syntax:
  content: public string GetItemPath()
  return:
    type: System.String
    description: A string containing a chain of item captions from the current Item to the root parent Item, separated by the dot character.
seealso: []
---
Each ChoiceActionItem can have a collection of ChoiceActionItems, each of which can also have a collection of ChoiceActionItems, and so on. The entire Items collection of a ChoiceAction can contain two or more ChoiceActionItems with the same captions. You can uniquely identify an item via the **GetItemPath** method. For instance, if "Item121" is the current Item's caption, the **GetItemPath** method return value can be "Item1.Item12.Item121".

To access a ChoiceActionItem using its full path, use the [SingleChoiceAction.FindItemByCaptionPath](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.FindItemByCaptionPath(System.String)) method.