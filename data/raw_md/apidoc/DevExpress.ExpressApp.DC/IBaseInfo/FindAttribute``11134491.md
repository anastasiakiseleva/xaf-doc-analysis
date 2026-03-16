---
uid: DevExpress.ExpressApp.DC.IBaseInfo.FindAttribute``1
name: FindAttribute<AttributeType>()
type: Method
summary: Indicates whether an attribute specified by the generic type parameter is associated with the type represented by the current [](xref:DevExpress.ExpressApp.DC.IBaseInfo) object.
syntax:
  content: |-
    AttributeType FindAttribute<AttributeType>()
        where AttributeType : Attribute
  typeParameters:
  - id: AttributeType
    description: 'The type of attribute to find.'
  return:
    type: '{AttributeType}'
    description: A [](xref:System.Attribute) class descendant that represents the attribute specified by the generic type parameter and associated with the current type.
seealso: []
---
This method searches over a type's own attributes as well as the inherited attributes. If an attribute of the specified type is not associated with the current type, the method returns `null`.