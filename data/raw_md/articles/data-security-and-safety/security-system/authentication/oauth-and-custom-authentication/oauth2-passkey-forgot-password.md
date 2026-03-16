---
uid: "405221"
title: OAuth2 Authentication - Passkey, Forgot My Password, and Two-Factor Authentication Support
owner: Eugeniy Burmistrov
---

# OAuth2 Authentication - Passkey, Forgot My Password, and Two-Factor Authentication Support

Your XAF Blazor or WinForms application can use external OAuth 2 authentication providers (for example, **Microsoft Entra ID** or **Google**) and their integrated capabilities such as _Passkey_, _Forgot Password_ and _Two-Factor Authentication_. Note that these features are implemented and maintained by the providers rather then by XAF. Their availability depends only on the provider's configuration and on the organization's domain policies if such policies are applicable and are in use. 

## Details

As an example, when a user initiates a logon process through Microsoft Entra ID, the following popup window appears:

![Entra ID logon form](~/images/oauth2-entraid-logon-form.png)

This window displays a logon form that is common for Microsoft web-based resources with all logon options available. For example: 

### Two-Factor Authentication

If [two-factor authentication](https://www.microsoft.com/en-ie/security/business/security-101/what-is-two-factor-authentication-2fa) is enabled, the logon form will prompt a user to take an additional verification step after the user enters their login ID and password. The additional step may differ depending on the two-factor authentication method used.

![Entra ID - two-factor authentication](~/images/oauth2-entraid-two-factor.png)

### Forgot My Password

The _Forgot my password_ action redirects the user to a password recovery page. Once the user has recovered the password, the initial logon page of the Entra ID logon form is displayed.

![Entra ID - forgot password](~/images/oauth2-entraid-forgot-password.png)

### Passkey

If a user clicks the _Sign-in options_ button on the initial logon page, the form switches to the page with additional authentication methods. For example, the user can follow the [passkey](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-register-passkey) flow to log in.

![Entra ID - passkey](~/images/oath2-entraid-passkey.png)

