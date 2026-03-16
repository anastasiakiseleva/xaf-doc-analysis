---
uid: DevExpress.ExpressApp.Win.ISupportOverlayForm.StartOverlayForm(System.Windows.Forms.Control)
name: StartOverlayForm(Control)
type: Method
summary: Shows an [Overlay Form](xref:120029) over a specified control.
syntax:
  content: IOverlaySplashScreenHandle StartOverlayForm(Control control)
  parameters:
  - id: control
    type: System.Windows.Forms.Control
    description: A control for the Overlay Form to cover.
  return:
    type: DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle
    description: An Overlay Form's handle. The **StartOverlayForm** method returns this handle, and the [ISupportOverlayForm.StopOverlayForm](xref:DevExpress.ExpressApp.Win.ISupportOverlayForm.StopOverlayForm(DevExpress.XtraSplashScreen.IOverlaySplashScreenHandle)) method uses this handle to access and close the form.
seealso:
- linkId: "112680"
- linkId: DevExpress.ExpressApp.Win.Utils.DXSplashScreen
  altText: DXSplashScreen
---
