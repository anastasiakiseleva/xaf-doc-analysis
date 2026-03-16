---
uid: DevExpress.ExpressApp.DC.CustomLogics.RegisterLogic(System.Type,System.Type)
name: RegisterLogic(Type, Type)
type: Method
summary: Registers a particular domain logic class for a specified Application Model interface.
syntax:
  content: public void RegisterLogic(Type forInterface, Type logicType)
  parameters:
  - id: forInterface
    type: System.Type
    description: A [](xref:System.Type) object representing the Application Model interface for which the _logicType_ domain logic will be registered.
  - id: logicType
    type: System.Type
    description: A [](xref:System.Type) object representing the domain logic class to be registered for the _forInterface_ Application Model interface.
seealso:
- linkId: "112580"
---
This method is used in the scope of the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method, when replacing the default domain logic implementations used for the Application Model interfaces with custom ones. For additional information, refer to the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method description.