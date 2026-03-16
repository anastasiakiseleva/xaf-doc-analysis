---
uid: DevExpress.ExpressApp.DC.ITypeInfo.UnderlyingTypeInfo
name: UnderlyingTypeInfo
type: Property
summary: Supplies metadata on the underlying type argument of the current nullable type.
syntax:
  content: ITypeInfo UnderlyingTypeInfo { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: An [](xref:DevExpress.ExpressApp.DC.ITypeInfo) object which supplies metadata on the underlying type argument of the current nullable type.
seealso: []
---
If the current type is not a nullable type, this property returns an **ITypeInfo** object which supplies metadata on the current type.