---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.AuditTrailXpoApplicationBuilderExtensions.AddAuditTrailXpo``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.AuditTrail.AuditTrailOptions})
name: AddAuditTrailXpo<TBuilder>(IModuleBuilder<TBuilder>, Action<AuditTrailOptions>)
type: Method
summary: '[!include[<\[Audit Trail Module\](xref:112782) (XPO)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: |-
    public static IModuleBuilder<TBuilder> AddAuditTrailXpo<TBuilder>(this IModuleBuilder<TBuilder> builder, Action<AuditTrailOptions> configureOptions)
        where TBuilder : IApplicationBuilder<TBuilder>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.AuditTrail.AuditTrailOptions}
    description: Options that you can use to configure the Audit Trail Module.
  typeParameters:
  - id: TBuilder
    description: The @DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method: 

[!include[AddAuditTrailXpo_Win_example](~/templates/AddAuditTrailXpo_Win_example.md)]