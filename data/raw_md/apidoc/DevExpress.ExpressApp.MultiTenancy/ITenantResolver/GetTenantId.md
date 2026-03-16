---
uid: DevExpress.ExpressApp.MultiTenancy.ITenantResolver.GetTenantId(System.String)
name: GetTenantId(String)
type: Method
summary: Determines the ID of a tenant based on user login.
syntax:
  content: Guid? GetTenantId(string userLogin)
  parameters:
  - id: userLogin
    type: System.String
    description: The user login.
  return:
    type: System.Nullable{System.Guid}
    description: The tenant identifier. The property returns `null` if the tenant cannot be determined for the specified user login.
seealso:
- linkId: "404436"
---
