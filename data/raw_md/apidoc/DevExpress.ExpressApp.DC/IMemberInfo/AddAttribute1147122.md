---
uid: DevExpress.ExpressApp.DC.IMemberInfo.AddAttribute(System.Attribute,System.Boolean)
name: AddAttribute(Attribute, Boolean)
type: Method
summary: Dynamically associates the specified attribute with the current member.
syntax:
  content: IMemberInfo AddAttribute(Attribute attribute, bool skipRefresh)
  parameters:
  - id: attribute
    type: System.Attribute
    description: '[](xref:System.Attribute) object that specifies the attribute to be applied.'
  - id: skipRefresh
    type: System.Boolean
    description: '**true**, if the [Types Info Subsystem](xref:113669) should not reload information from [](xref:DevExpress.Xpo.Metadata.XPDictionary) immediately; otherwise, **false**. If you set _skipRefresh_ to true, then you should call the **XafMemberInfo.Refresh** method for each updated member.'
  return:
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: ''
seealso: []
---
An example of using this method is provided in the [Use Metadata to Customize Business Classes Dynamically](xref:113583) topic.