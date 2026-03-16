---
uid: DevExpress.ExpressApp.Security.AuthenticationStandardLogonParameters
name: AuthenticationStandardLogonParameters
type: Class
summary: Logon Parameters type used by default with the [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authentication.
syntax:
  content: |-
    [DataContract]
    [DomainComponent]
    public class AuthenticationStandardLogonParameters : INotifyPropertyChanged, ICustomObjectSerialize, ISupportClearPassword, IAuthenticationStandardLogonParameters, ILogonParameters
seealso:
- linkId: DevExpress.ExpressApp.Security.AuthenticationStandardLogonParameters._members
  altText: AuthenticationStandardLogonParameters Members
---
This class exposes the [AuthenticationStandardLogonParameters.UserName](xref:DevExpress.ExpressApp.Security.AuthenticationStandardLogonParameters.UserName) and [AuthenticationStandardLogonParameters.Password](xref:DevExpress.ExpressApp.Security.AuthenticationStandardLogonParameters.Password) properties specifying user credentials.

When the [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) authentication is used, the **AuthenticationStandardLogonParameters** object is passed by default to:

* the static [SecuritySystem.LogonParameters](xref:DevExpress.ExpressApp.SecuritySystem.LogonParameters) property;
* the [AuthenticationStandard.LogonParameters](xref:DevExpress.ExpressApp.Security.AuthenticationStandard.LogonParameters) property;
* the [LogonEventArgs.LogonParameters](xref:DevExpress.ExpressApp.LogonEventArgs.LogonParameters) argument of the [XafApplication.LoggingOn](xref:DevExpress.ExpressApp.XafApplication.LoggingOn) and [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) events.