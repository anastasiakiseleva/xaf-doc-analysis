---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.WinAuthenticationBuilderExtensions.UseExternalAuthentication``1(DevExpress.ExpressApp.Win.ApplicationBuilder.IWinAuthenticationBuilder)
name: UseExternalAuthentication<TAuthenticationProvider>(IWinAuthenticationBuilder)
type: Method
summary: Creates a builder that allows you to enable external (non-XAF) authentication providers in a WinForms application.
syntax:
  content: |-
    public static WinExternalAuthenticationBuilder UseExternalAuthentication<TAuthenticationProvider>(this IWinAuthenticationBuilder authenticationBuilder)
        where TAuthenticationProvider : class, IAuthenticationProviderV2
  parameters:
  - id: authenticationBuilder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinAuthenticationBuilder
    description: A builder that allows you to configure the [Security System](xref:113366) in [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core) in your WinForms application.
  typeParameters:
  - id: TAuthenticationProvider
    description: The authentication provider type.
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.WinExternalAuthenticationBuilder
    description: The newly created builder.
seealso:
- linkId: "404436"
---
> [!important]
> [Middle Tier Security](xref:404640) does not support this method.
