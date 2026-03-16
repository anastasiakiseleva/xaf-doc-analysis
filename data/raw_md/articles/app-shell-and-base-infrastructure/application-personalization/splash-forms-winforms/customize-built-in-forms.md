---
uid: '400971'
title: 'Customize Built-In Splash Forms (WinForms)'
owner: Vera Ulitina
---
# Customize Built-In Splash Forms (WinForms)

In XAF, you can customize your application's built-in [splash forms](xref:112680): the [default splash screen](#customize-the-default-splash-screen) and the [default overlay form](#customize-the-default-overlay-form).

You can also use [custom splash forms](xref:400748).

## Prerequisites

[!include[DesignTime_WinForms_NuGet_Net5](~/templates/DesignTime_WinForms_NuGet_Net5.md)]

## Customize the Default Splash Screen

All new XAF applications [display the following default Splash Screen](xref:400732#enable-specific-splash-forms):

![splashformsplashscreen](~/images/SplashForm01_SplashScreen.png)

You can specify a custom **Application Name**, **Subtitle**, **Copyright**, and **Company Name**. Access your solution's [WinForms Application project](xref:118045) and open the _XafSplashScreen.cs_ (_XafSplashScreen.vb_) file in the Visual Studio Designer. Click the required element and change its **Text** property. 

Alternatively, you can open the _XafSplashScreen.cs_ (_XafSplashScreen.vb_) file in code and set these properties in the **XafSplashScreen** constructor:

# [C#](#tab/tabid-csharp)

```csharp
public XafSplashScreen() {
    InitializeComponent();
    this.labelApplicationName.Text = "My Application";
    // ...
}

```
***

You can also [localize a Splash Screen](xref:400836) or [use a custom Splash Screen](xref:400737).

## Customize the Default Overlay Form

When the [Template Kit](xref:405447) [enables a default Overlay Form](xref:400732#enable-specific-splash-forms), it uses a [DXSplashScreen](xref:DevExpress.ExpressApp.Win.Utils.DXSplashScreen) constructor that takes the _overlayFormOptions_ argument (the @DevExpress.ExpressApp.Win.DefaultOverlayFormOptions type).

You can use the @DevExpress.ExpressApp.Win.DefaultOverlayFormOptions.#ctor constructor to initialize the default Overlay Form, or you can apply custom settings and pass them to the @DevExpress.ExpressApp.Win.DefaultOverlayFormOptions.#ctor(DevExpress.XtraSplashScreen.OverlayWindowOptions) constructor.

To modify the default Overlay Form, create a [custom painter instance](xref:120029) from an **OverlayWindowPainterBase** descendant or **OverlayWindowOptions** class.


# [C#](#tab/tabid-csharp)

```csharp
Image waitImage = Image.FromFile("image.bmp");
OverlayWindowOptions options = new OverlayWindowOptions(
    useFadeIn,
    useFadeOut,
    backColor,
    foreColor,
    opacity,
    waitImage);
winApplication.SplashScreen = new DXSplashScreen(typeof(XafSplashScreen), new DefaultOverlayFormOptions(options));

```
***

