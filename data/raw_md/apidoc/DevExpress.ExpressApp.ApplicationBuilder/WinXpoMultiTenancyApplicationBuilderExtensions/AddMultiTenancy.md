---
uid: DevExpress.ExpressApp.ApplicationBuilder.WinXpoMultiTenancyApplicationBuilderExtensions.AddMultiTenancy(DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder,System.Boolean)
name: AddMultiTenancy(IWinApplicationBuilder, Boolean)
type: Method
summary: Creates a builder that allows you to set up a multi-tenant WinForms application with the XPO data model.
syntax:
  content: public static IMultiTenancyApplicationBuilder AddMultiTenancy(this IWinApplicationBuilder builder, bool isMiddleTier = false)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder
    description: The application builder that allows you to configure your WinForms application.
  - id: isMiddleTier
    type: System.Boolean
    defaultValue: "False"
    description: '`true` if the application uses the [Middle Tier Security](xref:113439); otherwise, `false`.'
  return:
    type: DevExpress.ExpressApp.MultiTenancy.Xpo.IMultiTenancyApplicationBuilder
    description: The newly created application builder.
seealso:
- linkId: "404436"
---
