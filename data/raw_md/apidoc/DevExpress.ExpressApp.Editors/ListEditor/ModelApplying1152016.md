---
uid: DevExpress.ExpressApp.Editors.ListEditor.ModelApplying
name: ModelApplying
type: Event
summary: Occurs when customizations from the [Application Model](xref:112580) are applied to the List Editor's control.
syntax:
  content: public event EventHandler<CancelEventArgs> ModelApplying
seealso: []
---
Handle this event to prohibit applying customizations from the Application Model to the List Editor's control. For this purpose, set the event handler's **CancelEventArgs.Cancel** parameter to **true**.