---
uid: "112696"
seealso:
- linkId: "112618"
- linkId: "113706"
- linkId: "114495"
- linkId: "113047"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-custom-template-blazor
  altText: XAF - How to create a custom template (ASP.NET Core Blazor)
title: Template Customization
owner: Ekaterina Kiseleva
---
# Template Customization

XAF provides built-in [](xref:112609) that generate UIs suitable for most business applications. You can also modify these templates to suit your needs.

## WinForms Templates

A template is created using the [XafApplication.CreateTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateTemplate(System.String)) method. This method is invoked by a @DevExpress.ExpressApp.Window or @DevExpress.ExpressApp.Frame object. The template type is determined using the caller object's `Context` property, initialized in the constructor. The following table lists available contexts and corresponding Template types:

{|
|-

! Context
! Templates
|-

| [TemplateContext.ApplicationWindow](xref:DevExpress.ExpressApp.TemplateContext.ApplicationWindow)
| **LightStyleMainForm**

**LightStyleMainRibbonForm**

**OutlookStyleMainRibbonForm**

**MainFormV2**

**MainRibbonFormV2**
|-

| [TemplateContext.View](xref:DevExpress.ExpressApp.TemplateContext.View)
| **DetailFormV2**

**DetailRibbonFormV2**
|-

| [TemplateContext.PopupWindow](xref:DevExpress.ExpressApp.TemplateContext.PopupWindow)
| **PopupForm**
|-

| [TemplateContext.LookupControl](xref:DevExpress.ExpressApp.TemplateContext.LookupControl)
| **LookupControlTemplate**
|-

| [TemplateContext.LookupWindow](xref:DevExpress.ExpressApp.TemplateContext.LookupWindow)
| **LookupForm**
|-

| [TemplateContext.NestedFrame](xref:DevExpress.ExpressApp.TemplateContext.NestedFrame)
| **NestedFrameTemplateV2**
|}

The created Template is assigned to the Window's [Window.Template](xref:DevExpress.ExpressApp.Window.Template) property, and then the Window's View (see [Frame.View](xref:DevExpress.ExpressApp.Frame.View)) is assigned to the Template using its [Frame.SetView](xref:DevExpress.ExpressApp.Frame.SetView*) method.

To implement a custom Template, use [module projects](xref:118046). If you need to use a Template that is not implemented in a module project, you must first initialize the [types info subsystem](xref:113224) with information on the Template. To do this, add a `XafTypesInfo.Instance.FindTypeInfo` method call to your `Program.Main` method in the _Program.cs_ file of the WinForms application project, and pass the custom Template type as the method parameter.

You can create a custom Template by inheriting from a control, and implementing the @DevExpress.ExpressApp.Templates.IFrameTemplate or @DevExpress.ExpressApp.Templates.IWindowTemplate interface. To supply Template implementation examples, XAF installation includes code templates for each Template kind. To create a Template for your application using a code template, invoke [Template Kit](xref:405447) and choose the required code template from **XAF WinForms Templates** category. Specify a name for the new Template and press **Add**.

![TemplateGallery_WinForms](~/images/templategalery_winforms123127.png)

You can customize the added Template at either design time or in code. To see an example for ribbon-based templates, refer to the [](xref:112618) topic. For other templates, refer to the [](xref:113706) topic. Note that all built-in Templates shipped with XAF are fully customizable using the Visual Studio designer and you can easily add custom [Action Containers](xref:112610).

[!include[Win_Design_Package_For_NET6+](~/templates/windesignpackagefornet6.md)]

To use your Template instead of the default one, handle the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event, and return an instance of your Template when needed. The following code demonstrates this.

# [C#](#tab/tabid-csharp)

```csharp
static class Program {
    //...
    public static void Main() {
        //...
        MySolutionWindowsFormsApplication application = new MySolutionWindowsFormsApplication();
        application.CreateCustomTemplate += application_CreateCustomTemplate;
        // ...
    }
    static void application_CreateCustomTemplate(object sender, CreateCustomTemplateEventArgs e) {
        if (e.Context == TemplateContext.ApplicationWindow)
            e.Template = new MySolution.Module.Win.MyMainForm();
    }
}
```
***

You can also customize a Template every time it is created in a particular context. For this purpose, handle the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) event in a manner similar to the `CreateCustomTemplate` event (see above).

To customize a Template when it is created for a particular Window (Frame), handle the [Frame.TemplateChanged](xref:DevExpress.ExpressApp.Frame.TemplateChanged) event. This event is raised after a Template is assigned to a Window (Frame).

## ASP.NET Core Blazor Templates

XAF ships with the following [built-in templates for ASP.NET Core Blazor](xref:403450) applications:

* `ApplicationWindowTemplate`
* `ApplicationRibbonWindowTemplate`
* `DetailFormTemplate`
* `DetailRibbonFormTemplate`
* `LogonWindowTemplate`
* `PopupWindowTemplate`
* `NestedFrameTemplate`

You can customize these templates to suit your needs. 

The following code sample accesses the Popup Window template and changes the template's `MaxWidth` property value.

[!include[<MySolution.Blazor.Server\Controllers\PopupResizeController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor;
using DevExpress.ExpressApp.Blazor.Templates;
// ...
public partial class PopupResizeController : WindowController {
    public PopupResizeController() {
        InitializeComponent();
        this.TargetWindowType = WindowType.Main;
    }

    protected override void OnActivated() {
        base.OnActivated();
        // Subscribe to the CustomizeTemplate event
        ((BlazorApplication)Application).CustomizeTemplate += 
            PopupResizeController_CustomizeTemplate;
    }

    private void PopupResizeController_CustomizeTemplate(object sender, CustomizeTemplateEventArgs e) {
        // Change MaxWidth for popup windows
        if(e.Context == TemplateContext.PopupWindow) {
            ((PopupWindowTemplate)e.Template).MaxWidth = "900px";
        }
    }

    protected override void OnDeactivated() {
        // Unsubscribe from the CustomizeTemplate event
        ((BlazorApplication)Application).CustomizeTemplate -=
            PopupResizeController_CustomizeTemplate;
        base.OnDeactivated();
    }
}
```

***

For more information and examples, refer to the following topics: 

* [](xref:403452) 
* [](xref:404014)

## Pop-up Window Template of the PopupWindowShowAction

The [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) displays a pop-up window with a specified View. In a WinForms application, the **PopupForm** or **LookupForm** Template is used, depending on whether a Detail or List View is included. To customize the pop-up window Template, handle the Action's [PopupWindowShowAction.CustomizeTemplate](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizeTemplate) event, which occurs after you assign the Template to a Window.
