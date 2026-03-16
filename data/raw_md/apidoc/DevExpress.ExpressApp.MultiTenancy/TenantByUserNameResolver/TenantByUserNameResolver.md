---
uid: DevExpress.ExpressApp.MultiTenancy.TenantByUserNameResolver
name: TenantByUserNameResolver
type: Class
summary: Determines the tenant name based on user login name according to the specified pattern. The pattern should contain '**{User}**' and '**{Tenant}**' parts. For instance, if the pattern is '**{Tenant}&#47;&#47;{User}**' and login is '**company&#47;John**', the user name is '**John**' and the tenant name is '**company**'.
syntax:
  content: 'public class TenantByUserNameResolver : ITenantResolver'
seealso:
- linkId: DevExpress.ExpressApp.MultiTenancy.TenantByUserNameResolver._members
  altText: TenantByUserNameResolver Members
- linkId: "404436"
- linkId: 404667#tenant-resolvers
  altText: Tenant Resolvers
---
```csharp
using DevExpress.ExpressApp.MultiTenancy;
using DevExpress.ExpressApp.Security;
// ...
public class TenantByUserNameResolverEx:TenantByUserNameResolver {
    public TenantByUserNameResolverEx(IServiceProvider serviceProvider)
    : base(
        serviceProvider, 
        "{User}\\\\{Tenant}", 
        (IAuthenticationStandardLogonParameters parameters) => parameters.UserName) { }
}
```