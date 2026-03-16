---
uid: DevExpress.ExpressApp.Model.IModelView.AllowEdit
name: AllowEdit
type: Property
summary: Specifies whether objects displayed in the current View can be edited when the View is Object View.
syntax:
  content: bool AllowEdit { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if objects displayed in the current View can be edited; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.DefaultListViewOptionsAttribute.AllowEdit
---
The **AllowEdit** value is used to calculate the [View.AllowEdit](xref:DevExpress.ExpressApp.View.AllowEdit) value. For ListView, this property affects [Inplace](xref:113249) editing only.