---
uid: "115213"
seealso: []
title: 'How to: Access the Bar Manager'
owner: Ekaterina Kiseleva
---
# How to: Access the Bar Manager

WinForms applications use the [Bar Manager](xref:5361) to show an application's menu when the [ribbon interface](xref:404212) is disabled (see [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle)), and to display a nested Frame's toolbar. This topic describes how to access the Bar Manager. Refer to the [How to: Customize Action Controls](xref:113183) topic to learn how to customize [bar items](xref:2511).

Follow the steps below to access the [](xref:DevExpress.XtraBars.BarManager) object and customize its settings:

1. Create a new [](xref:DevExpress.ExpressApp.Controller) in the WinForms module's _Controllers_ folder. This Controller customizes Bar Managers in all [Frames](xref:112608), including nested Frames (see [](xref:DevExpress.ExpressApp.NestedFrame)).
2. Override the Controller's **OnActivated** method and subscribe to the [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) event.
3. In the **TemplateChanged** event handler, ensure that the [Frame.Template](xref:DevExpress.ExpressApp.Frame.Template)'s type is **IBarManagerHolder**. Cast the Template to the **IBarManagerHolder** type and use the **IBarManagerHolder.BarManager** property to access the **BarManager** object. For instance, you can set the [BarManager.AllowCustomization](xref:DevExpress.XtraBars.BarManager.AllowCustomization) property to **false** to prohibit end-users from customizing a bar.
4. Override the Controller's **OnDeactivated** method and unsubscribe from the **TemplateChanged** event when the Controller is deactivated.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Controls;
using DevExpress.XtraBars;
// ...
public class BarManagerCustomizationWindowController : Controller {
    protected override void OnActivated() {
        base.OnActivated();
        Frame.TemplateChanged += Frame_TemplateChanged;
    }
    private void Frame_TemplateChanged(object sender, EventArgs e) {
        if (Frame.Template is IBarManagerHolder) {
            BarManager manager = ((IBarManagerHolder)Frame.Template).BarManager;
            manager.AllowCustomization = false;
        }
    }
    protected override void OnDeactivated() {
        Frame.TemplateChanged -= Frame_TemplateChanged;
        base.OnDeactivated();
    }
}
```
***

Run the application to ensure that bar customization is not allowed.

![BarManager_AllowCustomization](~/images/barmanager_allowcustomization132212.png)
