---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanExecute(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,System.String)
name: CanExecute(IRequestSecurityStrategy, String)
type: Method
summary: Checks whether the current user can execute the specified Action.
syntax:
  content: public static bool CanExecute(this IRequestSecurityStrategy security, string actionId)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.IRequestSecurityStrategy
    description: An object that specifies the application's security strategy.
  - id: actionId
    type: System.String
    description: The Action identifier.
  return:
    type: System.Boolean
    description: '`true`, if the current user can execute the specified Action; otherwise, `false`.'
seealso: []
---
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
// ...
public class CheckActionPermissionController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        SecurityStrategy securityStrategy = Application.GetSecurityStrategy();
        if (!securityStrategy.CanExecute("CustomAction")) {
            // ...  
        }
    }
}
```
***

You can find an Action's identifier in the Model Editor:

![XAF - Action's Identifier in Model Editor, DevExpress](~/images/Action_ID_ModelEditor.png)
