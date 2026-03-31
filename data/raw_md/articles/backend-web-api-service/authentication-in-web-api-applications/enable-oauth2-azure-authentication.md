---
uid: "403505"
title: 'Configure the OAuth2 Azure Authentication for the Web API'
seealso:
- linkType: HRef
  linkId: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
  altText: Microsoft identity platform and OAuth 2.0 authorization code flow
- linkId: "402197"  
---
# Configure the OAuth2 Azure Authentication for the Web API

The **Web API** supports the OAuth2 Azure Authentication. To use it, [set up](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant) a Microsoft Entra (Azure AD) tenant. After you obtain a tenant, [register](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) the **Web API** with the Microsoft identity platform. When you configure platform settings for the **Web API**, select _Single-page application_ as the **Web application** type and set the following **Redirect URI**: _https://localhost:44318/swagger/oauth2-redirect.html_.

## Enable Authentication in a New Project 

Use the [Template Kit](xref:405447) to create a **Web API** project. Enable the **Microsoft Entra ID (formerly Azure Active Directiry)** in the **Security Options** section:

![Select authentication](~/images/template-kit/template-kit-security-entra-id.png)

The wizard generates [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) authentication scaffolding code.

Update the generated code as follows:

1. Specify your [Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant) settings in the _"Authentication"_ section of the _appsettings.json_ file:

    **File:** _MySolution.WebApi\appsettings.json_ (_MySolution.Blazor.Server\appsettings.json_)
    # [JSON](#tab/tabid-json)
    ```JSON
    // ...
    "Authentication": {
        // ...
        "AzureAd": {
            "Instance": "https://login.microsoftonline.com/",
            "Domain": "abcdabcd-abcd-abcd-abcd-abcdabcdabcd", // This value is an example - replace it with your tenant domain.
            "TenantId": "organizations", // Use 'common', 'organizations', or the tenant Id obtained from the Azure portal. 
            "ClientId": "11111111-1111-1111-1111-111111111111", // This value is an example - replace it with your client Id (application ID obtained from the Azure portal).
            "CallbackPath": "/signin-oidc"
        }
    },    
    // ...
    ```
    ***

2. Configure scopes according to your Azure settings. See the following topic for details: [Quickstart: Configure an application to expose a web API](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-expose-web-apis).

    **File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
    # [C#](#tab/tabid-csharp)

    ```csharp{3,4}
        AuthorizationCode = new OpenApiOAuthFlow() {
            // ...
            Scopes = new Dictionary<string, string> {
                { "api://11111111-1111-1111-1111-111111111111/WebApi", "Read WebApi"} 
            }
        }
    ```
    ***

