---
uid: DevExpress.ExpressApp.DC.ITypeInfo.GetDependentTypes(System.Predicate{DevExpress.ExpressApp.DC.ITypeInfo})
name: GetDependentTypes(Predicate<ITypeInfo>)
type: Method
summary: Supplies metadata on the types considered dependent on the current type.
syntax:
  content: IEnumerable<ITypeInfo> GetDependentTypes(Predicate<ITypeInfo> filter)
  parameters:
  - id: filter
    type: System.Predicate{DevExpress.ExpressApp.DC.ITypeInfo}
    description: A **Predicate\<**[](xref:DevExpress.ExpressApp.DC.ITypeInfo)**>** object which can be specified to filter the collection returned by this method.
  return:
    type: System.Collections.Generic.IEnumerable{DevExpress.ExpressApp.DC.ITypeInfo}
    description: An **IEnumerable\<**[](xref:DevExpress.ExpressApp.DC.ITypeInfo)**>** object which supplies metadata on the types considered dependent on the current type.
seealso:
- linkId: DevExpress.ExpressApp.DC.ITypeInfo.GetRequiredTypes(System.Predicate{DevExpress.ExpressApp.DC.ITypeInfo})
---
The following types are considered dependent:

1. Types that are direct descendants of the current type.
2. Types which contain fields and properties of the current type.