---
uid: DevExpress.ExpressApp.Security.SecurityStrategyComplex
name: SecurityStrategyComplex
type: Class
summary: A Security Strategy that maintains users who have a list of associated roles.
syntax:
  content: 'public class SecurityStrategyComplex : SecurityStrategy, ISecurityComplex, ISecurityStrategyBase, IRoleTypeProvider, IServiceProviderContainer'
seealso:
- linkId: DevExpress.ExpressApp.Security.SecurityStrategyComplex._members
  altText: SecurityStrategyComplex Members
---
In the **SecurityStrategyComplex** security strategy, each user can belong to one or more groups. These groups are called Roles (see XPO [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRole) or EF Core [](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRole)). Roles are characterized by an associated permission set. An application administrator creates users and roles, and assigns roles to users. An application developer can create a set of predefined users and roles that can be extended later by an administrator (see [Client-Side Security (2-Tier Architecture)](xref:113436)).

> [!NOTE]
> To see what capabilities are provided to an administrator within the **SecurityStrategyComplex** security strategy, refer to the [Security System Overview](xref:113366) topic.
