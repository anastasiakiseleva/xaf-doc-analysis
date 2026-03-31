---
uid: "119064"
seealso: []
title: User Logon and Authentication
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF_logon-form-manage-users-register-a-new-user-restore-a-password
  altText: 'XAF Blazor UI: How to extend the logon form - register a new user, restore a password'
---
# User Logon and Authentication

The [Security System](xref:113366) supports the following authentication techniques:

* [Standard (requests login and password)](#standard-authentication)
* [Active Directory (uses Windows account)](#windows-active-directory-authentication)
* [Microsoft Entra ID (formerly Azure Active Directory)](#oauth2-and-custom-authentication) based on OAuth 2

When you create a new XAF application, select an appropriate [authentication](xref:119064) type in the **Security Options** section:

![Security Options section in the Template Kit](~/images/template-kit/template-kit-oauth-authentication.png) 

To enable authentication in an existing application, refer to the following sections:

* [Enable Active Directory Authentication](#enable-active-directory-authentication)
* [Enable Standard Authentication](#enable-standard-authentication)

## Standard Authentication
With [Standard Authentication](xref:DevExpress.ExpressApp.Security.AuthenticationStandard), the Security System uses the internal XAF authentication mechanism and stores user credentials in the application's database. Users need to input their name and password in the login form before application startup.

> [!NOTE]
> You can customize the authentication process and add extra logon parameters. The following help section describes how to do this: [](xref:404264).

For testing purposes, XAF generates administrative and non-administrative user objects (Admin and User) with empty passwords. In production code, create users and assign roles to them in the Administrative UI or database directly.

> [!TIP]
> To protect your applications from brute force attacks, XAF includes user lockout functionality. For more information, refer to the following topic: @DevExpress.ExpressApp.Security.ISecurityUserLockout.

### Enable Standard Authentication

#### WinForms (2-Tier Security) or ASP.NET Core Blazor + .NET

**Files**:
**ASP.NET Core Blazor** - _MySolution.Blazor.Server\Startup.cs_
**WinForms** - _MySolution.Win\Startup.cs_

# [C#](#tab/tabid-csharp-1)
```csharp
// ...
builder.Security
    .UseIntegratedMode(options => {
        // ...
    })
    .AddPasswordAuthentication(options => {
        options.IsSupportChangePassword = true;
        // ...
    });
// ...
```
***

#### WinForms (Middle-Tier Security) or Web API + .NET 

**Files**:
**Middle Tier Server** - _MySolution.MiddleTier\Startup.cs_
**Web API Service** - _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp-1)
```csharp
// ...
services.AddXafAspNetCoreSecurity(Configuration, options => {
        //...
    })
    .AddAuthenticationStandard(options => {
        options.IsSupportChangePassword = true;
    });
// ...
```
***

## Windows Active Directory Authentication

With [Active Directory Authentication](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth), Windows validates the user's identity through Active Directory, and XAF does not store user passwords in the database. The user name is obtained from the [WindowsIdentity](xref:System.Security.Principal.WindowsIdentity) object and includes the computer or domain name (for example, _COMPUTERNAME\UserName_ or _DOMAINNAME\UserName_). You can enable the [AuthenticationActiveDirectory.CreateUserAutomatically](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CreateUserAutomatically) option to create a new user object automatically when a user logs into the application for the first time.

For testing purposes, the Security System creates a new user object for your Windows account and assigns the **administrative** role to it when you start the application for the first time in `DEBUG` mode with the `CreateUserAutomatically` option enabled. In production code, the Security System does not create a new role or assign a role to a newly created user. In this case, you can assign a role manually in the Administrative UI or in the database directly, or specify the [SecurityStrategyComplex.NewUserRoleName](xref:DevExpress.ExpressApp.Security.SecurityStrategyComplex.NewUserRoleName) property. For further customization, you can handle the [AuthenticationActiveDirectory.CustomCreateUser](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CustomCreateUser) event (for example, you can automatically create restricted accounts associated with a specific default role).

### Enable Active Directory Authentication

#### WinForms (2-Tier Security) or ASP.NET Core Blazor + .NET

**Files**:
**ASP.NET Core Blazor** - _MySolution.Blazor.Server\Startup.cs_
**WinForms** - _MySolution.Win\Startup.cs_

# [C#](#tab/tabid-csharp-1)
```csharp
// ...
builder.Security
    .UseIntegratedMode(options => {
        // ...
        // Assign a role with the 'Default' name to new users.
        options.NewUserRoleName = "Default";
        // ...
    })
    .AddWindowsAuthentication(options => {
        // Enable auto-creation of new users.
        options.CreateUserAutomatically();
        // Customize new user auto-creation.
        options.Events.CustomCreateUser = (e) => {
            // ...
        };
    });
// ...
```
***

#### WinForms (Middle-Tier Security) or Web API + .NET 

**Files**:
**Middle Tier Server** - _MySolution.MiddleTier\Startup.cs_
**Web API Service** - _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp-1)
```csharp
// ...
services.AddXafAspNetCoreSecurity(Configuration, options => {
    // Assign a role with the 'Default' name to new users.
    options.NewUserRoleName = "Default";
    })
    .AddAuthenticationActiveDirectory(options => {
        // Enable auto-creation of new users.
        options.CreateUserAutomatically = true;
        // Customize new user auto-creation.
        options.Events.CustomCreateUser = (e) => {
            // ...
        };
    });
// ...
```
***

[`NewUserRoleName`]: xref:DevExpress.ExpressApp.Security.SecurityStrategyComplex.NewUserRoleName
[`CreateUserAutomatically`]: xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CreateUserAutomatically
[`CustomCreateUser`]: xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CustomCreateUser
[`UseIntegratedMode`]: xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder.UseIntegratedMode(System.Action{DevExpress.ExpressApp.Security.SecurityOptions},System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions})
[`AddWindowsAuthentication`]: xref:DevExpress.ExpressApp.ApplicationBuilder.BlazorSecurityBuilderExtensions.AddWindowsAuthentication(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder,System.Action{DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions})


## OAuth2 and Custom Authentication
The following examples demonstrate custom authentication implementations:

* [](xref:404264)
* [](xref:402197)
* [](xref:404752)

## Authenticate a User in Code (Blazor, Web API Service)

XAF supports API that you can use to access and manage application users as well as authenticate users. This API includes the following services:

@DevExpress.ExpressApp.Security.UserManager
:    Exposes API required to manage user objects in the database.
@DevExpress.ExpressApp.Security.SignInManager
:    Exposes API required to sign a user into an application.

The following code snippet demonstrates how to use API that the `UserManager` and `SignInManager` services expose to sign into a nested scope and execute a controller's action on a service user's behalf (user impersonation):

[!include[signinmanager-impersonation-example](~/templates/signinmanager-impersonation-example.md)]

