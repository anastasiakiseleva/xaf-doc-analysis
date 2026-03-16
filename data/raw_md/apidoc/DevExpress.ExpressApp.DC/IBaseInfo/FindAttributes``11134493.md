---
uid: DevExpress.ExpressApp.DC.IBaseInfo.FindAttributes``1
name: FindAttributes<AttributeType>()
type: Method
summary: Returns the attributes of the type specified by the generic type parameter, associated with the type represented by the current [](xref:DevExpress.ExpressApp.DC.IBaseInfo) object.
syntax:
  content: |-
    IEnumerable<AttributeType> FindAttributes<AttributeType>()
        where AttributeType : Attribute
  typeParameters:
  - id: AttributeType
    description: ''
  return:
    type: System.Collections.Generic.IEnumerable{{AttributeType}}
    description: An **IEnumerable\<AttributeType>** object that represents the attributes associated with the current type.
seealso: []
---
This method searches over a type's own attributes as well as the inherited attributes. If no attributes of the specified type are associated with the current type, the method returns an empty iterator.