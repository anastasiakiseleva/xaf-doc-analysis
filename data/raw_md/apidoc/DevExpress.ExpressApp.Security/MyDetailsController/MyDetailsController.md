---
uid: DevExpress.ExpressApp.Security.MyDetailsController
name: MyDetailsController
type: Class
summary: A [](xref:DevExpress.ExpressApp.WindowController) descendant that adds the **My Details** item to the [Navigation System](xref:113198), and contains the **MyDetails** Action.
syntax:
  content: 'public class MyDetailsController : WindowController'
seealso:
- linkId: DevExpress.ExpressApp.Security.MyDetailsController._members
  altText: MyDetailsController Members
- linkId: "113366"
---
The `MyDetailsController` [Controller](xref:112621) ships with the [SecuritySystem](xref:113366) module. XAF activates it for the main [Window](xref:112608) (see [Window.IsMain](xref:DevExpress.ExpressApp.Window.IsMain)) and generates the **My Details** navigation item.

<!--TODO: update image for WinForms -->

![MyDetailsNavigationItemWinWeb](~/images/mydetailsnavigationitemwinweb116625.png)

XAF adds this item to the same navigation group as the `User` object (see [IModelClassNavigation.NavigationGroupName](xref:DevExpress.ExpressApp.SystemModule.IModelClassNavigation.NavigationGroupName)) and displays it through the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController) Controller. When an end-user clicks this item in the navigation control, XAF displays a default Detail View (see [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView)) with the current `User`'s details.

The `MyDetailsController` class exposes the `CanGenerateMyDetailsNavigationItem` static field that indicates whether to generate the **My Details** navigation item. Its value is `true` by default. To prohibit generating the **My Details** navigation item, set `CanGenerateMyDetailsNavigationItem` to `false`:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
// ...
MyDetailsController.CanGenerateMyDetailsNavigationItem = false;
```
***

In a Windows Forms application project, add this code to the **Main** method located in _Program.cs_ file, before invoking the [WinApplication.Start](xref:DevExpress.ExpressApp.Win.WinApplication.Start) method.

In the legacy Security System, users can modify themselves, even if the **Write** access to the `User` object is denied, by default. Additionally, users can use the **MyDetails** Navigation Item when they have no **Navigate** access to the `User` object. To change this behavior, you can set the `ObjectAccessComparer.AllowModifyCurrentUserObject` and `ObjectAccessComparer.AllowNavigateToCurrentUserObject` properties to `false` in the `Main` method of the Windows Forms application. These settings have no effect in the [Security System](xref:113366). The required permissions are granted or omitted explicitly (see [Client-Side Security (2-Tier Architecture)](xref:113436)).

# [C#](#tab/tabid-csharp)

```csharp
ObjectAccessComparer currentComparer =
    (ObjectAccessComparer)ObjectAccessComparerBase.CurrentComparer;
// Prohibit changing the current user's properties in My Details Detail View
// for users who have no "Write" permission to User object:
currentComparer.AllowModifyCurrentUserObject = false;
// Hide the My Details Navigation Item and Action
// for users who have no "Navigate" permission to User object:
currentComparer.AllowNavigateToCurrentUserObject= false;
```
***