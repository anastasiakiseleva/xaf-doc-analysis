---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.GetMemberCaption(System.Type,System.String)
name: GetMemberCaption(Type, String)
type: Method
summary: Returns the display caption corresponding to a [business class](xref:112570)' property.
syntax:
  content: public static string GetMemberCaption(Type objectType, string memberName)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object representing the type of the business class that declares the required property.
  - id: memberName
    type: System.String
    description: A string specifying the name of the required property.
  return:
    type: System.String
    description: A string representing the display caption corresponding to the specified property.
seealso: []
---
For properties of business classes used in an **XAF** application, this method returns the [IModelCommonMemberViewItem.Caption](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.Caption) property value of the corresponding **Member** node. For all the other properties, the **GetMemberCaption** method returns the first part of the specified property name.

To see an example of using this method, refer to the [Add an Action with Option Selection](xref:402159) tutorial lesson.