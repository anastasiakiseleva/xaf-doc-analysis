---
uid: DevExpress.ExpressApp.Actions.HandleExceptionEventArgs
name: HandleExceptionEventArgs
type: Class
summary: Arguments passed to the [WinWindow.CustomHandleExceptionOnClosing](xref:DevExpress.ExpressApp.Win.WinWindow.CustomHandleExceptionOnClosing) event.
syntax:
  content: 'public class HandleExceptionEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Actions.HandleExceptionEventArgs._members
  altText: HandleExceptionEventArgs Members
---
The **CustomHandleExceptionOnClosing** event occurs when an exception is triggered while a [](xref:DevExpress.ExpressApp.Win.WinWindow) is being closed. You can handle this event to manually process an exceptional situation. The [CustomHandleExceptionEventArgs.Exception](xref:DevExpress.ExpressApp.Win.CustomHandleExceptionEventArgs.Exception) property specifies the original exception. Perform the actions required to correct it and set the **Handled** argument passed into the event handler to **true**, to suppress the original exception.