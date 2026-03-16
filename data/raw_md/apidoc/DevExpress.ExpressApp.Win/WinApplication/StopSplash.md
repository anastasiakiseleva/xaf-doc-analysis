---
uid: DevExpress.ExpressApp.Win.WinApplication.StopSplash(DevExpress.ExpressApp.Win.SplashType)
name: StopSplash(SplashType)
type: Method
summary: Executes the [DXSplashScreen.Stop(SplashType)](xref:DevExpress.ExpressApp.Win.Utils.DXSplashScreen.Stop(DevExpress.ExpressApp.Win.SplashType)) method.
syntax:
  content: public virtual void StopSplash(SplashType splashType)
  parameters:
  - id: splashType
    type: DevExpress.ExpressApp.Win.SplashType
    description: A splash form type to be closed.
seealso:
- linkId: "112680"
- linkId: DevExpress.ExpressApp.Win.Utils.DXSplashScreen
  altText: DXSplashScreen
---
Use the [](xref:DevExpress.ExpressApp.Win.WinApplication.StartSplash(DevExpress.ExpressApp.Win.SplashType)) method if you expect an operation to run long. The method shows a [Splash Screen](xref:10823), a [Wait Form](xref:10824) or a [Splash Image](xref:10825#create-and-show-splash-image-in-code) while the user waits for the operation to complete. Use the **StopSplash** method to close the form when the operation ends.

See [](xref:112680) on how to use splash forms.