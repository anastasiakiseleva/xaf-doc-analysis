---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.AssociationPermissionsMode
name: AssociationPermissionsMode
type: Property
summary: Specifies the mode of processing security permissions for associations.
syntax:
  content: |-
    [DefaultValue(AssociationPermissionsMode.Auto)]
    public AssociationPermissionsMode AssociationPermissionsMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Security.AssociationPermissionsMode
    description: An [](xref:DevExpress.ExpressApp.Security.AssociationPermissionsMode) value.
seealso:
- linkId: "113556"
---

Add the following code to the _Startup.cs_ file:

[!include[AssociationPermissionsMode-example](~/templates/AssociationPermissionsMode-example.md)]

Refer to the [Permissions for Associated Objects](xref:116170) for more information about the available modes.
