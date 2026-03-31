---
uid: "402197"
title: Active Directory and OAuth2 Authentication Providers in ASP.NET Core Blazor Applications
seealso:
  - linkId: '404752'
---
# Active Directory and OAuth2 Authentication Providers in ASP.NET Core Blazor Applications

This topic demonstrates how to extend your ASP.NET Core Blazor application with external authentication methods such as [Windows Authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth) and OAuth providers ([Google](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/google-logins), [Azure](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/azure-active-directory), and [GitHub](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/other-logins)). 

![|Extended Logon Window in an XAF ASP.NET Core Blazor Application, DevExpress|](~/images/ExternalAuthenticationBlazor.png)

> [!IMPORTANT]
> [!include[Wizard_Note](~/templates/wizard_note111144.md)]

## Prerequisites

Your application must use [Standard Authentication](xref:DevExpress.ExpressApp.Security.AuthenticationStandard). To enable Standard Authentication, select the cooresponding option in the [Template Kit](xref:405447) when you create a new application or follow the steps in the following help topic to enable it in an existing application: [Use the Security System](xref:404204).

If you want to disable Standard Authentication after you add other types of authentication, navigate to the _YourSolutionName.Blazor.Server_ folder, open the _Startup.cs_ file, and comment out the `AddPasswordAuthentication` method call:

# [C#](#tab/tabid-csharp)

```csharp{9}
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            // ...
            builder.Security
                // ...
                // .AddPasswordAuthentication()
                // ...
        });
        // ...
    }
    // ...
}
```

***

## Windows Authentication

1. In the _MySolution.Blazor.Server\\Properties\\launchSettings.json_ file, set `windowsAuthentication` to `true`. You can also set `anonymousAuthentication` to `false` to hide the logon page and always use Windows authentication:

    # [JSON](#tab/tabid-json)

    ```JSON
    {
      "iisSettings": {
        "windowsAuthentication": true,
        "anonymousAuthentication": false, // optional
        // ...
      },
      // ...
    }
    ```
    ***

    > [!important]
    > The _MySolution.Blazor.Server\Properties\launchSettings.json_ file affects applications in debug mode only; it does not impact deployed apps or those running on Kestrel. For more information, see the following topic: [Configure Windows Authentication in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth)

