---
uid: DevExpress.ExpressApp.Security.AuthenticationStandard
name: AuthenticationStandard
type: Class
summary: Authentication with an interactive logon. A user inputs logon parameters (for example, username and password) in the logon dialog window.
syntax:
  content: 'public class AuthenticationStandard : AuthenticationBase, IAuthenticationStandard, ISupportChangePasswordOption'
seealso:
- linkId: DevExpress.ExpressApp.Security.AuthenticationStandard._members
  altText: AuthenticationStandard Members
- linkId: "112649"
---
If the application uses Standard Authentication, the logon window displays a Detail View of an `AuthenticationStandardLogonParameters` object. This object has two string properties: `UserName` and `Password`. The `UserName` property is used to find the corresponding user in the database. You cannot log into the application if the user is not found or the specified password is wrong. 

Standard Authentication (the `AuthenticationStandard` object) works only with `AuthenticationStandardLogonParameters` objects, including descendants.

Logon Window in an ASP.NET Core Blazor Application
:   ![|Logon Window in an ASP.NET Core Blazor Application|](~/images/LogonWindowBlazor.png)

Logon Window in a Windows Forms Application
:   ![Logon Window in a WinForms Application](~/images/tutorial_ss_lesson1_1115528.png)

## Select Standard Authentication in the Template Kit

When you use the [Template Kit](xref:405447) to create a new application, select **Standard** as the authentication method in the **Security Options** section.

![Template Kit](~/images/template-kit/template-kit-security-standard.png)

## Enable Standard Authentication in an Existing Application

To enable Standard Authentication in an existing application without a security system, follow the steps described in the following help topic: [Use the Security System](xref:404204). Alternatively, create two applications - one with Standard Authentication and one without - and compare them side-by-side to see what changes you need to make to implement Standard Authentication in your application.

If your application uses server-side security, refer to the [Middle Tier Security](xref:113439) topic for instructions on how to enable Standard Authentication.
