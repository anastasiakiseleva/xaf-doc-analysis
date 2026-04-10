The Security System marks built-in Actions as non-secure and hides them in the **Denied Actions** tab. The @DevExpress.ExpressApp.Security.SecurityModule.NonSecureActionsInitializing event allows you to customize a list of non-secure Actions. Add custom or remove system Action identifiers from the @DevExpress.ExpressApp.Security.NonSecureActionsInitializingEventArgs.NonSecureActions collection to manage whether these Actions are available in the **Denied Actions** tab. 

You can find an Action's identifier in the Model Editor:

![Action Id in Model Editor](~/images/Action_ID_ModelEditor.png)

To add a @DevExpress.ExpressApp.Actions.ChoiceActionItem to the `NonSecureActions` collection, use its complex identifier that includes dot-separated identifiers of all parent items. For example, the `choiceActionItem` from the following Controller has the "_MySingleChoiceActionId.MyChoiceActionItemId_" complex identifier.

# [C#](#tab/tabid-csharpChoiceActionItem)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
// ...
public class MyController : ViewController {
    // ...
    public MyController() {
        // ...
        SingleChoiceAction MySingleChoiceAction = new SingleChoiceAction(this, "MySingleChoiceActionId", null);
        ChoiceActionItem MyChoiceActionItem = new ChoiceActionItem("MyChoiceActionItemId", null)
        MySingleChoiceAction.Items.Add(MyChoiceActionItem);
    }
}
```
***
The following code snippet adds and remove Action identifiers from the @DevExpress.ExpressApp.Security.NonSecureActionsInitializingEventArgs.NonSecureActions collection.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Win;
// ...
public partial class MySolutionWin : WinApplication {
    public MySolutionWin() {
        // ...
        securityModule1.NonSecureActionsInitializing += securityModule1_NonSecureActionsInitializing;
    }
    // ...
    private void securityModule1_NonSecureActionsInitializing(object sender, 
    NonSecureActionsInitializingEventArgs e) {
        // SimpleAction, PopupWindowShowAction, or ParametrizedAction 
        e.NonSecureActions.Add("Demo About Info");
        e.NonSecureActions.Remove("Export");
        // ChoiceActionItem
        e.NonSecureActions.Add("SetTaskAction.Priority"); 
    }
}
```
***
