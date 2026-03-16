---
uid: DevExpress.ExpressApp.SelectionType
name: SelectionType
type: Enum
summary: Contains values that specify the selection types that a [List Editor](xref:113189) or a [View](xref:112611) supports.
syntax:
  content: public enum SelectionType
seealso: []
---
These enumeration values are used to specify the selection type via the following properties:

* The selection type supported by a List Editor - the [ListEditor.SelectionType](xref:DevExpress.ExpressApp.Editors.ListEditor.SelectionType) property.
* The selection type supported by a List View - the [ListView.SelectionType](xref:DevExpress.ExpressApp.ListView.SelectionType) property.
* Detail Views' [DetailView.SelectionType](xref:DevExpress.ExpressApp.DetailView.SelectionType) property always returns [SelectionType.FocusedObject](xref:DevExpress.ExpressApp.SelectionType.FocusedObject), indicating that a Detail View can only have one selected object represented by the currently focused object.