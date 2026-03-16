---
uid: DevExpress.ExpressApp.ModuleBase.GetRealModuleType(System.Type)
name: GetRealModuleType(Type)
type: Method
summary: Returns the type of an XAF Module.
syntax:
  content: public static Type GetRealModuleType(Type moduleType)
  parameters:
  - id: moduleType
    type: System.Type
    description: The **System.Type** object which potentially can be the type of an XAF Module.
  return:
    type: System.Type
    description: The **System.Type** object which is the type of an XAF Module.
seealso: []
---
If the passed type is not assignable from the [](xref:DevExpress.ExpressApp.ModuleBase) type, or the passed type is obsolete, an **ArgumentException** is thrown. Otherwise, the type passed via the _moduleType_ parameter is returned.