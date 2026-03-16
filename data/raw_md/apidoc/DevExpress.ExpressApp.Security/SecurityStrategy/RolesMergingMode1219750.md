---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.RolesMergingMode
name: RolesMergingMode
type: Property
summary: Specifies how the Security System determines if a user can perform a specific operation when this user has multiple roles with different permission sets.
syntax:
  content: |-
    [DefaultValue(RolesMergingMode.GrantedInAnyRole)]
    public RolesMergingMode RolesMergingMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Security.RolesMergingMode
    description: A [](xref:DevExpress.ExpressApp.Security.RolesMergingMode) enumeration value specifying the roles merging mode when a user has multiple roles.
seealso: []
---
By default, a user can execute an operation if it is allowed in any role assigned to this user (the `GrantedInAnyRole` mode). You can set the `RolesMergingMode` property to `GrantedInAllRoles` to make the behavior more strict and demand that an operation should be allowed in all roles.