3. In the `options.Events.OnAuthenticated` delegate, implement the authentication logic. The auto-generated code maps an OAuth provider user to an application user. If this code suits your requirements, comment out `return`. 

    See the following topic for more information: [How to: Use Active Directory and OAuth2 Authentication Providers in ASP.NET Core Blazor Applications](xref:402197#google-azure-and-github-providers).

    **File:** _MySolution.Blazor.Server\Startup.cs_ (_MySolution.Blazor.Server\Startup.json_)
    # [C#](#tab/tabid-csharp)

    ```csharp{3}
    options.Events.OnAuthenticated = (externalAuthenticationContext) => {
        // When a user successfully logs in with an OAuth provider, you can get their unique user key.
        //return;
        if (externalAuthenticationContext.AuthenticatedUser == null &&
        externalAuthenticationContext.Principal.Identity.AuthenticationType != SecurityDefaults.PasswordAuthentication &&
        externalAuthenticationContext.Principal.Identity.AuthenticationType != SecurityDefaults.WindowsAuthentication && !(externalAuthenticationContext.Principal is WindowsPrincipal)) {
            const bool autoCreateUser = true;
        // ...
        }
    ```
    ***

See the following section for information on how to test the OAuth2 Azure authentication: [Use the Swagger UI to Test the OAuth2 Azure Authentication](#use-the-swagger-ui-to-test-the-oauth2-azure-authentication).    
## Enable Authentication in an Existing Project

Follow the steps below to add the OAuth2 Azure authentication to an existing **Web API** or **Blazor Server** project. 
### Step 1. Install the Required NuGet Packages
 
Install the following NuGet Packages:
- **DevExpress.ExpressApp.Security.Xpo** - to the _MySolution.WebApi_ and _MySolution.Module_ projects;
- **Microsoft.Identity.Web.UI** - to _MySolution.WebApi_. 

See the following topic for details: [](xref:116042). 
### Step 2. Modify appsettings.json

Add the **AzureAd** option to the **Authentication** section in the _appsettings.json_ file and specify your Azure AD credentials.

**File:** _MySolution.WebApi\appsettings.json_ (_MySolution.Blazor.Server\appsettings.json_)
# [JSON](#tab/tabid-json)
```JSON
// ...
"Authentication": {
    "AzureAd": {
        "Instance": "https://login.microsoftonline.com/",
        "Domain": "abcdabcd-abcd-abcd-abcd-abcdabcdabcd", // This value is an example, replace it with your tenant domain.
        "TenantId": "organizations", // Use 'common', 'organizations', or the tenant Id obtained from the Azure portal.
        "ClientId": "11111111-1111-1111-1111-111111111111", // This value is an example, replace it with your client Id (application ID obtained from the Azure portal).
        "CallbackPath": "/signout-oidc"
    }
},    
// ...
```
***
### Step 3. Modify Startup.cs

Add the following code to the **ConfigureServices** method to enable authentication:

 **File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
# [C#](#tab/tabid-csharp)
 
```csharp
// ...
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using DevExpress.ExpressApp;
using System.Security.Claims;
using Microsoft.Identity.Web;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.Extensions.DependencyInjection;
using System.Security.Principal;
// ...
public void AddXafAspNetCoreSecurity(Configuration,IServiceCollection services) {
    // ...
    services.AddXafAspNetCoreSecurity(Configuration, options => {
        options.RoleType = typeof(PermissionPolicyRole);
        options.UserType = typeof(MySolution.Module.BusinessObjects.ApplicationUser);
        options.UserLoginInfoType = typeof(MySolution.Module.BusinessObjects.ApplicationUserLoginInfo);
        options.Events.OnSecurityStrategyCreated = securityStrategy => ((SecurityStrategy)securityStrategy).RegisterXPOAdapterProviders();
        options.SupportNavigationPermissionsForTypes = false;
    })
    .AddAuthenticationStandard(Configuration, options => {
        options.IsSupportChangePassword = true;
    })
    .AddExternalAuthentication(options => {
        options.Events.OnAuthenticated = (externalAuthenticationContext) => {
            // When a user successfully logs in with an OAuth provider, you can get their unique user key.
            //return;
            if(externalAuthenticationContext.AuthenticatedUser == null &&
            externalAuthenticationContext.Principal.Identity.AuthenticationType != SecurityDefaults.PasswordAuthentication &&
            externalAuthenticationContext.Principal.Identity.AuthenticationType != SecurityDefaults.WindowsAuthentication && !(externalAuthenticationContext.Principal is WindowsPrincipal)) {
                const bool autoCreateUser = true;

                IObjectSpace objectSpace = externalAuthenticationContext.LogonObjectSpace;
                ClaimsPrincipal externalUser = (ClaimsPrincipal)externalAuthenticationContext.Principal;

                var userIdClaim = externalUser.FindFirst("sub") ?? externalUser.FindFirst(ClaimTypes.NameIdentifier) ?? throw new InvalidOperationException("Unknown user id");
                string providerUserId = userIdClaim.Value;

                var userLoginInfo = FindUserLoginInfo(externalUser.Identity.AuthenticationType, providerUserId);
                if(userLoginInfo != null || autoCreateUser) {
                    externalAuthenticationContext.AuthenticatedUser = userLoginInfo?.User ?? CreateApplicationUser(externalUser.Identity.Name, providerUserId);
                }

                object CreateApplicationUser(string userName, string providerUserId) {
                    if(objectSpace.FirstOrDefault<MySolution.Module.BusinessObjects.ApplicationUser>(user => user.UserName == userName) != null) {
                        throw new ArgumentException($"The username ('{userName}') was already registered within the system");
                    }
                    var user = objectSpace.CreateObject<MySolution.Module.BusinessObjects.ApplicationUser>();
                    user.UserName = userName;
                    user.SetPassword(Guid.NewGuid().ToString());
                    user.Roles.Add(objectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default"));
                    ((ISecurityUserWithLoginInfo)user).CreateUserLoginInfo(externalUser.Identity.AuthenticationType, providerUserId);
                    objectSpace.CommitChanges();
                    return user;
                }
                ISecurityUserLoginInfo FindUserLoginInfo(string loginProviderName, string providerUserId) {
                    return objectSpace.FirstOrDefault<MySolution.Module.BusinessObjects.ApplicationUserLoginInfo>(userLoginInfo =>
                                        userLoginInfo.LoginProviderName == loginProviderName &&
                                        userLoginInfo.ProviderUserKey == providerUserId);
                }
            }
        };
    });
    const string customBearerSchemeName = "CustomBearer";
    var authentication = services.AddAuthentication(customBearerSchemeName);
    authentication
    .AddJwtBearer(customBearerSchemeName, options => {
    options.TokenValidationParameters = new TokenValidationParameters() {
    ValidIssuer = Configuration["Authentication:Jwt:Issuer"],
    ValidAudience = Configuration["Authentication:Jwt:Audience"],
    IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(Configuration["Authentication:Jwt:IssuerSigningKey"]))
    };
    });
    authentication.AddMicrosoftIdentityWebApi(Configuration, configSectionName: "Authentication:AzureAd");

    services.AddAuthorization(options => {
        options.DefaultPolicy = new AuthorizationPolicyBuilder(
            JwtBearerDefaults.AuthenticationScheme)
                .RequireAuthenticatedUser()
                .RequireXafAuthentication()
                .Build();
    });
// ...
}
```
***
Use the **AddSecurityDefinition** and **AddSecurityRequirement** methods to add the OAuth2 Azure authentication to the Swagger UI.

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
# [C#](#tab/tabid-csharp)
 
```csharp
services.AddSwaggerGen(c => {
    //...
    var azureAdAuthorityUrl = $"{Configuration["Authentication:AzureAd:Instance"]}{Configuration["Authentication:AzureAd:TenantId"]}";
    c.AddSecurityDefinition("OAuth2", new OpenApiSecurityScheme
    {
        Type = SecuritySchemeType.OAuth2,
        Flows = new OpenApiOAuthFlows() {
            AuthorizationCode = new OpenApiOAuthFlow() {
                AuthorizationUrl = new Uri($"{azureAdAuthorityUrl}/oauth2/v2.0/authorize"),
                TokenUrl = new Uri($"{azureAdAuthorityUrl}/oauth2/v2.0/token"),
                Scopes = new Dictionary<string, string> {
                    // Configure scopes according to https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-expose-web-apis
                    {"api://11111111-1111-1111-1111-111111111111/WebApi", "Read WebApi"}
                }
            }
        }
    });
    c.AddSecurityRequirement(new OpenApiSecurityRequirement() {
        {
            new OpenApiSecurityScheme {
                Name = "OAuth2",
                Scheme = "OAuth2",
                Reference = new OpenApiReference {
                    Type = Microsoft.OpenApi.Models.ReferenceType.SecurityScheme,
                    Id = "OAuth2"
                },
                In = ParameterLocation.Header
            },
            new string[0]
        }
    });
});

```
***
Also, modify the **UseSwaggerUI** method as follows:

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)
# [C#](#tab/tabid-csharp)
 
```csharp{5-6}
public void Configure(IApplicationBuilder app, IWebHostEnvironment env) {
    // ...
    app.UseSwaggerUI(c => {
        c.SwaggerEndpoint("/swagger/v1/swagger.json", "MySolution WebApi v1");
        c.OAuthClientId(Configuration["Authentication:AzureAd:ClientId"]);
        c.OAuthUsePkce();
    });
    // ...
}    
```
***
### Step 4. Add the ApplicationUser and ApplicationUserLoginInfo Business Objects

XAF requires the _ApplicationUser_ and _ApplicationUserLoginInfo_ business objects to store user information. Add these business objects to the _MySolution.Module_ project as described in the following topic: [](xref:404204).

## Use the Swagger UI to Test the OAuth2 Azure Authentication

1. If your solution includes a **Web API** project, right-click the project in the **Solution Explorer** and choose **Debug | Start new instance** to run the **Web API** project. A browser displays the page with the available endpoints.

    If your solution includes a startup **Blazor Server** project with the **Web API**, run the application. Add _/swagger_ to the application address (for example, _https://localhost:44318/swagger_ ) and press _Enter_ to display a page with available endpoints. 

    Refer to the following link for more information on the page's UI: [Swagger UI](https://swagger.io/tools/swagger-ui/).

    ![|Select authentication](~/images/create-web-api-swagger.png)

2. Click the **Authorize** button: ![Authorize button](~/images/create-web-api-authorize-button.png). In the **Available authorizations** window, select a scope and click the **Authorize** button:

    ![The Available authorizations form](~/images/create-web-api-authorization.png)

    Refer to the following topic for information on how to create Web API endpoints: [Create Endpoints and Test the Web API](xref:403551).
