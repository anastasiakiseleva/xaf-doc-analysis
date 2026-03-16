---
uid: DevExpress.ExpressApp.Security.UserManager.GetLoginProviderName(System.Security.Principal.IPrincipal)
name: GetLoginProviderName(IPrincipal)
type: Method
summary: Takes a claims principal and returns the name of the login provider that produced this claims principal.
syntax:
  content: public string GetLoginProviderName(IPrincipal principal)
  parameters:
  - id: principal
    type: System.Security.Principal.IPrincipal
    description: An object that implements the `IPrincipal` interface.
  return:
    type: System.String
    description: A `System.String` value that contains the name of the login provider.
seealso: []
---

The following code snippet demonstrates how to use the `GetLoginProviderName` method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var userManager = serviceProvider.GetRequiredService<UserManager>();
string loginProviderName = userManager.GetLoginProviderName(principal);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider