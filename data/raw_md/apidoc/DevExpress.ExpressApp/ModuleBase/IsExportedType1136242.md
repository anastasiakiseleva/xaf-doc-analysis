---
uid: DevExpress.ExpressApp.ModuleBase.IsExportedType(System.Type)
name: IsExportedType(Type)
type: Method
summary: Detects whether the specified type is exported to the system class.
syntax:
  content: public virtual bool IsExportedType(Type type)
  parameters:
  - id: type
    type: System.Type
    description: A **Type** object that is the type to be tested.
  return:
    type: System.Boolean
    description: '**true** if the specified type is exported; otherwise, **flase**'
seealso: []
---
A module provides a list of exported types. These types (business classes) take part in the automatic application construction (they are loaded to the Application Model and they are managed by [Object Space](xref:113707)).