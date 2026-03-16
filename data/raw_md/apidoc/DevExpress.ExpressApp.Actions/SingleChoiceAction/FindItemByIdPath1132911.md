---
uid: DevExpress.ExpressApp.Actions.SingleChoiceAction.FindItemByIdPath(System.String)
name: FindItemByIdPath(String)
type: Method
summary: Provides access to the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction)'s [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) with the specified identifier path.
syntax:
  content: public ChoiceActionItem FindItemByIdPath(string idPath)
  parameters:
  - id: idPath
    type: System.String
    description: A string that represents the full identifier path to the required **ChoiceActionItem**.
  return:
    type: DevExpress.ExpressApp.Actions.ChoiceActionItem
    description: A [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) with the specified identifier path.
seealso:
- linkId: DevExpress.ExpressApp.Actions.SingleChoiceAction.FindItemByCaptionPath(System.String)
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItem.GetIdPath
---
Each item of a Choice Action has an identifier path associated with it. This path is represented by a sequence of parent item identifiers separated by the slash character. Use the `FindItemByIdPath` method to access a particular item, by specifying the path associated with it.  If an item with the specified path is not found, this method returns `null`. To retrieve the identifier path of a Choice Action Item, use the [ChoiceActionItem.GetIdPath](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.GetIdPath) method.

The following snippet illustrates how to disable the **SetTaskAction** Action's "Priority/High" item, when the current user is "John".

# [C#](#tab/tabid-csharp)

```csharp
ChoiceActionItem priorityHighItem = SetTaskAction.FindItemByIdPath("Priority/High");
if (priorityHighItem != null) 
    priorityHighItem.Enabled.SetItemValue(
        "SecurityAllowance", SecuritySystem.CurrentUserName != "John");
```
***

![FindItemByCaptionPath](~/images/finditembycaptionpath116702.png)

Alternatively, you can use the [SingleChoiceAction.FindItemByCaptionPath](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.FindItemByCaptionPath(System.String)) method to find a specific item by its caption path.