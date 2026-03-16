---
uid: "113604"
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.DesignFormCreated
title: 'How to: Customize the WinForms Report Designer Form'
owner: Ekaterina Kiseleva
---
# How to: Customize the WinForms Report Designer Form

This example demonstrates how to access the **Report Designer** form by handling the [WinReportServiceController.DesignFormCreated](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.DesignFormCreated) event.

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

Create a [View Controller](xref:112621) in the WinForms [WinForms application project](xref:118045).
Override the Controller's `OnActivated` method, access the [](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController) using the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method and subscribe to the [WinReportServiceController.DesignFormCreated](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.DesignFormCreated) event.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing.Design;
using DevExpress.XtraReports.UserDesigner;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2.Win;
// ...
public class CustomDesignerController : ViewController {
    private WinReportServiceController winReportServiceController;
    protected override void OnActivated() {
        base.OnActivated();
        winReportServiceController = Frame.GetController<WinReportServiceController>();
        if (winReportServiceController != null) {
            winReportServiceController.DesignFormCreated += winReportServiceController_DesignFormCreated;
        }
    }
    void winReportServiceController_DesignFormCreated(object sender, DesignFormEventArgs e) {
        e.DesignForm.DesignMdiController.DesignPanelLoaded += DesignMdiController_DesignPanelLoaded;
    }
    void DesignMdiController_DesignPanelLoaded(object sender, DesignerLoadedEventArgs e) {
        IToolboxService ts = (IToolboxService)e.DesignerHost.GetService(typeof(IToolboxService));
        ts.AddToolboxItem(new ToolboxItem(typeof(MyControl)), "New Category");
    }
}
```
***

In this code, a custom component is added to the Report Designer toolbar for demonstration purposes. To learn about other possible customizations, refer to the [Report Designer](xref:10715) topic.