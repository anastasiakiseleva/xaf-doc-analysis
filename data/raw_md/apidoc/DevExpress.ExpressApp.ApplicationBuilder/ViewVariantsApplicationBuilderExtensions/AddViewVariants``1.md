---
uid: DevExpress.ExpressApp.ApplicationBuilder.ViewVariantsApplicationBuilderExtensions.AddViewVariants``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsOptions})
name: AddViewVariants<TBuilder>(IModuleBuilder<TBuilder>, Action<ViewVariantsOptions>)
type: Method
summary: '[!include[<\[View Variants Module\](xref:113011)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: |-
    public static IModuleBuilder<TBuilder> AddViewVariants<TBuilder>(this IModuleBuilder<TBuilder> builder, Action<ViewVariantsOptions> configureOptions = null)
        where TBuilder : IApplicationBuilder<TBuilder>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsOptions}
    defaultValue: "null"
    description: Options that you can use to configure the View Variants Module.
  typeParameters:
  - id: TBuilder
    description: The @DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder or @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[AddViewVariants_example](~/templates/AddViewVariants_example.md)]