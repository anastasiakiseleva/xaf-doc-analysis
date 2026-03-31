---
uid: "404752"
title: Active Directory and OAuth2 Authentication Providers in WinForms Applications
seealso:
  - linkId: '402197'
---

# Active Directory and OAuth2 Authentication Providers in WinForms Applications

## Windows Authentication

Windows Active Directory authentication uses the current Windows account to authenticate a user in an XAF application. You can use Active Directory authentication in one of the following two configurations:

- As the only authentication mode.
- Together with password-based authentication.

### Create a New Application with Windows Authentication

To create an application with Active Directory authentication, run the DevExpress [Template Kit](xref:405447) and specify one of the following configurations in the  **Security Options** section:

- To only use Active Directory authentication, select **Active Directory (uses Windows account)**.
- To use Active Directory authentication as well as password-based authentication, select both **Standard (requests login and password)** and **Active Directory (uses Windows account)** options. 

![Standard and Active Directory Authentication](~/images/template-kit/template-kit-winforms-authentication.png)

### Add Windows Authentication to an Existing Application

To enable Active Directory authentication, add the following code snippet to the application's _Startup.cs_:

**File:** _MySolution.Win/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{15-17}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Win;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                // ...
            })
            .UseWindowsAuthentication(options => {
                options.CreateUserAutomatically();
            });
        // ...
    };
}
```
***

To use both Active Directory authentication and password-based authentication, use the following code sample:

**File:** _MySolution.Win/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{15-18}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Win;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                // ...
            })
            .UsePasswordAuthentication()
            .UseWindowsAuthentication(options => {
                options.CreateUserAutomatically();
            });
            // ... 
    };
    // ...
}; 
```
***

## OAuth 2 Authentication

XAF supports [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) (formerly known as Azure Active Directory) as an authentication method based on OAuth 2. You can also implement a [custom OAuth 2 authentication provider](#implement-a-custom-oauth-2-authentication-provider-google-github-facebook) to use other third-party authentication methods (Google, GitHub, Facebook, and so on).

### Create a New Application with OAuth 2 Authentication (Entra ID)

To create an application with OAuth 2 authentication, run the [Template Kit](xref:405447), select the **Microsoft Entra ID (formerly Azure Active Directory)** option in the **Security Option**s section. 

![Security Options section in the Template Kit](~/images/template-kit/template-kit-oauth-authentication.png)

After the application is created, open the application's _App.config_ (WinForms) or _App.config_ (Blazor) file and specify the following options to configure Microsoft Entra ID authentication:

- `azureAD_Instance` - Your Azure AD instance URL.
- `azureAD_TenantId` - `"common"`, `"organizations"`, or a Tenant ID.
- `azureAD_ClientId` - Application ID.

If you chose the [Middle Tier Security](xref:404389) option in the [Template Kit](xref:405447), also specify these:

- `azureAD_Scopes` - A list of permission scopes to request. For more information about scopes in this context, refer to the following Microsoft documentation topic: [Configure a native client application](https://learn.microsoft.com/en-us/azure/developer/mobile-apps/azure-mobile-apps/quickstarts/maui/authentication).
- `middleTierServer_SchemeName` - Server-side authentication scheme that handles the client-side authentication token. Default value is `AzureAd`.

Open the _appsettings.json_ file of your Middle Tier Security project and specify your Azure AD settings in the `Authentication` section:

**File:** _MySolution.MiddleTier\appsettings.json_
# [JSON](#tab/tabid-json)
```JSON
// ...
"Authentication": {
    // ...
    "AzureAd": {
        "Instance": "https://login.microsoftonline.com/",
        // Enter your tenant domain, for example, contoso.onmicrosoft.com
        "Domain": "",
        // Enter 'common', or 'organizations', or the Tenant Id obtained from the Azure portal. Select 'Endpoints' from the 'App registrations' blade and use the GUID in any of the URLs.
        "TenantId": "organizations",
        // Enter the Client Id (a GUID that is an application ID obtained from the Azure portal).
        "ClientId": "[Configure ClientId in appsettings.json before use.]",
        "CallbackPath": "/signin-oidc"
    }
},    
// ...
```
***

You can obtain values for these settings from the [Azure Portal](https://azure.microsoft.com/en-us/get-started/azure-portal). For more information, see [Desktop application authentication documentation](https://learn.microsoft.com/en-us/entra/identity-platform/index-desktop).

### Add OAuth 2 Authentication (Entra ID) to an Existing Application

To enable OAuth 2 authentication, add the following code to application's _Startup.cs_. Note that password-based authentication must also be enabled:

**File:** _MySolution.Win/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{15-23}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Win;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                // ...
            })
            .UsePasswordAuthentication()
            .UseExternalAuthentication<CustomAuthenticationProvider>()
            .AddAzureAD(opt => {
                opt.ClientId = ConfigurationManager.AppSettings["azureAD_ClientId"];
                opt.TenantId = ConfigurationManager.AppSettings["azureAD_TenantId"];
                opt.Instance = ConfigurationManager.AppSettings["azureAD_Instance"];
                // The following options are only required if you work with a Middle Tier Security project:
                // opt.Scopes = [ConfigurationManager.AppSettings["azureAD_Scopes"]];
                // opt.SchemeName = ConfigurationManager.AppSettings["middleTierServer_SchemeName"];
            });
            // ... 
    };
    // ...
}; 
```
***

Add the options required to use Entra ID authentication to the _App.config_ file:

**File:** _MySolution.Win/App.config_

# [XML](#tab/tabid-xml)

```XML
<?xml version="1.0"?>
<configuration>
  <appSettings>
  <!-- fill the following settings from Azure portal https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant -->
  <add key="azureAD_Instance" value="https://login.microsoftonline.com/" />
  <!-- Enter 'common', or 'organizations' or the Tenant Id obtained from the Azure portal. Select 'Endpoints' from the 'App registrations' blade and use the GUID in any of the URLs), for example, da41245a5-11b3-996c-00a8-4d99re19f292 -->
  <add key="azureAD_TenantId" value="organizations" />
  <!-- Enter the Client Id (application ID obtained from the Azure portal), for example, ba74781c-53c2-442a-97c2-3d60de42f403 -->
  <add key="azureAD_ClientId" value="[Configure ClientId in App.config before use.]" />

  <!-- The followjing oprions are only required if you have a Middle Tier Security project:-->

  <!--The list of scopes to request, for example api://ba74781c2-53c2-442a-97c2-3d60re42f403/WebApi-->
  <!--https://learn.microsoft.com/en-us/azure/developer/mobile-apps/azure-mobile-apps/quickstarts/maui/authentication-->
  <add key="azureAD_Scopes" value="" />
  <!--Server MicrosoftIdentityWebApi JwtBearerScheme property value name-->
  <add key="middleTierServer_SchemeName" value="AzureAd" />
  </appSettings>
