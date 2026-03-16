---
uid: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.Stop(DevExpress.ExpressApp.Win.SplashType)
name: Stop(SplashType)
type: Method
summary: 'Closes a specified [splash form](xref:112680): a [Splash Screen](xref:10823), a [Wait Form](xref:10824) or a [Splash Image](xref:10825#create-and-show-splash-image-in-code).'
syntax:
  content: public virtual void Stop(SplashType splashType)
  parameters:
  - id: splashType
    type: DevExpress.ExpressApp.Win.SplashType
    description: A @DevExpress.ExpressApp.Win.SplashType enumeration value.
seealso:
- linkId: "112680"
---
Call the **Stop** method and pass a @DevExpress.ExpressApp.Win.SplashType to close the required splash form.

| Value passed | Splash form closed | Example |
|---|---|---|
| @DevExpress.ExpressApp.Win.SplashType.SplashScreen | A [Splash Screen](xref:10823). | ![splashformsplashscreen](~/images/SplashForm01_SplashScreen.png)
| @DevExpress.ExpressApp.Win.SplashType.WaitForm | A [Wait Form](xref:10824). | ![splashformwaitform](~/images/SplashForm03_WaitForm.png)
| @DevExpress.ExpressApp.Win.SplashType.Image | A [Splash Image](xref:10825#create-and-show-splash-image-in-code) | ![splashformsplashimage](~/images/SplashForm04_SplashImage.png) |


Use the @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.StopOverlayForm(DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle) method to close an [Overlay Form](xref:120029). The **Stop** method cannot close an Overlay Form.