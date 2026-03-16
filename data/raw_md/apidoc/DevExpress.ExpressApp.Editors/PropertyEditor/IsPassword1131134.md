---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.IsPassword
name: IsPassword
type: Property
summary: Specifies whether the current Property Editor represents a password.
syntax:
  content: public bool IsPassword { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true** if the current Property Editor's value represents a password; otherwise, **false**."
seealso: []
---
By default, this property returns the [IModelCommonMemberViewItem.IsPassword](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.IsPassword) property value of the [Application Model](xref:112580)'s node. This node can be accessed using the [PropertyEditor.Model](xref:DevExpress.ExpressApp.Editors.PropertyEditor.Model) property.

If you implement a custom Property Editor for string property values, consider changing the control's behavior if the **IsPassword** property returns **true**.