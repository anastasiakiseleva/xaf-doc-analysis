---
uid: DevExpress.ExpressApp.DC.IBaseInfo.FindAttributes``1(System.Boolean)
name: FindAttributes<AttributeType>(Boolean)
type: Method
summary: Returns the attributes of the type specified by the generic type parameter, associated with the type represented by the current [](xref:DevExpress.ExpressApp.DC.IBaseInfo) object.
syntax:
  content: |-
    IEnumerable<AttributeType> FindAttributes<AttributeType>(bool recursive)
        where AttributeType : Attribute
  parameters:
  - id: recursive
    type: System.Boolean
    description: '**true**, to take into account inherited attributes; otherwise, **false**.'
  typeParameters:
  - id: AttributeType
    description: ''
  return:
    type: System.Collections.Generic.IEnumerable{{AttributeType}}
    description: An **IEnumerable\<AttributeType>** object that represents the attributes associated with the current type.
seealso: []
---
If no attributes of the specified type are associated with the current type, the method returns an empty iterator.