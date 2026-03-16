---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItem.GetIdPath
name: GetIdPath()
type: Method
summary: Returns a full identifier path from the current Item to the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection's first-level parent Item.
syntax:
  content: public string GetIdPath()
  return:
    type: System.String
    description: A string containing a chain of item identifiers from the current Item to the root parent Item, separated by the slash character.
seealso: []
---
Each ChoiceActionItem can have a collection of ChoiceActionItems, each of which can also have a collection of ChoiceActionItems, and so on. The entire Items collection of a ChoiceAction can contain two or more ChoiceActionItems with the same identifier. You can uniquely identify an item via the **GetIdPath** method. For instance, if "Item121" is the current Item's identifier, the **GetIdPath** method return value can be "Item1/Item12/Item121".

To access a ChoiceActionItem using its full identifier path, use the [SingleChoiceAction.FindItemByIdPath](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.FindItemByIdPath(System.String)) method.