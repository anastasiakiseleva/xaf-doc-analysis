---
uid: DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItem
name: SelectedItem
type: Property
summary: Specifies a Single Choice Action's selected item.
syntax:
  content: |-
    [Browsable(false)]
    public ChoiceActionItem SelectedItem { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.ChoiceActionItem
    description: A [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) object that represents the Single Choice Action's item which is currently selected.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionBase.Items
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItem.Items
---
Use this property to specify the Single Choice Action's item which is displayed as a selected item in a UI. Manual changing of this property value raises the [SingleChoiceAction.SelectedItemChanged](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItemChanged) event. However, when an end-user changes this value by selecting an item in the Action's control, the [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event is raised.

You may need to use this property and the corresponding event when implementing a custom [Action Container](xref:112610).