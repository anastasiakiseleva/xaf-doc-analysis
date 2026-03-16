---
uid: DevExpress.ExpressApp.DC.CustomLogics
name: CustomLogics
type: Class
summary: Arguments passed to the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method.
syntax:
  content: public sealed class CustomLogics
seealso:
- linkId: DevExpress.ExpressApp.DC.CustomLogics._members
  altText: CustomLogics Members
- linkId: "112580"
---
The [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method allows you to replace the default domain logic implementations used for the Application Model interfaces with custom ones. For this purpose, a [](xref:DevExpress.ExpressApp.DC.CustomLogics) object, exposed by the method's _customLogics_ parameter, supplies the following methods.

| Method | Description |
|---|---|
| [CustomLogics.RegisterLogic](xref:DevExpress.ExpressApp.DC.CustomLogics.RegisterLogic(System.Type,System.Type)) | Registers a particular domain logic class for a specified Application Model interface. |
| [CustomLogics.UnregisterLogic](xref:DevExpress.ExpressApp.DC.CustomLogics.UnregisterLogic(System.Type,System.Type)) | Unregisters a particular domain for a specified Application Model interface. |
| [CustomLogics.IsRegisteredLogic](xref:DevExpress.ExpressApp.DC.CustomLogics.IsRegisteredLogic(System.Type,System.Type)) | Indicates whether a particular domain logic class is registered for a specified Application Model interface. |
| [CustomLogics.IsUnregisteredLogic](xref:DevExpress.ExpressApp.DC.CustomLogics.IsUnregisteredLogic(System.Type,System.Type)) | Indicates whether a particular domain logic class was unregistered for a specified Application Model interface. |
| [CustomLogics.GetRegisteredLogics](xref:DevExpress.ExpressApp.DC.CustomLogics.GetRegisteredLogics(System.Type)) | Returns the list domain logic class types that are registered for a specified Application Model interface. |

To see an example of using the **CustomLogics** class' methods, refer to the [ModuleBase.CustomizeLogics](xref:DevExpress.ExpressApp.ModuleBase.CustomizeLogics(DevExpress.ExpressApp.DC.CustomLogics)) method description.