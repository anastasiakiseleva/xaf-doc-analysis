---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.ReportsApplicationBuilderExtensions.AddReports(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.ReportsV2.Blazor.ReportsOptions})
name: AddReports(IModuleBuilder<IBlazorApplicationBuilder>, Action<ReportsOptions>)
type: Method
summary: '[!include[<[Reports V2 Module](xref:113591)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IBlazorApplicationBuilder> AddReports(this IModuleBuilder<IBlazorApplicationBuilder> builder, Action<ReportsOptions> configureOptions)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.ReportsV2.Blazor.ReportsOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Reports V2 Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<options.EnableInplaceReports = true;>](~/templates/AddReports_Blazor_example.md)]