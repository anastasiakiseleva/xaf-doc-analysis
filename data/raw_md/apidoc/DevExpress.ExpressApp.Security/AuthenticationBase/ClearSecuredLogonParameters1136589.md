---
uid: DevExpress.ExpressApp.Security.AuthenticationBase.ClearSecuredLogonParameters
name: ClearSecuredLogonParameters()
type: Method
summary: Resets values exposed by the Logon Parameters object that should not be accessible after logon (e.g., password).
syntax:
  content: public virtual void ClearSecuredLogonParameters()
seealso: []
---
The logon parameters specified in the Logon Window can be accessed via the [SecuritySystem.LogonParameters](xref:DevExpress.ExpressApp.SecuritySystem.LogonParameters) property. You can clear the logon parameters, so they are not accessible in the application. For instance, a password can be hidden. For this purpose, clear these logon parameters when overriding the **ClearSecuredLogonParameters** method.