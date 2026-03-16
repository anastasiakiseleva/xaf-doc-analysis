---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRoleBase.CanEditModel
name: CanEditModel
type: Property
summary: Specifies whether users associated with the current role can use the [Model Editor](xref:112830).
syntax:
  content: |-
    [Appearance("EFCanEditModelIsAdministrative", Enabled = false, Criteria = "IsAdministrative", Context = "DetailView")]
    public virtual bool CanEditModel { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if users associated with the current role can use the Model Editor; otherwise - **false**.'
seealso: []
---
The **EditModel** action is available in the **Tools** ribbon page of the Windows Forms application's root window when this property is set to **true** in one of the current user's roles.

![ToolsEditModel](~/images/toolseditmodel115347.png)

![ModelEditor_Runtime](~/images/modeleditor_runtime115655.png)