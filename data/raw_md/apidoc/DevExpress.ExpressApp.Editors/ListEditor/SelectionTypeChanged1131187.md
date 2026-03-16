---
uid: DevExpress.ExpressApp.Editors.ListEditor.SelectionTypeChanged
name: SelectionTypeChanged
type: Event
summary: Occurs after a [List Editor](xref:113189)'s supported selection type is changed.
syntax:
  content: public event EventHandler SelectionTypeChanged
seealso: []
---
Generally, you do not have to handle this event.

When deriving from the [](xref:DevExpress.ExpressApp.Editors.ListEditor) class, call the **OnSelectionTypeChanged** method after the List Editor's control changes its supported selection type. This will raise the **SelectionTypeChanged** event.