---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.EnsureNavigationPermission(DevExpress.Persistent.Base.IPermissionPolicyRole,System.String)
name: EnsureNavigationPermission(IPermissionPolicyRole, String)
type: Method
summary: Searches for the first permission for the specified navigation item in the current role. If the navigation permission is not found, it is created.
syntax:
  content: public static IPermissionPolicyNavigationPermissionObject EnsureNavigationPermission(this IPermissionPolicyRole role, string itemPath)
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: An [](xref:DevExpress.Persistent.Base.IPermissionPolicyRole) object specifying the security role.
  - id: itemPath
    type: System.String
    description: A **String** value which is the path to the particular navigation item or group.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyNavigationPermissionObject
    description: A DevExpress.Persistent.Base.IPermissionPolicyNavigationPermissionObject object specifying the found or created navigation permission.
seealso: []
---
You can get the correct _itemPath_ value using the [Model Editor](xref:112582). For this purpose, expand the **NavigationItems** category, find the target navigation item and copy the **ItemPath** property value.

![ModelEditor_ItemPath](~/images/modeleditor_itempath125239.png)
> [!NOTE]
> If your application is created in earlier XAF versions and uses Entity Framework as the ORM system, you may need to [perform a migration](https://supportcenter.devexpress.com/ticket/details/t459507/obsolete-how-to-add-navigation-permissions-to-an-entity-framework-6-ef-6-application) to use the [Navigation Permissions](xref:113366) functionality.
