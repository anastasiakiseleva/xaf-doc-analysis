---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.OfficeApplicationBuilderExtensions.AddOffice(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Blazor.ApplicationBuilder.OfficeOptions})
name: AddOffice(IModuleBuilder<IBlazorApplicationBuilder>, Action<OfficeOptions>)
type: Method
summary: '[!include[<\[Office Module\](xref:400003)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IBlazorApplicationBuilder> AddOffice(this IModuleBuilder<IBlazorApplicationBuilder> builder, Action<OfficeOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: Allows you to register and configure Modules in your application and chain further Module registrations.
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Blazor.ApplicationBuilder.OfficeOptions}
    defaultValue: "null"
    description: Contains options that you can use to configure the [Office Module](xref:400003).
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[<options.RichTextMailMergeDataType = typeof(RichTextMailMergeData);>](~/templates/AddOffice_Blazor_example.md)]

> [!IMPORTANT]
> If you use Entity Framework Core, register the `DevExpress.Persistent.BaseImpl.EF.RichTextMailMergeData` type in the `DbContext` (see [Ways to Add a Business Class - Import Classes from a Business Class Library or Module](xref:112847#import-classes-from-a-business-class-library-or-module)).