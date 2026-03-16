---
uid: DevExpress.ExpressApp.Security.UserManager.IsLockedOut(System.Object)
name: IsLockedOut(Object)
type: Method
summary: Gets a value that indicates whether the specified user account is locked out by "Brute Force" attack protection.
syntax:
  content: public bool IsLockedOut(object user)
  parameters:
  - id: user
    type: System.Object
    description: An application user object.
  return:
    type: System.Boolean
    description: A `System.Boolean` value that indicates whether or not the user account is locked out.
seealso:
- linkId: DevExpress.ExpressApp.Security.UserManager.ResetLockout(System.Object)
  altText: ResetLockout
- linkId: DevExpress.ExpressApp.Security.UserManager.AccessFailed(System.Object)
  altText: AccessFailed
---

[!include[usermanager-user-lockout-example](~/templates/usermanager-user-lockout-example.md)]