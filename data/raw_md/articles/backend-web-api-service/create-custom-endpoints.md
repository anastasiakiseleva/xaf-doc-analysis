---
uid: "403858"
title: 'Create Custom Endpoints'
seealso: 
- linkId: "403861"
- linkId: "403715"
---

# Create Custom Endpoints

Follow the steps below to implement custom endpoints for the [Web API Service](xref:403394):

1. Right-click the Web API Service project in the Visual Studio Solution Explorer and select **Add | New Item** in the context menu. Choose the **API Controller – Empty** template in the invoked window.

    ![Add API Controller](~/images/add-api-controller.png)

2. Add custom endpoint methods to the new Controller (_Get_, _Post_, _Put_, and _Delete_ methods in the code sample below).

3. If you wish to use Web API authentication, decorate the new Controller with the @Microsoft.AspNetCore.Authorization.AuthorizeAttribute. See the following topic for more information on how to configure authentication: [](xref:403413). 

The Controller's code:

# [C#](#tab/tabid-csharp)
 
```csharp
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace MainDemo.Blazor.Server.Controllers;
[Route("api/[controller]")]
[ApiController]
[Authorize]
public class CustomEndpointController : ControllerBase {
    [HttpGet]
    public IEnumerable<string> Get() {
        return new string[] { "value1", "value2" };
    }

    [HttpGet("{id}")]
    public string Get(int id) {
        return "value";
    }

    [HttpPost]
    public void Post([FromBody] string value) {
    }

    [HttpPut("{id}")]
    public void Put(int id, [FromBody] string value) {
    }

    [HttpDelete("{id}")]
    public void Delete(int id) {
    }
}

```

