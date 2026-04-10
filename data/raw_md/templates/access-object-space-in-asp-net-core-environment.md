### From a Razor Component

**File:** _MySolution.Blazor.Server\Pages\MyComponent.razor_.

# [Razor](#tab/tabid-razor)

```Razor{2,12-13}
@page "/MyComponent"
@inject DevExpress.ExpressApp.IObjectSpaceFactory objectSpaceFactory

<h3>MyComponent</h3>

@code {
    protected override async Task OnAfterRenderAsync(bool firstRender) {
        if (!firstRender) {
            return;
        }
        try {
            using(IObjectSpace objectSpace = objectSpaceFactory.CreateObjectSpace<Contact>()) {
                // ...
            }
        }
        catch(Exception ex) {
            // User authentication has failed.
            // ...
        }
    }
}
```
***

### From Middleware

**File:** _MySolution.Blazor.Server\CustomMiddleware.cs_.

# [C#](#tab/tabid-csharp)

```csharp{12-17}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Core;
using Microsoft.AspNetCore.Http;
using System.Threading.Tasks;

namespace MySolution.Blazor.Server {
    public class CustomMiddleware {
        private readonly RequestDelegate next;
        public CustomMiddleware(RequestDelegate next) {
            this.next = next;
        }
        public async Task InvokeAsync(HttpContext context, IObjectSpaceFactory objectSpaceFactory) {
            try {
                using(IObjectSpace objectSpace = objectSpaceFactory.CreateObjectSpace<Contact>()) {
                    // ...
                }
            }
            catch(Exception ex) {
                // User authentication is failed.
                // ...
            }
            await next(context);
        }
    }
}
```
***

### From an ASP.NET Core Controller

**File**: _MySolution.Blazor.Server.Controllers\CustomController.cs_.

# [C#](#tab/tabid-csharp)
```csharp{8,14}
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Core;
using Microsoft.AspNetCore.Mvc;

namespace MySolution.Blazor.Server.Controllers {
    public class CustomController : ControllerBase {
        internal IObjectSpaceFactory objectSpaceFactory;
        public CustomController(IObjectSpaceFactory objectSpaceFactory) {
            this.objectSpaceFactory = objectSpaceFactory;
        }
        [HttpGet]
        public object GetUserObject(string userName) {
            using (IObjectSpace objectSpace = objectSpaceFactory.CreateObjectSpace<ApplicationUser>()) {
                ApplicationUser user = objectSpace.FindObject<ApplicationUser>(
                    CriteriaOperator.FromLambda<ApplicationUser>(u => u.UserName == userName));
                // ...
            }
        }
    }
}
```
***
