---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItem.ToString
name: ToString()
type: Method
summary: Returns a Choice Action Item's textual representation.
syntax:
  content: public override string ToString()
  return:
    type: System.String
    description: A [](xref:System.String) value which is the current Choice Action Item's textual representation.
seealso: []
---
The **ToString** method returns the human readable name of the current **Choice Action Item**. This name is formed from the Item's caption and the analogous textual representation of the Item's nested Items (from their [ChoiceActionItem.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Items) collection). For instance, the Item that contains two nested Items, one of which contains an Item, is represented by the following string: "Entry1[Item1[Item11],Item2]". If an Item's caption is not specified, the item type name is used, instead.