1. In the _MySolution.Blazor.Server\\Startup.cs_ file, call the `AddWindowsAuthentication` method in the security builder to add Windows Authentication. You can also automatically create a user object with a predefined role when a user attempts to log on for the first time:

    # [EF Core](#tab/tabid-csharp-efcore)

    ```csharp
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy; // for EF Core-based applications

    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXaf(Configuration, builder => {
                // ...
                builder.Security
                    // ...
                    .AddWindowsAuthentication(options => {
                        options.CreateUserAutomatically((objectSpace, user) => {
                            var defaultRole = objectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default");
                            ((ApplicationUser)user).Roles.Add(defaultRole);
                        });
                    });
            });
            // ...
        }
        // ...
    }
    ```

    # [XPO](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.Persistent.BaseImpl.PermissionPolicy; // for XPO-based applications

    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXaf(Configuration, builder => {
                // ...
                builder.Security
                    // ...
                    .AddWindowsAuthentication(options => {
                        options.CreateUserAutomatically((objectSpace, user) => {
                            var defaultRole = objectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default");
                            ((ApplicationUser)user).Roles.Add(defaultRole);
                        });
                    });
            });
            // ...
        }
        // ...
    }
    ```
    ***

2. You can specify a page where to redirect unauthorized users. To do this, create a Razor component with the `@page` directive and specify its route in your Active Directory configuration:

    # [C#](#tab/tabid-csharp-1)

    ```csharp{3}
    .AddWindowsAuthentication(options => {
        // ...
        options.SignOutRedirect = "/UserSignedOut";
    })
    ```
    ***

    This page prevents endless redirects under the following combination of circumstances:

    * You turned off the login page in step 1 (`anonymousAuthentication` is set to `false`).
    * You disabled automatic user creation in step 2 (the `CreateUserAutomatically` method is not called).
    * The user who opened the application is not registered in the database.

### See Also
[Windows Authentication in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth)

## Google, Azure, and GitHub Providers

1. Add the following NuGet packages to the ASP.NET Core Blazor application project (_MySolution.Blazor.Server_):
    * [Microsoft.Identity.Web.UI](https://www.nuget.org/packages/Microsoft.Identity.Web.UI/)
    * [Microsoft.AspNetCore.Authentication.Google](https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.Google/)
2. In the _MySolution.Blazor.Server\\Startup.cs_ file, extend the default cookie-based authentication scheme with the following external schemes: 
    
    # [C#](#tab/tabid-csharp)
    
    ```csharp
    using Microsoft.AspNetCore.Authentication;
    using Microsoft.AspNetCore.Authentication.Cookies;
    using Microsoft.AspNetCore.Authentication.OAuth;
    using Microsoft.Identity.Web;
    using System.Text.Json;
    using System.Net.Http;
    using System.Net.Http.Headers;
    using System.Security.Claims;
    // ...
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
            .AddCookie(options => options.LoginPath = "/LoginPage")
            .AddGoogle(options => {
                Configuration.Bind("Authentication:Google", options);
                options.AuthorizationEndpoint += "?prompt=consent";
                options.SignInScheme = CookieAuthenticationDefaults.AuthenticationScheme;
                options.ClaimActions.MapJsonKey(XafClaimTypes.UserImageUrl, "picture");
            })
            .AddOAuth("GitHub", "GitHub", options => {
                Configuration.Bind("Authentication:GitHub", options);
                options.ClaimActions.MapJsonKey(ClaimTypes.NameIdentifier, "id");
                options.ClaimActions.MapJsonKey(ClaimTypes.Name, "login");
                options.ClaimActions.MapJsonKey(XafClaimTypes.UserImageUrl, "avatar_url");

                options.Events = new OAuthEvents {
                    OnCreatingTicket = async context => {
                        var request = new HttpRequestMessage(HttpMethod.Get, context.Options.UserInformationEndpoint);
                        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", context.AccessToken);
                        request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));

                        var response = await context.Backchannel.SendAsync(request, context.HttpContext.RequestAborted);
                        response.EnsureSuccessStatusCode();
                        var json = JsonDocument.Parse(await response.Content.ReadAsStringAsync());
                        context.RunClaimActions(json.RootElement);
                    }
                };
            })
            .AddMicrosoftIdentityWebApp(options => {
                Configuration.Bind("Authentication:AzureAd", options);
            }, openIdConnectScheme: "AzureAD", cookieScheme: null);
            // ...
        }
    }
    ```
    
    ***
3. In the _MySolution.Blazor.Server\\Services_ folder, create the `CustomAuthenticationProvider` class that implements the `IAuthenticationProviderV2` interface:

    # [EF Core](#tab/tabid-csharp-efcore)

    ```csharp
    using System;
    using System.Security.Claims;
    using System.Security.Principal;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using MySolution.Module.BusinessObjects;

    namespace MySolution.Blazor.Server.Services;

    public class CustomAuthenticationProvider : IAuthenticationProviderV2 {
        private readonly IPrincipalProvider principalProvider;

        public CustomAuthenticationProvider(IPrincipalProvider principalProvider) {
            this.principalProvider = principalProvider;
        }

        public object Authenticate(IObjectSpace objectSpace) {
            if(!CanHandlePrincipal(principalProvider.User)) {
                return null;
            }

            const bool autoCreateUser = true;

            ClaimsPrincipal claimsPrincipal = (ClaimsPrincipal)principalProvider.User;
            var userIdClaim = claimsPrincipal.FindFirst("sub") ?? claimsPrincipal.FindFirst(ClaimTypes.NameIdentifier) ?? throw new InvalidOperationException("Unknown user id");

            var providerUserKey = userIdClaim.Value;
            var loginProviderName = claimsPrincipal.Identity.AuthenticationType;
            var userName = claimsPrincipal.Identity.Name;

            var userLoginInfo = FindUserLoginInfo(objectSpace, loginProviderName, providerUserKey);
            if(userLoginInfo != null) {
                return userLoginInfo.User;
            }

            if(autoCreateUser) {
                return CreateApplicationUser(objectSpace, userName, loginProviderName, providerUserKey);
            }

            return null;
        }

        private bool CanHandlePrincipal(IPrincipal user) {
            return user.Identity.IsAuthenticated &&
                user.Identity.AuthenticationType != SecurityDefaults.Issuer &&
                user.Identity.AuthenticationType != SecurityDefaults.PasswordAuthentication &&
                user.Identity.AuthenticationType != SecurityDefaults.WindowsAuthentication &&
                !(user is WindowsPrincipal);
        }

        private object CreateApplicationUser(IObjectSpace objectSpace, string userName, string loginProviderName, string providerUserKey) {
            if(objectSpace.FirstOrDefault<ApplicationUser>(user => user.UserName == userName) != null) {
                throw new ArgumentException($"The username ('{userName}') was already registered within the system");
            }

            var user = objectSpace.CreateObject<ApplicationUser>();
            user.UserName = userName;
            user.SetPassword(Guid.NewGuid().ToString());
            user.Roles.Add(objectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default"));
            ((ISecurityUserWithLoginInfo)user).CreateUserLoginInfo(loginProviderName, providerUserKey);
            objectSpace.CommitChanges();
            return user;
        }

        private ISecurityUserLoginInfo FindUserLoginInfo(IObjectSpace objectSpace, string loginProviderName, string providerUserKey) {
            return objectSpace.FirstOrDefault<ApplicationUserLoginInfo>(userLoginInfo =>
                                userLoginInfo.LoginProviderName == loginProviderName &&
                                userLoginInfo.ProviderUserKey == providerUserKey);
        }
    }
    ```
    # [XPO](#tab/tabid-csharp-xpo)

    ```csharp
    using System;
    using System.Security.Claims;
    using System.Security.Principal;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Security;
    using DevExpress.Persistent.BaseImpl.PermissionPolicy;
    using MySolution.Module.BusinessObjects;

    namespace MySolution.Blazor.Server.Services;

    public class CustomAuthenticationProvider : IAuthenticationProviderV2 {
        private readonly IPrincipalProvider principalProvider;

        public CustomAuthenticationProvider(IPrincipalProvider principalProvider) {
            this.principalProvider = principalProvider;
        }

        public object Authenticate(IObjectSpace objectSpace) {
            if(!CanHandlePrincipal(principalProvider.User)) {
                return null;
            }

            const bool autoCreateUser = true;

            ClaimsPrincipal claimsPrincipal = (ClaimsPrincipal)principalProvider.User;
            var userIdClaim = claimsPrincipal.FindFirst("sub") ?? claimsPrincipal.FindFirst(ClaimTypes.NameIdentifier) ?? throw new InvalidOperationException("Unknown user id");

            var providerUserKey = userIdClaim.Value;
            var loginProviderName = claimsPrincipal.Identity.AuthenticationType;
            var userName = claimsPrincipal.Identity.Name;

            var userLoginInfo = FindUserLoginInfo(objectSpace, loginProviderName, providerUserKey);
            if(userLoginInfo != null) {
                return userLoginInfo.User;
            }

            if(autoCreateUser) {
                return CreateApplicationUser(objectSpace, userName, loginProviderName, providerUserKey);
            }

            return null;
        }

        private bool CanHandlePrincipal(IPrincipal user) {
            return user.Identity.IsAuthenticated &&
                user.Identity.AuthenticationType != SecurityDefaults.Issuer &&
                user.Identity.AuthenticationType != SecurityDefaults.PasswordAuthentication &&
                user.Identity.AuthenticationType != SecurityDefaults.WindowsAuthentication &&
                !(user is WindowsPrincipal);
        }

        private object CreateApplicationUser(IObjectSpace objectSpace, string userName, string loginProviderName, string providerUserKey) {
            if(objectSpace.FirstOrDefault<ApplicationUser>(user => user.UserName == userName) != null) {
                throw new ArgumentException($"The username ('{userName}') was already registered within the system");
            }

            var user = objectSpace.CreateObject<ApplicationUser>();
            user.UserName = userName;
            user.SetPassword(Guid.NewGuid().ToString());
            user.Roles.Add(objectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default"));
            ((ISecurityUserWithLoginInfo)user).CreateUserLoginInfo(loginProviderName, providerUserKey);
            objectSpace.CommitChanges();
            return user;
        }

        private ISecurityUserLoginInfo FindUserLoginInfo(IObjectSpace objectSpace, string loginProviderName, string providerUserKey) {
            return objectSpace.FirstOrDefault<ApplicationUserLoginInfo>(userLoginInfo =>
                                userLoginInfo.LoginProviderName == loginProviderName &&
                                userLoginInfo.ProviderUserKey == providerUserKey);
        }
    }
    ```
    ***

4. Navigate to the _YourSolutionName.Blazor.Server_ folder. Register the `CustomAuthenticationProvider` class in the _Startup.cs_ file:

    # [EF Core](#tab/tabid-csharp-efcore)

    ```csharp
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using DevExpress.ExpressApp;
    using Microsoft.Extensions.DependencyInjection;
    using System.Security.Principal;
    using Microsoft.Extensions.DependencyInjection;
    
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXaf(Configuration, builder => {
                // ...
                builder.Security
                    // ...
                    .AddAuthenticationProvider<CustomAuthenticationProvider>();
            });
            // ...
        }
        // ...
    }
    ```
    # [XPO](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.Persistent.BaseImpl.PermissionPolicy;
    using DevExpress.ExpressApp;
    using Microsoft.Extensions.DependencyInjection;
    using System.Security.Principal;
    using Microsoft.Extensions.DependencyInjection;
    
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddXaf(Configuration, builder => {
                // ...
                builder.Security
                    // ...
                    .AddAuthenticationProvider<CustomAuthenticationProvider>();
            });
            // ...
        }
        // ...
    }
    ```

    ***

    When a user successfully logs in with an OAuth provider, XAF obtains the user's unique key and finds an `ApplicationUser` object associated with this key. If a user logs in with specified credentials for the first time, XAF creates a new `ApplicationUser` object for this key, generates a random password, and assigns the **Default** Role. We recommend that you create a random password to prevent users from logging in with a username and an empty password.

    You can modify the `CustomAuthenticationProvider.Authenticate` method's body to implement custom logic to process user logins with different authentication methods.

