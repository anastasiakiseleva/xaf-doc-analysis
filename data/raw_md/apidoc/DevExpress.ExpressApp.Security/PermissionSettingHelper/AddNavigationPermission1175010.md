---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.AddNavigationPermission(DevExpress.Persistent.Base.IPermissionPolicyRole,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState})
name: AddNavigationPermission(IPermissionPolicyRole, String, Nullable<SecurityPermissionState>)
type: Method
summary: Adds the navigation permission to the current role with the specified settings.
syntax:
  content: public static IPermissionPolicyNavigationPermissionObject AddNavigationPermission(this IPermissionPolicyRole role, string itemPath, SecurityPermissionState? state)
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: An [](xref:DevExpress.Persistent.Base.IPermissionPolicyRole) object specifying the security role.
  - id: itemPath
    type: System.String
    description: A **String** value which is the path to the particular navigation item or group.
  - id: state
    type: System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionState) enumeration value specifying if access is granted or denied.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyNavigationPermissionObject
    description: A DevExpress.Persistent.Base.IPermissionPolicyNavigationPermissionObject object specifying the added navigation permission.
seealso: []
---
You can get the correct _itemPath_ value using the [Model Editor](xref:112582). For this purpose, expand the **NavigationItems** category, find the target navigation item and copy the **ItemPath** property value.

![ModelEditor_ItemPath](~/images/modeleditor_itempath125239.png)