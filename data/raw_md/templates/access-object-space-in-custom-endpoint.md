# [C#](#tab/tabid-csharp) 
 
```csharp{18}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Core;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.OData.Routing.Controllers;

namespace MySolution.WebApi {
    [Route("api/[controller]")]
    [ApiController]
    [Authorize]
    public class CustomEndpointController : ControllerBase {
        IObjectSpaceFactory objectSpaceFactory;
        public CustomEndpointController(IObjectSpaceFactory objectSpaceFactory) {
            this.objectSpaceFactory = objectSpaceFactory;
        }
        [HttpGet]
        public IActionResult Get() {
            using IObjectSpace newObjectSpace = objectSpaceFactory.CreateObjectSpace<Contact>();
            // ...
            return Ok();
        }
        //...
    }
}
```
***