---
uid: DevExpress.ExpressApp.CustomCheckCompatibilityEventArgs.IsCompatibilityChecked
name: IsCompatibilityChecked
type: Property
summary: |-
  Indicates whether a compatibility has already been checked.  

  The @DevExpress.ExpressApp.XafApplication.CustomCheckCompatibility event is raised many times when logging on to the application and when creating each Object Space. Use the `IsCompatibilityChecked` property to perform database checking on the first compatibility check only. 
syntax:
  content: public bool IsCompatibilityChecked { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if the compatibility check has already been performed; `false`, if the compatibility check is being performed for the first time.'
seealso: []
---
