---
uid: DevExpress.ExpressApp.Security.AuthenticationBase
name: AuthenticationBase
type: Class
summary: An abstract base class for Security System authentication types.
syntax:
  content: 'public abstract class AuthenticationBase : Component'
seealso:
- linkId: DevExpress.ExpressApp.Security.AuthenticationBase._members
  altText: AuthenticationBase Members
---
Built-in authentication types that inherit this class are [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) and [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard), To implement a custom authentication, override the following virtual methods and properties:

@DevExpress.ExpressApp.Security.AuthenticationBase.Authenticate(DevExpress.ExpressApp.IObjectSpace)
:    Called when authentication is required. Authenticates a user trying to find the corresponding object by comparing logon parameter values with the information stored in the database. Returns the object if it is found.
@DevExpress.ExpressApp.Security.AuthenticationBase.ClearSecuredLogonParameters
:    The logon parameters specified in the Logon Window can be accessed via the SecuritySystem's `LogonParameters` property. You can clear the logon parameters so they are not accessible in the application. For instance, a password can be hidden. For this purpose, clear these logon parameters in the `ClearSecuredLogonParameters` method.
@DevExpress.ExpressApp.Security.AuthenticationBase.GetBusinessClasses
:    Returns a list of business classes to be added to the [Application Model](xref:112580). For instance, if you do not return the LogonParameters class, its Detail View will not be displayed in the Logon Window.
@DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.AskLogonParametersViaUI
:    Returns `true` if a Logon Window should be displayed to get a user's logon parameters. If you can get these parameters from another location, as in Active Directory authentication, return `false`.
@DevExpress.ExpressApp.Security.AuthenticationBase.LogonParameters
:    Returns an object representing current logon parameters.
@DevExpress.ExpressApp.Security.AuthenticationBase.IsLogoffEnabled
:    Indicates whether to enable the `Logoff` Action.
@DevExpress.ExpressApp.Security.AuthenticationBase.Logoff
:    Recreates the Logon Parameters object when a user logs off.
@DevExpress.ExpressApp.Security.AuthenticationBase.SetLogonParameters(System.Object)
:    Initializes the logon parameters (required in the [client-server security](xref:113439) with custom logon parameters configuration only).
