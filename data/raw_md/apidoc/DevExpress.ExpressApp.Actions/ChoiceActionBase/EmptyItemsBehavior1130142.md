---
uid: DevExpress.ExpressApp.Actions.ChoiceActionBase.EmptyItemsBehavior
name: EmptyItemsBehavior
type: Property
summary: Specifies how to display a Choice Action if its [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection is empty.
syntax:
  content: |-
    [DefaultValue(EmptyItemsBehavior.Deactivate)]
    public EmptyItemsBehavior EmptyItemsBehavior { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.EmptyItemsBehavior
    description: A [](xref:DevExpress.ExpressApp.Actions.EmptyItemsBehavior) enumeration value identifying the Choice Action behavior.
seealso: []
---
The following values are available:

* **None**
    
    The Action's control is displayed with an empty drop-down list.
* **Disable**
    
    The Action is disabled.
* **Deativate**
    
    The Action is deactivated. So, it will not be visible at all.

By default, the **Diactivate** value is set.