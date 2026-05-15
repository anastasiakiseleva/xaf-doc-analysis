---
uid: DevExpress.ExpressApp.Win.Utils.DXSplashScreen
name: DXSplashScreen
type: Class
summary: Uses the [WinForms Splash Screen Manager](xref:10826) and enables a [Splash Screen](xref:10823), a [Wait Form](xref:10824), a [Splash Image](xref:10825#create-and-show-splash-image-in-code), and an [Overlay Form](xref:120029) in XAF Win applications.
syntax:
  content: 'public class DXSplashScreen : ISplash, ISupportUpdateSplash, ISupportSplashTypes, ISupportOverlayForm'
seealso:
- linkId: DevExpress.ExpressApp.Win.Utils.DXSplashScreen._members
  altText: DXSplashScreen Members
---
The **DXSplashScreen** class uses the [WinForms Splash Screen Manager](xref:10826) to show, update, and close [splash forms](xref:112680). You can use the following forms in XAF applications:
* a [Splash Screen](xref:10823)

  ![splashformsplashscreen](~/images/SplashForm01_SplashScreen.png)
  
* an [Overlay Form](xref:120029)

  ![splashformoverlayform](~/images/SplashForm02_OverlayForm.png)
* a [Wait Form](xref:10824)

  ![splashformwaitform](~/images/SplashForm03_WaitForm.png)
* a [Splash Image](xref:10825#create-and-show-splash-image-in-code)

  ![splashformsplashimage](~/images/SplashForm04_SplashImage.png)

You can pass custom form types, an image, and Overlay From options to a **DXSplashScreen** constructor and assign the initialized **DXSplashScreen** instance to the [WinApplication.SplashScreen](xref:DevExpress.ExpressApp.Win.WinApplication.SplashScreen) property. The [](xref:DevExpress.ExpressApp.Win.WinApplication) object uses **DXSplashScreen** methods to show splashes where required.

For example, you can add the following code to the _WinApplication.cs_ file in the [WinForms Application project](xref:118045) to enable all four splash forms:

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

# [VB.NET](#tab/tabid-vb)

```vb
Namespace MySolution.Win
    Partial Public Class MySolutionWindowsFormsApplication
        Inherits WinApplication
        Public Sub New()
            ' ...
            SplashScreen = SplashScreen = New DXSplashScreen(GetType(SplashScreen1), GetType(WaitForm1), svgImage, _
                New DefaultOverlayFormOptions())
            ExecuteStartupLogicBeforeClosingLogonWindow = True
        End Sub
        ' ...
    End Class
End Namespace

```
***

You can also use [](xref:DevExpress.ExpressApp.Win.WinApplication) methods to show, update and close splash forms. See the [](xref:112680) article for details. 

