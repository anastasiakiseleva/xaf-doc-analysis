---
uid: DevExpress.ExpressApp.MultiTenancy.ITenantResolver.GetTenantId(DevExpress.ExpressApp.Security.IAuthenticationStandardLogonParameters)
name: GetTenantId(IAuthenticationStandardLogonParameters)
type: Method
summary: Determines the ID of a tenant based on user logon parameters.
syntax:
  content: Guid? GetTenantId(IAuthenticationStandardLogonParameters parameters)
  parameters:
  - id: parameters
    type: DevExpress.ExpressApp.Security.IAuthenticationStandardLogonParameters
    description: User logon parameters.
  return:
    type: System.Nullable{System.Guid}
    description: The tenant identifier. The property returns `null` if the tenant for specified parameters cannot be determined.
seealso:
- linkId: "404436"
---
