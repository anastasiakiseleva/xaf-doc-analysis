---
uid: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.Start
name: Start()
type: Method
summary: Shows a [Splash Screen](xref:10823) or [Splash Image](xref:10825#create-and-show-splash-image-in-code).
syntax:
  content: public virtual void Start()
seealso:
- linkId: "112680"
---
The **Start** method accesses the following properties one by one. As soon as the **Start** method successfully gets a value, the method shows the relevant splash form.

| Access order | Property accessed | Result if not _null_ | Result if _null_ |
|---|---|---|---|
| 1 | @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.SplashFormType | Shows a Splash Screen | Accesses the next property |
| 2 | @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.SplashImage | Shows a Splash Image | Accesses the next property
| 3 | @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.SplashSvgImage | Shows an SVG Splash Image | Does not show anything

If all accessed properties return _null_, the **Start** method does not show any forms.

To show other [splash forms](xref:112680) use the @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.Start(DevExpress.ExpressApp.Win.SplashType) and @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.StartOverlayForm(System.Windows.Forms.Control) methods.