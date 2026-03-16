---
uid: DevExpress.ExpressApp.SystemModule.CustomizeWindowStatusMessagesEventArgs
name: CustomizeWindowStatusMessagesEventArgs
type: Class
summary: Arguments passed to the [WindowTemplateController.CustomizeWindowStatusMessages](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowStatusMessages) event.
syntax:
  content: 'public class CustomizeWindowStatusMessagesEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.CustomizeWindowStatusMessagesEventArgs._members
  altText: CustomizeWindowStatusMessagesEventArgs Members
- linkId: "113253"
---
The **CustomizeWindowStatusMessagesEventArgs** class declares the [CustomizeWindowStatusMessagesEventArgs.StatusMessages](xref:DevExpress.ExpressApp.SystemModule.CustomizeWindowStatusMessagesEventArgs.StatusMessages) property, specific to the [WindowTemplateController.CustomizeWindowCaption](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowCaption) event. This event is raised before the [Window](xref:112608) status messages collection is updated. Handle the **CustomizeWindowStatusMessages** event in a custom [Window Controller](xref:112621) to modify Window status messages. Refer to the [How to: Customize Window Status Messages (WinForms)](xref:113253) for details.