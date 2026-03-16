---
uid: DevExpress.Persistent.Base.ValueManager.GetValueManager``1(System.String)
name: GetValueManager<ValueType>(String)
type: Method
summary: Finds the platform-specific value manager with a specified identifier. If the appropriate value manager is not found, this method creates it.
syntax:
  content: public static IValueManager<ValueType> GetValueManager<ValueType>(string key)
  parameters:
  - id: key
    type: System.String
    description: A value manager identifier.
  typeParameters:
  - id: ValueType
    description: ''
  return:
    type: DevExpress.Persistent.Base.IValueManager{{ValueType}}
    description: A platform-specific value manager with the _key_ identifier.
seealso: []
---
The following example demonstrates how to use this method:

[!include[ValueManager-example](~/templates/ValueManager-example.md)]
