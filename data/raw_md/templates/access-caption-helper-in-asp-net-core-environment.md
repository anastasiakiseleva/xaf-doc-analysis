**From a Razor Component**

**File**: _MySolution.Blazor.Server\Pages\MyComponent.razor_.

# [Razor](#tab/tabid-razor)

```Razor{2,12-13}
@page "/MyComponent"
@using DevExpress.ExpressApp.Utils
@inject DevExpress.ExpressApp.Services.Localization.ICaptionHelperProvider captionHelperProvider

<h3>MyComponent</h3>

@code {
    protected override async Task OnAfterRenderAsync(bool firstRender) {
        if (!firstRender) {
            return;
        }
        ICaptionHelper helper = captionHelperProvider.GetCaptionHelper();
        string newActionName = helper.GetActionCaption("New");
        // ...
    }
}
```
***

**From Middleware**

**File**: _MySolution.Blazor.Server\CustomMiddleware.cs_.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.AspNetCore.Services.Localization;
using DevExpress.ExpressApp.Utils;

namespace MySolution.Blazor.Server.Pages {
    public class CustomMiddleware {
        private readonly RequestDelegate next;
        public CustomMiddleware(RequestDelegate next) {
            this.next = next;
        }
        public async Task InvokeAsync(HttpContext context, ICaptionHelperProvider captionHelperProvider) {
            ICaptionHelper helper = captionHelperProvider.GetCaptionHelper();
            string newActionName = helper.GetActionCaption("New");
            // ...
            await next(context);
        }
    }
}
```
***

**From an ASP.NET Core Controller**

**File**: _MySolution.Blazor.Server.Controllers\CustomLocalizationController.cs_.

# [C#](#tab/tabid-csharp)
```csharp{7,13}
using DevExpress.ExpressApp.AspNetCore.Services.Localization;
using DevExpress.ExpressApp.Utils;
using Microsoft.AspNetCore.Mvc;

namespace MySolution.Blazor.Server.Controllers {
    public class CustomLocalizationController : ControllerBase {
        internal ICaptionHelperProvider captionHelperProvider;
        public CustomLocalizationController(ICaptionHelperProvider captionHelperProvider) {
            this.captionHelperProvider = captionHelperProvider;
        }
        [HttpGet]
        public string GetActionCaption(string actionName) {
            ICaptionHelper helper = captionHelperProvider.GetCaptionHelper();
            return helper.GetActionCaption(actionName);
        }
    }
}
```
***
