---
uid: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1
name: SecuredEFCoreObjectSpaceProvider<TDbContext>
type: Class
summary: Provides an [Object Space](xref:113707) in EF Core-based applications that use the [Security System](xref:113366).
syntax:
  content: 'public class SecuredEFCoreObjectSpaceProvider<TDbContext> : EFCoreObjectSpaceProvider<TDbContext>, INonsecuredObjectSpaceProvider where TDbContext : DbContext'
  typeParameters:
  - id: TDbContext
    description: The [database provider](https://learn.microsoft.com/en-us/ef/core/providers/)
seealso:
- linkId: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1._members
  altText: SecuredEFCoreObjectSpaceProvider<TDbContext> Members
---
The following example demonstrates how to create the **SecuredEFCoreObjectSpaceProvider** in a non-XAF application. 

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.EntityFrameworkCore.Security;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
using Microsoft.EntityFrameworkCore;
using System.Configuration;
// ...
class Program {
    static void Main() {
        AuthenticationStandard authentication = new AuthenticationStandard();
        SecurityStrategyComplex security = new SecurityStrategyComplex(
            typeof(PermissionPolicyUser), typeof(PermissionPolicyRole),
            authentication
        );
        var objectSpaceProvider = new SecuredEFCoreObjectSpaceProvider<ApplicationDbContext>(security,
            XafTypesInfo.Instance, ConfigurationManager.ConnectionStrings["ConnectionString"].ConnectionString,
            (builder, connectionString) => builder.UseConnectionString(connectionString)
        );
        // ...
    }
}
```
***

You can find the full example in the following GitHub repository: [How to use the Integrated mode of the Security System in non-XAF applications (EF Core)](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/20.1.5+/EFCore). 
