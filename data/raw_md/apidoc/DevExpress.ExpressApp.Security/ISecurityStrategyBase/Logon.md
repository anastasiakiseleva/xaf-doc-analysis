---
uid: DevExpress.ExpressApp.Security.ISecurityStrategyBase.Logon(DevExpress.ExpressApp.IObjectSpace)
name: Logon(IObjectSpace)
type: Method
summary: Authenticates a user in the application.
syntax:
  content: void Logon(IObjectSpace objectSpace)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: The Object Space that this method uses to find a user in the database.
seealso: []
---
This method searches for a user with the specified logon parameters in the database and authenticates the user in the application.