---
uid: "112696"
title: Template Customization
seealso: []
---
# Template Customization

XAF built-in [Templates](xref:112609) generate UIs suitable for most business applications. You can modify these default templates or create fully custom templates at design time, or change template settings at runtime.

XAF determines the type of template to display based on @DevExpress.ExpressApp.TemplateContext. The following table lists the built-in XAF templates and their Contexts.  

Template | Blazor Template Class | WinForms Template Class | Template Context
---------|----------|---------|----
 Main Form Template (with a toolbar menu) | [ApplicationWindowTemplate](xref:403450#main-form-template-applicationwindowtemplate) | [LightStyleMainForm](xref:403446#main-form-template-lightstylemainform) |@DevExpress.ExpressApp.TemplateContext.ApplicationWindow
 Main Ribbon Form Template | [ApplicationRibbonWindowTemplate](xref:403450#main-ribbon-form-template-applicationribbonwindowtemplate) | [LightStyleMainRibbonForm](xref:403446#main-ribbon-form-template-lightstylemainribbonform) |@DevExpress.ExpressApp.TemplateContext.ApplicationWindow
 Detail Form Template (with a toolbar menu) | [DetailFormTemplate](xref:403450#detail-form-template-detailformtemplate) | [DetailFormV2](xref:403446#detail-form-template-detailformv2) |@DevExpress.ExpressApp.TemplateContext.View
 Detail Ribbon Form Template | [DetailRibbonFormTemplate](xref:403450#detail-ribbon-form-template-detailribbonformtemplate) | [DetailRibbonFormV2](xref:403446#detail-ribbon-form-template-detailribbonformv2) |@DevExpress.ExpressApp.TemplateContext.View
 Popup Window/Form Template | [PopupWindowTemplate](xref:403450#popup-window-template-popupwindowtemplate) | [PopupForm](xref:403446#popup-form-template-popupform) |@DevExpress.ExpressApp.TemplateContext.PopupWindow
 Nested Frame Template | [NestedFrameTemplate](xref:403450#nested-frame-template-nestedframetemplate) | [NestedFrameTemplateV2](xref:403446#nested-frame-template-nestedframetemplatev2) |@DevExpress.ExpressApp.TemplateContext.NestedFrame
 Lookup Form Template | — | [LookupForm](xref:403446#lookup-form-template-lookupform) |@DevExpress.ExpressApp.TemplateContext.LookupWindow
 Lookup Control Template | — | [LookupControlTemplate](xref:403446#lookup-control-template-lookupcontroltemplate) | @DevExpress.ExpressApp.TemplateContext.LookupControl
 Logon Window Template | [LogonWindowTemplate](xref:403450#logon-window-template-logonwindowtemplate) | [LogonPopupForm](xref:403446#logon-window-template-logonpopupform) |@DevExpress.ExpressApp.TemplateContext.LogonWindow

## Create a Custom Template at Design Time

The DevExpress [Template Kit](xref:405447) allows you to add default XAF Template code to your application, customize it, and use your modified Templates instead of default Templates.

1. Add Template code in your project (_SolutionName.Blazor.Server_ or _SolutionName.Win_) as described in the following help topic: [Template Kit: Create a new item](xref:405447#create-a-new-item).

    ![Template Kit with a list of Templates](~/images/template-kit/template-kit-item-templates.png)

2. Modify the added template according to your needs. 

    For WinForms templates, ensure that the **DevExpress.ExpressApp.Win.Design** NuGet package is added to the **SolutionName.Win** project. This package contains design-time functionality required for Visual Studio designer.

    Alternatively, you can create a custom Template from scratch, inherit it from a control, and implement the @DevExpress.ExpressApp.Templates.IFrameTemplate or @DevExpress.ExpressApp.Templates.IWindowTemplate interface.

3. Handle the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event to make the application to use your Template instead of the default Template. In the event handler, assign your Template class to the @DevExpress.ExpressApp.CreateCustomTemplateEventArgs.Template property.

    # [SolutionName.Blazor.Server\BlazorApplication.cs](#tab/tabid-blazor)

    ```csharp
    public class SolutionNameBlazorApplication : BlazorApplication {
        // ...
        public SolutionNameBlazorApplication() {
            // ...
            CreateCustomTemplate += application_CreateCustomTemplate;
        }
        static void application_CreateCustomTemplate(object sender, CreateCustomTemplateEventArgs e) {
            if (e.Context == TemplateContext.ApplicationWindow)
                e.Template = new SolutionName.Blazor.Server.Templates.CustomBlazorMainFormTemplate();
        }
    }
    ```

    # [SolutionName.Win\Program.cs](#tab/tabid-win)

    ```csharp
    static class Program {
        //...
        public static void Main() {
            //...
            var winApplication = ApplicationBuilder.BuildApplication(connectionString);
            winApplication.CreateCustomTemplate += winApplication_CreateCustomTemplate;
            // ...
        }
        static void winApplication_CreateCustomTemplate(object sender, CreateCustomTemplateEventArgs e) {
            if (e.Context == TemplateContext.ApplicationWindow)
                e.Template = new SolutionName.Win.Templates.CustomWinMainFormTemplate();
        }
    }
    ```

    ***


### Examples
* <xref:403452>
* <xref:112618>
* <xref:113706>

## Customize Template Settings at Runtime

Handle the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) event to customize a Template every time it is created.

The following code sample accesses the Popup Window Template and specifies the template's size limits.

# [SolutionName.Blazor.Server\Controllers\LimitPopupSize.cs](#tab/tabid-blazor)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Templates;

public class LimitPopupSizeController : WindowController {
    public LimitPopupSizeController() {
        TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        Application.CustomizeTemplate += Application_CustomizeTemplate;
    }
    void Application_CustomizeTemplate(object sender, CustomizeTemplateEventArgs e) {
        if ((e.Context == TemplateContext.PopupWindow || e.Context == TemplateContext.LookupWindow)
            && e.Template is PopupWindowTemplate popupWindow) {
            popupWindow.MaxWidth = "900px";
            popupWindow.MaxHeight = "600px";
        }
    }
    protected override void OnDeactivated() {
        Application.CustomizeTemplate -= Application_CustomizeTemplate;
        base.OnDeactivated();
    }
}
```

# [SolutionName.Win\Controllers\LimitPopupSize.cs](#tab/tabid-win)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Templates;

public class LimitPopupSizeController : WindowController {
    public LimitPopupSizeController() {
        TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        Application.CustomizeTemplate += Application_CustomizeTemplate;
    }
    void Application_CustomizeTemplate(object sender, CustomizeTemplateEventArgs e) {
        if (e.Context == TemplateContext.PopupWindow && e.Template is PopupFormBase popupForm) {
            popupForm.MaximumSize = new Size(900, 600);
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        Application.CustomizeTemplate -= Application_CustomizeTemplate;
    }
}
```

***

* To customize a particular Window's (Frame) Template, handle the @DevExpress.ExpressApp.Frame.TemplateChanged event.
* To customize a Template of a pop-up window displayed by @DevExpress.ExpressApp.Actions.PopupWindowShowAction, handle the Action's [PopupWindowShowAction.CustomizeTemplate](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizeTemplate) event.

### Examples

* <xref:404014>
* <xref:404978>
* <xref:405643>
* <xref:115213>
* <xref:113443>
* <xref:115214>
* <xref:117231>