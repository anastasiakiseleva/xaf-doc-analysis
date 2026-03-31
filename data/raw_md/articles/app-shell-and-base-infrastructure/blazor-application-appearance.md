---
uid: "403068"
title: 'ASP.NET Core Blazor Application Appearance'
---
# ASP.NET Core Blazor Application Appearance

You can configure the appearance of an XAF ASP.NET Core Blazor application in several ways. DevExpress Blazor includes built-in classic and fluent themes, and the fluent theme support both light and dark modes. You can also apply external Bootstrap themes or libraries such as Bootswatch. This topic describes options you can use to customize your application.

![XAF ASP.NET Core Blazor Application Built-In Themes, DevExpress](~/images/xaf-blazor-built-in-themes.png)

## DevExpress Themes

The DevExpress Blazor component suite includes a set of built-in DevExpress themes that are also available in XAF applications. When you create an XAF application, the [Template Kit](xref:405447) adds these themes to the application [Theme Switcher](#theme-switcher). The following themes are included by default:

* DevExpress Fluent themes with [predefined](xref:DevExpress.Blazor.ThemeFluentAccentColor) or custom accent colors (light and dark modes are available).
* DevExpress Classic themes (Blazing Berry, Blazing Dark, Purple, and Office White).

![Theme Switcher in an XAF Blazor Application](~/images/xaf-blazor-theme-switcher.png)

The **DevExpress.ExpressApp.Blazor** package ships with _Generic Light_ and _Generic Dark_ themes. The stylesheet for the Generic Dark theme (_dx.dark.css_) is used with the _Blazing Dark_ and _Fluent Dark_ themes. The stylesheet for the Generic Light theme (_dx.light.css_) is applied to all [custom](#external-bootstrap-themes) themes and other XAF themes.

For more information about DevExpress Blazor Themes, refer to the following topic: [](xref:401523).

### Theme Switcher

The [application configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/) file (_MySolution.Blazor.Server\appsettings.json_) includes the `ThemeSwitcher` section that specifies the switcher's settings and available themes. 

> [!spoiler][Display the list of available Theme Switcher options][Hide options]
> **Root level options**
> * `DefaultItemName` specifies the default theme's name.
> * `ShowSizeModeSwitcher` specifies whether the [Size Mode switcher](#size-mode) is visible.
> * `Groups` contains a collection of theme groups. Each group must have a caption and a collection of themes.
> 
> **Fluent group options**
> * `IsFluent` specifies whether the current group contains Fluent theme settings.
> * `ShowCustomColorSelector` specifies whether the custom color selector is visible.
> * `ShowModeSwitcher` specifies whether the Light/Dark selector is visible.
> * `DefaultMode` specifies the default fluent theme mode.
> * `Caption` specifies the group name in the Theme Switcher.
> * `Items` contains a collection of themes in the group.
> * `CustomUrls` contains a collection of [custom stylesheets](#custom-stylesheets) used with the Fluent theme.
> 
> **Fluent item options**
> * `Caption` specifies the theme's name in the Theme Switcher.
> * `Color` specifies the theme's accent color in the hexadecimal format or a @DevExpress.Blazor.ThemeFluentAccentColor enumeration value.
> 
> **Classic group options**
> * `Caption` specifies the group name in the Theme Switcher.
> * `Items` contains a collection of themes in the group.
> 
> **Classic Item options**
> * `Caption` specifies the theme's name in the Theme Switcher.
> * `Color` specifies square icon color for the Theme Switcher.
> * `Url` specifies a link to the theme's CSS file.
> * `CustomUrls` contains a collection of [custom stylesheets](#custom-stylesheets) used with the theme.

# [appsettings.json](#tab/tabid-json)
 
```JSON
"DevExpress": {
  "ExpressApp": {
    "Languages": "en-US;",
    "ShowLanguageSwitcher": false,
    "Security": {
      // ...
    },
    "ThemeSwitcher": {
      "DefaultItemName": "DevExpress Fluent",
      "ShowSizeModeSwitcher": true,
      "Groups": [
        {
          "IsFluent": true,
          "ShowModeSwitcher": false,
          "ShowCustomColorSelector": false,
          "DefaultMode": "Dark",
          "Caption": "DevExpress Fluent",
          "Items": [
            {
              "Caption": "Blue",
              "Color": "Blue"
            },
            {
              "Caption": "Cool Blue",
              "Color": "CoolBlue"
            },
            {
              "Caption": "Desert",
              "Color": "Desert"
            },
            {
              "Caption": "Mint",
              "Color": "Mint"
            },
            {
              "Caption": "Moss",
              "Color": "Moss"
            },
            {
              "Caption": "Orchid",
              "Color": "Orchid"
            },
            {
              "Caption": "Purple",
              "Color": "Purple"
            },
            {
              "Caption": "Rose",
              "Color": "Rose"
            },
            {
              "Caption": "Rust",
              "Color": "Rust"
            },
            {
              "Caption": "Steel",
              "Color": "Steel"
            },
            {
              "Caption": "Storm",
              "Color": "Storm"
            }
          ]
        },
        {
          "Caption": "DevExpress Classic",
          "Items": [
            {
              "Caption": "Blazing Berry",
              "Url": "_content/DevExpress.Blazor.Themes/blazing-berry.bs5.min.css",
              "Color": "#5c2d91"
            },
            {
              "Caption": "Blazing Dark",
              "Url": "_content/DevExpress.Blazor.Themes/blazing-dark.bs5.min.css",
              "Color": "#46444a"
            },
            {
              "Caption": "Office White",
              "Url": "_content/DevExpress.Blazor.Themes/office-white.bs5.min.css",
              "Color": "#fe7109"
            },
            {
              "Caption": "Purple",
              "Url": "_content/DevExpress.Blazor.Themes/purple.bs5.min.css",
              "Color": "#7989ff"
            }
          ]
        }
      ]
    }
  }
}
``` 
***

### Disable the Theme Switcher

The application gear menu displays the Theme Switcher if your project has more than one theme. To hide the Theme Switcher, specify a single application theme in the _appsettings.json_ file.

# [appsettings.json](#tab/tabid-json)
 
```JSON
"DevExpress": {
  "ExpressApp": {
    "ThemeSwitcher": {
      "Groups": [
        {
          "Caption": "DevExpress Themes",
          "Items": [
            {
              "Caption": "Office White",
              "Url": "_content/DevExpress.Blazor.Themes/office-white.bs5.min.css",
              "Color": "#fe7109"
            }
          ]
        }
      ]
    }
  }
} 
```

***

If the `ThemeSwitcher` section does not specify any themes, the application uses the default Fluent Light Blue theme.

## External Bootstrap Themes

You can apply external [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) themes to your XAF ASP.NET Core Blazor application. The following code sample applies the [Sketchy](https://bootswatch.com/sketchy/) theme from the [Bootswatch](https://bootswatch.com/) theme set. For more information about Bootswatch themes, refer to the [Bootswatch documentation](https://bootswatch.com/help/). 

# [appsettings.json](#tab/tabid-json)

```json{14-23}
"DevExpress": {
  "ExpressApp": {
    //...
    "ThemeSwitcher": {
      "DefaultItemName": "DevExpress Fluent",
      "ShowSizeModeSwitcher": true,
      "Groups": [
        {
          "Caption": "DevExpress Themes",
          "Items": [
            // ...
          ]
        },
        {
          "Caption": "Third Party Themes",
          "Items": [
            {
              "Caption": "Sketchy",
              "Url": "https://cdn.jsdelivr.net/npm/bootswatch@5.1.3/dist/sketchy/bootstrap.min.css",
              "Color": "#000"
            }
          ]
        }
      ]
    }
  }
}
```
***

![XAF ASP.NET Core Blazor Application With a Custom Bootstrap Theme, DevExpress](~/images/xaf-blazor-custom-theme.png)

The _bootstrap-external_ stylesheet shipped with **DevExpress.Blazor.Themes** package is added by default. To exclude it, set the `ExcludeBootstrapExternal` to `true`:

# [appsettings.json](#tab/tabid-json)

```json{19}
"DevExpress": {
  "ExpressApp": {
    //...
    "ThemeSwitcher": {
      "DefaultItemName": "DevExpress Fluent",
      "ShowSizeModeSwitcher": true,
      "Groups": [
        {
          "Caption": "DevExpress Themes",
          "Items": [
            // ...
          ]
        },
        {
          "Caption": "Third Party Themes",
          "Items": [
            {
              "Caption": "Custom",
              "ExcludeBootstrapExternal": "true";
              "Url": "css/custom-bootstrap.min.css",
              "Color": "#5c2d91"
            }
          ]
        }
      ]
    }
  }
}
```
***

## Switch Themes in Code

You can use the `IThemeService` interface to obtain the current theme, change a theme, and track theme changes.

The following steps describe how to implement an Action that changes your XAF application's theme to Blazing Dark.

1. Use the [Template Kit](xref:405447#create-a-new-item) to create the new _BlazingDarkController.cs_ Window Controller in the _MySolution.Blazor.Server/Controllers_ folder.

2. Replace automatically generated file content with the following code:

    # [BlazingDarkController.cs](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp.Blazor.Services;
    namespace MySolution.Blazor.Server.Controllers;

    public partial class BlazingDarkController : WindowController {
        public BlazingDarkController() {
            TargetWindowType = WindowType.Main;
            // Create a Simple Action.
            new SimpleAction(this, "EnableBlazingDark", "View", async (s, e) => {
                var themeService = Application.ServiceProvider.GetService<IThemeService>();
                // Obtain the Blazing Dark theme.
                var theme = themeService.GetThemeByCaption("Blazing Dark");
                // Set the current theme to Blazing Dark.
                await themeService.SetCurrentThemeAsync(theme);
            });
        }
    }
    ```
    ***

3. Run the application. Click the **Enable Blazing Dark** Action to change the theme. Navigate to the gear menu: the Blazing Dark theme should be selected.

   ![Switch themes in code in an XAF ASP.NET Core Blazor application, DevExpress](~/images/xaf-blazor-swith-theme-in-code.gif)

## Custom Stylesheets

You can add your own stylesheet to a built-in or custom theme. The following code snippet loads custom stylesheets with the Blazing Berry theme:

# [appsettings.json](#tab/tabid-json)
 
```JSON
// ...
{ 
  "Caption": "Blazing Berry",
  "Url": "_content/DevExpress.Blazor.Themes/blazing-berry.bs5.min.css",
  "Color": "#5c2d91",
  // The collection of stylesheets used with the theme.
  "CustomUrls": [
    // Add a link to the 'dx.light.css' or 'dx.dark.css' stylesheet 
    // to ensure that XAF renders application components consistently
    "_content/DevExpress.ExpressApp.Blazor/dx.light.css",
    "css/custom1.css",
    "css/custom2.css"
  ]
}, 
// ...

```
***

## Size Mode

XAF can display Blazor applications in different size modes. Users can select from **Standard** and **Compact** options in the [Theme Switcher](#theme-switcher). 

![Theme Switcher in an XAF ASP.NET Core Blazor Application](~/images/xaf-blazor-size-mode-compact.png)

### Hide Size Mode Switcher

When you create a new application, the [Template Kit](xref:405447) enables the **Size Mode** switcher in the _MySolution.Blazor.Server\appsettings.json_ file. Set the `ShowSizeModeSwitcher` option to `false` (or remove the option) to hide the switcher.

# [appsettings.json](#tab/tabid-json)

```json
// ...
"ThemeSwitcher": {
  // "ShowSizeModeSwitcher": true,
  // ...
```
***

### Set Size Mode in Code

Use the [GlobalOptions.SizeMode](xref:DevExpress.Blazor.Configuration.GlobalOptions.SizeMode) property to specify the size mode in code. The **Compact** option corresponds to the `Small` property value and the **Standard** option corresponds to the `Medium` value.

## Customize UI Elements Using CSS

This section demonstrates how [CSS classes](https://www.w3schools.com/css/css_intro.asp) can help you customize the appearance of various UI elements in XAF ASP.NET Core Blazor applications. You can use CSS to modify items like Actions or layout groups in a [Detail View](xref:112611).

![|XAF ASP.NET Core Blazor - Customize Layout Elements Using Custom CSS Classes](~/images/xaf_blazor_css_customization_overview.png)

Examples in this topic apply customizations to the **Employee** Detail View from the **MainDemo** demo project. This project is installed as a part of the XAF package. The default project location is _[!include[](~/templates/path-to-main-demo-ef-core.md)]_.

### Common Steps to Apply a CSS Class to a UI Element

1. Set the `CustomCSSClassName` property of an appropriate element ([IModelViewLayoutElementBlazor.CustomCSSClassName](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelViewLayoutElementBlazor.CustomCSSClassName) or [IModelActionBlazor.CustomCSSClassName](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.CustomCSSClassName)) to a new CSS class name in the [Model Editor](xref:112582). 

    ![|XAF ASP.NET Core Blazor - Set the CustomCSSClassName property value in the Model Editor](~/images/xaf_blazor_css_customization_property_editors_model_editor.png)

1. Run the application and use the page Inspector tools to locate the newly created class name on the corresponding Detail View page.

    ![|XAF ASP.NET Core Blazor - The page Inspector tools display the newly created class name](~/images/xaf_blazor_css_customization_inspector_tools.png)

1. Fin the DOM elements you need to customize and review their CSS classes to build a proper selector.

1. Use Developer Tools to adjust CSS rules and edit the element according to your needs.

1. Add these rules with the appropriate selectors to the _MySolution.Blazor.Server\wwwroot\css\site.css_ file.

The following sections describe several popular use cases.

### Change a Group Header Color

This section explains how to change the font and background colors of the **Details** group header in the **Employee** Detail View.

1. Locate the following layout group in the Model Editor: **Employee_DetailView** > **Layout** > **Main** > **SimpleEditors** > **Person**. Set the `CustomCSSClassName` property to `EmployeeInfoGroupStyle`.  

1.  Run the application and use the page Inspector tools to locate the newly created class name on the corresponding Detail View page.
    
1. Inspect the element's markup to implement an appropriate CSS selector. This example customizes items with the `dxbl-text` and `dxbl-group-header` classes.

1. Add the following CSS rules to the _site.css_ file:

    # [site.css](#tab/tabid-css)
    ```CSS
      /* Change a header's font color */
    .EmployeeInfoGroupStyle .dxbl-group .dxbl-group-header .dxbl-text {
          color: white;
      }

      /* Change a header's background color */
    .EmployeeInfoGroupStyle .dxbl-group .dxbl-group-header {
          background-color: purple;
      }
    ```
    ***

1. Save your changes and refresh the **Employee** Detail View page to see the result.

    ![XAF ASP.NET Core Blazor - Customize Group Header's Color](~/images/xaf_blazor_css_customization_group_header.png)

### Customize a Property Editor's Label and Text Box Appearance

This section explains how to customize [Property Editors](xref:113097) displayed in a Detail View. The example below changes settings for the label and edit box of the **First Name** Property Editor. This editor is displayed in the **Employee** Detail View. 


1. Locate the following layout element in the Model Editor: **Employee_DetailView** > **Layout** > **Main** > **SimpleEditors** > **Person** > **Person_inner** > **Person_col1** > **Person_col1a** > **FirstName**. Set the `CustomCSSClassName` property to `EmployeeFirstNameStyle`.

1.  Run the application and use the page Inspector tools to locate the newly created class name on the corresponding Detail View page.

1. Inspect the element's markup to implement an appropriate CSS selector. This example customizes items with the `.dxbl-text` and `.dxbl-text-edit` classes.

1. Add the following CSS rules to the _site.css_ file:

    # [site.css](#tab/tabid-css)
    ```CSS
      /* Change a captions's font */
    .EmployeeFirstNameStyle .dxbl-text {
          font-weight: bold;
      }

      /* Change an editor's text and color settings */
    .EmployeeFirstNameStyle .dxbl-text-edit {
          background-color: purple;
          color: white;
          font-size: 14px;
      }
    ```
    ***

1. Save your changes and refresh the **Employee** Detail View page to see the result.

    ![XAF ASP.NET Core Blazor - Customize Property Editor's Appearance](~/images/xaf_blazor_css_customization_property_editor.png)


### Add Colons to Property Editor Labels

This section explains how to customize [Property Editor](xref:113097) labels. The example below walks you through the steps needed to add a colon (`:`) to all editor labels displayed in the **Employee** Detail View. 

1. Locate the following layout group in the Model Editor: **Employee_DetailView** > **Layout** > **Main**. Set the `CustomCSSClassName` property to `EmployeePropertyEditorCaptionStyle`.

1.  Run the application and use the page Inspector tools to locate the newly created class name on the corresponding Detail View page.

1. Inspect the element's markup to implement an appropriate CSS selector. This example customizes items with the `.label` class.

1. Add the following CSS rules to the _site.css_ file:

    # [site.css](#tab/tabid-css)
    ```CSS
      /* Change a captions's font */
    .EmployeePropertyEditorCaptionStyle label::after {
          content: ":"
      }
    ```
    ***

1. Save your changes and refresh the **Employee** Detail View page to see the result.

    ![XAF ASP.NET Core Blazor - Add colons to Property Editor Captions](~/images/xaf_blazor_css_customization_property_editors_with_colons.png)


### Change Tab Color Settings

This section explains how to customize the appearance settings of active and inactive tabs in a tabbed layout group. The following example changes the background and caption colors of all tabs displayed in the **Employee** Detail View.


1. Locate the following tabbed group in the Model Editor: **Employee_DetailView > Layout > Main > Tabs**. Set the `CustomCSSClassName` property to `EmployeeTabsStyle`.

1.  Run the application and use the page Inspector tools to locate the newly created class name on the corresponding Detail View page.

1. Inspect element markup to implement an appropriate CSS selector. This example customizes items with the `.dxbl-active`, `.dxbl-text`, and `.dxbl-tabs-item` classes.

1. Add the following CSS rules to the _site.css_ file:

    # [site.css](#tab/tabid-css)
    ```CSS
      /* Change an active tab's background and text color */
      .EmployeeTabsStyle .dxbl-tabs .dxbl-scroll-viewer .dxbl-scroll-viewer-content .dxbl-active {
          background-color: purple !important;
      }

      .EmployeeTabsStyle .dxbl-tabs .dxbl-scroll-viewer .dxbl-scroll-viewer-content .dxbl-active .dxbl-text {
          color: white;
      }

      /* Change the background color for all inactive tabs */
      .EmployeeTabsStyle .dxbl-tabs .dxbl-scroll-viewer .dxbl-scroll-viewer-content .dxbl-tabs-item {
          background-color: thistle;
      }
    ```
    ***

1. Save your changes and refresh the **Employee** Detail View page to see the result.

    ![|XAF ASP.NET Core Blazor - Customize a Tabbed Group](~/images/xaf_blazor_css_customization_tabbed_group.png)


### Customize Action Appearance

This section describes two approaches used for [Action](xref:112622) customization.

* Specify the Action's @DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.CustomCSSClassName property in the Model Editor to apply the CSS class to this Action in all the Views where it appears.
* Specify the CSS class name in a [Controller](xref:112621) to apply a CSS rule to the Action in a specified View only.

#### Use the CustomCssClassName Property
  
The following example changes the background and text colors of the **New** Action. This customization applies to all Views that display this action. 


1. Locate the following Action node in the Model Editor: **Main Demo > ActionDesign > Actions > New**. Set the @DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.CustomCSSClassName property to `NewActionStyle`.

1.  Run the application and use the page Inspector tools to locate the newly created class name on the corresponding Detail View page.

1. Inspect the element's markup to implement an appropriate CSS selector. This example customizes items with the `.NewActionStyle` class.

1. Add the following CSS rules to the _site.css_ file:

    # [site.css](#tab/tabid-css)

    ```CSS
    /* Change an Action's background and text color */
    .NewActionStyle {
        background: purple;
        color: white;
    }
    ```
    ***

1. Save your changes and refresh the **Employee** Detail View page to see the result.

    ![|XAF ASP.NET Core Blazor - Customize an Action's appearance using the CustomCSSClassName property](~/images/xaf_blazor_css_customization_action_using_customcssclassname_property.png)


#### Use a Controller

The following example changes the **New** Action's color settings in the **Employee > Details** Detail View only. 

1. Add the following CSS rule to the `site.css` file:

    # [site.css](#tab/tabid-css)
    ```CSS
      /* Change an Action's background and text color */
      .NewActionStyle {
          background: purple;
          color: white;
      }
    ```
    ***

1. Create a new `CustomizeEmployeeDetailViewAction` Controller. The created Controller should be a descendant of the [](xref:DevExpress.ExpressApp.Controller) class. 

1. Handle the @DevExpress.ExpressApp.Actions.ActionBase.CustomizeControl event to apply the `NewActionStyle` CSS class to the **New** Action.

    ```csharp{15,20-23,29-37}
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Actions;
    using DevExpress.ExpressApp.Blazor.Templates.Toolbar.ActionControls;
    using DevExpress.ExpressApp.SystemModule;

    public class CustomizeEmployeeDetailViewAction : Controller {
        const string EmployeeDetailViewId = "Employee_DetailView";
        DxToolbarItemSingleChoiceActionControl? actionControl = null;
        NewObjectViewController? newObjectViewController;

        protected override void OnActivated() {
            base.OnActivated();
            newObjectViewController = Frame.GetController<NewObjectViewController>();
            if(newObjectViewController != null) {
                newObjectViewController.NewObjectAction.CustomizeControl += NewObjectAction_CustomizeControl;
                Frame.ViewChanged += Frame_ViewChanged;
            }
        }

        private void NewObjectAction_CustomizeControl(object? sender, CustomizeControlEventArgs e) {
            actionControl = (DxToolbarItemSingleChoiceActionControl)e.Control;
            CustomizeNewActionControl();
        }

        private void Frame_ViewChanged(object? sender, ViewChangedEventArgs e) {
            CustomizeNewActionControl();
        }

        private void CustomizeNewActionControl() {
            if(actionControl != null) {
                if(Frame.View?.Id == EmployeeDetailViewId) {
                    actionControl.ToolbarItemModel.CssClass += " NewActionStyle";
                } else if(actionControl.ToolbarItemModel.CssClass != null) {
                    actionControl.ToolbarItemModel.CssClass = actionControl.ToolbarItemModel.CssClass.Replace(" NewActionStyle", string.Empty);
                }
            }
        }

        protected override void OnDeactivated() {
            base.OnDeactivated();
            if(newObjectViewController != null) {
                newObjectViewController.NewObjectAction.CustomizeControl -= NewObjectAction_CustomizeControl;
                newObjectViewController = null;
                Frame.ViewChanged -= Frame_ViewChanged;
            }
        }
    }
    ```

1. Save your changes and refresh the **Employee** Detail View page to see the result.

    ![|XAF ASP.NET Core Blazor - Customize an Action's appearance using a Controller](~/images/xaf_blazor_css_customization_action_using_controller.png)

### Enable CSS Isolation for Custom Components

[Blazor CSS isolation](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/css-isolation) allows you to you create styles specific to each component, preventing conflicts with other components or libraries. Refer to the following help topic for examples of using CSS isolation with DevExpress components: <xref:404361>.

XAF projects initially do not include component-specific styles, so the [bundled](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/css-isolation#css-isolation-bundling) stylesheet is not added. To enable isolated styles, uncomment or manually add the wizard-generated stylesheet link in _Pages/Host.cshtml_.

# [Host.cshtml](#tab/tabid-cs)

```cshtml
<!-- Uncomment this link to enable CSS isolation. For more information, refer to the following topic: -->
<!-- https://learn.microsoft.com/en-us/aspnet/core/blazor/components/css-isolation.-->
<link href="_MySolution.Blazor.Server.styles.css" rel="stylesheet">
```
***

> [!NOTE]
> The _MySolution.Blazor.Server.styles.css_ file is generated when at least one component in the **_MySolution.Blazor.Server** project contains a CSS file as described in the Microsoft documentation: [Enable CSS isolation](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/css-isolation#enable-css-isolation). Otherwise, the 404 (Not Found) error occurs.
