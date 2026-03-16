---
uid: DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute.MemberName
name: MemberName
type: Property
summary: Indicates the persistent property which the system uses as an identifier-like property.
syntax:
  content: public string MemberName { get; }
  parameters: []
  return:
    type: System.String
    description: A string that represents the name of an identifier-like persistent property.
seealso: []
---
You can change the property name, which is specified in code, via the **BOModel** | **_\<Class\>_** node's [IModelClass.FriendlyKeyProperty](xref:DevExpress.ExpressApp.Model.IModelClass.FriendlyKeyProperty) property in the [Model Editor](xref:112830).