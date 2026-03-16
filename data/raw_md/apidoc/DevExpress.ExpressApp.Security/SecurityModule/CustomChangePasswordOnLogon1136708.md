---
uid: DevExpress.ExpressApp.Security.SecurityModule.CustomChangePasswordOnLogon
name: CustomChangePasswordOnLogon
type: Event
summary: Occurs when the **ChangePasswordOnLogon** Action is being executed.
syntax:
  content: public event EventHandler<CustomChangePasswordOnLogonEventArgs> CustomChangePasswordOnLogon
seealso: []
---
Handle this event to customize the behavior of the**ChangePasswordOnLogon** Action. By default, a separate [](xref:DevExpress.ExpressApp.IObjectSpace) is created, a [SecuritySystem.CurrentUser](xref:DevExpress.ExpressApp.SecuritySystem.CurrentUser) object is queried and the **ChangePasswordOnLogonParameters.NewPassword** value is passed to the [IAuthenticationStandardUser.SetPassword](xref:DevExpress.Persistent.Base.Security.IAuthenticationStandardUser.SetPassword(System.String)) method to update the password. The password change is immediately committed to the database. After the change is successfully committed, the new password is passed to the [SecurityModule.TryUpdateLogonParameters](xref:DevExpress.ExpressApp.Security.SecurityModule.TryUpdateLogonParameters(System.String,System.Object)) method.