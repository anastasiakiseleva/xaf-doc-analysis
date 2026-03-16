---
uid: DevExpress.ExpressApp.ApplicationBuilder.BlazorXpoMultiTenancyApplicationBuilderExtensions.AddMultiTenancy(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder,System.Boolean)
name: AddMultiTenancy(IBlazorApplicationBuilder, Boolean)
type: Method
summary: Creates a builder that allows you to set up a multi-tenant Blazor application with the XPO ORM.
syntax:
  content: public static IMultiTenancyApplicationBuilder AddMultiTenancy(this IBlazorApplicationBuilder builder, bool isMiddleTier = false)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder
    description: An application builder that allows you to configure your Blazor application.
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
