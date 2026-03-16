---
uid: DevExpress.ExpressApp.DC.ITypesInfo.CanInstantiate(System.Type)
name: CanInstantiate(Type)
type: Method
summary: Indicates whether a specific type can be instantiated.
syntax:
  content: bool CanInstantiate(Type type)
  parameters:
  - id: type
    type: System.Type
    description: A [](xref:System.Type) object which represents the requried type.
  return:
    type: System.Boolean
    description: '**true**, if the specified type can be instantiated; otherwise, **false**.'
seealso: []
---
This method returns **true**, if the specified type is persistent, non-abstract, has a public constructor and is not an interface.