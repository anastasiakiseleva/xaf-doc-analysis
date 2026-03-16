---
uid: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.CanEditModel
name: CanEditModel
type: Property
summary: Specifies whether users associated with the current role can use the [Model Editor](xref:112830). A **DevExpress.Xpo.Session** object, which is a persistent objects cache where the user will be instantiated.
syntax:
  content: |-
    [Appearance("XPOCanEditModelIsAdministrative", Enabled = false, Criteria = "IsAdministrative", Context = "DetailView")]
    public bool CanEditModel { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if users associated with the current role can use the Model Editor; otherwise - **false**.'
seealso: []
---
The **EditModel** action is available in the **Tools** menu item of the Windows Forms application's root window when this property is set to **true** in one of the current user's roles.

![ToolsEditModel](~/images/toolseditmodel115347.png)

![ModelEditor_Runtime](~/images/modeleditor_runtime115655.png)