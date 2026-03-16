---
uid: DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnAuthenticate
name: OnAuthenticate
type: Property
summary: Specifies custom authentication logic.
syntax:
  content: public Action<FindUserContext> OnAuthenticate { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.Security.FindUserContext}
    description: A delegate method that implements custom authentication logic.
seealso:
- linkId: "404264"
---

Handle the `OnAuthenticate` event to implement custom password-based authentication logic (for example, to implement authentication based on custom logon parameters).  

> [!IMPORTANT]
>
> The logic implemented in this event's handler completely overrides the standard authentication logic. Since this event is used to implement entirely custom logic, XAF does not validate the result returned by the handler method in any way, so you need to manually carry out all required checks in the handler. 
>
> If you only need to override logic used to find the user object and want the authentication system to carry out all checks that are standard for password-based authentication, use the [OnFindUser](xref:DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnFindUser) event instead.

## Example

To implement custom authentication, do the following:

1. Find a user object based on the specified logon parameters.

2. Check the found user object against the logon parameters specified during a logon attempt (for example, verify the password).

3. If the authentication succeeds, assign the user object to `context.User`; otherwise, throw an `AuthenticationException`. After the `context.User` property is set, XAF authentication returns the specified user without any additional checks or other actions.

The following code snippet illustrates these steps:

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_ 

# [C#](#tab/tabid-csharp-1)

```csharp{6-20}
services.AddXaf(Configuration, builder => {
    // ...
    builder.Security
        .AddPasswordAuthentication(options => {
            options.IsSupportChangePassword = true;
            options.Events.OnAuthenticate += context => {
                ApplicationUser applicationUser = 
                    context.ObjectSpace.FirstOrDefault<ApplicationUser>(e => e.UserName == context.LogonParameters.UserName);
                if (applicationUser == null)
                    throw new AuthenticationException(
                        context.LogonParameters.UserName, 
                        SecurityExceptionLocalizer.GetExceptionMessage(SecurityExceptionId.RetypeTheInformation)
                    );
                if (!((IAuthenticationStandardUser)applicationUser).ComparePassword(context.LogonParameters.Password))
                    throw new AuthenticationException(
                        context.LogonParameters.UserName, 
                        SecurityExceptionLocalizer.GetExceptionMessage(SecurityExceptionId.RetypeTheInformation)
                    );
                context.User = applicationUser;
            };
        });
        // ...
});
```
***