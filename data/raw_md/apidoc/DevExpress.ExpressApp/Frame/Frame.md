---
uid: DevExpress.ExpressApp.Frame
name: Frame
type: Class
summary: Serves as the site for a nested [View](xref:112611).
syntax:
  content: 'public class Frame : IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.Frame._members
  altText: Frame Members
- linkId: "112607"
- linkId: "112608"
- linkId: "112611"
- linkId: "112609"
---
[Frames](xref:112608) are used to represent nested [Views](xref:112611). Frames are constructed automatically by XAF, and you do not need to instantiate them manually.

You can access the current Frame from a [Controller](xref:112621) via its [Controller.Frame](xref:DevExpress.ExpressApp.Controller.Frame) property. Using the retrieved Frame, you can access all [Controllers](xref:112621) created for the current Frame via the [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) property. You can also access the View displayed by the Frame via the [Frame.View](xref:DevExpress.ExpressApp.Frame.View) property. To access the control representing a Frame in a UI, use the [Frame.Template](xref:DevExpress.ExpressApp.Frame.Template) property.

For additional information on Frames, refer to the [Windows and Frames](xref:112608) help topic.