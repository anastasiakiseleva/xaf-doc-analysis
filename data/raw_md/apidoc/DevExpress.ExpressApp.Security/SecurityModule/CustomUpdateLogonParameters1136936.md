---
uid: DevExpress.ExpressApp.Security.SecurityModule.CustomUpdateLogonParameters
name: CustomUpdateLogonParameters
type: Event
summary: Occurs when the [SecurityModule.TryUpdateLogonParameters](xref:DevExpress.ExpressApp.Security.SecurityModule.TryUpdateLogonParameters(System.String,System.Object)) method is executed.
syntax:
  content: public static event EventHandler<CustomUpdateLogonParametersEventArgs> CustomUpdateLogonParameters
seealso: []
---
Handle this event if you need to perform custom actions when the **TryUpdateLogonParameters** method is called, for instance, to manually update a password that is stored in a custom Logon Parameters object referenced by the [SecuritySystem.LogonParameters](xref:DevExpress.ExpressApp.SecuritySystem.LogonParameters) property.