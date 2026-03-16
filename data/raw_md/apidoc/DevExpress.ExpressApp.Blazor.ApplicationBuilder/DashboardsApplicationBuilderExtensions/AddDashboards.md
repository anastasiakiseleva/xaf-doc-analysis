---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.DashboardsApplicationBuilderExtensions.AddDashboards(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Dashboards.Blazor.DashboardsOptions})
name: AddDashboards(IModuleBuilder<IBlazorApplicationBuilder>, Action<DashboardsOptions>)
type: Method
summary: '[!include[<\[Dashboards Module\](xref:117449)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IBlazorApplicationBuilder> AddDashboards(this IModuleBuilder<IBlazorApplicationBuilder> builder, Action<DashboardsOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Dashboards.Blazor.DashboardsOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Dashboards Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<options.DashboardDataType = typeof(DashboardData);>](~/templates/AddDashboards_Blazor_example.md)]