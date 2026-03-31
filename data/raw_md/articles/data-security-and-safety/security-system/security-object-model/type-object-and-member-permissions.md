---
uid: "404633"
title: 'Type, Object and Member Permissions'
seealso:
  - linkType: HRef
    linkId: 'https://supportcenter.devexpress.com/ticket/details/t589182/how-to-diagnose-effective-access-rights-for-a-specific-user-or-get-full-information'
    altText: How to diagnose effective access rights for a specific user or get full information about inner security permissions calculations
  - linkType: HRef
    linkId: 'https://supportcenter.devexpress.com/ticket/details/e4045/xaf-how-to-restrict-inter-departmental-data-access-using-security-permissions-ef-core'
    altText: 'How to restrict inter-departmental data access using Security Permissions (EF Core)'
  - linkType: HRef
    linkId: https://supportcenter.devexpress.com/ticket/details/t868197/xaf-generate-database-updater-code-for-security-roles-created-in-application-ui-in
    altText: How to generate database updater code for security roles created with the application UI in a development environment
---

# Type, Object and Member Permissions

This topic describes the Security System's permission types. Configure permissions in a role and assign it to a user. Each user should have at least one role. The Security System checks permissions for each role and determines access rights as described in the following topic: [Merging of Permissions Defined in Different Roles](xref:400290).

## Permission Policy

The Permission Policy determines the Security System's behavior when a specific type, object, or member does not have explicitly specified permissions. Refer to the following topic for more information: [Permission Policy](xref:116172).

![PermissionPolicy](~/images/permissionpolicy123615.png)

## Administrative Permission
The [IPermissionPolicyRole.IsAdministrative](xref:DevExpress.Persistent.Base.IPermissionPolicyRole.IsAdministrative) option grants all available permissions to a role.

![Security_AdministrativePermission](~/images/security_administrativepermission117173.png)

You cannot deny any rights for a role with the Administrative Permission.

## Edit Model Permission
The [IPermissionPolicyRole.CanEditModel](xref:DevExpress.Persistent.Base.IPermissionPolicyRole.CanEditModel) option allows users associated with the current role to use the [Model Editor](xref:112582).

![CanEditModel](~/images/caneditmodel132242.png)

When the Edit Model or Administrative permission is granted, the **EditModel** Action is available in the **Tools** category.

![ToolsEditModel](~/images/toolseditmodel115347.png)

## Navigation Permissions
In XAF applications, you can manage access to [navigation control](xref:113198) items in the **Navigation Permissions** tab. You can grant or deny a permission for a single navigation item or for the entire navigation group as shown in the image below:

![Security_NavigationPermissions](~/images/security_navigationpermissions125163.png)

Item permissions have a greater priority than group permissions. For instance, if you deny access to the group, but grant access for one of its items, this item is enabled in the navigation control.

> [!IMPORTANT]
> Navigation permissions manage the visibility of the navigation control's items. They do not grant or deny access to navigation items' associated business objects. Use Type permissions or Object permissions to manage access to these objects.

> [!NOTE]
> If you created an application in XAF v16.1 or earlier, you should [upgrade the application's project to the Allow/Deny Permissions Policy](https://supportcenter.devexpress.com/ticket/details/t418166/how-to-upgrade-an-existing-project-to-the-allow-deny-permission-policy-migrate-to) to enable the **Navigation Permissions** tab. If you use the Entity Framework as the ORM system, you may also need to [perform a migration](https://supportcenter.devexpress.com/ticket/details/t459507/obsolete-how-to-add-navigation-permissions-to-an-entity-framework-6-ef-6-application) to specify permissions for each navigation item.

## Type Permissions
The **Type Permissions** tab specifies access to all objects of a particular type. The image below illustrates the [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRole) Detail View.

![Security_TypePermissions](~/images/security_typepermissions117148.png)

The following operation types can be granted or denied:

| Operation | Description |
|---|---|
| **Read** | Objects of the current type are readable. To make an object read-only, allow the **Read** operation and deny the **Write** operation. |
| **Write** | Objects of the current type are editable. |
| **Create** | New objects of the current type can be created. Note that granting **Create** without **Write** does not allow a user to save new objects. |
| **Delete** | Objects of the current type can be deleted. |

### Restrict Non-Persistent Types Access
[!include[](~/templates/AdditionalSecuredTypes_example.md)]

> [!NOTE]
> Non-persistent types support only the Type and Member permissions, and the Security System applies these permissions only at the UI Level. Refer to the [Client-Side Security (2-Tier Architecture) - UI Level Mode](xref:113436#ui-level-mode) topic for more information about this mode and its limitations.

## Object Permissions
Object permissions grant access to object instances that fit a specified criterion. The following image illustrates the **Object Permissions** tab in the **Type Operation Permissions** dialog.

![Security_SetObjectPermissions](~/images/security_setobjectpermissions116997.png)

## Member Permissions
Member permissions grant access to specific members of an object. Double-click a record in a type permission list to invoke the following dialog:

![Security_SetMemberPermissions](~/images/security_setmemberpermissions116996.png)

For example, users can have access to objects of a particular type and simultaneously have no access to several members of this type. For another example, it is possible to deny access to objects of a particular type and only allow access to a strict list of its members. You can set a **Members** value to a string that is a semicolon-separated list of property names. In runtime, the **CheckedListBoxPropertyEditor** simplifies the specification of a `Members` value (select member names in the combo box). 

![Security_MemberPermissions_Members](~/images/security_memberpermissions_members117486.png)

You can also specify a criterion for a Member permission entry. The entry is active when the current object meets the criterion.

![Security_MemberPermissions_Criteria](~/images/security_memberpermissions_criteria117487.png)

> [!NOTE]
> 
> * In ASP.NET Core Blazor applications, you can input or modify a criterion only as a string. XAF validates this criterion before it saves a Member Permission record.
> * When you create a new object, Member Permissions do not affect the enabled/disabled state of its editors until you save the object. To disable specific editors for a new object, use the [Conditional Appearance Module](xref:113286).
> * Member Permissions affect [non-persistent properties](xref:113583) at the UI level only. If you deny access for a particular non-persistent property, XAF hides its editor from the UI, but you can access its value in code.

## Action Permissions

The Security System allows you to prohibit execution of both custom and XAF system Actions. Click the **Denied Actions** tab and specify Actions to be hidden from the UI. The image below illustrates the Role Detail View that shows this tab.

![Security_ActionPermissions](~/images/ActionPermissions_DeniedActionsTab.png)

The Security System marks built-in Actions as non-secure and hides them in the **Denied Actions** tab. The @DevExpress.ExpressApp.Security.SecurityModule.NonSecureActionsInitializing event allows you to customize a list of non-secure Actions. Add custom or remove system Actions from the @DevExpress.ExpressApp.Security.NonSecureActionsInitializingEventArgs.NonSecureActions collection to manage whether they are available in the **Denied Actions** tab. 

Note that Action Permissions hide Actions unconditionally. If you want to change Action visibility dynamically, use the  [Conditional Appearance](xref:113286) or [State Machine](xref:113713) Module functionality, set @DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria, or create custom rules that depend on criteria or object/UI changes in Controllers.