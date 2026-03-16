---
uid: DevExpress.ExpressApp.DC.ITypeInfo.IsAssignableFrom(DevExpress.ExpressApp.DC.ITypeInfo)
name: IsAssignableFrom(ITypeInfo)
type: Method
summary: Indicates whether the type can be assigned from a specific type.
syntax:
  content: bool IsAssignableFrom(ITypeInfo from)
  parameters:
  - id: from
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypeInfo) object that represents the type to compare with the current type.
  return:
    type: System.Boolean
    description: '`true`, if a type represented by the _from_ parameter and the current type are the same, or if the current type is in the inheritance hierarchy of the _from_ type, or if the current type is an interface that the _from_ type implements, or if the _from_ type is a generic type parameter and the current type represents one of its constraints. `false`, if none of the above is true, or if `null` was passed as the _from_ parameter.'
seealso: []
---