***
The result in the [Swagger UI](xref:404281#use-the-swagger-ui-to-test-the-web-api):

![|Web API Custom Endpoint](~/images/custom-endpoint-1.png)

## Authorize Endpoint Requests

Decorate a controller or its actions with the [AuthorizeAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authorization.authorizeattribute) to restrict access. Only authenticated users will have access permissions. `AuthorizeAttribute` is **mandatory** if a controller action accesses services that use the Security System (for example [](xref:DevExpress.ExpressApp.IObjectSpaceFactory) or [](xref:DevExpress.ExpressApp.Security.ISecurityProvider)). In such instances, we recommend that you decorate the entire controller with the `AuthorizeAttribute` to avoid faulty behavior:

# [C#](#tab/tabid-csharp)

```csharp{9,14-15}
using DevExpress.ExpressApp.Core;
using DevExpress.ExpressApp.Security;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace MainDemo.Blazor.Server.Controllers;
[ApiController]
[Route("api/[controller]")]
[Authorize]
public class CustomEndPointController : ControllerBase {
    private readonly ISecurityProvider _securityProvider;
    private readonly IObjectSpaceFactory _securedObjectSpaceFactory;
    public CustomEndPointController(ISecurityProvider securityProvider, IObjectSpaceFactory securedObjectSpaceFactory) {
        _securityProvider = securityProvider;
        _securedObjectSpaceFactory = securedObjectSpaceFactory;
    }
    // ...
}
```
***

>[!NOTE]
>
> If an endpoint does not access any secured services, you can skip the `AuthorizeAttribute` and make the endpoint available to unauthenticated users. Refer to the [Non-Secured Endpoint Examples](#non-secured-endpoint-examples) section for examples on how to implement endpoints that can work without authentication.

Be sure to apply the `AuthorizeAttribute` in the following cases:

- **You run a standalone Web API Service and access a secured service in a controller action.** 
    When the code accesses the service, XAF Security System attempts to authenticate the user even if the `AuthorizeAttribute` is not used. This operation will fail with an exception if the request does not contain an authentication header.

- **JWT-based authentication is not the default authentication method in your application.** 
    For example, this is the case if you use Web API Service as a part of an XAF Blazor application, where the default authentication method is cookie-based. When a controller action without the `AuthorizeAttribute` accesses a secured service, the ASP.NET Core authentication system attempts to authenticate a user with the default method (a cookie). In this case, the XAF Security System throws an exception even if an authentication header is specified, because the ASP.NET Core authentication system failed to authenticate the user based on a cookie. However, if you specify the `AuthorizeAttribute`, the ASP.NET Core authorization system tries all available authentication methods, so it handles JWT authentication correctly.

See the [Secured Endpoint Examples](#secured-endpoint-examples) section for examples of custom endpoints that require the `AuthorizeAttribute`.

## Access an Object Space

Use one of the following techniques to access an Object Space from a custom endpoint controller:

### Use IDataService (Recommended)

Inject the `IDataService` and call its `GetObjectSpace` method to obtain a _secured_ Object Space instance for the specified type:

# [C#](#tab/tabid-csharp)

```csharp{10-11,16}
using DevExpress.ExpressApp.WebApi.Services;
using MainDemo.Module.BusinessObjects;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace MainDemo.Blazor.Server.Controllers;
[ApiController]
[Route("api/[controller]")]
public class CustomEndpointController : ControllerBase {
    private readonly IDataService dataService;
    public CustomEndpointController(IDataService dataService) => this.dataService = dataService;
    
    [HttpGet(nameof(MyEndpoint))]
    [Authorize]
    public ActionResult MyEndpoint() {
        var objectSpace = dataService.GetObjectSpace(typeof(Employee));
        // ...
    }
}
```
***

You do not need to dispose an Object Space obtained from the `IDataService`. This service manages Object Spaces internally and disposes of them automatically.

### Use IObjectSpaceFactory

If your scenario requires you to create a new Object Space instance, use the [IObjectSpaceFactory.CreateObjectSpace](xref:DevExpress.ExpressApp.IObjectSpaceFactory.CreateObjectSpace(System.Type)) method. Note that you need to correctly dispose of Object Spaces returned by this method:

# [C#](#tab/tabid-csharp)

```csharp{11,13,34-39}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Core;
using MainDemo.Module.BusinessObjects;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace MainDemo.Blazor.Server.Controllers;
[ApiController]
[Route("api/[controller]")]
public class CustomEndpointController : ControllerBase, IDisposable {
    private readonly IObjectSpaceFactory securedObjectSpaceFactory;
    private readonly List<IObjectSpace> objectSpaces = new List<IObjectSpace>();
    public CustomEndpointController(IObjectSpaceFactory securedObjectSpaceFactory) => this.securedObjectSpaceFactory = securedObjectSpaceFactory;

    [HttpGet(nameof(MyEndpoint))]
    [Authorize]
    public ActionResult MyEndpoint() {
        var objectSpace = GetObjectSpace(typeof(Employee));
        //...
    }
    protected virtual IObjectSpace GetObjectSpace(Type objectType) {
        if(objectSpaces.Count > 0) {
            foreach(var os in objectSpaces) {
                if(os.IsKnownType(objectType)) {
                    return os;
                }
            }
        }
        IObjectSpace objectSpace = securedObjectSpaceFactory.CreateObjectSpace(objectType);
        objectSpaces.Add(objectSpace);
        return objectSpace;
    }

    public void Dispose() {
        foreach(var os in objectSpaces) {
            os?.Dispose();
        }
        objectSpaces.Clear();
    }
}
```
***

In the code sample above, the controller class implements `IDisposable` and disposes of all created Object Spaces in the `Dispose` method. We recommend this approach in most cases. 

Note that it is often incorrect to create Object Spaces in a `using` block. In these cases, objects returned by a controller action outlive the Object Space that returned them. If these objects implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface and try to access the Object Space in one of their property getters, an exception occurs when an ASP.NET Core serializer attempts to serialize an object.

## Non-Secured Endpoint Examples

### Get Server Time

To check the server's current time across different time zones, use a `GET` request as shown below. You can optionally decorate this controller action with the [AuthorizeAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authorization.authorizeattribute) to restrict this operation to authenticated users only.

# [C#](#tab/tabid-csharp)

```csharp
[HttpGet("api/Custom/ServerTime/{timezone}")]
// [Authorize]
public ActionResult<string> GetServerTime(string timezone) {
    try {
        TimeZoneInfo tz = TimeZoneInfo.FindSystemTimeZoneById(timezone);
        DateTime serverTime = TimeZoneInfo.ConvertTimeFromUtc(DateTime.UtcNow, tz);
        return Ok($"Server time in {timezone}: {serverTime}");
    }
    catch (TimeZoneNotFoundException) {
        return BadRequest($"Invalid timezone: {timezone}");
    }
}
```
***

### Clear Logs

Use a `POST` request to clear logs stored on the server machine. The [AuthorizeAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authorization.authorizeattribute) can restrict this operation to authenticated users only.

# [C#](#tab/tabid-csharp)

```csharp
[HttpPost(nameof(ClearLogs))]
// [Authorize]
[SwaggerOperation("Clears logs older than today")]
public IActionResult ClearLogs() {
    try {
        var logDirectory = @"C:\path\to\your\logs";
        var di = new DirectoryInfo(logDirectory);
        foreach (var file in di.GetFiles()) {
            if (file.CreationTime < DateTime.Today) {
                file.Delete();
            }
        }
        return Ok(new { status = "Logs older than today have been deleted successfully" });
    }
    catch (Exception e){
        return BadRequest(e);
    }
}
```
***

### Check the Database Connection Health

To check the health of the Web API Service application's database connection, use a `GET` request. For this operation, you can use the [](xref:DevExpress.ExpressApp.INonSecuredObjectSpaceFactory) service, which operates outside of the Security System and does not require user authentication.

# [C#](#tab/tabid-csharp)

```csharp
[ApiController]
[Route("api/[controller]")]
public class CustomController : ControllerBase {
    private readonly INonSecuredObjectSpaceFactory _nonSecuredObjectSpaceFactory;
    public CustomController(INonSecuredObjectSpaceFactory nonSecuredObjectSpaceFactory) => _nonSecuredObjectSpaceFactory = nonSecuredObjectSpaceFactory;

    [HttpGet(nameof(DbConnectionHealthCheck))]
    [SwaggerOperation("Returns the current database connection health")]
    // [Authorize]
    public IActionResult DbConnectionHealthCheck() {
        try {
            using var objectSpace = _nonSecuredObjectSpaceFactory.CreateNonSecuredObjectSpace(typeof(ApplicationUser));
            return Ok(new { status = "Healthy" });
        }
        catch (Exception e) {
            return StatusCode(500,e.Message);
        }      
    }
}
```
***

## Secured Endpoint Examples

### Current User Identifier

Use a `GET` request to obtain the current user's ID. This operation requires the [](xref:DevExpress.ExpressApp.Security.ISecurityProvider) service.
  
# [C#](#tab/tabid-csharp)

```csharp
[ApiController]
[Route("api/[controller]")]
public class CustomController : ControllerBase {
    private readonly ISecurityProvider _securityProvider;
    public CustomController(ISecurityProvider securityProvider) => _securityProvider = securityProvider;

    [HttpGet()]
    [SwaggerOperation("Returns the current user's identifier")]
    [Authorize]
    public IActionResult GetUserId() 
        => Ok(_securityProvider.GetSecurity().UserId);
}
```
***

### Obtain an Object or a Collection of Objects

Use a `GET` request to fetch a serialized business object. You can return an anonymous object with an arbitrary structure from the controller action to control which data to include in the response. This operation uses the `IDataService` and takes Security System configuration into account .

# [C#](#tab/tabid-csharp)

```csharp
[ApiController]
[Route("api/[controller]")]
public class CustomController : ControllerBase {
    private readonly IObjectSpace objectSpace;
    public CustomController(IDataService dataService) {
         objectSpace = dataService.GetObjectSpace(typeof(Employee));
    }

    [HttpGet(nameof(Employee)+"/{id}")]
    [SwaggerOperation("Returns an Employee object based on its ID")]
    [Authorize]
    public ActionResult GetEmployee(int id) {
        var employee = objectSpace.GetObjectByKey<Employee>(id);
        return employee == null ? NotFound($"Employee ({id}) not found.") : Ok (new {employee.EmployeeId,employee.DepartmentName});
    }

    [HttpGet(nameof(Employee)+"/{department}")]
    [SwaggerOperation("Returns all Employees in the specified department")]
    [Authorize]
    public ActionResult GetEmployees(string department) {
        return Ok(objectSpace.GetObjectsQuery<Employee>()
        .Select(employee => new { employee.EmployeeId, employee.DepartmentName })
            .Where(employee => employee.DepartmentName == department));
    }
}
```
***

> [!NOTE]
> DevExpress Web API Service automatically exposes similar actions used to _create_, _read_, _delete_, and _update_ a business object if this object is registered as a part of the OData model in the application's _Startup.cs_ file:
> 
> ```csharp
> services.AddXafWebApi(builder => {
>    builder.ConfigureOptions(options => {
>        options.BusinessObject<Employee>()
> ```
>
> For information on how to override the logic implemented for these default endpoints, see [Execute Custom Operations on Endpoint Requests](xref:403850).

### Stream an Image

Use a `GET` request to stream an image from a byte array field. You can use the same technique to return a file of any type from an arbitrary source.

# [C#](#tab/tabid-csharp)

```csharp
[HttpGet("EmployeePhoto/{employeeId}")]
[Authorize]
public FileStreamResult EmployeePhoto(int employeeId) {
    var objectSpace = dataService.GetObjectSpace(typeof(Employee));
    var bytes = objectSpace.GetObjectByKey<Employee>(employeeId).Photo;
    return File(new MemoryStream(bytes), "application/octet-stream");
}
```
***

### Create a New Object

To create an object, use a `POST` request. This operation uses the [](xref:DevExpress.ExpressApp.Security.ISecurityProvider) service to obtain permission to create objects of the specified type and the `IDataService` to create objects.
  
# [C#](#tab/tabid-csharp)

```csharp
[ApiController]
[Route("api/[controller]")]
public class CustomController : ControllerBase {
    private readonly IDataService _dataService;
    private readonly ISecurityProvider _securityProvider;
    public CustomController(IDataService dataService, ISecurityProvider securityProvider) {
        _dataService = dataService;
        _securityProvider = securityProvider;
    }

    [HttpPost(nameof(CreateUserEmployee)+"/{email}")]
    [SwaggerOperation("Creates a new user based on email")]
    [Authorize]
    public IActionResult CreateUserEmployee(string email) {
        var strategy = (SecurityStrategy)_securityProvider.GetSecurity();
        if (!strategy.CanCreate(typeof(Employee)))
            return Forbid("You do not have permissions to add a new employee!");
        var objectSpace = _dataService.GetObjectSpace(typeof(Employee));
        if (objectSpace.FirstOrDefault<Employee>( e => e.Email == email) != null)
            return ValidationProblem("Email is already registered!");
        var employee = objectSpace.CreateObject<Employee>();
        employee.Email = email;
        objectSpace.CommitChanges();
        return Ok();
    }
}
```
***

### Stream a PDF File

Use a `GET` request to stream a PDF document. The code below illustrates a use case, in which the [Office File API](https://www.devexpress.com/products/net/office-file-api/)'s [Mail Merge](xref:400006) feature is used to dynamically generate a PDF document. The resulting document is then added to the server response.

> [!NOTE]
>
> For more information on this solution and a complete code example, refer to the following blog post: [JavaScript — Consume the DevExpress Backend Web API with Svelte (Part 7. Mail Merge)](https://community.devexpress.com/blogs/news/archive/2023/12/20/javascript-consume-the-devexpress-backend-web-api-with-svelte-part-7-mail-merge.aspx).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Core;
using DevExpress.Persistent.BaseImpl.EF;
using DevExpress.XtraRichEdit;
using DevExpress.XtraRichEdit.API.Native;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Collections;
using System.Net.Mime;

[Authorize]
[Route("api/[controller]")]
public class MailMergeController : ControllerBase, IDisposable {
  private readonly IObjectSpaceFactory objectSpaceFactory;

  public MailMergeController(IObjectSpaceFactory objectSpaceFactory) {
    this.objectSpaceFactory = objectSpaceFactory;
  }

  private IObjectSpace objectSpace;

  public void Dispose() {
    if (objectSpace != null) {
      objectSpace.Dispose();
      objectSpace = null;
    }
  }

  [HttpGet("MergeDocument({mailMergeId})/{objectIds?}")]
  public async Task<object> MergeDocument(
    [FromRoute] string mailMergeId,
    [FromRoute] string? objectIds) {
    // Fetch the mail merge data by the given ID
    objectSpace = objectSpaceFactory.CreateObjectSpace<RichTextMailMergeData>();
    RichTextMailMergeData mailMergeData =
      objectSpace.GetObjectByKey<RichTextMailMergeData>(new Guid(mailMergeId));

    // Fetch the list of objects by their IDs
    List<Guid> ids = objectIds?.Split(',').Select(s => new Guid(s)).ToList();
    IList dataObjects = ids != null
      ? objectSpace.GetObjects(mailMergeData.DataType, new InOperator("ID", ids))
      : objectSpace.GetObjects(mailMergeData.DataType);

    using RichEditDocumentServer server = new();
    server.Options.MailMerge.DataSource = dataObjects;
    server.Options.MailMerge.ViewMergedData = true;
    server.OpenXmlBytes = mailMergeData.Template;

    MailMergeOptions mergeOptions = server.Document.CreateMailMergeOptions();
    mergeOptions.MergeMode = MergeMode.NewSection;

    using RichEditDocumentServer exporter = new();
    server.Document.MailMerge(mergeOptions, exporter.Document);

    MemoryStream output = new();
    exporter.ExportToPdf(output);

    output.Seek(0, SeekOrigin.Begin);
    return File(output, MediaTypeNames.Application.Pdf);
  }
}
```
***

Note that this code uses the `RichTextMailMergeData` type to access persistent document templates. If you intend to use similar code in your application, make sure to add `RichTextMailMergeData` to your DBContext (if using EF Core) and call the [WebApiOptions.BusinessObject](xref:DevExpress.ExpressApp.WebApi.Services.WebApiOptions.BusinessObject``1) method for this type to generate endpoints:

**File**: _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{7}
public class Startup {
  public void ConfigureServices(IServiceCollection services) {
    // ...
    services.AddXafWebApi(builder => {
      builder.ConfigureOptions(options => {
        // ...
        options.BusinessObject<RichTextMailMergeData>();
      });
      // ...
    });
    // ...
  }
}
```
***

## Example Solutions

The following example solutions implement client applications for a Web API Service backend: 

- [Blazor WebAssembly App](https://go.devexpress.com/XAF_Security_NonXAF_Blazor_WebAssembly.aspx)
- [.NET MAUI (iOS/Android) App](https://go.devexpress.com/XAF_Security_NonXAF_MAUI.aspx)

In both solutions, the backend implements several custom endpoints including the following:

`CanCreate`  
:   Checks the current user's permission to create new posts.
`Archive`  
:   Archives the specified post to disk.
`AuthorPhoto`  
:   Responds with a photo of the specified post's author.

Also see our blog post series on how to implement a Svelte app with a custom Web API Service backend: [JavaScript with Svelte + ASP.NET Core Web API/OData App](https://github.com/oliversturm/demo-dx-webapi-js/tree/stage-5).

## SignalR: How to Perform CRUD operations in a Hub Method

The following code snippet demonstrates a [SignalIR Hub class](https://learn.microsoft.com/en-us/aspnet/core/signalr/hubs?view=aspnetcore-9.0) that allows authenticated users to call the `UpdateUserData` method via SignalIR. It uses the user's identity to create an `ObjectSpace` and perform data operations securely:

**File**: _MySolution.WebApi/HubMethod.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Core;
using DevExpress.ExpressApp.Security;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.SignalR;

// Add this attribute to ensure only authenticated users can conned and invoke methods in this hub.
[Authorize]
public class HubMethod : Hub {
    readonly IObjectSpaceFactory objectSpaceFactory;
    readonly SignInManager signInManager;
    public HubMethod(IObjectSpaceFactory objectSpaceFactory, SignInManager signInManager) {
        this.signInManager = signInManager;
        this.objectSpaceFactory = objectSpaceFactory;
    }
    // SignalIR Hub method
    [HubMethodName(nameof(UpdateUserData))]
    public async Task UpdateUserData(string data) {
        // Logs the SignalR connection's Context.User into the XAF security system
        var result = signInManager.SignInByPrincipal(Context.User!);
        if(result.Succeeded) {
            // Creates a new ObjectSpace
            using(var objectSpace = objectSpaceFactory.CreateObjectSpace(typeof(ApplicationUser))) {
                // Add your code here.
            }
        }
    }
}
```
***
