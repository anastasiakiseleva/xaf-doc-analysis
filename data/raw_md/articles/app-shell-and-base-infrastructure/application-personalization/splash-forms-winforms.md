---
uid: "112680"
seealso: []
title: Loading Panels / Splash Forms (WinForms)
seealso:
  - linkId: '404738'
---
# Loading Panels / Splash Forms (WinForms)

This article provides a general overview of [splash forms](xref:10826). It shows splash forms available in XAF, describes how they are [initialized](#splash-form-initialization), and provides information on how to [customize](#splash-form-customization) them.

Splash forms are forms XAF WinForms applications show automatically at the application's startup and when users log in. You can also show splash forms when the application retrieves or saves data or for other operations that may run long -  to indicate progress.


The following splash forms are available:

| Splash Form Name | Default Use Scenarios | Possible Use Scenarios | Splash Form Appearance |
|---|---|---|---|
| A [Splash Screen](xref:10823) | At the application's startup | To indicate progress when the application retrieves data or when an application exits and saves all related data. | ![splashformsplashscreen](~/images/SplashForm01_SplashScreen.png) |
| An [Overlay Form](xref:120029) | When you log in | To indicate progress and disable the current window while the application accesses data. |  ![splashformoverlayform](~/images/SplashForm02_OverlayForm.png)
| A [Wait Form](xref:10824) | Not shown | At the application's startup or to indicate progress when the application loads data. | ![splashformwaitform](~/images/SplashForm03_WaitForm.png) |
| A [Splash Image](xref:10825#create-and-show-splash-image-in-code) | Not shown | To show an image that indicates progress on an application's startup or when an application works with the database. | ![splashformsplashimage](~/images/SplashForm04_SplashImage.png)

XAF uses a @DevExpress.ExpressApp.Win.Utils.DXSplashScreen instance and the [WinForms Splash Screen Manager](xref:10826) to show, update, and close splash forms.
If you need to access additional methods, use the @DevExpress.XtraSplashScreen.SplashScreenManager component directly.

## Splash Form Initialization

When you create a new XAF WinForms Application, the[Template Kit](xref:405447) sets the [WinApplication.SplashScreen](xref:DevExpress.ExpressApp.Win.WinApplication.SplashScreen) property value to a new @DevExpress.ExpressApp.Win.Utils.DXSplashScreen instance. The [Template Kit](xref:405447) uses the [](xref:DevExpress.ExpressApp.Win.Utils.DXSplashScreen.#ctor(System.Type,DevExpress.ExpressApp.Win.DefaultOverlayFormOptions)) constructor.

You can find this code in the [WinForms Application project](xref:118045)'s _WinApplication.cs_ (_WinApplication.vb_) file.



# [C#](#tab/tabid-csharp)

```csharp
namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        public MySolutionWindowsFormsApplication() {
            //...
            SplashScreen = new DXSplashScreen(typeof(XafSplashScreen), new DefaultOverlayFormOptions());
        }
        // ...
    }
}

```
***
The [Template Kit](xref:405447) sets the `ExecuteStartupLogicBeforeClosingLogonWindow` property to `true` in all new XAF applications. This setting keeps the [Logon Window](xref:113151) and the [Overlay Form](xref:120029) open until the Main Window loads and while all [Startup Actions](xref:DevExpress.ExpressApp.ModuleBase.GetStartupActions) are executed. [!include[default_settings_compatibility_mode_set_to_latest](~/templates/default_settings_compatibility_mode_set_to_latest.md)] 

All new XAF WinForms applications show the default [Splash Screen](xref:10823) and [Overlay Form](xref:120029).

## Splash Form Customization

You can customize your application's splash forms in several ways:

* [Manage splash forms in an application](xref:400732)
* [Customize built-in splash forms](xref:400971)
* [Create and show splash forms](xref:400748)
* [Use a custom class to show splash forms](xref:400737)

You can also [localize splash forms](xref:400836).
