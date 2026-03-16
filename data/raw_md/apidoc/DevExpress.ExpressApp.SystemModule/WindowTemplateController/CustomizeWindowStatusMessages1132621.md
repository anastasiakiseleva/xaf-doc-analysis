---
uid: DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowStatusMessages
name: CustomizeWindowStatusMessages
type: Event
summary: Occurs when the [Window](xref:112608) status messages collection is updated. Allows you to modify the Window status messages collection.
syntax:
  content: public event EventHandler<CustomizeWindowStatusMessagesEventArgs> CustomizeWindowStatusMessages
seealso:
- linkId: "113253"
---
The [](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController) event is raised before setting the Window status messages collection. Handle this event in a custom [Window Controller](xref:112621), to modify Window status messages. Refer to the [How to: Customize Window Status Messages (WinForms)](xref:113253) topic, for details.
> [!NOTE]
> You can use the [WindowTemplateController.UpdateWindowStatusMessage](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.UpdateWindowStatusMessage) method to refresh the Window status messages.