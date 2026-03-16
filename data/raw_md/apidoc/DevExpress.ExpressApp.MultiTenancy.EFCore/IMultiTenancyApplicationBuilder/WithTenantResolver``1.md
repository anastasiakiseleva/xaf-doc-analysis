---
uid: DevExpress.ExpressApp.MultiTenancy.EFCore.IMultiTenancyApplicationBuilder.WithTenantResolver``1
name: WithTenantResolver<TTenantResolver>()
type: Method
summary: Enables automatic tenant detection based on user login using the specified tenant resolver type.
syntax:
  content: |-
    void WithTenantResolver<TTenantResolver>()
        where TTenantResolver : class, ITenantResolver
  typeParameters:
  - id: TTenantResolver
    description: The type of the tenant resolver.
seealso:
- linkId: "404436"
---
