---
uid: DevExpress.ExpressApp.Security.AuthenticationActiveDirectory
name: AuthenticationActiveDirectory
type: Class
summary: An Authentication that assumes an automatic logon.
syntax:
  content: 'public class AuthenticationActiveDirectory : AuthenticationBase'
seealso:
- linkId: DevExpress.ExpressApp.Security.AuthenticationActiveDirectory._members
  altText: AuthenticationActiveDirectory Members
- linkId: DevExpress.ExpressApp.Security.AuthenticationStandard
- linkId: "402197"
---
XAF uses the [WindowsIdentity](https://learn.microsoft.com/en-us/dotnet/api/system.security.principal.windowsidentity) object to obtain the user name from the Windows account. For additional information, refer to the following topic: [AuthenticationActiveDirectory.Authenticate](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.Authenticate(DevExpress.ExpressApp.IObjectSpace)).

The `AuthenticationActiveDirectory` authentication type does not support [Active Directory Security Groups](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups) out of the box. For information on how to map XAF security roles to AD groups, refer to the following topic: [How to: Assign the Same Permissions for All Users of an Active Directory Group](xref:118740).

Use [IBlazorApplicationBuilder.Security.AddWindowsAuthentication](xref:DevExpress.ExpressApp.ApplicationBuilder.BlazorSecurityBuilderExtensions.AddWindowsAuthentication(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder,System.Action{DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions})) in ASP.NET Core Blazor applications or [IWinApplicationBuilder.Security.UseWindowsApplication](xref:DevExpress.ExpressApp.Win.ApplicationBuilder.WinSecurityBuilderExtensions.UseWindowsAuthentication(DevExpress.ExpressApp.Win.ApplicationBuilder.IWinAuthenticationBuilder,System.Action{DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions})) in Windows Forms applications to add this authentication.

> [!NOTE]
> Certain browsers (for example, Firefox), may prompt users to type their Windows credentials in a logon dialog which is rendered by the browser itself. Refer to the browser documentation to see if it is possible to avoid this dialog. The standard XAF logon dialog is not displayed in any case.
