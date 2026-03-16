---
uid: DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnFindUser
name: OnFindUser
type: Property
summary: Specifies custom logic used to find a user object.
syntax:
  content: public Action<FindUserContext> OnFindUser { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.Security.FindUserContext}
    description: A delegate method that implements custom logic.
seealso: []
---

Handle this event to implement custom logic used to find a user object. In the event handler, if the user object is found, assign this object to the `context.User` property. After that, the XAF authentication system carries out all checks required for standard password-based authentication.

> [!NOTE]
>
> In contrast to the `OnFindUser` event, the [OnAuthenticate](xref:DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnAuthenticate) event completely overrides the authentication logic and requires you to implement all checks manually. Use this event for deeper customization of authentication behavior (for example, to implement authentication based on custom logon parameters).  

The following code snippet demonstrates how to use the `OnFindUser` event:

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_ 

# [C#](#tab/tabid-csharp-1)

```csharp{6-10}
services.AddXaf(Configuration, builder => {
    // ...
    builder.Security
        .AddPasswordAuthentication(options => {
            options.IsSupportChangePassword = true;
            options.Events.OnFindUser += context => { 
                context.User = context.ObjectSpace.FirstOrDefault<ApplicationUser>(
                    x => x.UserName == context.LogonParameters.UserName
                ); 
            };
        });
        // ...
});
```
***
