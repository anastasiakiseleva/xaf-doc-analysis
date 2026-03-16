---
uid: DevExpress.ExpressApp.Editors.ListEditor.ModelSaving
name: ModelSaving
type: Event
summary: Occurs when the List Editor's control customizations are saved to the [Application Model](xref:112580).
syntax:
  content: public event EventHandler<CancelEventArgs> ModelSaving
seealso: []
---
Handle this event to prohibit saving the List Editor's control customizations to the Application Model. For this purpose, set the event handler's **CancelEventArgs.Cancel** parameter to **true**.