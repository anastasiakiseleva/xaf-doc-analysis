---
uid: "117716"
seealso: []
title: 'Access the WinForms Dashboard Designer'
owner: Ekaterina Kiseleva
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
***