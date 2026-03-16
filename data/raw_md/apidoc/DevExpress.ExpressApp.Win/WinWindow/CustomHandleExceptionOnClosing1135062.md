---
uid: DevExpress.ExpressApp.Win.WinWindow.CustomHandleExceptionOnClosing
name: CustomHandleExceptionOnClosing
type: Event
summary: Occurs when an exception is triggered while the [](xref:DevExpress.ExpressApp.Win.WinWindow) is being closed.
syntax:
  content: public event EventHandler<HandleExceptionEventArgs> CustomHandleExceptionOnClosing
seealso: []
---
Handle this event to manually process an exceptional situation occurring while the Window is being closed. The [CustomHandleExceptionEventArgs.Exception](xref:DevExpress.ExpressApp.Win.CustomHandleExceptionEventArgs.Exception) property specifies the original exception. Perform the actions required to correct it and set the **Handled** argument passed into the event handler to **true**, to suppress the original exception.