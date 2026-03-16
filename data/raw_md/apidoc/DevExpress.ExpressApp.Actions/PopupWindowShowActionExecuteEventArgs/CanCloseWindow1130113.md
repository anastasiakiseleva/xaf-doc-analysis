---
uid: DevExpress.ExpressApp.Actions.PopupWindowShowActionExecuteEventArgs.CanCloseWindow
name: CanCloseWindow
type: Property
summary: Specifies whether to close a Pop-up Window Show Action's pop-up Window after clicking its accepting button.
syntax:
  content: public bool CanCloseWindow { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the current pop-up Window must be closed; otherwise, **false**.'
seealso: []
---
After all [PopupWindowShowAction.Execute](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute) event handlers have been invoked, the current pop-up Window is closed, if this property is set to **true.**