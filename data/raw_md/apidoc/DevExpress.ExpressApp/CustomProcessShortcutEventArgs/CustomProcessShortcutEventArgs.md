---
uid: DevExpress.ExpressApp.CustomProcessShortcutEventArgs
name: CustomProcessShortcutEventArgs
type: Class
summary: Arguments passed to the [XafApplication.CustomProcessShortcut](xref:DevExpress.ExpressApp.XafApplication.CustomProcessShortcut) event.
syntax:
  content: 'public class CustomProcessShortcutEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.CustomProcessShortcutEventArgs._members
  altText: CustomProcessShortcutEventArgs Members
---
The **CustomProcessShortcut** event is raised as a result of calling the [XafApplication.ProcessShortcut](xref:DevExpress.ExpressApp.XafApplication.ProcessShortcut(DevExpress.ExpressApp.ViewShortcut)) method. Handle this event to create a custom [View](xref:112611) for the shortcut specified by the [CustomProcessShortcutEventArgs.Shortcut](xref:DevExpress.ExpressApp.CustomProcessShortcutEventArgs.Shortcut) property.