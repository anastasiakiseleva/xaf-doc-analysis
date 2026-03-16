---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.MiddleTierAuthenticationBuilderExtensions.AddAzureAD(DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder,System.Action{DevExpress.ExpressApp.Security.MiddleTierClientAzureAdAuthenticationOptions})
name: AddAzureAD(IMiddleTierAuthenticationBuilder, Action<MiddleTierClientAzureAdAuthenticationOptions>)
type: Method
summary: Provides access to options to configure Microsoft Entra ID authentication.
syntax:
  content: public static IMiddleTierAuthenticationBuilder AddAzureAD(this IMiddleTierAuthenticationBuilder builder, Action<MiddleTierClientAzureAdAuthenticationOptions> configureOptions)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Security.MiddleTierClientAzureAdAuthenticationOptions}
    description: Options that allow you to configure the Microsoft Entra ID authentication.
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: Allows you to enable and configure the [Security System](xref:113366) in your application, and chain further configuration.
seealso: []
---

For more information, refer to the following topic: [](xref:404752#oauth-2-authentication)