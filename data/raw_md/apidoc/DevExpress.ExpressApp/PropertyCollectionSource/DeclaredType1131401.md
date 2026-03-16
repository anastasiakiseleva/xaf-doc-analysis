---
uid: DevExpress.ExpressApp.PropertyCollectionSource.DeclaredType
name: DeclaredType
type: Property
summary: Returns the type in which the collection property represented by the current [](xref:DevExpress.ExpressApp.PropertyCollectionSource) is declared.
syntax:
  content: public Type DeclaredType { get; }
  parameters: []
  return:
    type: System.Type
    description: The type in which the collection property represented by the current **PropertyCollectionSource** is declared.
seealso: []
---
Note, that the **DeclaredType** and [PropertyCollectionSource.MasterObjectType](xref:DevExpress.ExpressApp.PropertyCollectionSource.MasterObjectType) properties will return different types, if the collection property is declared in a base class of the **MasterObjectType** class.