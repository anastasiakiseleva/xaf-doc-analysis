---
uid: '400732'
title: 'Manage Splash Forms in an Application (WinForms)'
owner: Vera Ulitina
---
# Manage Splash Forms in an Application (WinForms)

This article describes how to [enable specific splash forms](#enable-specific-splash-forms), [disable built-in splash forms](#disable-all-built-in-splash-forms), or [show splash forms for specific tasks](#show-splash-forms-for-specific-tasks).

## Enable Specific Splash Forms

In all new XAF WinForms applications, the [Template Kit](xref:405447) [initializes a DXSplashScreen instance](xref:112680#splash-form-initialization) that enables a Splash Screen and an Overlay Form.

You can use a different @DevExpress.ExpressApp.Win.Utils.DXSplashScreen constructor to enable a different combination of splash forms.

Access the _WinApplication.cs_ (_WinApplication.vb_) file in the [WinForms Application project](xref:118045) and modify the default code. For example, you can use a default Wait Form, [upload an image](xref:400748#use-a-splash-image), and [create a custom Splash Screen](xref:400748#create-and-use-a-splash-screen-or-a-wait-form). Use the @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.#ctor(System.Type,System.Drawing.Image,System.Type,DevExpress.ExpressApp.Win.DefaultOverlayFormOptions) constructor to enable all four [splash forms](xref:112680).


# [C#](#tab/tabid-csharp)

```csharp
namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        public MySolutionWindowsFormsApplication() {
            // ...
            SplashScreen = new DXSplashScreen(typeof(MyCustomSplashScreen), typeof(WaitForm), mySvgImage, 
                new DefaultOverlayFormOptions());
        }
        // ...
    }
}

```
***

## Disable All Built-In Splash Forms

To disable all [splash forms](xref:112680) in an application, access the the _WinApplication.cs_ (_WinApplication.vb_) file in the [WinForms Application project](xref:118045) and set the @DevExpress.ExpressApp.Win.WinApplication.SplashScreen property to _null_:

# [C#](#tab/tabid-csharp)

```csharp
namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        public MySolutionWindowsFormsApplication() {
            // ...
            SplashScreen = null;
        }
        // ...
    }
}

```
***


## Show Splash Forms for Specific Tasks  

XAF shows splash forms in [default scenarios](xref:112680#splash-form-initialization). You can invoke default forms or [custom forms](xref:400748) to indicate a specific operation's progress, for example when the application performs startup or retrieves data.

Use the following methods to start and close splash forms:

| Method | Description |
|---|---|
|[WinApplication.StartSplash](xref:DevExpress.ExpressApp.Win.WinApplication.StartSplash(DevExpress.ExpressApp.Win.SplashType))| Shows a  [Splash Screen](xref:10823), a [Wait Form](xref:10824), or a [Splash Image](xref:10825#create-and-show-splash-image-in-code).
|[WinApplication.StopSplash](xref:DevExpress.ExpressApp.Win.WinApplication.StopSplash(DevExpress.ExpressApp.Win.SplashType))| Stops a  Splash Screen, a Wait Form, or a Splash Image.
|[WinApplication.StartOverlayForm](xref:DevExpress.ExpressApp.Win.WinApplication.StartOverlayForm(System.Windows.Forms.Control))| Shows an [Overlay Form](xref:120029) over a specified control.
|[WinApplication.StopOverlayForm](xref:DevExpress.ExpressApp.Win.WinApplication.StopOverlayForm(DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle))| Stops an Overlay Form that has a specific handle.|

Call the appropriate **Start** method before an operation if you expect it to run long. The method shows a splash form at runtime while the user waits for the operation to complete.
To close the form after the operation ends, call the appropriate **Stop** method.

For example, you can show a Splash Screen when an [Action](xref:112622) starts an operation: 

# [C#](#tab/tabid-csharp)

```csharp
private void StartLongOperationAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
    ((WinApplication)Application).StartSplash(SplashType.SplashScreen);
    //Perform an operation that runs long.
    ((WinApplication)Application).StopSplash(SplashType.SplashScreen);
} 

```
***

The code below demonstrates how to start and close a Wait Form and a Splash Image:

# [C#](#tab/tabid-csharp)

```csharp
((WinApplication)Application).StartSplash(SplashType.WaitForm);
// ...
((WinApplication)Application).StopSplash(SplashType.WaitForm);
// ...
((WinApplication)Application).StartSplash(SplashType.Image);
// ...
((WinApplication)Application).StopSplash(SplashType.Image);

```
***


To show an Overlay Form, use the Overlay Form handle:

# [C#](#tab/tabid-csharp)

```csharp
IOverlaySplashScreenHandle overlayFormHandle = ((WinApplication)Application).StartOverlayForm(requiredControl);
// ...
((WinApplication)Application).StopOverlayForm(overlayFormHandle);

```
***