</configuration>
```
***

Add a `CustomAuthenticationProvider` class that implements the `IAuthenticationProviderV2` to the **MySolution.Module** project. You can use the following code as a reference implementation of this class ([Template Kit](xref:405447) generates equivalent code):

[!include[customauthenticationprovider-wizard-generated](~/templates/customauthenticationprovider-wizard-generated.md)]

Register your custom authentication provider in the application builder. Navigate to the _MySolution.Win\Startup.cs_ file and add the following code:

**File:** _MySolution.Win\Startup.cs_

```csharp{17-22}
// ...
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Design;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Win;
using DevExpress.ExpressApp.Win.ApplicationBuilder;

namespace MySolution.Win;

public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication() {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            // ...
            .AddExternalAuthentication<MySolution.Module.CustomAuthenticationProvider>()
            .AddAzureAD(opt => {
                opt.ClientId = ConfigurationManager.AppSettings["azureAD_ClientId"];
                opt.TenantId = ConfigurationManager.AppSettings["azureAD_TenantId"];
                opt.Instance = ConfigurationManager.AppSettings["azureAD_Instance"];
            });
        // ...
    }
}
```

If you work with a Middle Tier Security project, it requires additional configuration.

Add the `AzureAd` option to the `Authentication` section in the _appsettings.json_ file and specify your Azure AD credentials.

**File:** _MySolution.MiddleTier\appsettings.json_

# [JSON](#tab/tabid-json)
```JSON
// ...
"Authentication": {
    "AzureAd": {
        "Instance": "https://login.microsoftonline.com/",
        // Enter your tenant domain, for example, contoso.onmicrosoft.com
        "Domain": "",
        // Enter 'common', or 'organizations', or the Tenant Id obtained from the Azure portal. Select 'Endpoints' from the 'App registrations' blade and use the GUID in any of the URLs.
        "TenantId": "organizations",
        // Enter the Client Id (a GUID that is the application ID obtained from the Azure portal).
        "ClientId": "[Configure ClientId in appsettings.json before use.]",
        "CallbackPath": "/signin-oidc"
    }
},    
// ...
```
***

Modify the _Startup.cs_ file as follows:

**File:** _MySolution.MiddleTier/Startup.cs_

# [JSON](#tab/tabid-csharp)
```csharp
// ...
using DevExpress.Data.Filtering;
using System.Security.Principal;
using System.Security.Claims;
using Microsoft.Identity.Web;

