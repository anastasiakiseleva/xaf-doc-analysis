---
uid: DevExpress.Persistent.BaseImpl.ModelDifference.UserId
name: UserId
type: Property
summary: Specifies the identifier of a user who owns the current [](xref:DevExpress.Persistent.BaseImpl.ModelDifference) object.
syntax:
  content: |-
    [Browsable(false)]
    [ModelDefault("AllowEdit", "False")]
    public string UserId { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string which is the identifier of a user who owns the current model differences.
seealso:
- linkId: "403527"
---
If the Security System is enabled, the [SecuritySystem.CurrentUserId](xref:DevExpress.ExpressApp.SecuritySystem.CurrentUserId) value is used as the identifier. If the Security System is disabled, the **System.Security.Principal.WindowsIdentity.GetCurrent().Name** value is used. If this property value is empty, then the current [](xref:DevExpress.Persistent.BaseImpl.ModelDifference) object specifies the model differences layer shared by all users (administrator model differences).