---
uid: DevExpress.ExpressApp.Editors.ListEditor.AllowEdit
name: AllowEdit
type: Property
summary: Indicates whether the data bound to the current [List Editor](xref:113189) can be edited via the List Editor's control.
syntax:
  content: public virtual bool AllowEdit { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if editing data is allowed; otherwise, **false**.'
seealso: []
---
Use this property to allow or prohibit editing of the bound data in the List Editor's control. Handle the [ListEditor.AllowEditChanged](xref:DevExpress.ExpressApp.Editors.ListEditor.AllowEditChanged) event, to perform the required actions after the ListEditor's **EditMode** property has changed.