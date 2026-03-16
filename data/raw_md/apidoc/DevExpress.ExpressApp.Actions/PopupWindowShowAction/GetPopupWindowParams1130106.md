---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowAction.GetPopupWindowParams
name: GetPopupWindowParams()
type: Method
summary: Creates and returns the [](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs) object to be used when generating a Pop-up Window Show Action's pop-up Window.
syntax:
  content: public CustomizePopupWindowParamsEventArgs GetPopupWindowParams()
  return:
    type: DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs
    description: A [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs) object containing data required to generate the current Pop-up Window Show Action's pop-up Window.
seealso: []
---
Generally, you do not need to use this method. It is for internal use only. Instead, handle the [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event.