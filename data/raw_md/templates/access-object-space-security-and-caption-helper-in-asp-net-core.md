## Object Space

To create an Object Space in an ASP.NET Core application, inject the @DevExpress.ExpressApp.IObjectSpaceFactory service. Note that this service ensures if a user is logged on. If not, it throws an authorization exception. To avoid this exception, you can use the following techniques:

* Use the `INonSecuredObjectSpaceFactory` service instead of `IObjectSpaceFactory`. 
* Use another way to ensure if a user is logged on (for example, use `AuthorizationPolicyBuilder.RequireXafAuthentication` with `AuthorizeAttribute`).

[!include[<:0:>](~/templates/<:0:>.md)]

## Security System

To access the Security System in an ASP.NET Core application, inject the @DevExpress.ExpressApp.Security.ISecurityProvider service. Note that this service ensures if a user is logged on. If not, it throws an authorization exception. To avoid this exception, you can use the following techniques:

* Use the `ISecurityStrategyBase` service instead of `ISecurityProvider` if you do not need to operate with an authenticated user object. This service does not ensure if a user is logged on or not, so the current user object might not be available here.
* Use another way to ensure if a user is logged on (for example, use `AuthorizationPolicyBuilder.RequireXafAuthentication` with `AuthorizeAttribute`.

These workarounds do not guarantee that you will not receive authentication exceptions, even if you specify the correct user credentials.

[!include[<:1:>](~/templates/<:1:>.md)]

## Caption Helper

The [Caption Helper](xref:DevExpress.ExpressApp.Utils.CaptionHelper) class allows you to get localized captions for XAF [Controllers](xref:112621) and [Razor Components](xref:113610) that are shown in XAF [Views](xref:112611). XAF initializes the Application Model of this class on requests to standard XAF pages. To get captions with other requests (middleware, Web API method, and so on), use the @DevExpress.ExpressApp.Services.Localization.ICaptionHelperProvider service.

This service uses a shared Application Model and does not return user-specific localized strings from a user Model Differences Storage. If your application does not store different captions for different users in the Application Model, use the @DevExpress.ExpressApp.Services.Localization.ICaptionHelperProvider service as a unified way to get localized captions.

[!include[<:2:>](~/templates/<:2:>.md)]

The [CaptionHelper.GetService](xref:DevExpress.ExpressApp.Utils.CaptionHelper.GetService(System.IServiceProvider)) method returns an `ICaptionHelper` instance to use on other platforms such as Win and Web.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Utils;

ICaptionHelper helper = CaptionHelper.GetService(Application.ServiceProvider)
string newActionName = helper.GetActionCaption("New");
// ...
```
***