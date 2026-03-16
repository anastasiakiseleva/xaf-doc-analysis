---
uid: DevExpress.ExpressApp.SystemModule.DialogControllerAcceptingEventArgs
name: DialogControllerAcceptingEventArgs
type: Class
summary: Represents arguments passed to the [DialogController.Accepting](xref:DevExpress.ExpressApp.SystemModule.DialogController.Accepting) event.
syntax:
  content: 'public class DialogControllerAcceptingEventArgs : CancelEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.DialogControllerAcceptingEventArgs._members
  altText: DialogControllerAcceptingEventArgs Members
---
The [](xref:DevExpress.ExpressApp.SystemModule.DialogControllerAcceptingEventArgs) class declares properties specific to the [DialogController.Accepting](xref:DevExpress.ExpressApp.SystemModule.DialogController.Accepting) event. This event is designed to execute custom code when clicking the accept button on a pop-up Window with a [](xref:DevExpress.ExpressApp.SystemModule.DialogController). You can handle this event to perform custom code, and specify a View to be displayed after this Action has been executed.

This class is inherited from the **CancelEventArgs** class, so, you can use the handler's **Cancel** parameter to prevent saving the changes made to the current Detail View's persistent object.