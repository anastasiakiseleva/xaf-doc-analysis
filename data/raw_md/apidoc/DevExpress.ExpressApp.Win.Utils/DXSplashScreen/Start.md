---
uid: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.Start(DevExpress.ExpressApp.Win.SplashType)
name: Start(SplashType)
type: Method
summary: 'Shows a specified [splash forms](xref:112680): a [Splash Screen](xref:10823), a [Wait Form](xref:10824) or a [Splash Image](xref:10825#create-and-show-splash-image-in-code).'
syntax:
  content: public virtual void Start(SplashType splashType)
  parameters:
  - id: splashType
    type: DevExpress.ExpressApp.Win.SplashType
    description: A @DevExpress.ExpressApp.Win.SplashType enumeration value.
seealso:
- linkId: "112680"
---
Call the **Start** method and pass a @DevExpress.ExpressApp.Win.SplashType to show the required splash form.

| Value passed | Splash form shown | Example |
|---|---|---|
| @DevExpress.ExpressApp.Win.SplashType.SplashScreen | A [Splash Screen](xref:10823). | ![splashformsplashscreen](~/images/SplashForm01_SplashScreen.png)
| @DevExpress.ExpressApp.Win.SplashType.WaitForm | A [Wait Form](xref:10824). | ![splashformwaitform](~/images/SplashForm03_WaitForm.png)
| @DevExpress.ExpressApp.Win.SplashType.Image | A [Splash Image](xref:10825#create-and-show-splash-image-in-code) | ![splashformsplashimage](~/images/SplashForm04_SplashImage.png) |


Use the @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.StartOverlayForm(System.Windows.Forms.Control) method to show an [Overlay Form](xref:120029). The **Start** method cannot display an Overlay Form.