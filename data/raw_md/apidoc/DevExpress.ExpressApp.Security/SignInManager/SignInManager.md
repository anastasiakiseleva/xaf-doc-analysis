---
uid: DevExpress.ExpressApp.Security.SignInManager
name: SignInManager
type: Class
summary: Exposes API required for user sign in. Use [Dependency Injection](xref:404364) to access this class's instance in an application.
syntax:
  content: public sealed class SignInManager
seealso:
- linkId: DevExpress.ExpressApp.Security.SignInManager._members
  altText: SignInManager Members
---

The code sample below demonstrates how to use the `SignInManager.AuthenticateByLogonParameters` method to implement a [Backend Web API Service](xref:403394) controller for JSON Web Token (JWT)-based authentication. The [Template Kit](xref:405447) generates equivalent code for Blazor projects with integrated Web API.

[!include[sign-in-manager-example](~/templates/sign-in-manager-example.md)]