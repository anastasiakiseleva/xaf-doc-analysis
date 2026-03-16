---
uid: DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions.SignOutRedirect
name: SignOutRedirect
type: Property
summary: Specifies a page where an unauthorized user is redirected.
syntax:
  content: public string SignOutRedirect { get; set; }
  parameters: []
  return:
    type: System.String
    description: Page relative path.
seealso: []
---
If you do not create a new user or when a user signs out of the application, you may want to redirect the user to a custom page for unauthorized users. Add the following line to your [Active Directory configuration](xref:402197):

# [C#](#tab/tabid-csharp-1)

```csharp{3}
.AddAuthenticationActiveDirectory(options => {
    // ...
    options.SignOutRedirect = "/UserSignedOut"
})
```
***
