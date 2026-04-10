---
uid: DevExpress.ExpressApp.XafApplication.MaxLogonAttemptCount
name: MaxLogonAttemptCount
type: Property
summary: Specifies the number of failed login attempts before the application closes. (WinForms only)
syntax:
  content: |-
    [DefaultValue(3)]
    public int MaxLogonAttemptCount { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: The allowed number of failed login attempts.
seealso: []
---
To limit the maximum login attempt count in both ASP.NET Core Blazor and Windows Forms XAF applications, use @DevExpress.ExpressApp.Security.LockoutOptions.

The `MaxLogonAttemptCount` property takes effect when the [LockoutOptions.Enabled](xref:DevExpress.ExpressApp.Security.LockoutOptions.Enabled) property is set to `false`.
