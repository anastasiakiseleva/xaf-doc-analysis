---
uid: DevExpress.ExpressApp.DC.CustomLogics.IsUnregisteredLogic(System.Type,System.Type)
name: IsUnregisteredLogic(Type, Type)
type: Method
summary: Indicates whether a particular domain logic class was unregistered for a specified Application Model interface.
syntax:
  content: public bool IsUnregisteredLogic(Type forInterface, Type logicType)
  parameters:
  - id: forInterface
    type: System.Type
    description: A [](xref:System.Type) object representing the domain logic supposedly unregistered for the _forInterface_ Application Model interface.
  - id: logicType
    type: System.Type
    description: A [](xref:System.Type) object representing the Application Model interface for which the _logicType_ domain logic was supposedly unregistered.
  return:
    type: System.Boolean
    description: '**true**, if the _logicType_ domain logic class was unregistered for the _forInterface_ Application Model interface; otherwise, **false**.'
seealso:
- linkId: "112580"
---
This method is used in the scope of the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method, when replacing the default domain logic implementations used for the Application Model interfaces with custom ones. For additional information, refer to the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method description.