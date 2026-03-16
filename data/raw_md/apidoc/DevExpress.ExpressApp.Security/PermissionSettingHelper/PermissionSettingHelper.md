---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper
name: PermissionSettingHelper
type: Class
summary: Provides [extension methods](https://learn.microsoft.com/en-us/dotnet/articles/csharp/programming-guide/classes-and-structs/extension-methods) for security roles that support the **Allow/Deny** [Permission Policy](xref:116172), and for type permissions associated with these roles.
syntax:
  content: public static class PermissionSettingHelper
seealso:
- linkId: DevExpress.ExpressApp.Security.PermissionSettingHelper._members
  altText: PermissionSettingHelper Members
---
You can use extension methods provided by the [](xref:DevExpress.ExpressApp.Security.PermissionSettingHelper) class in both Entity Framework and XPO implementations of the [](xref:DevExpress.Persistent.Base.IPermissionPolicyRole) interface. Additionally, **PermissionSettingHelper** provides extension methods for the **IPermissionPolicyTypePermissionObject** objects assigned to the [IPermissionPolicyRole.TypePermissions](xref:DevExpress.Persistent.Base.IPermissionPolicyRole.TypePermissions) collection. You can call these extension methods from the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method implemented in the [!include[File_Updater](~/templates/file_updater111114.md)] file to easily configure predefined permissions in code.
