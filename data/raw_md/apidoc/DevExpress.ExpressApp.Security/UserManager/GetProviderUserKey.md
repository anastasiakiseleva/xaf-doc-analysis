---
uid: DevExpress.ExpressApp.Security.UserManager.GetProviderUserKey(System.Security.Principal.IPrincipal)
name: GetProviderUserKey(IPrincipal)
type: Method
summary: Returns the value of the User ID claim from the specified claims principal.
syntax:
  content: public string GetProviderUserKey(IPrincipal principal)
  parameters:
  - id: principal
    type: System.Security.Principal.IPrincipal
    description: An object that implements the `IPrincipal` interface.
  return:
    type: System.String
    description: A `System.String` value that contains the user key.
seealso:
- linkId: DevExpress.ExpressApp.Security.UserManager.GetUserName(System.Security.Principal.IPrincipal)
  altText: GetUserName
- linkId: DevExpress.ExpressApp.Security.UserManager.GetProviderUserKey(System.Security.Principal.IPrincipal)
  altText: GetProviderUserKey
---

The following code snippet demonstrates how to use the `GetProviderUserKey` method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var userManager = serviceProvider.GetRequiredService<UserManager>();
string userKey = userManager.GetProviderUserKey(principal);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider