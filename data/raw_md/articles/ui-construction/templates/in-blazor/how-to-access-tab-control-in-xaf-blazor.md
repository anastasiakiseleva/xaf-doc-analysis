---
uid: "404978"
title: How to Access the Tab Control to Customize Tabbed UI Behavior in Code
---
# How to Access the Tab Control to Customize Tabbed UI Behavior in Code

XAF ASP.NET Core Blazor applications use the @DevExpress.Blazor.DxTabs component in Tabbed MDI mode. This topic demonstrates how to access and customize this component.

## Access the DxTabs Component of the Main Form Template

1. In **Solution Explorer**, navigate to the ASP.NET Core Blazor application.
2. Add a Window Controller to the _Controllers_ folder.
3. Override the `OnActivated` method as demonstrated in the following code snippet:

    ```csharp
    using DevExpress.Blazor;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.Templates;

    namespace YourSolutionName.Blazor.Server.Controllers;

    public class TabsCustomizationWindowController : WindowController {
        public TabsCustomizationWindowController() {
            TargetWindowType = WindowType.Main;
        }
        protected override void OnActivated() {
            base.OnActivated();
            Window.TemplateChanged += Window_TemplateChanged;
        }
        private void Window_TemplateChanged(object sender, EventArgs e) {
            if(Window.Template is ITabbedMdiMainFormTemplate template) {
                // Access the Component Model object for the DxTabs component.
                template.TabsModel.RenderMode = TabsRenderMode.AllTabs;
            }
        }
    }
    ```

## Access a Tab Page Component that Contains the Detail Form Template

1. In **Solution Explorer**, navigate to the ASP.NET Core Blazor application.
2. Add a Window Controller to the _Controllers_ folder.
3. Override the `OnActivated` method as demonstrated in the following code snippet:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.Templates;

    namespace YourSolutionName.Blazor.Server.Controllers;
    
    public class TabsCustomizationWindowController : WindowController {
        public TabsCustomizationWindowController() {
            TargetWindowType = WindowType.Child;
        }
        protected override void OnActivated() {
            base.OnActivated();
            Window.TemplateChanged += Window_TemplateChanged;
        }
        private void Window_TemplateChanged(object sender, EventArgs e) {
            if(Window.Template is ITabbedMdiDetailFormTemplate template) {
                // Access the Component Model object for the DxTabPage component.
                template.TabPageModel.CssClass = "custom-tab-page-css-class";
            }
        }
    }
    ```
