---
uid: DevExpress.ExpressApp.DC.FieldSizeAttribute
name: FieldSizeAttribute
type: Class
summary: Specifies the maximum number of characters that users can type in Property Editors of the current member. You can also specify the current member's [IModelMember.Size](xref:DevExpress.ExpressApp.Model.IModelMember.Size) property in the Model Editor. If the value passed to the **FieldSize** attribute is more than the **Size** property value, Property Editors ignore the attribute. In the XPO data model, use the [](xref:DevExpress.Xpo.SizeAttribute) instead of **FieldSizeAttribute**.
syntax:
  content: 'public class FieldSizeAttribute : Attribute'
seealso:
- linkId: DevExpress.ExpressApp.DC.FieldSizeAttribute._members
  altText: FieldSizeAttribute Members
---
To specify the maximum number of characters that users can enter into a specific Property Editor, use the [IModelMemberViewItem.MaxLength](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.MaxLength) property.