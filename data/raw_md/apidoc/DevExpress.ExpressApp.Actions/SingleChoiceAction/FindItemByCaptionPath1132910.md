---
uid: DevExpress.ExpressApp.Actions.SingleChoiceAction.FindItemByCaptionPath(System.String)
name: FindItemByCaptionPath(String)
type: Method
summary: Provides access to the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction)'s [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) with the specified caption path.
syntax:
  content: public ChoiceActionItem FindItemByCaptionPath(string captionPath)
  parameters:
  - id: captionPath
    type: System.String
    description: A string that represents the full caption path to the required **ChoiceActionItem**.
  return:
    type: DevExpress.ExpressApp.Actions.ChoiceActionItem
    description: A [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) with the specified caption path.
seealso:
- linkId: DevExpress.ExpressApp.Actions.SingleChoiceAction.FindItemByIdPath(System.String)
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItem.GetCaptionPath
---
Each item of a Choice Action has a caption path associated with it. This path is represented by a sequence of parent item captions separated by the slash character. Use the `FindItemByCaptionPath` method to access a particular item by specifying the path associated with it. If an item with the specified path is not found, this method returns `null`. To retrieve the caption path of a Choice Action Item, use the [ChoiceActionItem.GetCaptionPath](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.GetCaptionPath) method.

The following snippet illustrates how to disable the **SetTaskAction** Action's "Priority/High" item when the current user is "John".

# [C#](#tab/tabid-csharp)

```csharp
ChoiceActionItem priorityHighItem = SetTaskAction.FindItemByCaptionPath("Priority/High");
if (priorityHighItem != null) 
    priorityHighItem.Enabled.SetItemValue(
        "SecurityAllowance", SecuritySystem.CurrentUserName != "John");
```
***

![FindItemByCaptionPath](~/images/finditembycaptionpath116702.png)

Alternatively, you can use the [SingleChoiceAction.FindItemByIdPath](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.FindItemByIdPath(System.String)) Method, to find a specific item by its ID path.