---
uid: DevExpress.ExpressApp.Security.SecurityModule.ChangePasswordOnLogonAction
name: ChangePasswordOnLogonAction
type: Property
summary: An [Action](xref:112622) that shows the **Change password on first logon** dialog.
syntax:
  content: |-
    [Browsable(false)]
    public PopupWindowShowAction ChangePasswordOnLogonAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.PopupWindowShowAction
    description: A [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) Action that shows the **Change password on first logon** dialog.
seealso: []
---
Users that implement the [](xref:DevExpress.Persistent.Base.Security.IAuthenticationStandardUser) interface have the [IAuthenticationStandardUser.ChangePasswordOnFirstLogon](xref:DevExpress.Persistent.Base.Security.IAuthenticationStandardUser.ChangePasswordOnFirstLogon) property. This property specifies whether they are prompted to change their password on the first logon. When this property is set to **true** for a particular user, an additional dialog represented by the **ChangePasswordOnLogonParameters** Detail View is displayed by the **ChangePasswordOnLogonAction** Action after authentication. The image below shows the displayed dialog.

![ChangePasswordOnFirstLogon](~/images/changepasswordonfirstlogon115373.png)

When executed, the **ChangePasswordOnLogonAction** Action can throw the **RetypeTheInformation** exception  in the following cases:

* New password value is the same as an old password value.
* New password value and a confirmed password value are different.