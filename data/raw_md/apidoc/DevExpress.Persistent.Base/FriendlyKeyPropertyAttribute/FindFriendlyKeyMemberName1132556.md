---
uid: DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute.FindFriendlyKeyMemberName(DevExpress.ExpressApp.DC.ITypeInfo,System.Boolean)
name: FindFriendlyKeyMemberName(ITypeInfo, Boolean)
type: Method
summary: Returns the name of the persistent property which the system uses as an identifier-like property for a specific type.
syntax:
  content: public static string FindFriendlyKeyMemberName(ITypeInfo typeInfo, bool recursive)
  parameters:
  - id: typeInfo
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypeInfo) object which supplies metadata on the required type.
  - id: recursive
    type: System.Boolean
    description: '**true**, to take into account inherited **FriendlyKeyPropertyAttribute** attributes; otherwise, **false**.'
  return:
    type: System.String
    description: A string holding the name of the persistent property which the system uses as an identifier-like property for a specific type.
seealso: []
---
If the [](xref:DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute) is not applied to a class or its ancestors, the **FindFriendlyKeyMemberName** method returns `null`.