5. Register your application in the corresponding developer account and obtain the Client ID and Application Secret token:
    * [Facebook, Google, and external provider authentication in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/)
    * [Azure Active Directory with ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/azure-active-directory)

    We recommend that you use the [Secret Manager](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets) tool to store the Client ID and Application Secret token. You can store them in the _YourSolutionName.Blazor.Server\appsettings.json_ file for testing purposes only:

    # [JSON](#tab/tabid-json)

    ```JSON
    {
      "Authentication": {
        "Google": {
          "ClientId": "{CLIENT ID}",
          "ClientSecret": "{CLIENT SECRET}"
        },
        "GitHub": {
          "ClientId": "{CLIENT ID}",
          "ClientSecret": "{CLIENT SECRET}"
        },
        "AzureAd": {
          "ClientId": "{CLIENT ID}",
          "ClientSecret": "{CLIENT SECRET}"
        }
      },
      // ...
    }
    ```
    ***

### Automatic Login

An XAF ASP.NET Core Blazor application automatically tries to log in the user if there is only one authentication method enabled and it is not password authentication. Automatic login is disabled if two or more authentication schemes are registered (for example, if you allow users to log in with either Google or GitHub), or if password authentication is enabled.

### Automatic Logoff

If you use an OpenID provider (such as Microsoft Entra ID) to authenticate users, you can force the lifetime of an authentication session to match that of an ID token issued during the authentication process. Set the [OpenIdConnectOptions.UseTokenLifetime](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.openidconnectoptions.usetokenlifetime#microsoft-aspnetcore-builder-openidconnectoptions-usetokenlifetime) option to `true`:

**File:** _MySolution.Blazor.Server/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{8}
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        authentication.AddMicrosoftIdentityWebApp(options => {
            // ...
            options.UseTokenLifetime = true;
        }, openIdConnectScheme: "AzureAD", cookieScheme: null);
    }
}
```
***

When you enable this option, users must re-authenticate after their ID token expires (after a user refreshes the browser tab). In the time period between the current session's expiration and the next authentication, users can continue to interact with the application. Note that some features will not work if they require HTTP requests to the server. For example, images will not be loaded and dashboards may not respond to user interaction.

### See Also

[Deployment Recommendations for XAF Blazor UI Applications](xref:403362)

[Log File Generated in Azure](xref:112575#log-file-generated-in-azure)

## Access External Authentication Provider Actions

Actions for additional authentication schemes registered in @Microsoft.AspNetCore.Authentication.AuthenticationBuilder are displayed below the **Log In** button. To customize these Actions, follow the steps described in this section.

1. Navigate to the _YourSolutionName.Module\\Controllers_ folder and create a [Window Controller](xref:112621#window-controllers).
2. In the `OnActivated` method, get `AdditionalLogonActionsController`.
3. Use the @DevExpress.ExpressApp.Controller.Actions property to access the collection of the Controller's Actions.

    # [C#](#tab/tabid-csharp-1)

    ```csharp
    using System.Linq;
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Blazor.SystemModule;
    // ...
    public class AdditionalLogonActionsCustomizationController : WindowController {
        protected override void OnActivated() {
            base.OnActivated();
            AdditionalLogonActionsController additionalLogonActionsController = Frame.GetController<AdditionalLogonActionsController>();
            if(additionalLogonActionsController != null) {
                var action = additionalLogonActionsController.Actions.Where(action => action.Id == "OpenIdConnect").FirstOrDefault();
                if(action != null) {
                    action.Caption = "Azure";
                    action.ImageName = "Action_LogOnViaAzureAD";
                }
            }
        }
    }
    ```
    ***

4. Navigate to the _YourSolutionName.Blazor.Server_ folder and open the _YourSolutionNameBlazorApplication.cs_ file. Override the `CreateLogonWindowControllers` method and add `AdditionalLogonActionsCustomizationController` to the collection of Controllers activated for the Logon window:

    # [C#](#tab/tabid-csharp)
    
    ```csharp
    using DevExpress.ExpressApp.Blazor;
    using System.Collections.Generic;
    using DevExpress.ExpressApp;
    // ...
    public partial class YourSolutionNameBlazorApplication : BlazorApplication {
        // ...
        protected override List<Controller> CreateLogonWindowControllers() {
            var result = base.CreateLogonWindowControllers();
            result.Add(new AdditionalLogonActionsCustomizationController());
            return result;
        }
    }
    ```
    
    ***


[`PermissionPolicyUser`]: xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser
[`IObjectSpaceLink`]: xref:DevExpress.ExpressApp.IObjectSpaceLink
[`IXafEntityObject`]: xref:DevExpress.ExpressApp.IXafEntityObject
[`DevExpress.Xpo.Aggregated`]: xref:DevExpress.Xpo.AggregatedAttribute
[`Association`]: xref:DevExpress.Xpo.AssociationAttribute
[`XPCollection`]: xref:DevExpress.Xpo.XPCollection
[`IObjectSpace`]: xref:DevExpress.ExpressApp.IObjectSpace
[`BaseObject`]: xref:DevExpress.Persistent.BaseImpl.BaseObject
[`Indexed`]: xref:DevExpress.Xpo.IndexedAttribute
[`DevExpress.ExpressApp.DC.Aggregated`]: xref:DevExpress.ExpressApp.DC.AggregatedAttribute
[`Required`]: xref:System.ComponentModel.DataAnnotations.RequiredAttribute
[`ForeignKey`]: xref:System.ComponentModel.DataAnnotations.Schema.ForeignKeyAttribute
[`Entity`]: xref:Microsoft.EntityFrameworkCore.ModelBuilder.Entity*
[`HasIndex`]: xref:Microsoft.EntityFrameworkCore.Metadata.Builders.EntityTypeBuilder`1.HasIndex*
[`IsUnique`]: xref:Microsoft.EntityFrameworkCore.Metadata.Builders.IndexBuilder`1.IsUnique*
[`ClaimsPrincipal`]: xref:System.Security.Claims.ClaimsPrincipal 
[`WindowsPrincipal`]: xref:System.Security.Principal.WindowsPrincipal
[`IApplicationBuilder`]: xref:Microsoft.AspNetCore.Builder.IApplicationBuilder 
[`IWebHostEnvironment`]: xref:Microsoft.AspNetCore.Hosting.IWebHostEnvironment
[`UseMiddleware`]: xref:Microsoft.AspNetCore.Builder.UseMiddlewareExtensions.UseMiddleware*
[`IServiceCollection`]: xref:Microsoft.Extensions.DependencyInjection.IServiceCollection 
[`IISServerOptions`]: xref:Microsoft.AspNetCore.Builder.IISServerOptions
[`AddAuthentication`]: xref:Microsoft.Extensions.DependencyInjection.AuthenticationServiceCollectionExtensions.AddAuthentication*
[`CookieAuthenticationDefaults.AuthenticationScheme`]: xref:Microsoft.AspNetCore.Authentication.Cookies.CookieAuthenticationDefaults.AuthenticationScheme
[`AddGoogle`]: xref:Microsoft.Extensions.DependencyInjection.GoogleExtensions.AddGoogle*
[`AuthorizationEndpoint`]: xref:Microsoft.AspNetCore.Authentication.OAuth.OAuthOptions.AuthorizationEndpoint*
[`SignInScheme`]: xref:Microsoft.AspNetCore.Authentication.RemoteAuthenticationOptions.SignInScheme*
[`AddOAuth`]: xref:Microsoft.Extensions.DependencyInjection.OAuthExtensions.AddOAuth*
[`OAuthEvents`]: xref:Microsoft.AspNetCore.Authentication.OAuth.OAuthEvents 
[`OnCreatingTicket`]: xref:Microsoft.AspNetCore.Authentication.OAuth.OAuthEvents.OnCreatingTicket 
[`WindowController`]: xref:DevExpress.ExpressApp.WindowController

## Localize External Authentication Action Captions

Edit the _Localization_->_Captions_->_LogInWithActionCaption_ item in the Blazor [Application Model](xref:112579) to modify the localization value for the external authentication caption (_"Log In with"_ in _en-US_ localization):

![Model Editor - Localize External Authentication Provider Actions](~/images/blazor-model-editor-localize-auth-provider-actions.png)

The image below illustrates the result.

![Login Form - Localize External Authentication Provider Actions](~/images/blazor-localize-auth-provider-actions.png)

> [!NOTE]
> In Blazor applications, an external authentication action caption contains the _"Log In with"_ substring (or its localized version) only if a single action is available. Otherwise, only the external authentication method's name is displayed.

