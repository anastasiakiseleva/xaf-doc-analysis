---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.DashboardsApplicationBuilderExtensions.AddDashboards(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Dashboards.Win.DashboardsOptions})
name: AddDashboards(IModuleBuilder<IWinApplicationBuilder>, Action<DashboardsOptions>)
type: Method
summary: '[!include[<\[Dashboards Module\](xref:117449)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddDashboards(this IModuleBuilder<IWinApplicationBuilder> builder, Action<DashboardsOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Dashboards.Win.DashboardsOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Dashboards Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<options.DashboardDataType = typeof(DashboardData);>](~/templates/AddDashboards_Win_example.md)]