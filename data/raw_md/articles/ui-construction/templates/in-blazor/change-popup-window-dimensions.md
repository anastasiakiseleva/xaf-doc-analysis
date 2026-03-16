---
uid: "404014"
title: 'How to: Adjust the Size and Style of Pop-up Dialogs (Blazor)'
owner: Alexey Kazakov
---
# How to: Adjust the Size and Style of Pop-up Dialogs (Blazor)

This article explains how to resize a pop-up window in an XAF Blazor application.

## Change Dimensions for All Popups Within the Application

You can specify custom dimensions for all pop-up windows displayed within your XAF Blazor application. 

### On the Blazor Application Level

Add the following code to the _[SolutionName].Blazor.Server/BlazorApplication.cs_ file when you customize this behavior for a specific app and do not want to reuse these customizations in other apps.

# [C#](#tab/tabid-csharp1)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor;
using DevExpress.ExpressApp.Blazor.Templates;

namespace MySolution.Blazor.Server {
    public partial class MySolutionBlazorApplication : BlazorApplication {
        public MySolutionBlazorApplication() {
            CustomizeTemplate += MySolutionBlazorApplication_CustomizeTemplate;
        }
        private void MySolutionBlazorApplication_CustomizeTemplate(object sender, CustomizeTemplateEventArgs e) {
            if(e.Template is IPopupWindowTemplateSize size) {
                size.MaxWidth = "100vw";
                size.Width = "800px";
                size.MaxHeight = "100vh";
                size.Height = "600px";
            }
        }
    }
}
```
***

### On the Blazor Module Level

Use this approach to create a reusable Blazor module that affects the appearance of the application where it is used.

Add the following code to the _[CustomModuleName].Blazor.Server/BlazorModule.cs_ file:

# [C#](#tab/tabid-csharp1)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Templates;

namespace MyCustomModule.Module.Blazor {
    public sealed partial class MySolutionBlazorModule : ModuleBase {
        public override void Setup(XafApplication application) {
            base.Setup(application);
            application.CustomizeTemplate += Application_CustomizeTemplate;
        }
        private void Application_CustomizeTemplate(object sender, CustomizeTemplateEventArgs e) {
            if(e.Template is IPopupWindowTemplateSize size) {
                size.MaxWidth = "100vw";
                size.Width = "800px";
                size.MaxHeight = "100vh";
                size.Height = "600px";
            }
        }
    }
}
```
***

## Change Dimensions for an Individual Popup Window

### In a WindowController

To change the dimensions of an individual popup, add a new window controller to the _[SolutionName].Blazor.Server/Controllers_ folder with the following code:

# [C#](#tab/tabid-csharp1)
 
```csharp{15-16}
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Templates;

namespace MySolution.Blazor.Server.Controllers {
    public class CustomizePopupSizeController : WindowController {
        protected override void OnActivated() {
            base.OnActivated();

            Window.TemplateChanged += Window_TemplateChanged;
        }
        private void Window_TemplateChanged(object sender, EventArgs e) {
            // Change the dimensions only for the View  
            // with Id set to "PermissionPolicyRole_DetailView".
            if (Window.Template is IPopupWindowTemplateSize size 
                && Window.View.Id == "PermissionPolicyRole_DetailView") {
                size.MaxWidth = "100vw";
                size.Width = "1800px";
                size.MaxHeight = "100vh";
                size.Height = "1600px";
            }
        }
        protected override void OnDeactivated() {
            Window.TemplateChanged -= Window_TemplateChanged;
            base.OnDeactivated();
        }
    }
}
```
***


### In the PopupWindowShowAction

If you [invoke a pop-up window using a custom Action](xref:402158), you can customize the pop-up window dimensions as follows:

# [C#](#tab/tabid-csharp1)
 
```csharp
using System.Drawing;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;

namespace MySolution.Module.Blazor.Controllers {
    public class PopupWindowShowAction_CustomSizeController : ViewController {
        public PopupWindowShowAction_CustomSizeController() {
            PopupWindowShowAction showCustomSizePopup = new PopupWindowShowAction(this, "ShowCustomSizePopup", PredefinedCategory.RecordEdit);
            showCustomSizePopup.Caption = "ShowCustomSizePopup";
            showCustomSizePopup.CustomizePopupWindowParams += ShowCustomSizePopup_CustomizePopupWindowParams;
        }
        private void ShowCustomSizePopup_CustomizePopupWindowParams(object sender, CustomizePopupWindowParamsEventArgs e) {
            IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(SampleObject));
            SampleObject obj = objectSpace.CreateObject<SampleObject>();
            e.View = Application.CreateDetailView(objectSpace, obj);
            
            e.Maximized = true;
            // OR
            // e.Size = new Size(800, 600);
        }
    }
} 
```
***
