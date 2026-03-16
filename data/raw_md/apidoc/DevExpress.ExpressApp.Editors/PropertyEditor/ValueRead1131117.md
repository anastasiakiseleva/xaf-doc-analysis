---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.ValueRead
name: ValueRead
type: Event
summary: Occurs after the property value has been read to the current Property Editor's control.
syntax:
  content: public event EventHandler ValueRead
seealso: []
---
This event is raised as a result of calling the [PropertyEditor.ReadValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ReadValue) method. Handle it, to perform custom actions after the property value is written to the Property Editor's control (see [ViewItem.Control](xref:DevExpress.ExpressApp.Editors.ViewItem.Control)).