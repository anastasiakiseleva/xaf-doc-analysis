# [C#](#tab/tabid-csharp) 
```csharp{19-20}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.OData.Routing.Controllers;
using MySolution.Module.BusinessObjects;

namespace MySolution.WebApi {
    [Route("api/[controller]")]
    [ApiController]
    [Authorize]
    public class CustomEndpointController : ControllerBase {
        ISecurityProvider securityProvider;
        public CustomEndpointController(ISecurityProvider securityProvider) {
            this.securityProvider = securityProvider;
        }
        [HttpGet]
        public IActionResult Get() {
            ISecurityStrategyBase security = securityProvider.GetSecurity();
            var userId = security.UserId; 
            // ...
            return Ok();
        }
        //...
    }
}
```
***