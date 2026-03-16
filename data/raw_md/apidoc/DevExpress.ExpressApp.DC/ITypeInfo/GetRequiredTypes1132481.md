---
uid: DevExpress.ExpressApp.DC.ITypeInfo.GetRequiredTypes(System.Predicate{DevExpress.ExpressApp.DC.ITypeInfo})
name: GetRequiredTypes(Predicate<ITypeInfo>)
type: Method
summary: Supplies metadata on the types considered required by the current type.
syntax:
  content: IEnumerable<ITypeInfo> GetRequiredTypes(Predicate<ITypeInfo> filter)
  parameters:
  - id: filter
    type: System.Predicate{DevExpress.ExpressApp.DC.ITypeInfo}
    description: A **Predicate\<**[](xref:DevExpress.ExpressApp.DC.ITypeInfo)**>** object which can be specified to filter the collection returned by this method.
  return:
    type: System.Collections.Generic.IEnumerable{DevExpress.ExpressApp.DC.ITypeInfo}
    description: An **IEnumerable\<**[](xref:DevExpress.ExpressApp.DC.ITypeInfo)**>** object which supplies metadata on the types considered required by the current type.
seealso:
- linkId: DevExpress.ExpressApp.DC.ITypeInfo.GetDependentTypes(System.Predicate{DevExpress.ExpressApp.DC.ITypeInfo})
---
The following types are considered required:

1. All the interfaces implemented in the current type.
2. The type from which the current type directly inherits.
3. The current class properties' types.