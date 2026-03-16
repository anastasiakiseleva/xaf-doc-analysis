---
uid: DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnUserValidated
name: OnUserValidated
type: Property
summary: Specifies custom logic used to implement additional validation checks that run after the standard checks succeed.
syntax:
  content: public Action<ValidateUserContext> OnUserValidated { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.Security.ValidateUserContext}
    description: A delegate method that implements custom logic.
seealso: []
---

Use this event to implement additional user validation logic on top of the standard validation checks. The specified validation logic runs after the standard checks succeed. If validation fails, assign an `AuthenticationException` to the `context.ValidationError` property.

> [!IMPORTANT]
>
> Do not throw an exception directly from the handler method. This can lead to faulty behavior.

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_ 

The following code snippet demonstrates how to use the `OnUserValidated` event:

# [C#](#tab/tabid-csharp-1)

```csharp{6-10}
services.AddXaf(Configuration, builder => {
    // ...
    builder.Security
        .AddPasswordAuthentication(options => {
            options.IsSupportChangePassword = true;
            options.Events.OnUserValidated += context => { 
                if(((CustomLogonParameters)context.LogonParameters).CustomData == "FAIL") { 
                    context.ValidationError = new AuthenticationException(context.User.UserName); 
                }
            };
        });
        // ...
});
```
***

