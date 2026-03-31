---
uid: DevExpress.ExpressApp.Security.SecuredXPObjectSpace
name: SecuredXPObjectSpace
type: Class
summary: An [Object Space](xref:113707) for XPO-based applications that use the [Security System](xref:113366).
syntax:
  content: 'public class SecuredXPObjectSpace : XPObjectSpace, ISecuredObjectSpace'
seealso:
- linkId: DevExpress.ExpressApp.Security.SecuredXPObjectSpace._members
  altText: SecuredXPObjectSpace Members
---
XAF creates Object Spaces of the `SecuredXPObjectSpace` type if an application calls the @DevExpress.ExpressApp.ApplicationBuilder.SecuredObjectSpaceProviderBuilderExtensions.AddSecuredXpo* method at startup.

If you implement a custom `SecuredObjectSpaceProvider` with the @DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.CreateObjectSpace method overridden, make sure this method returns an object of the `SecuredXPObjectSpace` type instead of @DevExpress.ExpressApp.Xpo.XPObjectSpace.

In non-XAF applications, use @DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider to create `SecuredXPObjectSpace` as the following code snippet demonstrates: 

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
using System.Diagnostics;
// ...
class Program {
    static void Main() {
        // ...
        // Initialization. Create a Secured Data Store and Set Authentication Options
        AuthenticationStandard authentication = new AuthenticationStandard();
        SecurityStrategyComplex security = new SecurityStrategyComplex(typeof(ApplicationUser), typeof(PermissionPolicyRole), authentication, typesInfo);
        security.RegisterXPOAdapterProviders();
        SecuredObjectSpaceProvider objectSpaceProvider = new SecuredObjectSpaceProvider(security, dataStoreProvider, typesInfo, null);

        // Authentication. Log in as a 'User' with an Empty Password
        authentication.SetLogonParameters(new AuthenticationStandardLogonParameters(userName: "User", password: string.Empty));
        IObjectSpace loginObjectSpace = objectSpaceProvider.CreateObjectSpace();
        security.Logon(loginObjectSpace);

        // Authorization. Access and Manipulate Data/UI Based on User/Role Rights
        using(IObjectSpace securedObjectSpace = objectSpaceProvider.CreateObjectSpace()) {
            // User cannot read protected entities like PermissionPolicyRole.
        }
    }
}
```
***

You can find the full example in the following GitHub repository: [How to use the Integrated mode of the Security System in non-XAF applications (XPO)](https://github.com/DevExpress-Examples/XAF_Security_E4908/tree/22.2.4+/XPO).

[!include[more-information-on-object-spaces-and-providers](~/templates/more-information-on-object-spaces-and-providers.md)]
