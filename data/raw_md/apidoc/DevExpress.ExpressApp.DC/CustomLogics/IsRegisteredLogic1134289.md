---
uid: DevExpress.ExpressApp.DC.CustomLogics.IsRegisteredLogic(System.Type,System.Type)
name: IsRegisteredLogic(Type, Type)
type: Method
summary: Indicates whether a particular domain logic class is registered for a specified Application Model interface.
syntax:
  content: public bool IsRegisteredLogic(Type forInterface, Type logicType)
  parameters:
  - id: forInterface
    type: System.Type
    description: A [](xref:System.Type) object representing the domain logic class supposedly registered for the _forInterface_ Application Model interface.
  - id: logicType
    type: System.Type
    description: A [](xref:System.Type) object representing the Application Model interface for which the _logicType_ domain logic is supposedly registered.
  return:
    type: System.Boolean
    description: '**true**, if the _logicType_ domain logic class is registered for the _forInterface_ Application Model interface; otherwise, **false**.'
seealso:
- linkId: "112580"
---
This method is used in the scope of the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method, when replacing the default domain logic implementations used for the Application Model interfaces with custom ones. For additional information, refer to the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method description.