namespace MySolution.MiddleTier;

public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        services.AddXafMiddleTier(Configuration, builder => {
            // ...
            builder.Security
                // ....
                .AddAuthenticationProvider<MySolution.Module.CustomAuthenticationProvider>();
            // ...
        });

        services.AddAuthentication("AzureAd")

            //Configure OAuth2 Identity Providers based on your requirements. For more information, see
            //https://docs.devexpress.com/eXpressAppFramework/402197/task-based-help/security/how-to-use-active-directory-and-oauth2-authentication-providers-in-blazor-applications
            //https://developers.google.com/identity/protocols/oauth2
            //https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
            //https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow
            .AddMicrosoftIdentityWebApi(
                jwtBearerOptions => {
                    jwtBearerOptions.TokenValidationParameters.NameClaimType = "preferred_username";
                },
                msIdentityOptions => {
                    Configuration.Bind("Authentication:AzureAd", msIdentityOptions);
                },
                jwtBearerScheme: "AzureAd");

        services.AddAuthorization(options => {
            options.DefaultPolicy = new AuthorizationPolicyBuilder(
                "AzureAd")
                .RequireAuthenticatedUser()
                .RequireXafAuthentication()
                .Build();
        });
    }

    // ...
}
```
***

### Implement a Custom OAuth 2 Authentication Provider (Google, GitHub, Facebook)

> [!important]
> This approach can only be used in Windows Forms applications without the middle tier application server.

XAF includes API that allows you to extend your application with popular third-party authentication methods (Google, GitHub, Facebook, and so on). Follow the steps below to implement a custom external authentication provider and use it in a WinForms application.

First, create a class that implements the `IAuthenticationHandler` interface:

# [C#](#tab/tabid-csharp)

```csharp
using System.Security.Claims;
using DevExpress.ExpressApp.Actions;

class CustomAuthenticationHandler : DevExpress.ExpressApp.Win.ExternalAuthentication.IAuthenticationHandler {
    public Task<ClaimsPrincipal> Logon(ActionBase initiator) {
        var result = new ClaimsPrincipal();
        // ...
        // Here, implement logic used to display authentication UI.
        // On successful authentication, create a ClaimsPrincipal object
        // that contains an authenticated user's information. 
        return Task.FromResult(result);
    }
    public Task Logoff() {
        // ...
        // Here, implement logic that sends a log off command
        // to an external authentication provider
        // or invalidates the authentication token.
        return Task.CompletedTask;
    }
}
```
***

Implement an extension method that registers the new authentication scheme and required services:

# [C#](#tab/tabid-csharp)

```csharp
public static class CustomAuthenticationExtensions {
    public static WinExternalAuthenticationBuilder AddCustomAuthentication(this WinExternalAuthenticationBuilder externalWinAuthenticationBuilder) {
        IServiceCollection services = externalWinAuthenticationBuilder.Context.Services;
        services.AddSingleton<CustomAuthenticationHandler>();
        services.AddSingleton((IAuthenticationScheme)new AuthenticationScheme(
            "CustomAuthenticationScheme", "Custom Authentication", typeof(CustomAuthenticationHandler)));
        return externalWinAuthenticationBuilder;
    }
}
```
***

The above-mentioned code sample specifies the following settings:

- `“CustomAuthenticationScheme”` - The new authentication scheme's unique name. We recommend that you use a name similar to the name of the used authentication provider (Google, GitHub, Facebook, and so on).
- `“Custom Authentication”` - The authentication scheme's name to display on the Login form.

In the WinForms application project, add a `CustomAuthenticationProvider` class that implements the `IAuthenticationProviderV2` interface. In this class, implement authorization logic that involves the `ClaimsPrincipal` produced by your `IAuthenticationHandler` implementation. For example, you can authenticate the user on the application side based on data queried from an Object Space; or create a new user record if the user was not found. You can use the following code as a reference implementation of the `CustomAuthenticationProvider` class:

[!include[customauthenticationprovider-wizard-generated](~/templates/customauthenticationprovider-wizard-generated.md)]

To enable your custom authentication provider, add the following code snippet to application's _Startup.cs_:

**File:** _MySolution.Win/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{16-18}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Win;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                // ...
            })
            UsePasswordAuthentication() 
            .UseExternalAuthentication<CustomAuthenticationProvider>()
                .AddCustomAuthentication();
            };
        // ...
};  
```
***

