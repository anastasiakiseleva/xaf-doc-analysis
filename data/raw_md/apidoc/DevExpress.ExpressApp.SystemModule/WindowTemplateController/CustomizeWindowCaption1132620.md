---
uid: DevExpress.ExpressApp.SystemModule.WindowTemplateController.CustomizeWindowCaption
name: CustomizeWindowCaption
type: Event
summary: Occurs before the [Window](xref:112608) caption is updated. Allows you to change the Window caption.
syntax:
  content: public event EventHandler<CustomizeWindowCaptionEventArgs> CustomizeWindowCaption
seealso:
- linkId: "113252"
---
The `CustomizeWindowCaption` event is raised before setting the Window caption text. Handle this event in a custom [Window Controller](xref:112621), to modify a Window caption. In Blazor application, this event affects only the browser window's caption. Refer to the [How to: Customize a Window Caption](xref:113252) topic, for details.
> [!NOTE]
> You can use the [WindowTemplateController.UpdateWindowCaption](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController.UpdateWindowCaption*) method to refresh the Window caption.