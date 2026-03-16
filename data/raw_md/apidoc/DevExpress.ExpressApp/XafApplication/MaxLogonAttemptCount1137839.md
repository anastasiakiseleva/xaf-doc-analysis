---
uid: DevExpress.ExpressApp.XafApplication.MaxLogonAttemptCount
name: MaxLogonAttemptCount
type: Property
summary: Specifies the allowed number of failed login attempts before the application closes.
syntax:
  content: |-
    [DefaultValue(3)]
    public int MaxLogonAttemptCount { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value that specifies the allowed number of failed login attempts before the application closes.
seealso: []
---
The application closes automatically is the failed logins count exceeds the **MaxLogonAttemptCount**. The default value is 3. You can modify this value in code.