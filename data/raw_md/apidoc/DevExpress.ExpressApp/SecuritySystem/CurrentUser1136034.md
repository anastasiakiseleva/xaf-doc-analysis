---
uid: DevExpress.ExpressApp.SecuritySystem.CurrentUser
name: CurrentUser
type: Property
summary: Gets the user who is currently logged on.
syntax:
  content: public static object CurrentUser { get; }
  parameters: []
  return:
    type: System.Object
    description: An object that is the user who is currently logged on.
seealso:
- linkId: "113152"
---
The example below demonstrates how to invoke the current user's [Detail View](xref:112611#detail-view) via a @DevExpress.ExpressApp.Actions.PopupWindowShowAction.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
// ...
public class ShowCurrentUserController : WindowController {
    public ShowCurrentUserController() {
        PopupWindowShowAction showCurrentUserAction = new PopupWindowShowAction(
        this, "ShowCurrentUser", PredefinedCategory.Edit);
        showCurrentUserAction.CustomizePopupWindowParams += ShowCurrentUserAction_CustomizePopupWindowParams;
    }
    private void ShowCurrentUserAction_CustomizePopupWindowParams(
        object sender, CustomizePopupWindowParamsEventArgs e) {
        IObjectSpace newObjectSpace = Application.CreateObjectSpace(SecuritySystem.CurrentUser.GetType());
        object currentUser = newObjectSpace.GetObject(SecuritySystem.CurrentUser);
        e.View = Application.CreateDetailView(newObjectSpace, currentUser);
    }
}

```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base

Public Class ShowCurrentUserController
    Inherits WindowController
    Public Sub New()
        Dim showCurrentUserAction As New PopupWindowShowAction(Me, "ShowCurrentUser", PredefinedCategory.Edit)
        AddHandler showCurrentUserAction.CustomizePopupWindowParams, _
            AddressOf ShowCurrentUserAction_CustomizePopupWindowParams
    End Sub
    Private Sub ShowCurrentUserAction_CustomizePopupWindowParams(ByVal sender As Object, _
        ByVal e As CustomizePopupWindowParamsEventArgs)
        Dim newObjectSpace As IObjectSpace = Application.CreateObjectSpace(SecuritySystem.CurrentUser.GetType())
        Dim currentUser As Object = newObjectSpace.GetObject(SecuritySystem.CurrentUser)
        e.View = Application.CreateDetailView(newObjectSpace, currentUser)
    End Sub
End Class
```
***