---
uid: DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedIndex
name: SelectedIndex
type: Property
summary: Specifies the index of the selected item in a Single Choice Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) list.
syntax:
  content: |-
    [Browsable(false)]
    public int SelectedIndex { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value representing an index of the Single Choice Action's currently selected item.
seealso: []
---
Use this property to specify the index of Single Choice Action's item which is displayed as a selected item in a UI. Manual changing of this property value raises the [SingleChoiceAction.SelectedItemChanged](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItemChanged) event. However, when an end-user changes this value by selecting an item in the Action's control, the [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event is raised.

If none of the Single Choice Action's items is selected, this property returns -1.