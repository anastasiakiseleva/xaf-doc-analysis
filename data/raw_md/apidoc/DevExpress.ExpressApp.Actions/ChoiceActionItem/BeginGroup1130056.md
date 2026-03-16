---
uid: DevExpress.ExpressApp.Actions.ChoiceActionItem.BeginGroup
name: BeginGroup
type: Property
summary: Specifies whether the current Choice Action Item starts a group.
syntax:
  content: |-
    [DefaultValue(false)]
    public bool BeginGroup { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the current Choice Action Item starts a group; otherwise, **false**.'
seealso: []
---
If this property is set to **true**, this Choice Action Item is delimited from the preceding Items by a line. In the following image, the **BeginGroup** property of the  **Department** Item is set to **true**:

![ChoiceActionItem_BeginGroup](~/images/choiceactionitem_begingroup116844.png)
> [!NOTE]
> This property is considered when the [SingleChoiceAction.ItemType](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemType) property is set to the [SingleChoiceActionItemType.ItemIsOperation](xref:DevExpress.ExpressApp.Actions.SingleChoiceActionItemType.ItemIsOperation) value.

When setting a value to this property, the [ChoiceActionBase.ItemsChanged](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ItemsChanged) event is raised.