---
uid: DevExpress.ExpressApp.SystemModule.DialogController.SaveOnAccept
name: SaveOnAccept
type: Property
summary: Specifies whether to save changes made to the object represented by the current pop-up Window's Detail View when executing the [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction).
syntax:
  content: public bool SaveOnAccept { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if the object represented by the current pop-up Window's Detail View is saved when executing the [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction); otherwise, **false**."
seealso: []
---
When the pop-up Window for which the current Dialog Controller is activated contains a Detail View, the Accept button allows you to save the changes made to the current object before closing the Window. To change this behavior, set the **SaveOnAccept** property to **false**. In this instance, the Accept button only closes the Window.

By default, the **SaveOnAccept** property is set to **true**.