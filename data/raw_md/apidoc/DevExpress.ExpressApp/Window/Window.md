---
uid: DevExpress.ExpressApp.Window
name: Window
type: Class
summary: Serves as the base class for [Windows](xref:112608).
syntax:
  content: 'public class Window : Frame'
seealso:
- linkId: DevExpress.ExpressApp.Window._members
  altText: Window Members
- linkId: "112608"
- linkId: "112609"
- linkId: "112607"
---
The **Window** is a [](xref:DevExpress.ExpressApp.Frame) descendant. The difference between the **Window** and **Frame** classes is that Windows are independent objects. Generally, they represent root [Views](xref:112611), while Frames represent nested Views. Like Frames, Windows are constructed automatically by XAF, and except in very rare cases, like [implementing a custom Property Editor](xref:113097), displaying a pop-up Window, you do not need to instantiate them manually.

The **Window** class is the base class from which all Window classes derive. The [](xref:DevExpress.ExpressApp.Win.WinWindow) descendant is used in Windows Forms applications.

You can access the current Window from a [Window Controller](xref:112621) via its [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window) property. Using the retrieved Window, you can access all [Controllers](xref:112621) created for the current Window via the [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) property. To access the control representing a Window in a UI, use the [Window.Template](xref:DevExpress.ExpressApp.Window.Template) property.

For additional information on Windows, refer to the [Windows and Frames](xref:112608) help topic.