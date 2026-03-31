---
uid: "115214"
seealso: []
title: 'How to: Access the Ribbon Control'
---
# How to: Access the Ribbon Control

This topic demonstrates how to access the [Ribbon](xref:2500) control used to show the WinForms application menu when the [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property is set to **Ribbon** (when the [ribbon interface](xref:404212) is enabled). Refer to the [How to: Customize Action Controls](xref:113183) topic to learn how to customize [bar items](xref:2511).

Follow the steps below to access the [](xref:DevExpress.XtraBars.Ribbon.RibbonControl) object and customize its settings:

1. Create a new [](xref:DevExpress.ExpressApp.WindowController) in the WinForms module's _Controllers_ folder.
2. Override the Controller's **OnActivated** method and subscribe to the [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) event.
3. In the **TemplateChanged** event handler, ensure that the [Frame.Template](xref:DevExpress.ExpressApp.Frame.Template)'s type is [](xref:DevExpress.XtraBars.Ribbon.RibbonForm). Use the [RibbonForm.Ribbon](xref:DevExpress.XtraBars.Ribbon.RibbonForm.Ribbon) property to access the **RibbonControl** object. For instance, you can specify the minimum allowed page header's width using the [RibbonControl.PageHeaderMinWidth](xref:DevExpress.XtraBars.Ribbon.RibbonControl.PageHeaderMinWidth) property, and hide the Expand/Collapse button using the [RibbonControl.ShowExpandCollapseButton](xref:DevExpress.XtraBars.Ribbon.RibbonControl.ShowExpandCollapseButton) property.
4. Override the Controller's **OnDeactivated** method and unsubscribe from the **TemplateChanged** event when the Controller is deactivated.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.XtraBars.Ribbon;
using DevExpress.Utils;
// ...
public class RibbonCustomizationWindowController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        Window.TemplateChanged += Window_TemplateChanged;
    }
    private void Window_TemplateChanged(object sender, EventArgs e) {
        RibbonForm ribbonForm = Frame.Template as RibbonForm;
        if (ribbonForm != null && ribbonForm.Ribbon != null) {
            RibbonControl ribbon = ribbonForm.Ribbon;
            ribbon.PageHeaderMinWidth = 100;
            ribbon.ShowExpandCollapseButton = DefaultBoolean.False;
        }
    }
    protected override void OnDeactivated() {
        Window.TemplateChanged -= Window_TemplateChanged;
        base.OnDeactivated();
    }
}
```
***

Run the application to ensure that Ribbon control customizations are applied.
