---
uid: DevExpress.ExpressApp.SystemModule.WindowTemplateController
name: WindowTemplateController
type: Class
summary: A [](xref:DevExpress.ExpressApp.WindowController) descendant. Updates the current [Window](xref:112608) status messages and caption.
syntax:
  content: 'public class WindowTemplateController : WindowController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.WindowTemplateController._members
  altText: WindowTemplateController Members
- linkId: "113141"
- linkId: "113252"
- linkId: "113253"
---
The **WindowTemplateController** is activated in all Windows, and allows you to customize the Window status messages and caption. For this purpose, the Controller exposes two public events:

* [WindowTemplateController.CustomizeWindowCaption](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowCaption) - allows you to customize Windows captions;
* [WindowTemplateController.CustomizeWindowStatusMessages](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowStatusMessages) - allows you to customize Windows status messages.

To see examples of handling these events, refer to the [How to: Customize a Window Caption](xref:113252) and [How to: Customize Window Status Messages (WinForms)](xref:113253) topics.

You can use the [WindowTemplateController.UpdateWindowCaption](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.UpdateWindowCaption*) and [WindowTemplateController.UpdateWindowStatusMessage](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.UpdateWindowStatusMessage) methods to refresh the window caption and status messages when required.