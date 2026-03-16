---
uid: "403824"
title: Determine if the Current User Has Specific Permissions
owner: Yekaterina Kiseleva
seealso:
  - linkId: '113152'
---
# Determine if the Current User Has Specific Permissions

## Determine if a User Is an Administrator

1. Get the current user object as described in the following topic: [Get the Current User in Code](xref:113152).
2. Check if this user has an administrative role in the @DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.Roles collection.

# [C#](#tab/tabid-csharp)

```csharp{10-11}
using Microsoft.AspNetCore.Mvc;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// ...
[Route("api/[controller]")]
[ApiController]
public class CustomEndpointController : ControllerBase {
    [HttpGet]
    public IEnumerable<string> Get(ISecurityProvider securityProvider) {
        ISecurityUserWithRoles user = (ISecurityUserWithRoles)securityProvider.GetSecurity().User;
        bool isAdministativeRole = user.Roles.Any(r => ((PermissionPolicyRole)r).IsAdministrative);
        // ...
    }

}
```

***

## Determine if a User Has a Particular Role

### Use the IsUserInRole Extension Method

1. Get the current user object as described in the following topic: [Get the Current User in Code](xref:113152).
2. Call the `DevExpress.ExpressApp.Security.UserWithRolesExtensions.IsUserInRole(DevExpress.Persistent.Base.Security.IUserWithRoles,System.String)` method with the `"Manager"` parameter to check if the user has a role with this name.

# [C#](#tab/tabid-csharp)

```csharp{10-11}
using Microsoft.AspNetCore.Mvc;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// ...
[Route("api/[controller]")]
[ApiController]
public class CustomEndpointController : ControllerBase {
    [HttpGet]
    public IEnumerable<string> Get(ISecurityProvider securityProvider) {
        ISecurityUserWithRoles user = (ISecurityUserWithRoles)securityProvider.GetSecurity().User;
        bool isManager = user.IsUserInRole("Manager");
        // ...
    }
}
```

***

### Use the Current User's Roles Collection

Alternatively, you can inspect a user's [Roles](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.Roles) collection to determine if the user belongs to a certain role:

# [C#](#tab/tabid-csharp)

```csharp{10-11}
using Microsoft.AspNetCore.Mvc;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// ...
[Route("api/[controller]")]
[ApiController]
public class CustomEndpointController : ControllerBase {
    [HttpGet]
    public IEnumerable<string> Get(ISecurityProvider securityProvider) {
        ISecurityUserWithRoles user = (ISecurityUserWithRoles)securityProvider.GetSecurity().User;
        bool isManager = user.Roles.Any(r => r.Name == "Managers");
        // ...
    }
}
```

***

### Use Criteria Syntax (in Filters)

Use one of the following techniques to check for a user role in criteria syntax:

- You can use the [`IsCurrentUserInRole`](xref:113307) criteria function in your filters. For example: `IsCurrentUserInRole('Administrators')`.

- You can use Free Joins on the current user's Roles collection. For example: `[<PermissionPolicyRole>][Name='Managers' && Users[Oid=CurrentUserId()]]`


## Check if a User Has Permission to Perform a Specific Operation

### Permission to Edit the Application Model

1. Get the current user object as the following topic describes: [Get the Current User in Code](xref:113152).
2. Use the @DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.CanEditModel property to check if the user has permission to edit the Application Model.

# [C#](#tab/tabid-csharp)

```csharp{10-13}
using Microsoft.AspNetCore.Mvc;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// ...
[Route("api/[controller]")]
[ApiController]
public class CustomEndpointController : ControllerBase {
    [HttpGet]
    public IEnumerable<string> Get(ISecurityProvider securityProvider) {
        ISecurityUserWithRoles user = (ISecurityUserWithRoles)securityProvider.GetSecurity().User;
        if (user.Roles.Any(r => r.CanEditModel)) {
            // ...
        }
        // ...
    }
}
```

***

### Permission to Edit an Object of a Specific Type

1. Get the current user object as described in the following topic: [Get the Current User in Code](xref:113152).
2. Use the [IsGrantedExtensions.CanWrite](xref:DevExpress.ExpressApp.Security.IsGrantedExtensions.CanWrite``1(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace,System.String)) method to check if the user has permission to edit the `Department`'s `Office` property.

> [!Note]
> You can also use other @DevExpress.ExpressApp.Security.IsGrantedExtensions methods to check permissions for CRUD and navigate operations. You can check permissions for the current user, a specific user, or a particular role.

# [C#](#tab/tabid-csharp)

```csharp{10-13}
using Microsoft.AspNetCore.Mvc;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// ...
[Route("api/[controller]")]
[ApiController]
public class CustomEndpointController : ControllerBase {
    [HttpGet]
    public IEnumerable<string> Get(ISecurityProvider securityProvider) {
        ISecurityUserWithRoles user = (ISecurityUserWithRoles)securityProvider.GetSecurity().User;
        if (!securityStrategy.CanWrite<Department>(ObjectSpace, nameof(Department.Office))) {
            // ...
        }
        // ...
    }
}
```

***

[`ViewController`]: xref:DevExpress.ExpressApp.ViewController
[`Application`]: xref:DevExpress.ExpressApp.Controller.Application
[`SimpleAction`]: xref:DevExpress.ExpressApp.Actions.SimpleAction
[`Active`]: xref:DevExpress.ExpressApp.Actions.ActionBase.Active
[`SecurityStrategy`]: xref:DevExpress.ExpressApp.Security.SecurityStrategy
[`GetSecurityStrategy`]: xref:DevExpress.ExpressApp.Security.XafApplicationExtensions.GetSecurityStrategy(DevExpress.ExpressApp.XafApplication)
[`Roles`]: xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.Roles
[`IsAdministrative`]: xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.IsAdministrative
[`User`]: xref:DevExpress.ExpressApp.Security.SecurityStrategyBase.User
[`ISecurityUserWithRoles`]: xref:DevExpress.ExpressApp.Security.ISecurityUserWithRoles
[`CurrentUser`]: xref:DevExpress.ExpressApp.SecuritySystem.CurrentUser
[`Enabled`]: xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled
[`CanEditModel`]: xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.CanEditModel
[`CanWrite`]: xref:DevExpress.ExpressApp.Security.IsGrantedExtensions.CanWrite``1(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace,System.String)
