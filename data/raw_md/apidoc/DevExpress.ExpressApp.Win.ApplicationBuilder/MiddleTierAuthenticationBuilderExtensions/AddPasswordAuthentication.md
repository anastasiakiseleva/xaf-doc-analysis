---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.MiddleTierAuthenticationBuilderExtensions.AddPasswordAuthentication(DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder,System.Action{DevExpress.ExpressApp.ApplicationBuilder.MiddleTierPasswordAuthenticationOptions})
name: AddPasswordAuthentication(IMiddleTierAuthenticationBuilder, Action<MiddleTierPasswordAuthenticationOptions>)
type: Method
summary: Enables standard authentication (with a login and password) in your application.
syntax:
  content: public static IMiddleTierAuthenticationBuilder AddPasswordAuthentication(this IMiddleTierAuthenticationBuilder builder, Action<MiddleTierPasswordAuthenticationOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.MiddleTierPasswordAuthenticationOptions}
    defaultValue: "null"
    description: Options that you can use to configure standard authentication (with a login and password).
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: Allows you to enable and configure the [Security System](xref:113366) in your application, and chain further configuration.
seealso: []
---
