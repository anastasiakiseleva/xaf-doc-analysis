**From Middleware**

**File**: _MySolution.Blazor.Server\CustomMiddleware.cs_.

# [C# (ISecurityProvider)](#tab/tabid-csharp-ISecurityProvider)
```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using Microsoft.AspNetCore.Http;
using System.Threading.Tasks;

namespace MySolution.Blazor.Server {	
    public class CustomMiddleware {
        private readonly RequestDelegate next;
        public CustomMiddleware(RequestDelegate next) {
            this.next = next;
        }
        public async Task InvokeAsync(HttpContext context, ISecurityProvider securityProvider) {
            try {
                ISecurityStrategyBase securityStrategy = securityProvider.GetSecurity();
                // If authentication has failed, GetSecurity throws an exception.
                ApplicationUser user = (ApplicationUser)securityStrategy.User;
            	// ...
            }
            catch(Exception ex) {
                // User authentication has failed.
                // ...
            }
            await next(context);
        }
    }
}
```
# [C# (ISecurityStrategyBase)](#tab/tabid-csharp-ISecurityStrategyBase)
```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using Microsoft.AspNetCore.Http;
using System.Threading.Tasks;

namespace MySolution.Blazor.Server {
    public class CustomMiddleware {
        private readonly RequestDelegate next;
        public CustomMiddleware(RequestDelegate next) {
            this.next = next;
        }
        public async Task InvokeAsync(HttpContext context, ISecurityStrategyBase securityStrategy) {
            bool isAuthenticated = securityStrategy.IsAuthenticated;
            ApplicationUser user = (ApplicationUser)securityStrategy.User;
            // ...
            await next(context);
        }
    }
}
```
***

**From a Razor Component**

**File:** _MySolution.Blazor.Server\Pages\MyComponent.razor_.

# [Razor (ISecurityProvider)](#tab/tabid-razor-ISecurityProvider)

```Razor{4-5,15-17}
@page "/MyComponent"
@using DevExpress.ExpressApp
@using DevExpress.ExpressApp.Security
@inject DevExpress.ExpressApp.Security.ISecurityStrategyBase securityStrategy
@inject DevExpress.ExpressApp.Security.ISecurityProvider securityProvider

<h3>MyComponent</h3>

@code {
    protected override async Task OnAfterRenderAsync(bool firstRender) {
        if (!firstRender) {
            return;
        }
        try {
            securityStrategy = securityProvider.GetSecurity();
            // If authentication has failed, GetSecurity throws an exception.
            ApplicationUser user = (ApplicationUser)securityStrategy.User;
        }
        catch (Exception ex) {
            // User authentication has failed.
            // ...
        }
    }
}
```
# [Razor (ISecurityStrategyBase)](#tab/tabid-razor-ISecurityStrategyBase)

```Razor{4,13-14}
@page "/MyComponent"
@using DevExpress.ExpressApp
@using DevExpress.ExpressApp.Security
@inject DevExpress.ExpressApp.Security.ISecurityStrategyBase securityStrategy

<h3>MyComponent</h3>

@code {
    protected override async Task OnAfterRenderAsync(bool firstRender) {
        if (!firstRender) {
            return;
        }
        bool isAuthenticated = securityStrategy.IsAuthenticated;
        ApplicationUser user = (ApplicationUser)securityStrategy.User;
    }
}
```
***

**From an ASP.NET Core Controller**

**File**: _MySolution.Blazor.Server.Controllers\CustomController.cs_.

# [C# (ISecurityProvider)](#tab/tabid-csharp-ISecurityProvider)
```csharp
using Microsoft.AspNetCore.Mvc;
using DevExpress.ExpressApp.Security;

namespace MySolution.Blazor.Server.Controllers {
    public class CustomController : ControllerBase {
        internal ISecurityProvider securityProvider;
        public CustomController(ISecurityProvider securityProvider) {
            this.securityProvider = securityProvider;
        }
        [HttpGet]
        public object GetUserObject() {
            ISecurityStrategyBase securityStrategy = securityProvider.GetSecurity();
            // If authentication has failed, GetSecurity throws an exception.
            ApplicationUser user = (ApplicationUser)securityStrategy.User;
            // ...
        }
    }
}

```
# [C# (ISecurityStrategyBase)](#tab/tabid-csharp-ISecurityStrategyBase)
```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using Microsoft.AspNetCore.Http;
using System.Threading.Tasks;

namespace MySolution.Blazor.Server {
    public class CustomMiddleware {
        private readonly RequestDelegate next;
        public CustomMiddleware(RequestDelegate next) {
            this.next = next;
        }
        public async Task InvokeAsync(HttpContext context, ISecurityStrategyBase securityStrategy) {
            bool isAuthenticated = securityStrategy.IsAuthenticated;
            ApplicationUser user = (ApplicationUser)securityStrategy.User;
            // ...
            await next(context);
        }
    }
}
```
***
