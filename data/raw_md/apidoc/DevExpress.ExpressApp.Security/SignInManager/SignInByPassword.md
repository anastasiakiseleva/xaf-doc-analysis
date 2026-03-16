---
uid: DevExpress.ExpressApp.Security.SignInManager.SignInByPassword(System.String,System.String)
name: SignInByPassword(String, String)
type: Method
summary: Signs in a user based on the specified user name and password.
syntax:
  content: public AuthenticationResult SignInByPassword(string userName, string password)
  parameters:
  - id: userName
    type: System.String
    description: A string value that specifies the user name.
  - id: password
    type: System.String
    description: A string value that specifies the user password.
  return:
    type: DevExpress.ExpressApp.Security.AuthenticationResult
    description: An object of the `AuthenticationResult` type that contains the result of an authentication attempt.
seealso: []
---

Use this method to programmatically sign a user into an XAF application. This method takes an object that contains a user's logon parameters and returns an `AuthenticationResult` object.

[!include[signin-manager-authentication-result-description](~/templates/signin-manager-authentication-result-description.md)]

The following code snippet demonstrates how to use the `SignInByPassword` method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var signInManager = serviceProvider.GetRequiredService<SignInManager>();
var authResult = signInManager.SignInByPassword("User", "Password");
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider


## Usage Considerations

[!include[signin-manager-signin-method-usage-considerations](~/templates/signin-manager-signin-method-usage-considerations.md)]