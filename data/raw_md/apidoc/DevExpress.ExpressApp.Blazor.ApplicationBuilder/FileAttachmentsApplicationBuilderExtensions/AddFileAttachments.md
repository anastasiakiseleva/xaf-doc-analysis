---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.FileAttachmentsApplicationBuilderExtensions.AddFileAttachments(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.FileAttachments.Blazor.FileAttachmentsOptions})
name: AddFileAttachments(IModuleBuilder<IBlazorApplicationBuilder>, Action<FileAttachmentsOptions>)
type: Method
summary: '[!include[<\[File Attachments Module\](xref:112781)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IBlazorApplicationBuilder> AddFileAttachments(this IModuleBuilder<IBlazorApplicationBuilder> builder, Action<FileAttachmentsOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.FileAttachments.Blazor.FileAttachmentsOptions}
    defaultValue: "null"
    description: Options that you can use to configure the File Attachments Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<// ...>](~/templates/AddFileAttachments_Blazor_example.md)]