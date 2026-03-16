---
uid: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithCustomTenantType``1
name: WithCustomTenantType<TTenantType>()
type: Method
summary: Specifies the persistent type used to store tenant information.
syntax:
  content: |-
    IMultiTenancyApplicationBuilder WithCustomTenantType<TTenantType>()
        where TTenantType : ITenant, ITenantWithConnectionString
  typeParameters:
  - id: TTenantType
    description: The type of object that stores tenant information.
  return:
    type: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder
    description: The application builder that processed the action.
seealso:
- linkId: "404436"
---
