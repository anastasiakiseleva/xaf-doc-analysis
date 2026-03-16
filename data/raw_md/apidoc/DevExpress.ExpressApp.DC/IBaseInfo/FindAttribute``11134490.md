---
uid: DevExpress.ExpressApp.DC.IBaseInfo.FindAttribute``1(System.Boolean)
name: FindAttribute<AttributeType>(Boolean)
type: Method
summary: Indicates whether an attribute specified by the generic type parameter is associated with the type represented by the current [](xref:DevExpress.ExpressApp.DC.IBaseInfo) object.
syntax:
  content: |-
    AttributeType FindAttribute<AttributeType>(bool recursive)
        where AttributeType : Attribute
  parameters:
  - id: recursive
    type: System.Boolean
    description: '`true`, to take into account inherited attributes; otherwise, `false`.'
  typeParameters:
  - id: AttributeType
    description: The type of attribute to find.
  return:
    type: '{AttributeType}'
    description: A [](xref:System.Attribute) class descendant that represents the attribute specified by the generic type parameter and associated with the current type.
seealso: []
---
If an attribute of the specified type is not associated with the current type, the method returns `null`.