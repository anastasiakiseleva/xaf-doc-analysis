---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.FileAttachmentsApplicationBuilderExtensions.AddFileAttachments(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsOptions})
name: AddFileAttachments(IModuleBuilder<IWinApplicationBuilder>, Action<FileAttachmentsOptions>)
type: Method
summary: '[!include[<\[File Attachments Module\](xref:112781)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddFileAttachments(this IModuleBuilder<IWinApplicationBuilder> builder, Action<FileAttachmentsOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentsOptions}
    defaultValue: "null"
    description: Options that you can use to configure the File Attachments Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<CustomSaveFiles>](~/templates/AddFileAttachments_Win_example.md)]