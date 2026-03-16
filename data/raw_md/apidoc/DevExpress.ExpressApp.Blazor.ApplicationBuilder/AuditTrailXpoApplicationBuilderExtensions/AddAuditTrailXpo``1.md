---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.AuditTrailXpoApplicationBuilderExtensions.AddAuditTrailXpo``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0})
name: AddAuditTrailXpo<TBuilder>(IModuleBuilder<TBuilder>)
type: Method
summary: '[!include[<\[Audit Trail Module\](xref:112782) (XPO)>](~/templates/ApplicationBuilderExtensions_Member_Summary.md)]'
syntax:
  content: |-
    public static IModuleBuilder<TBuilder> AddAuditTrailXpo<TBuilder>(this IModuleBuilder<TBuilder> builder)
        where TBuilder : IApplicationBuilder<TBuilder>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
  typeParameters:
  - id: TBuilder
    description: The @DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder type.
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: '[!include[IModuleBuilder_Parameter_Description](~/templates/IModuleBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method: 

[!include[AddAuditTrailXpo_Blazor_example](~/templates/AddAuditTrailXpo_Blazor_example.md)]