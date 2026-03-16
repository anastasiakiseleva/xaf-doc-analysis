---
uid: DevExpress.ExpressApp.Security.UserManager.AccessFailed(System.Object)
name: AccessFailed(Object)
type: Method
summary: Increases the counter for failed login attempts by a specified user. If the counter value exceeds the limit, the user account is locked out.
syntax:
  content: public void AccessFailed(object user)
  parameters:
  - id: user
    type: System.Object
    description: An application user object.
seealso:
- linkId: DevExpress.ExpressApp.Security.UserManager.ResetLockout(System.Object)
  altText: ResetLockout
- linkId: DevExpress.ExpressApp.Security.UserManager.AccessFailed(System.Object)
  altText: AccessFailed
---

See the @DevExpress.ExpressApp.Security.ISecurityUserLockout topic for information on the user lockout ("Brute Force" attack protection) feature in XAF.

The following code snippet demonstrates how to use the `AccessFailed` method to increase the number of failed login attempts allowed for the specified user:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var userManager = serviceProvider.GetRequiredService<UserManager>();
userManager.AccessFailed(applicationUserObject);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider
