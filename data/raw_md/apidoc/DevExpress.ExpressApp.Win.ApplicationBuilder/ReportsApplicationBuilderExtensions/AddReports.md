---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.ReportsApplicationBuilderExtensions.AddReports(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.ReportsV2.Win.ReportsOptions})
name: AddReports(IModuleBuilder<IWinApplicationBuilder>, Action<ReportsOptions>)
type: Method
summary: '[!include[<[Reports V2 Module](xref:113591)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddReports(this IModuleBuilder<IWinApplicationBuilder> builder, Action<ReportsOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.ReportsV2.Win.ReportsOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Reports V2 Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<options.EnableInplaceReports = true;>](~/templates/AddReports_Win_example.md)]