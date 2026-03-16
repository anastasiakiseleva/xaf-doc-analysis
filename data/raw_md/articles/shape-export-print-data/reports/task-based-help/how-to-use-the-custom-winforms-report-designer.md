---
uid: "113605"
seealso: []
title: 'How to: Use the Custom WinForms Report Designer'
owner: Ekaterina Kiseleva
---
# How to: Use the Custom WinForms Report Designer

This example demonstrates how to use the custom **Report Designer** form by handling the [WinReportServiceController.CreateCustomDesignForm](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.CreateCustomDesignForm) event.

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

Create a [View Controller](xref:112621) in the [WinForms application project](xref:118045) (_MySolution.Win_).
Override the Controller's `OnActivated` method, access the [](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController) using the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method and subscribe to the [WinReportServiceController.CreateCustomDesignForm](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.CreateCustomDesignForm) event.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2.Win;
using DevExpress.XtraReports.UserDesigner;
// ...
public class CustomDesignerController : ViewController {
    private WinReportServiceController winReportServiceController;
    protected override void OnActivated() {
        base.OnActivated();
        winReportServiceController = Frame.GetController<WinReportServiceController>();
        if (winReportServiceController != null) {
            winReportServiceController.CreateCustomDesignForm +=
                delegate(object sender, CreateCustomDesignFormEventArgs e) {
                    e.DesignForm = new XRDesignRibbonForm();
                };
        }
    }
}
```
***

In the code above, the built-in [](xref:DevExpress.XtraReports.UserDesigner.XRDesignRibbonForm) is used instead of the default [](xref:DevExpress.XtraReports.UserDesigner.XRDesignForm). You can create a custom form from scratch based on the [Creating a Custom End-User Report Designer](xref:116704) document and use it instead.