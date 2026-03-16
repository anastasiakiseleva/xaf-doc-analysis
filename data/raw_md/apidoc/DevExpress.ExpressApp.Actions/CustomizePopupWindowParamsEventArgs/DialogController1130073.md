---
uid: DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.DialogController
name: DialogController
type: Property
summary: Specifies a Dialog Controller which is activated for a Pop-up Window Show Action's pop-up Window.
syntax:
  content: public DialogController DialogController { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.SystemModule.DialogController
    description: A **DialogController** object that represents a special [Controller](xref:112621) for the pop-up Window.
seealso: []
---
The default Dialog Controller provides the **Accept** and **Cancel** [Actions](xref:112622) that represent the **OK** and **Cancel** buttons on a pop-up Window. The captions of these buttons are specifies by the [PopupWindowShowAction.AcceptButtonCaption](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.AcceptButtonCaption) and [PopupWindowShowAction.CancelButtonCaption](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CancelButtonCaption) properties. You can implement a custom Dialog Controller and add required Actions to it. For instance, you can inherit from the **DialogController** class. To do this, use the **XafApplication.CreateController\<YourController>** method. To  activate it for a particular Pop-up Window Show Action's pop-up Window, assign it to the **DialogController** property.