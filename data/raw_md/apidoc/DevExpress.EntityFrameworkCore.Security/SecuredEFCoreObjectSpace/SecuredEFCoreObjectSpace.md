---
uid: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpace
name: SecuredEFCoreObjectSpace
type: Class
summary: An [Object Space](xref:113707) for EF Core-based applications that use the [Security System](xref:113366).
syntax:
  content: 'public class SecuredEFCoreObjectSpace : EFCoreObjectSpace, ISessionObjectProvider'
seealso:
- linkId: DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpace._members
  altText: SecuredEFCoreObjectSpace Members
---
XAF creates Object Spaces of the `SecuredEFCoreObjectSpace` type when an application calls the [SecuredEFCoreObjectSpaceProviderBuilderExtensions.AddSecuredEFCore](xref:DevExpress.ExpressApp.ApplicationBuilder.SecuredEFCoreObjectSpaceProviderBuilderExtensions.AddSecuredEFCore*) method at startup.

The following example demonstrates how to use @DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1 to create **SecuredEFCoreObjectSpace** in a non-XAF application. 

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
        IObjectSpace securedObjectSpace = objectSpaceProvider.CreateObjectSpace();
    }
}
```
***

You can find the full example in the following GitHub repository: [How to use the Integrated mode of the Security System in non-XAF applications (EF Core)](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/20.1.5+/EFCore).

[!include[more-information-on-object-spaces-and-providers](~/templates/more-information-on-object-spaces-and-providers.md)]
