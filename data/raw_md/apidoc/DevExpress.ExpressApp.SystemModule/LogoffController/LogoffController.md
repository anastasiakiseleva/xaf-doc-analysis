---
uid: DevExpress.ExpressApp.SystemModule.LogoffController
name: LogoffController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **Logoff** Action.
syntax:
  content: 'public class LogoffController : WindowController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.LogoffController._members
  altText: LogoffController Members
---
The **LogoffController** is intended for presenting the **Logoff** Action. For details on the **Logoff** Action, refer to the description of the [LogoffController.LogoffAction](xref:DevExpress.ExpressApp.SystemModule.LogoffController.LogoffAction) property that provides access to this Action.

![LogOffAction_Win](~/images/logoffaction_win116762.png)

![LogOffAction_Web](~/images/logoffaction_web116266.png)

> [!NOTE]
> If you are using custom logon parameters and authentication, you need to implement the [AuthenticationBase.Logoff](xref:DevExpress.ExpressApp.Security.AuthenticationBase.Logoff) method [AuthenticationBase.IsLogoffEnabled](xref:DevExpress.ExpressApp.Security.AuthenticationBase.IsLogoffEnabled) property to support logoff functionality. Refer to the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic to see an example.