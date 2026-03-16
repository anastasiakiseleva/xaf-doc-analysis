---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.SupportNavigationPermissionsForTypes
name: SupportNavigationPermissionsForTypes
type: Property
summary: Specifies whether or not the navigation permissions are supported for types.
syntax:
  content: |-
    [DefaultValue(true)]
    public bool SupportNavigationPermissionsForTypes { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if the navigation permissions are supported for types, otherwise `false`.'
seealso: []
---
To provide support for navigation permissions determined in the [Type Permissions](xref:113366) tab, set the `SupportNavigationPermissionsForTypes` property to `true`. This property switches between the two modes described in the table below:

| Property value | Mode description |
|---|---|
| `true` | This mode is used in applications created in version 16.1 or earlier and updated to 16.2 or later. Navigation permissions from the **Type Permissions** tab have effect, but its priority is less than the settings in the **Navigation Permissions** tab. Access to the navigation items will not be changed while you don't specify any settings in the **Navigation Permissions** tab. In this mode, non-persistent navigation items are always available if access is not denied in the **Navigation Permissions** tab. |
| `false` | This mode is used in applications created in versions 16.2 and later. Navigation permissions from the **Type Permissions** tab have no effect and only new settings from the **Navigation Permissions** tab will be used. If permissions are not determined, access will be allowed or denied consistent with the role's policy. In this mode, non-persistent navigation items are available if access is not denied in the **Navigation Permissions** or not disabled in the role's policy. |
