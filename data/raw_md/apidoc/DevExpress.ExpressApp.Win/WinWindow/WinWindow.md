---
uid: DevExpress.ExpressApp.Win.WinWindow
name: WinWindow
type: Class
summary: A [Window](xref:112608) used in Windows Forms applications.
syntax:
  content: 'public class WinWindow : Window'
seealso:
- linkId: DevExpress.ExpressApp.Win.WinWindow._members
  altText: WinWindow Members
- linkId: "112608"
- linkId: "112609"
- linkId: "112607"
---
The **WinWindow** is a [](xref:DevExpress.ExpressApp.Window) descendant used in Windows Forms applications. As such, it is visualized by a form which you can access via the [WinWindow.Form](xref:DevExpress.ExpressApp.Win.WinWindow.Form) property. Compared to the base **Window** class, **WinWindow** introduces certain useful events. The [WinWindow.KeyDown](xref:DevExpress.ExpressApp.Win.WinWindow.KeyDown) event allows you to perform specific actions in response to a key press while the Window has focus. The complementary [WinWindow.KeyUp](xref:DevExpress.ExpressApp.Win.WinWindow.KeyUp) event occurs when a key is released and can be used to perform cleanup, necessary after execution of the **KeyDown** event handler. The [WinWindow.Closing](xref:DevExpress.ExpressApp.Win.WinWindow.Closing) and [WinWindow.Closed](xref:DevExpress.ExpressApp.Win.WinWindow.Closed) events can be used to perform actions when a Window is closed or to prevent it from closing altogether. There is also the static [WinWindow.QueryDefaultFormIcon](xref:DevExpress.ExpressApp.Win.WinWindow.QueryDefaultFormIcon) event, allowing you to specify custom default icons to be used by all **WinWindows**.

For general information on Windows, refer to the [](xref:DevExpress.ExpressApp.Window) class description and [Windows and Frames](xref:112608) help topic.