After you run the application, you will see a button that initiates authentication with your custom provider on the Login form:

![Login Form - Custom Authentication Action](~/images/winforms-custom-authentication-action.png)

### Automatic Login

An XAF Windows Forms application automatically tries to log in the user if there is only one authentication method enabled and it is not password or [Windows](xref:404752#windows-authentication) authentication. You can adjust this behavior for the entire application or specific authentication schemes.

#### Disable Automatic Login

To disable automatic login, add the following controller to your application:

**File:** _MySolution.Win/Controllers/CustomizeAutoLoginController.cs_

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Win.SystemModule;

namespace MySolution.Win.Controllers;

public class CustomizeAutoLoginController : ObjectViewController<DetailView, ILogonParameters> {
    protected override void OnActivated() {
        base.OnActivated();
        var additionalLogonActionsController = Frame.GetController<AdditionalLogonActionsController>();
        if (additionalLogonActionsController is not null) {
            additionalLogonActionsController.CanLogInAutomatically = false;
        }
    }
}
```

Register this controller for the logon window:


**File:** _MySolution.Win/MySolutionWindowsFormsApplication.cs_

```csharp
// ...
public class MySolutionWindowsFormsApplication : WinApplication {
    // ...
    protected override List<Controller> CreateLogonWindowControllers() {
        var controllers = base.CreateLogonWindowControllers();
        controllers.Add(CreateController<CustomizeAutoLoginController>());
        return controllers;
    }
}
```

***

#### Prevent Automatic Login for an Authentication Scheme

You can disallow automatic login behavior for custom authentication schemes when you register them:

```csharp
new AuthenticationScheme("CustomAuthenticationScheme", "Custom Authentication", typeof(CustomAuthenticationHandler)) {
    CanLogInAutomatically = false
}
```

***

## Access External Authentication Provider Actions

When you use Entra ID and/or Active Directory authentication in conjunction with password-based authentication, corresponding action buttons are added to the Login form:

![Login Form - External Authentication Provider Actions](~/images/winforms-access-auth-provider-actions.png)

To customize these buttons, implement a custom controller that accesses the buttons as shown below:

# [C#](#tab/tabid-csharp)

```csharp{8-17}
using DevExpress.ExpressApp.Win.SystemModule;
using DevExpress.ExpressApp;

namespace MySolution.Win.Controllers { 
    public class AdditionalLogonActionsCustomizationController : WindowController {
        protected override void OnActivated() {
            base.OnActivated();
            AdditionalLogonActionsController additionalLogonActionsController = Frame.GetController<AdditionalLogonActionsController>();
            if (additionalLogonActionsController != null) {
                var action = additionalLogonActionsController.Actions.Where(
                    action => action.Id == "EntraID"
                ).FirstOrDefault();
                if (action != null) {
                    // action.Caption = "CustomCaption";
                    // action.ImageName = "CustomImageName";
                }
            }
        }
    }
}
```
***

Override the [XafApplication](xref:DevExpress.ExpressApp.XafApplication) class's `CreateLogonWindowControllers` method as shown below:

**File:** _MySolution.Win/WinApplication.cs_

# [C#](#tab/tabid-csharp)

```csharp
public class MySolutionWindowsFormsApplication : WinApplication {
    // ...
    protected override List<Controller> CreateLogonWindowControllers() {
        var result = base.CreateLogonWindowControllers();
        result.Add(new AdditionalLogonActionsCustomizationController());
        return result;
    }
}
```
***

## Localize External Authentication Action Captions

Edit the _Localization_->_Captions_->_LogInWithActionCaption_ item in the WinForms [Application Model](xref:112579) to modify the localization value for external authentication captions (_"Log In with"_ in _en-US_ localization):

![Model Editor - Localize External Authentication Provider Actions](~/images/winforms-model-editor-localize-auth-provider-actions.png)

The image below illustrates the result.

![Login Form - Localize External Authentication Provider Actions](~/images/winforms-localize-auth-provider-actions.png)

