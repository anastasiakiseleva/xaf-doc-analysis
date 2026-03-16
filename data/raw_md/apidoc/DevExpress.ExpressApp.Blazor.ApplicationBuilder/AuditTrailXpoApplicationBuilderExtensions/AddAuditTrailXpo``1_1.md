---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.AuditTrailXpoApplicationBuilderExtensions.AddAuditTrailXpo``1(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{``0},System.Action{DevExpress.ExpressApp.AuditTrail.AuditTrailOptions})
name: AddAuditTrailXpo<TBuilder>(IModuleBuilder<TBuilder>, Action<AuditTrailOptions>)
type: Method
summary: ''
syntax:
  content: |-
    public static IModuleBuilder<TBuilder> AddAuditTrailXpo<TBuilder>(this IModuleBuilder<TBuilder> builder, Action<AuditTrailOptions> configureOptions)
        where TBuilder : IApplicationBuilder<TBuilder>, IAccessor<IServiceCollection>
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: ''
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.AuditTrail.AuditTrailOptions}
    description: ''
  typeParameters:
  - id: TBuilder
    description: ''
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{{TBuilder}}
    description: ''
seealso: []
---
