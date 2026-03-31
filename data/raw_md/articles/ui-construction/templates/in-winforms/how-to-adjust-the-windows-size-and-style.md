---
uid: "117231"
title: "How to: Adjust Window Size and Style (WinForms)"
seealso:
- linkId: "404014"
---
# How to: Adjust Window Size and Style (WinForms)

In WinForms XAF applications, end-users can drag the size grip in the bottom-right corner to resize windows. You can also customize the initial form size in code. This topic describes how to programmatically resize and customize windows depending on the displayed View. Pop-up dialog windows are used as an example.

![Popup_Win](~/images/popup_win125036.png)

## Set the Default Size and Style of Pop-up Windows
Popup windows can be customized in the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) and [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) events. Create a new [Window Controller](xref:112621) and subscribe to either of these events when the Controller is activated ([Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event) as shown below.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Templates;
//...
public class CustomizeFormSizeController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        Window.TemplateChanged += Window_TemplateChanged;     
    }
    private void Window_TemplateChanged(object sender, EventArgs e) {
        if(Window.Template is System.Windows.Forms.Form && 
Window.Template is ISupportStoreSettings) {
            ((ISupportStoreSettings)Window.Template).SettingsReloaded += 
OnFormReadyForCustomizations;
        }
    }
    private void OnFormReadyForCustomizations(object sender, EventArgs e) {
        if(YourCustomBusinessCondition(Window.View)) {
            ((System.Windows.Forms.Form)sender).Size = 
((IFormSizeProvider)Window.View.CurrentObject).GetFormSize();
        }
    }
    private bool YourCustomBusinessCondition(View view) {
        return view != null && view.CurrentObject is IFormSizeProvider;
    }
    protected override void OnDeactivated() {
        Window.TemplateChanged -= Window_TemplateChanged;
        base.OnDeactivated();
    }
}
```
***

In this code, the target window template is accessed by subscribing to the **TemplateChanged** event from a Controller. Then, handle the [ISupportStoreSettings.SettingsReloaded](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SettingsReloaded) event to make customizations after the default XAF template settings were applied. Also, you can handle the [Form.HandleCreated](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.control.handlecreated) or [Form.Load](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.form.load) event. Place your customization code into the **OnFormReadyForCustomizations** event handler.

As a result, the size of the target pop-up window is determined depending on the parent window size.

## Customize a Pop-up Window Depending on its View
If you want to customize pop-up windows for a particular type, create a [](xref:DevExpress.ExpressApp.ObjectViewController`2) Controller and specify the business object type. To maximize the  **DemoObject** pop-up window, do the following:

* [Create PopupWindowShowAction](xref:402158).
* Handle the [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event.
* Set the [CustomizePopupWindowParamsEventArgs.View](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.View) parameter  to a particular View instance.
* Set the [CustomizePopupWindowParamsEventArgs.Maximized](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.Maximized) property to **true**.

See the example in the [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) class description.

> [!NOTE]
> Certain form [templates](xref:112609) (e.g., **LookupForm**, **PopupForm**, **LookupControlTemplate**) may have particular specifics.
> 
> * Minimum form size may be set by default (the **InitialMinimumSize** property).
> * Size may be calculated dynamically based on the content.
> * The Form may have resizing restrictions (the **IsSizeable** property).
> * The Form size may automatically shrink (the **AutoShrink** property)
> * The Form may expand to occupy the whole space (the **Maximized** property).
