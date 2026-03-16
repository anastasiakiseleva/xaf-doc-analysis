---
uid: DevExpress.ExpressApp.SystemModule.IModelListViewNewItemRow.NewItemRowPosition
name: NewItemRowPosition
type: Property
summary: Specifies whether to display the new item row in the current List View.
syntax:
  content: NewItemRowPosition NewItemRowPosition { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.NewItemRowPosition
    description: A [](xref:DevExpress.ExpressApp.NewItemRowPosition) enumeration value specifying whether to display the new item row in the current List View.
seealso:
- linkId: "113249"
---
The new item row allows end-users to create new objects directly in a List View. To support this, the List View should be editable and object creation should be allowed (see [IModelView.AllowEdit](xref:DevExpress.ExpressApp.Model.IModelView.AllowEdit) and [IModelView.AllowNew](xref:DevExpress.ExpressApp.Model.IModelView.AllowNew)).