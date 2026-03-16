---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.GetMemberCaption(DevExpress.ExpressApp.DC.IMemberInfo)
name: GetMemberCaption(IMemberInfo)
type: Method
summary: Returns the display caption corresponding to a [business class](xref:112570)' property.
syntax:
  content: public static string GetMemberCaption(IMemberInfo memberInfo)
  parameters:
  - id: memberInfo
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object specifying member's metadata information.
  return:
    type: System.String
    description: A string representing the display caption corresponding to the specified property.
seealso: []
---
For properties of business classes used in an **XAF** application, this method returns the [IModelCommonMemberViewItem.Caption](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.Caption) property value of the corresponding **Member** node. For all the other properties, the **GetMemberCaption** method returns the first part of the specified property name.