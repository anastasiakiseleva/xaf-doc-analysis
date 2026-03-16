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

A newly created XAF application uses no security. To enable the **SecurityStrategyComplex** security strategy, invoke the Application Designer and drag the **SecurityStrategyComplex** component from the **Toolbox**'s **DX.<:xx.x:>: XAF Security** category to the designer's **Security** pane.

![Security_UseSecurityStrategyComplex](~/images/security_usesecuritystrategycomplex116998.png)

You can specify a custom user and role type by changing the [SecurityStrategy.UserType](xref:DevExpress.ExpressApp.Security.SecurityStrategy.UserType) and [SecurityStrategyComplex.RoleType](xref:DevExpress.ExpressApp.Security.SecurityStrategyComplex.RoleType) values in the **Properties** window.

![Security_SetCustomUserType](~/images/security_setcustomusertype117028.png)

Then, specify the authentication type that will accompany the security strategy. Drag either the [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard) or [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) component from the toolbox to the **Security** pane of the designer. You can also use a custom authentication (see [](xref:404264)).

![Security_DesignerAuthenticationSimple](~/images/security_designerauthenticationsimple117033.png)

Alternatively, you can enable the **SecurityStrategyComplex** Security Strategy in code. It is required to instantiate the **SecurityStrategyComplex** class and assign this instance to the [XafApplication.Security](xref:DevExpress.ExpressApp.XafApplication.Security) property. In a Windows Forms application project, modify the **Program.cs** file in the following manner.

# [C#](#tab/tabid-csharp)

```csharp
public static void Main(string[] arguments) {
    MySolutionWinApplication winApplication = new MySolutionWinApplication();
    winApplication.Security = 
        new SecurityStrategyComplex(typeof(ApplicationUser), typeof(PermissionPolicyRole), 
            new AuthenticationStandard());
    // ...
}
```

***

As a result, in a WinForms application you can see the User, Role, and My Details navigation items. The active user name is displayed in the status bar.![Tutorial_Security_ActiveDir](~/images/tutorial_security_activedir117116.png)
