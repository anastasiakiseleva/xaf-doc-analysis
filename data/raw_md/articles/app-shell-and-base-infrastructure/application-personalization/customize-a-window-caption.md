---
uid: "113252"
seealso:
- linkId: "112608"
- linkId: "112621"
- linkId: DevExpress.ExpressApp.Utils.SplitString
- linkId: DevExpress.ExpressApp.SystemModule.WindowTemplateController
- linkId: DevExpress.ExpressApp.WindowController.TargetWindowType
- linkId: DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowCaption
- linkId: "113253"
title: 'Customize a Window Caption'
owner: Vera Ulitina
---
# Customize a Window Caption

A caption of a typical Windows Forms XAF application [Window](xref:112608) consists of two parts separated by a dash sign. In the main Window, the first part is the active object caption, and the second part is the application's [Title](xref:DevExpress.ExpressApp.XafApplication.Title). In a [Detail View](xref:112611) window, the first part of a caption is the Detail View node's `ObjectCaptionFormat` property value, and the second part is the current class caption.

![HowToCustomizeCaptionDefault](~/images/howtocustomizecaptiondefault116552.png)

Default captions can be changed. This topic describes how to customize captions.

> [!Note]
> ASP.NET Core Blazor applications only support customization of the window caption text.

## Set a Custom Text as a Caption
The [](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController) is activated in all Windows, and updates a current Window status and caption. The `WindowTemplateController` exposes the [WindowTemplateController.CustomizeWindowCaption](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowCaption) event. This event occurs before a Window caption is updated, and allows you to change that caption. A Window caption is represented by the [](xref:DevExpress.ExpressApp.Utils.SplitString) class in XAF.

To modify a Window caption, create a custom [Window Controller](xref:112621), subscribe to the `CustomizeWindowCaption` event and handle it. Assign a custom value to the `WindowCaption.Text` property in the `CustomizeWindowCaption` event handler. To activate the custom Window Controller in the main Window only, set the `TargetWindowType` to `Main` in the Controller constructor. Refer to the [WindowController.TargetWindowType](xref:DevExpress.ExpressApp.WindowController.TargetWindowType) and [Window.IsMain](xref:DevExpress.ExpressApp.Window.IsMain) topics for details.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
// ...
public class CustomizeWindowController : WindowController {
    public CustomizeWindowController() {
        TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        WindowTemplateController controller = Frame.GetController<WindowTemplateController>();
        controller.CustomizeWindowCaption += Controller_CustomizeWindowCaption;
    }
    private void Controller_CustomizeWindowCaption(object sender, CustomizeWindowCaptionEventArgs e) {
        e.WindowCaption.Text = "My Custom Caption";
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        WindowTemplateController controller = Frame.GetController<WindowTemplateController>();
        controller.CustomizeWindowCaption -= Controller_CustomizeWindowCaption;
    }
}
```
***

The following image illustrates a custom caption in a Windows Forms application.

![HowToCustomizeCaptionCustom1](~/images/howtocustomizecaptioncustom1116553.png)

## Modify a Part of a Caption
To change the second part of a caption, modify the `WindowCaption.SecondPart` property in the `CustomizeWindowCaption` event handler.

# [C#](#tab/tabid-csharp)

```csharp
private void Controller_CustomizeWindowCaption(object sender, CustomizeWindowCaptionEventArgs e) {
    e.WindowCaption.SecondPart += " (Powered by XAF)";
}
```
***

The following images illustrate a customized caption with the second part modified.

![HowToCustomizeCaptionCustom2](~/images/howtocustomizecaptioncustom2116554.png)

## Modify a Caption Separator

To change a caption separator, assign a custom value to the `WindowCaption.Separator` property in the `CustomizeWindowCaption` event handler.

# [C#](#tab/tabid-csharp)

```csharp
private void Controller_CustomizeWindowCaption(object sender, CustomizeWindowCaptionEventArgs e) {
    e.WindowCaption.Separator = ": ";
}
```
***

The following images illustrate a caption with a customized separator.

![HowToCustomizeCaptionCustom3](~/images/howtocustomizecaptioncustom3116555.png)

## Swap Parts of a Caption
To change the order of caption parts, swap the values of `WindowCaption.FirstPart` and `WindowCaption.SecondPart` properties in the `CustomizeWindowCaption` event handler.

# [C#](#tab/tabid-csharp)

```csharp
private void Controller_CustomizeWindowCaption(object sender, CustomizeWindowCaptionEventArgs e) {
    string TmpString = e.WindowCaption.FirstPart;
    e.WindowCaption.FirstPart = e.WindowCaption.SecondPart;
    e.WindowCaption.SecondPart = TmpString;
}
```
***

The following images illustrate a customized caption with the left and right parts swapped.

![HowToCustomizeCaptionCustom4](~/images/howtocustomizecaptioncustom4116556.png)

## Display Only One Part of a Caption

To display only the second part of a caption, set the `WindowCaption.FirstPart` to`null`.

# [C#](#tab/tabid-csharp)

```csharp
private void Controller_CustomizeWindowCaption(object sender, CustomizeWindowCaptionEventArgs e) {
    e.WindowCaption.FirstPart = null;
}
```
***

> [!NOTE]
> You do not have to set the **`WindowCaption.Separator`** property to `null` to disable the separator display when one of the caption parts is an empty string or `null`. The separator will be omitted automatically. For more information, refer to the following topic: [](xref:DevExpress.ExpressApp.Utils.SplitString).

The following images illustrate a customized caption.

![HowToCustomizeCaptionCustom5](~/images/howtocustomizecaptioncustom5116557.png)

You can use the [WindowTemplateController.UpdateWindowCaption](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.UpdateWindowCaption*) method to refresh a window caption.