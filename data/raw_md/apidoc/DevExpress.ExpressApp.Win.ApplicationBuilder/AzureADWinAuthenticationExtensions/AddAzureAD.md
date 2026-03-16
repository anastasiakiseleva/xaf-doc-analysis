---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.AzureADWinAuthenticationExtensions.AddAzureAD(DevExpress.ExpressApp.Win.ApplicationBuilder.WinExternalAuthenticationBuilder,System.Action{DevExpress.ExpressApp.Win.ApplicationBuilder.AzureAdAuthenticationOptions})
name: AddAzureAD(WinExternalAuthenticationBuilder, Action<AzureAdAuthenticationOptions>)
type: Method
summary: Adds the capability to authenticate a user with a [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) (Azure Active Directory) account in a WinForms application.
syntax:
  content: public static WinExternalAuthenticationBuilder AddAzureAD(this WinExternalAuthenticationBuilder externalWinAuthenticationBuilder, Action<AzureAdAuthenticationOptions> configureOptions)
  parameters:
  - id: externalWinAuthenticationBuilder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.WinExternalAuthenticationBuilder
    description: A builder that enables the [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) authentication in the application.
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Win.ApplicationBuilder.AzureAdAuthenticationOptions}
    description: A delegate method that allows you to cofigure authentication settings.
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.WinExternalAuthenticationBuilder
    description: The builder that processed the action.
seealso:
- linkId: "404436"
---
> [!important]
> [Middle Tier Security](xref:404640) does not support this method.