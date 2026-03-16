---
uid: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithMultiTenancyModelDifferenceStore``1(System.Action{DevExpress.ExpressApp.ApplicationBuilder.ModelDifferencesOptions})
name: WithMultiTenancyModelDifferenceStore<TTenantModelDifferenceStore>(Action<ModelDifferencesOptions>)
type: Method
summary: Configures application model settings set to be used for host user interface and tenant user interfaces.
syntax:
  content: |-
    IMultiTenancyApplicationBuilder WithMultiTenancyModelDifferenceStore<TTenantModelDifferenceStore>(Action<ModelDifferencesOptions> setupOptions = null)
        where TTenantModelDifferenceStore : class, ITenantModelDifferenceStore
  parameters:
  - id: setupOptions
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.ModelDifferencesOptions}
    defaultValue: "null"
    description: A delegate that configures application model settings.
  typeParameters:
  - id: TTenantModelDifferenceStore
    description: The type of an application model differences store.
  return:
    type: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder
    description: The application builder that processed the action.
seealso:
- linkId: "404436"
---
