---
uid: DevExpress.ExpressApp.Editors.ListEditor.FocusedObjectChanging
name: FocusedObjectChanging
type: Event
summary: Occurs before the focused object is changed in a [List Editor](xref:113189)'s control.
syntax:
  content: public event EventHandler<CancelEventArgs> FocusedObjectChanging
seealso:
- linkId: DevExpress.ExpressApp.Editors.ListEditor.FocusedObject
---
Handle this event to prohibit changing of the focused object. For this purpose, set the event handler's **CancelEventArgs.Cancel** parameter to **true**.