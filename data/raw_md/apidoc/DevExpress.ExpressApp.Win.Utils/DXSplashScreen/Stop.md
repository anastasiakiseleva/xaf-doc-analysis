---
uid: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.Stop
name: Stop()
type: Method
summary: Closes a [Splash Screen](xref:10823) or [Splash Image](xref:10825#create-and-show-splash-image-in-code).
syntax:
  content: public virtual void Stop()
seealso:
- linkId: "112680"
---
The **Start** method accesses the following properties one by one. As soon as the **Start** method successfully gets a value, the method closes the relevant splash form.

| Access order | Property accessed | Result if not _null_ | Result if _null_ |
|---|---|---|---|
| 1 | @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.SplashFormType | Closes a Splash Screen | Accesses the next property |
| 2 | @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.SplashImage and @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.SplashSvgImage | Closes a Splash Image | Does not close anything |

If all accessed properties return _null_, the **Stop** method does not close any forms.

To close other [splash forms](xref:112680) use the @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.Stop(DevExpress.ExpressApp.Win.SplashType) and @DevExpress.ExpressApp.Win.Utils.DXSplashScreen.StopOverlayForm(DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle) methods.