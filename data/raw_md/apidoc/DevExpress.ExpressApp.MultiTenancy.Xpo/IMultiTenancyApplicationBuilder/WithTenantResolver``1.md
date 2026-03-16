---
uid: DevExpress.ExpressApp.MultiTenancy.Xpo.IMultiTenancyApplicationBuilder.WithTenantResolver``1
name: WithTenantResolver<TTenantResolver>()
type: Method
summary: Enables automatic tenant detection based on user login with the specified tenant resolver type.
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
