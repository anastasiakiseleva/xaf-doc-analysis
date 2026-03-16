---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.OfficeApplicationBuilderExtensions.AddOffice(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Office.Win.OfficeOptions})
name: AddOffice(IModuleBuilder<IWinApplicationBuilder>, Action<OfficeOptions>)
type: Method
summary: '[!include[<\[Office Module\](xref:400003)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddOffice(this IModuleBuilder<IWinApplicationBuilder> builder, Action<OfficeOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Office.Win.OfficeOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Office Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<options.RichTextMailMergeDataType = typeof(RichTextMailMergeData);>](~/templates/AddOffice_Win_example.md)]