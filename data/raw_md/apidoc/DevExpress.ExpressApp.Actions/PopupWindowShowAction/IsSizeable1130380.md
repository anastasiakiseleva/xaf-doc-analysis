---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowAction.IsSizeable
name: IsSizeable
type: Property
summary: Indicates whether a Pop-up Window Show Action's pop-up Window can be resized by an end-user.
syntax:
  content: |-
    [DefaultValue(true)]
    public bool IsSizeable { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if an end-user can resize the current Pop-up Window Show Action's pop-up Window; otherwise, **false**."
seealso: []
---
This property is processed by built-in [Action Containers](xref:112610) that visualize Pop-up Window Show Actions. You can implement a cusotm Action Container that will not consider this property and will always display a nonsizable pop-up Window.

By default, the **IsSizeable** property is set to **true**.