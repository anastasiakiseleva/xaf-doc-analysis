---
uid: DevExpress.ExpressApp.DC.ITypeInfo.DeclaredDefaultMember
name: DeclaredDefaultMember
type: Property
summary: Supplies metadata on the type's property declared as the default.
syntax:
  content: IMemberInfo DeclaredDefaultMember { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object supplying metadata on the type's property declared as the default.
seealso: []
---
This method returns the type's public visible property marked with the `DefaultPropertyAttribute`. If the `DefaultPropertyAttribute` is not applied to a type or its ancestors, the `DeclaredDefaultMember` property returns `null`.

If a property is the default, then:

* It is displayed in Lookup Property Editors.
* It takes part in form caption generation.
* It is used in the FullTextSearch Action's engine.
* It is displayed first in List Views.