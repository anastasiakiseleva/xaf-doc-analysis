---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.TreeListEditorsApplicationBuilderExtensions.AddTreeListEditors(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditorOptions})
name: AddTreeListEditors(IModuleBuilder<IWinApplicationBuilder>, Action<TreeListEditorOptions>)
type: Method
summary: '[!include[<\[Tree List Editors Module\](xref:112841)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: public static IModuleBuilder<IWinApplicationBuilder> AddTreeListEditors(this IModuleBuilder<IWinApplicationBuilder> builder, Action<TreeListEditorOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditorOptions}
    defaultValue: "null"
    description: Options that you can use to configure the Tree List Editors Module.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

[!include[AddTreeListEditors_example](~/templates/AddTreeListEditors_example.md)]
