---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.MaxLength
name: MaxLength
type: Property
summary: Specifies the maximum length that the current Property Editor's value can have.
syntax:
  content: public int MaxLength { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: A positive integer value specifying the maximum number of characters end users can enter.
seealso: []
---
Use this property when the current [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) is used to edit string values. By default, it is initialized by the [IModelMemberViewItem.MaxLength](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.MaxLength) property value that can be edited in the [Model Editor](xref:112582).

If you implement a custom Property Editor for string property values, consider setting up the control in accordance with this property .