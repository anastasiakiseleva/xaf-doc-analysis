---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.GetMemberCaption(DevExpress.ExpressApp.DC.ITypeInfo,System.String)
name: GetMemberCaption(ITypeInfo, String)
type: Method
summary: Returns the display caption corresponding to a [business class](xref:112570)' property.
syntax:
  content: public static string GetMemberCaption(ITypeInfo typeInfo, string memberName)
  parameters:
  - id: typeInfo
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypeInfo) object supplying metadata on the type of the business class that declares the required property.
  - id: memberName
    type: System.String
    description: A string specifying the name of the required property.
  return:
    type: System.String
    description: A string representing the display caption corresponding to the specified property.
seealso: []
---
For properties of business classes used in an **XAF** application, this method returns the [IModelCommonMemberViewItem.Caption](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.Caption) property value of the corresponding **Member** node. For all the other properties, the **GetMemberCaption** method returns the first part of the specified property name.