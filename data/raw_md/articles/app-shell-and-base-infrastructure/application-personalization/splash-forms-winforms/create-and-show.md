---
uid: '400748'
title: 'Create and Show a Splash Form (WinForms)'
---
# Create and Show a Splash Form (WinForms)

This topic describes how to create three [splash forms](xref:112680) (a Splash Screen, a Wait Form, and a Splash Image) and use them in an application.

## Prerequisites

[!include[DesignTime_WinForms_NuGet_Net5](~/templates/DesignTime_WinForms_NuGet_Net5.md)]

## Create and Use a Splash Screen or a Wait Form

To create a [Splash Screen](xref:112680) or a [Wait Form](xref:112680), create a new Windows Form in your [WinForms Application project](xref:118045). Inherit the form from the @DevExpress.XtraSplashForm.SplashFormBase class or **SplashFormBase** descendant and customize the form.

To use the Splash Screen or the Wait Form at the application's startup, open the _WinApplication.cs_ file and pass the form to any @DevExpress.ExpressApp.Win.Utils.DXSplashScreen constructor as the _xtraSplashFormType_ parameter.

# [C#](#tab/tabid-csharp)

```csharp
namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        public MySolutionWindowsFormsApplication() { 
            // ...
            SplashScreen = new DXSplashScreen(typeof(MySplashScreenOrWaitForm));
        }
        // ...
    }
}

```

# [VB.NET](#tab/tabid-vb)

```vb
Namespace MySolution.Win
    Partial Public Class MySolutionWindowsFormsApplication
        Inherits WinApplication
        Public Sub New()
            ' ...
            SplashScreen = New DXSplashScreen(GetType(MySplashScreenOrWaitForm))
            ExecuteStartupLogicBeforeClosingLogonWindow = True
        End Sub
        ' ...
    End Class
End Namespace

```
***

To use the Wait Form with other splash forms, [use a different constructor](xref:400732#enable-specific-splash-forms) and pass the Wait Form as the _waitFormType_ parameter.

You can use forms to [indicate specific operations' progress](xref:400732#show-splash-forms-for-specific-tasks).

## Use a Splash Image

To show a [Splash Image](xref:112680), add an image file to the **Images** folder in the [WinForms Application project](xref:118045) and set the file's Build Action property to Embedded Resource.

The following file types are acceptable:
* SVG,
* PNG,
* other raster formats.

> [!NOTE]
> You can use the [Bitmap.MakeTransparent](https://learn.microsoft.com/en-us/dotnet/api/system.drawing.bitmap.maketransparent#System_Drawing_Bitmap_MakeTransparent) method to enable transparency for BMP images. You can also use an image editing application to convert your BMP file to PNG or another raster format that supports transparency.

To enable the image, access the _WinApplication.cs_ file and assign the image to an Image or SVGImage object. Pass the object to the @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.#ctor(System.Drawing.Image) or @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.#ctor(DevExpress.Utils.Svg.SvgImage) constructor to set the Splash Image as the application's default Splash Screen.

**Raster Image** 

# [C#](#tab/tabid-csharp)

```csharp
using System.IO;
using System.Reflection;
using DevExpress.ExpressApp.Win.Utils;

namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        public MySolutionWindowsFormsApplication() {
            // ...
            Assembly executingAssembly = Assembly.GetExecutingAssembly();
            Stream splashImageStream = executingAssembly.GetManifestResourceStream(
                assembly.GetName().Name + ".Images.MySplashImage.png");
            SplashScreen = new DXSplashScreen(Image.FromStream(splashImageStream));
        }
        // ...
    }
}

```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System.IO
Imports System.Reflection
Imports DevExpress.ExpressApp.Win.Utils

Namespace MySolution.Win
    Partial Public Class MySolutionWindowsFormsApplication
        Inherits WinApplication
        Public Sub New()
            ' ...
            Dim executingAssembly As Assembly = Assembly.GetExecutingAssembly()
            Dim splashImageStream As Stream = executingAssembly.GetManifestResourceStream( _
                assembly.GetName().Name + ".Images.MySplashImage.png")
            SplashScreen = New DXSplashScreen(Image.FromStream(splashImageStream))
        End Sub
        ' ...
    End Class
End Namespace

```
***

**SVG Image**

# [C#](#tab/tabid-csharp)

```csharp
using System.Reflection;
using DevExpress.Utils.Svg;
using DevExpress.ExpressApp.Win.Utils;

namespace MySolution.Win {
    public partial class MySolutionWindowsFormsApplication : WinApplication {
        public MySolutionWindowsFormsApplication() {
            // ...
            Assembly executingAssembly = Assembly.GetExecutingAssembly();
            SplashScreen = new DXSplashScreen(SvgImage.FromResources(
                assembly.GetName().Name + ".Images.SplashImage.svg", assembly));
        }
        // ...
    }
}

```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System.Reflection
Imports DevExpress.Utils.Svg
Imports DevExpress.ExpressApp.Win.Utils

Namespace MySolution.Win
    Partial Public Class MySolutionWindowsFormsApplication
        Inherits WinApplication
        Public Sub New()
            ' ...
            Dim executingAssembly As Assembly = Assembly.GetExecutingAssembly()
            SplashScreen = New DXSplashScreen(SvgImage.FromResources( _
                assembly.GetName().Name + ".Images.SplashImage.svg", assembly))
        End Sub
        ' ...
    End Class
End Namespace

```
***

To use the Splash Image with other splash forms, [use a different constructor](xref:400732#enable-specific-splash-forms).

After you enable the Splash Image, you can show it for [specific operations to indicate their progress](xref:400732#show-splash-forms-for-specific-tasks).
