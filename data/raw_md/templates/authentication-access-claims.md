You can use one of the following techniques to access claims from an ASP.NET Core Blazor application's code at runtime:

- Use the `DevExpress.ExpressApp.Security.IPrincipalProvider` service's `User.Claims` property.
- In an MVC controller, you can use the controller's `User.Claims` property. In middleware, use the HttpContext's `context.User.Claims` property.

The code sample below demonstrates how to implement a [custom Controller](xref:112676) that injects the `IPrincipalProvider` service and uses it to access claims:

**File:** _MySolution.Blazor.Server\Controllers\MyController.cs_

# [C#](#tab/tabid-csharp)

```csharp{7,13-18}
using System.Security.Claims;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;

namespace MainDemo.Blazor.Server.Controllers {
    public class MyController : ViewController {
        readonly IPrincipalProvider principalProvider;

        public MyController() { }

        [ActivatorUtilitiesConstructor]
        public MyController(IServiceProvider serviceProvider) : this() {
            principalProvider = serviceProvider.GetRequiredService<IPrincipalProvider>();
            var _claimsPrincipal = (ClaimsPrincipal)principalProvider.User;
            var customClaim = _claimsPrincipal.FindFirst(c => c.Type == "CustomClaim");
            if(customClaim != null && customClaim.Value == "ClaimValue") {
                Active.SetItemValue("CustomClaim", false);
            }
        }
    }
}
```
***