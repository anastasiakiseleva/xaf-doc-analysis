---
uid: "403358"
title: 'Assign an Image to a User'
owner: Yekaterina Kiseleva
---
# Assign an Image to a User

This topic describes how to assign an avatar or icon to an application user. ASP.NET Core Blazor applications display this image in the top right corner of an application page.

![XAF ASP.NET Core Blazor, Current User Image, DevExpress](~/images/CurrentUserImage_Blazor.png)

## Apply the CurrentUserDisplayImage Attribute

[!include[CurrentUserDisplayImageAttribute_example](~/templates/CurrentUserDisplayImageAttribute_example.md)]

## Add the XafClaimTypes.UserImageUrl Claim

In ASP.NET Core Blazor applications with OAuth authentication, you can add a claim of the `XafClaimTypes.UserImageUrl` type to read a user image on sign in. The following example configures the Google authentication provider and creates the `XafClaimTypes.UserImageUrl` claim from the `picture` key in Google user data:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)

```csharp{14}
using DevExpress.ExpressApp.Security;
using Microsoft.AspNetCore.Authentication.OAuth;
using Microsoft.AspNetCore.Authentication;
using Microsoft.Extensions.DependencyInjection;
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
        .AddCookie(options => options.LoginPath = "/LoginPage")
        .AddGoogle(options => {
            // ...
            options.ClaimActions.MapJsonKey(XafClaimTypes.UserImageUrl, "picture");
        });
    }
}
```
***

[`MapJsonKey`]: xref:Microsoft.AspNetCore.Authentication.ClaimActionCollectionMapExtensions.MapJsonKey*

## Register an IUserProfileInfoProviderAsync Service

You can register a service that implements the `IUserProfileInfoProviderAsync` interface to specify a custom user image and name. Follow the steps below to implement this technique in your application:

1. In the ASP.NET Core Blazor application project, create a new class that implements the `IUserProfileInfoProviderAsync` interface:

    **File**: _MySolution.Blazor.Server\Services\MyUserProfileInfoProviderAsync.cs_.

    # [C#](#tab/tabid-csharp-1)

    ```csharp
    using DevExpress.ExpressApp.Blazor.Services;
    using DevExpress.ExpressApp.Security;
    using System;
    using System.Threading.Tasks;
    // ...
    public class MyUserProfileInfoProviderAsync : IUserProfileInfoProviderAsync {
        private readonly IPrincipalProvider principalProvider;
        private readonly ISecurityStrategyBase securitySystem;
        public MyUserProfileInfoProviderAsync(IPrincipalProvider principalProvider, ISecurityStrategyBase securitySystem) {
            this.principalProvider = principalProvider;
            this.securitySystem = securitySystem;
        }

        public Task<string> GetUserImageUrlAsync(Func<Task<string>> defaultUrlAccessor) {
            //or: securitySystem.UserName == "Admin"
            if(principalProvider.User.Identity.Name == "Admin") {
                return Task.FromResult(@"https://github.com/DevExpress.png");
            }
            return defaultUrlAccessor();
        }

        public Task<string> GetUserNameAsync(Func<Task<string>> defaultNameAccessor) {
            //or: principalProvider.User.Identity.Name == "Admin"
            if(securitySystem.UserName == "Admin") {
                return Task.FromResult(@"Custom Admin Name");
            }
            return defaultNameAccessor();
        }
    }
    ```
    ***

2. Add this scoped service to your ASP.NET Core Blazor application service collection:

    **File**: _MySolution.Blazor.Server\Startup.cs_.

    # [C#](#tab/tabid-csharp-1)

    ```csharp
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddScoped<IUserProfileInfoProviderAsync, MyUserProfileInfoProviderAsync>();
        }
    }
    ```
    ***
