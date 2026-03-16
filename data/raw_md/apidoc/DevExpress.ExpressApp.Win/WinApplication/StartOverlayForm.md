---
uid: DevExpress.ExpressApp.Win.WinApplication.StartOverlayForm(System.Windows.Forms.Control)
name: StartOverlayForm(Control)
type: Method
summary: Executes the [DXSplashScreen.StartOverlayForm](xref:DevExpress.ExpressApp.Win.Utils.DXSplashScreen.StartOverlayForm(System.Windows.Forms.Control)) method.
syntax:
  content: public virtual IOverlaySplashScreenHandle StartOverlayForm(Control control)
  parameters:
  - id: control
    type: System.Windows.Forms.Control
    description: A control for the Overlay Form to cover.
  return:
    type: DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle
    description: An Overlay Form's handle. The **StartOverlayForm** method returns this handle, and the [WinApplication.StopOverlayForm](xref:DevExpress.ExpressApp.Win.WinApplication.StopOverlayForm(DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle)) method uses this handle to access and close the form.
seealso:
- linkId: "112680"
- linkId: DevExpress.ExpressApp.Win.Utils.DXSplashScreen
  altText: DXSplashScreen
---
