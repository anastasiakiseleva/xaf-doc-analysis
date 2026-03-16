---
uid: DevExpress.ExpressApp.Win.Utils.DXSplashScreen.StartOverlayForm(System.Windows.Forms.Control)
name: StartOverlayForm(Control)
type: Method
summary: Shows an [Overlay Form](xref:120029) over a specified control.
syntax:
  content: public IOverlaySplashScreenHandle StartOverlayForm(Control control)
  parameters:
  - id: control
    type: System.Windows.Forms.Control
    description: A control for the Overlay Form to cover.
  return:
    type: DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle
    description: An Overlay Form's handle. The **StartOverlayForm** method returns this handle, and the [DXSplashScreen.StopOverlayForm](xref:DevExpress.ExpressApp.Win.Utils.DXSplashScreen.StopOverlayForm(DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle)) method uses this handle to access and close the form.
seealso:
- linkId: "112680"
---
