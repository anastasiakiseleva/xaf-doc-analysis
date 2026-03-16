---
uid: DevExpress.ExpressApp.ModuleBase.GetStartupActions
name: GetStartupActions()
type: Method
summary: Returns a list of Pop-up Window Show Actions that must be executed before loading the application's main Window.
syntax:
  content: public virtual IList<PopupWindowShowAction> GetStartupActions()
  return:
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.Actions.PopupWindowShowAction}
    description: An IList\<[](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction)> object that represents a collection of Actions to be executed before invoking the application's main Window.
seealso: []
---
Override this method to return a custom list of Pop-up Window Show Actions to be executed when the application is starting up. In the following example, an Action that shows the **BusinessObject1** List View is added.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Actions;
// ...
public override IList<PopupWindowShowAction> GetStartupActions() {
    List<PopupWindowShowAction> actions = new List<PopupWindowShowAction>(base.GetStartupActions());
    IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(BusinessObject1));
    PopupWindowShowAction startupAction = new PopupWindowShowAction();
    startupAction.CustomizePopupWindowParams += 
        delegate(Object sender, CustomizePopupWindowParamsEventArgs e) {
        e.View = Application.CreateListView(objectSpace, typeof(BusinessObject1), true);
    };
    actions.Add(startupAction);
    return actions;
}
```
***

If your XAF WinForms application uses the [Security System](xref:113366) and requires users to log in, the [Overlay Form](xref:120029) covers the [Logon Form](xref:113151) after the user clicks the **Log In** button and until the Main Window loads. If any startup Actions are available, the Actions show forms while the Logon Form and the Overlay Form are displayed.

You can close the Logon Form after the user clicks **Log In** and then perform startup Actions. To do this, access the [WinForms Application project](xref:118045)'s _WinApplication.cs_ (_WinApplication.vb_) file and set the **ExecuteStartupLogicBeforeClosingLogonWindow** property to **false**:

# [C#](#tab/tabid-csharp)

```csharp
namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        public MySolutionWindowsFormsApplication() {
            // ...
            ExecuteStartupLogicBeforeClosingLogonWindow = false;
        }
        // ...
    }
}
```
***

To disable the Overlay Form, you can [deactivate all built-in splash forms](xref:400732#disable-all-built-in-splash-forms) or use a [constructor that does not enable the Overlay Form](xref:400732#enable-specific-splash-forms).