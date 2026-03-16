---
uid: DevExpress.ExpressApp.Win.WinApplication.StartSplash(DevExpress.ExpressApp.Win.SplashType)
name: StartSplash(SplashType)
type: Method
summary: Executes the [DXSplashScreen.Start](xref:DevExpress.ExpressApp.Win.Utils.DXSplashScreen.Start(DevExpress.ExpressApp.Win.SplashType)) method
syntax:
  content: public virtual void StartSplash(SplashType splashType)
  parameters:
  - id: splashType
    type: DevExpress.ExpressApp.Win.SplashType
    description: A splash form type to be shown.
seealso:
- linkId: "112680"
- linkId: DevExpress.ExpressApp.Win.Utils.DXSplashScreen
  altText: DXSplashScreen
---
@DevExpress.ExpressApp.Win.WinApplication uses this method to show a [Splash Screen](xref:10823), a [Wait Form](xref:10824) or a [Splash Image](xref:10825#create-and-show-splash-image-in-code).

Call this method before an operation if you expect it to run long. The method shows a splash form while the user waits for the operation to complete.
To close the form after the operation completes, call the @DevExpress.ExpressApp.Win.WinApplication.StopSplash method.

See [](xref:112680) on how to use splash forms.
