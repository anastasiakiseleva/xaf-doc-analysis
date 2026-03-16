---
uid: DevExpress.ExpressApp.DC.CustomLogics.GetRegisteredLogics(System.Type)
name: GetRegisteredLogics(Type)
type: Method
summary: Returns the list domain logic class types that are registered for a specified Application Model interface.
syntax:
  content: public Type[] GetRegisteredLogics(Type forInterface)
  parameters:
  - id: forInterface
    type: System.Type
    description: A [](xref:System.Type) object that specifies the Application Model interface.
  return:
    type: System.Type[]
    description: A **System.Type[]** array of domain logic types that are registered for the _forInterface_ Application Model interface.
seealso: []
---
This method is used in the scope of the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method, when replacing the default domain logic implementations used for the Application Model interfaces with custom ones. For additional information, refer to the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method description.