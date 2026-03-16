---
uid: DevExpress.ExpressApp.Security.UserManager
name: UserManager
type: Class
summary: Exposes API required to manage user objects in the database. Use [Dependency Injection](xref:404364) to access this class's instance in an application.
syntax:
  content: public sealed class UserManager
seealso:
- linkId: DevExpress.ExpressApp.Security.UserManager._members
  altText: UserManager Members
- linkId: "119064"
- linkId: "403413"
---

The `UserManager` service exposes methods that you can use to create and access application users and their login information. You can also use `UserManager` to interact with the [user lockout](xref:DevExpress.ExpressApp.Security.ISecurityUserLockout) mechanism.

The following code snippet demonstrates how to use the `UserManager` service to create a new application user. The [Template Kit](xref:405447) generates equivalent logic in the application's [Module Updater](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) code.

[!include[usermanager-create-user-example](~/templates/usermanager-create-user-example.md)]

For more use case scenarios, refer to the descriptions of the `UserManager` class members. For example:

- [AddLogin](xref:DevExpress.ExpressApp.Security.UserManager.AddLogin``1(``0,System.String,System.String)) - Adds login method information to a user record.
- [FindUserByName](xref:DevExpress.ExpressApp.Security.UserManager.FindUserByName``1(DevExpress.ExpressApp.IObjectSpace,System.String)) - Finds an application user object based on a user name.
- [GetAuthenticationToken](xref:DevExpress.ExpressApp.Security.UserManager.GetAuthenticationToken``1(``0,System.Int32,System.Collections.Generic.IEnumerable{System.Security.Claims.Claim})) - Generates an authentication token for a user with the capability to add additional claims to the token.
- [GetCurrentPrincipal](xref:DevExpress.ExpressApp.Security.UserManager.GetCurrentPrincipal) - Gets the current user's `ClaimsPrincipal` object.
- [IsLockedOut](xref:DevExpress.ExpressApp.Security.UserManager.IsLockedOut(System.Object)) - Demonstrates how to interact with the user lockout mechanism.