---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.FocusedObject
name: FocusedObject
type: Property
summary: Gets or sets the focused object in a [](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor).
syntax:
  content: public override object FocusedObject { get; set; }
  parameters: []
  return:
    type: System.Object
    description: The focused object.
seealso: []
---
Use this property to access the focused object. To perform the required actions when this property's value is changed, handle the following events:

* The [ListEditor.FocusedObjectChanging](xref:DevExpress.ExpressApp.Editors.ListEditor.FocusedObjectChanging) event occurs before the focused object is changed in a [List Editor](xref:113189)'s control.
* The [ListEditor.FocusedObjectChanged](xref:DevExpress.ExpressApp.Editors.ListEditor.FocusedObjectChanged) event occurs after the focused object has been changed in a List Editor's control.