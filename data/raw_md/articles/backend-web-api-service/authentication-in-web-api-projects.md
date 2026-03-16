---
uid: "403413"
title: 'Authenticate and Authorize Web API Endpoints'
owner: Eugenia Simonova
seealso:
- linkId: "402197"
---
# Authenticate and Authorize Web API Endpoints

The **Web API** supports all standard ASP.NET Core [authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication) techniques that you can specify in the _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_) file. See the following topic for more information: [Authentication](xref:119064).

If you use the [Template Kit](xref:405447) to create a **Web API** project, enable authentication in the **Security Options** section:

![Select authentication](~/images/template-kit/template-kit-webAPI-and-securoty-options.png)

Standard (requests login and password)
:   The kit generates [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) authentication scaffolding code for the **Web API**. 

Active Directory (uses Windows account)
:   The kit adds the JWT scaffolding code to the _MySolution.WebApi\appsettings.json_ file and the scaffolding code for Windows Active Directory to the _MySolution.WebApi\Properties\launchSettings.json_ file.

Microsoft Entra ID (formerly Azure Active Directory)
:   The kit adds the JWT and [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) scaffolding code to the _MySolution.WebApi\appsettings.json_ file. 

Middle Tier Security - No direct database access
:   The kit adds the  _MySolution.MiddleTier_ project to the application. Refer to the following help topic for more information: <xref:404389>.

 See the following topics for information on how to configure the authentication scaffolding code and enable authentication:
 * [Configure the JWT Authentication](xref:403504)
 * [Configure the OAuth2 Azure Authentication](xref:403505)

[!include[configure-authorization-for-endpoints](~/templates/configure-authorization-for-endpoints.md)]

## Authenticate a User in Code

XAF supports API that you can use to access and manage application users as well as authenticate users. This API includes the following services:

@DevExpress.ExpressApp.Security.UserManager
:    Exposes API required to manage user objects in the database.
@DevExpress.ExpressApp.Security.SignInManager
:    Exposes API required to sign a user into an application.

The following code snippet demonstrates how to use API that the `UserManager` and `SignInManager` services expose to sign in to a nested scope and execute [custom endpoint](xref:403858) logic on a service user's behalf (user impersonation):

# [C#](#tab/tabid-csharp)

```csharp{27,31}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using MySolution.WebApi.BusinessObjects;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
// ...
namespace MySolution.WebApi {
    [Route("api/[controller]")]
    [ApiController]
    [Authorize]
    public class CustomEndpointController : ControllerBase {
        private readonly IServiceProvider serviceProvider;
        public CustomEndpointController(IServiceProvider serviceProvider) {
            this.serviceProvider = serviceProvider;
        }

        [HttpPost]
        public void Post([FromBody] string value) {
            // ...
            // Create a nested service scope whithin which to establish a separate login session.
            IServiceScopeFactory serviceScopeFactory = serviceProvider.GetRequiredService<IServiceScopeFactory>();
            using (IServiceScope impersonationScope = serviceScopeFactory.CreateScope()) {
                // Use the UserManager to obtain the "ServiceUser" user object.
                using IObjectSpace nonSecuredObjectSpace = impersonationScope.ServiceProvider
                    .GetRequiredService<INonSecuredObjectSpaceFactory>().CreateNonSecuredObjectSpace<ApplicationUser>();
                ApplicationUser serviceUser = impersonationScope.ServiceProvider
                    .GetRequiredService<UserManager>().FindUserByName<ApplicationUser>(nonSecuredObjectSpace, "ServiceUser");

                // Sign in as "ServiceUser" to the nested scope.
                SignInManager signInManager = impersonationScope.ServiceProvider.GetService<SignInManager>();
                signInManager.SignIn(serviceUser);

                // Obtain an Object Space from the nested scope and use this Object Space
                // to manipulate business objects on the "ServiceUser" user's behalf.
                using IObjectSpace objectSpace = impersonationScope.ServiceProvider
                    .GetRequiredService<IObjectSpaceFactory>().CreateObjectSpace<Employee>();
                Employee newEmployee = objectSpace.CreateObject<Employee>();
                newEmployee.Name = value;
                // ...
                objectSpace.CommitChanges();
                // ...
            }
        }
    }
}

```
***

[`UserManager`]: DevExpress.ExpressApp.Security.UserManager
[`SignInManager`]: DevExpress.ExpressApp.Security.UserManager
