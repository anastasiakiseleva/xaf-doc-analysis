# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.AspNetCore.Services.Localization;
using DevExpress.ExpressApp.Utils;
using Microsoft.AspNetCore.Mvc;

namespace MySolutionName.Module.Blazor.Controllers {
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
