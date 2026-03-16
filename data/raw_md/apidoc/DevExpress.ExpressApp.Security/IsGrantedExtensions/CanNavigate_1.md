---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanNavigate(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,System.String)
name: CanNavigate(IRequestSecurityStrategy, String)
type: Method
summary: Checks whether the current user can navigate to the specified item.
syntax:
  content: public static bool CanNavigate(this IRequestSecurityStrategy security, string itemPath)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.IRequestSecurityStrategy
    description: An object that specifies the application's security strategy.
  - id: itemPath
    type: System.String
    description: The path to the navigation item.
  return:
    type: System.Boolean
    description: '`true`, if the current user can navigate to the specified item; otherwise, `false`.'
seealso: []
---
You can find a navigation item's path in the Model Editor: 

![XAF - Navigation Item's Path in Model Editor, DevExpress](~/images/NavigationItem_ItemPath.png)

The following example shows how to use this method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
// ...
public class CheckNavigationPermissionController : WindowController {
    public CheckNavigationPermissionController() {
        TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        SecurityStrategy securityStrategy = Application.GetSecurityStrategy();
        if (!securityStrategy.CanNavigate("Application/NavigationItems/Items/Default/Items/Department_ListView")) {
            // ...
        }
    }
}
```
***
