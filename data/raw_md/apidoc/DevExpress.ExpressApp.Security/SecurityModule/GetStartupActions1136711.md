---
uid: DevExpress.ExpressApp.Security.SecurityModule.GetStartupActions
name: GetStartupActions()
type: Method
summary: Returns a list of Pop-up Window Show Actions that must be executed before loading the application's main Window.
syntax:
  content: public override IList<PopupWindowShowAction> GetStartupActions()
  return:
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.Actions.PopupWindowShowAction}
    description: An **IList\<**[](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction)**>** list  that must be executed before loading the application's main Window.
seealso: []
---
This method returns the **ChangePasswordOnLogon** Action.