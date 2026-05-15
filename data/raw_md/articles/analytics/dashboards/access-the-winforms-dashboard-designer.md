---
uid: "117716"
seealso: []
title: 'Access the WinForms Dashboard Designer'
---
# Access the WinForms Dashboard Designer

This topic describes how to customize the [](xref:DevExpress.DashboardWin.DashboardDesigner) control used to create and modify dashboards in WinForms XAF applications.

![DashboardWinDesigner](~/images/dashboardwindesigner125576.png)

* In a Windows Forms module, add a Controller that is activated in the [](xref:DevExpress.Persistent.Base.IDashboardData) Views only.
* Access the **WinShowDashboardDesignerController** using the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method.
* Access the **DashboardDesignerManager** object using the **WinShowDashboardDesignerController.DashboardDesignerManager** property.
* Handle the **DashboardDesignerManager.DashboardDesignerCreated** event and access the [](xref:DevExpress.DashboardWin.DashboardDesigner) object using the **DashboardDesigner** event argument.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.DashboardWin; 
using DevExpress.ExpressApp; 
using DevExpress.ExpressApp.Dashboards.Win; 
using DevExpress.Persistent.Base; 
// ... 
public class CustomizeDashboardDesigner : ObjectViewController<ObjectView, IDashboardData> { 
    protected override void OnActivated() { 
        base.OnActivated(); 
        WinShowDashboardDesignerController showDashboardDesignerController = 
             Frame.GetController<WinShowDashboardDesignerController>();
        if (showDashboardDesignerController != null) { 
            showDashboardDesignerController.DashboardDesignerManager.DashboardDesignerCreated += 
                DashboardDesignerManager_DashboardDesignerCreated; 
        }
    } 
    private void DashboardDesignerManager_DashboardDesignerCreated(object sender, DashboardDesignerShownEventArgs e) { 
        e.DashboardDesigner.ActionOnClose = DashboardActionOnClose.Save; 
    } 
    protected override void OnDeactivated() { 
        WinShowDashboardDesignerController showDashboardDesignerController = 
            Frame.GetController<WinShowDashboardDesignerController>(); 
        if (showDashboardDesignerController != null) { 
            showDashboardDesignerController.DashboardDesignerManager.DashboardDesignerCreated -= 
                DashboardDesignerManager_DashboardDesignerCreated; 
        }
        base.OnDeactivated(); 
    } 
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.DashboardWin
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Dashboards.Win
Imports DevExpress.Persistent.Base
' ... 
Public Class CustomizeDashboardDesigner
    Inherits ObjectViewController(Of ObjectView, IDashboardData)

    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        Dim showDashboardDesignerController As WinShowDashboardDesignerController = Frame.GetController(Of WinShowDashboardDesignerController)()
        If showDashboardDesignerController IsNot Nothing Then
            AddHandler showDashboardDesignerController.DashboardDesignerManager.DashboardDesignerCreated, AddressOf DashboardDesignerManager_DashboardDesignerCreated
        End If
    End Sub
    Private Sub DashboardDesignerManager_DashboardDesignerCreated(ByVal sender As Object, ByVal e As DashboardDesignerShownEventArgs)
        e.DashboardDesigner.ActionOnClose = DashboardActionOnClose.Save
    End Sub
    Protected Overrides Sub OnDeactivated()
        Dim showDashboardDesignerController As WinShowDashboardDesignerController = Frame.GetController(Of WinShowDashboardDesignerController)()
        If showDashboardDesignerController IsNot Nothing Then
            RemoveHandler showDashboardDesignerController.DashboardDesignerManager.DashboardDesignerCreated, AddressOf DashboardDesignerManager_DashboardDesignerCreated
        End If
        MyBase.OnDeactivated()
    End Sub
End Class
```

***