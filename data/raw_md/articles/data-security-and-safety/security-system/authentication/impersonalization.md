---
uid: "404929"
title: Execute Operations on Another User's Behalf (User Impersonation)
owner: Eugeniy Burmistrov
seealso:
- linkId: 119065
---

# Execute Operations on Another User's Behalf (User Impersonation)

> [!important]
> This functionality is supported only for ASP.NET Core-based applications (Blazor and Web API Service) and is not available for applications that use a [Middle Tier server](xref:404389).

This topic describes how to use a nested scope and a service user account to safely create system-level business objects (such as metrics) without exposing them to end users.

## Scenario

Consider a controller action that executes custom logic. You want to collect some metrics within this action and persist them as business objects. For instance, you can create a class that stores how many times the action is executed per month:

# [C# (EF Core)](#tab/tabid-csharp-efcore)

```csharp
public class MyActionPerMonth : BaseObject {
    public virtual int ViewCount { get; set; }
    public virtual int Year { get; set; }
    public virtual int Month { get; set; }
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
public class MyActionPerMonth : BaseObject {
    private int viewCount;
    private int year;
    private int month;

    public MyActionPerMonth(Session session)
        : base(session) {
    }

    public int ViewCount {
        get { return viewCount; }
        set { SetPropertyValue(nameof(ViewCount), ref viewCount, value); }
    }

    public int Year {
        get { return year; }
        set { SetPropertyValue(nameof(Year), ref year, value); }
    }

    public int Month {
        get { return month; }
        set { SetPropertyValue(nameof(Month), ref month, value); }
    }
}
```

***

## Why Use a Service User

Metric objects should not be editable by application users. For this reason, you should not create them directly in the controller using the current user context.

Instead, create a service user with the required permissions and perform all metric-related operations on behalf of this account.

## Implementation Details

To execute code under a service user:

1. Create a nested service scope.
2. Programmatically sign in as the service user within this scope.
3. Obtain the scope's `IServiceProvider`.
4. Use this service provider to perform the required operations (for instance, create and save metric objects).

# [C#](#tab/tabid-csharp)

```csharp{13,18-34}
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
// ...
public partial class MyController : ViewController<ListView> {
    SimpleAction myAction;
    IServiceScopeFactory serviceScopeFactory;

    [ActivatorUtilitiesConstructor]
    public MyController(IServiceProvider serviceProvider) : this() {
        // ...
        myAction.Execute += MyAction_Execute;
        serviceScopeFactory = serviceProvider.GetRequiredService<IServiceScopeFactory>();
    }
    // ...
    private void MyAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        // ...
        // Create a nested service scope.
        using IServiceScope impersonalizationScope = serviceScopeFactory.CreateScope();

        // Use UserManager to obtain the ServiceUser object.
        using IObjectSpace nonSecuredObjectSpace = impersonalizationScope.ServiceProvider
            .GetRequiredService<INonSecuredObjectSpaceFactory>().CreateNonSecuredObjectSpace<ApplicationUser>();
        ApplicationUser serviceUser = impersonalizationScope.ServiceProvider
            .GetRequiredService<UserManager>().FindUserByName<ApplicationUser>(nonSecuredObjectSpace, "ServiceUser");

        // Sign in as ServiceUser to the nested scope.
        SignInManager signInManager = impersonalizationScope.ServiceProvider.GetService<SignInManager>();
        signInManager.SignIn(serviceUser);

        // Obtain an Object Space from the nested scope and use this Object Space
        // to manipulate business objects on ServiceUser's behalf.
        using IObjectSpace objectSpace = impersonalizationScope.ServiceProvider
            .GetRequiredService<IObjectSpaceFactory>().CreateObjectSpace<MyActionPerMonth>();

        var actionThisMonth = objectSpace.FirstOrDefault<MyActionPerMonth>(
            r => r.Year == DateTime.Now.Year
                && r.Month == DateTime.Now.Month);

        if (actionThisMonth == null) {
            actionThisMonth = objectSpace.CreateObject<MyActionPerMonth>();
            actionThisMonth.Year = DateTime.Now.Year;
            actionThisMonth.Month = DateTime.Now.Month;
            actionThisMonth.ViewCount = 0;
        }

        actionThisMonth.ViewCount += 1;
        objectSpace.CommitChanges();
    }
}
```

***

## Multi-Tenant Application Specifics

If your application supports [multiple tenants](xref:404436), configure the nested scope as follows:

* Use the parent scope's Tenant Provider to obtain the current tenant ID.
* Assign this tenant ID to the nested scope's Tenant Provider. This step is required because a new scope is treated as single-tenant by default.
If you skip this step, the Tenant Provider's `TenantName` property returns `null`.
* Use the nested scope's `TenantName` property to obtain the current tenant name. Specify the fully qualified service user name based on this tenant name when signing in.


# [C#](#tab/tabid-csharp)

```csharp{26-38}
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.MultiTenancy;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
// ...
public partial class MyController : ViewController<ListView> {
    SimpleAction myAction;
    IServiceScopeFactory serviceScopeFactory;
    IServiceProvider serviceProvider;
    ITenantProvider tenantProvider;

    [ActivatorUtilitiesConstructor]
    public MyController(IServiceProvider serviceProvider) : this() {
        // ...
        myAction.Execute += MyAction_Execute;

        this.serviceProvider = serviceProvider;
        serviceScopeFactory = serviceProvider.GetRequiredService<IServiceScopeFactory>();
        tenantProvider = serviceProvider.GetRequiredService<ITenantProvider>();
    }
    // ...
    private void MyAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        // ...
        using IServiceScope impersonalizationScope = serviceScopeFactory.CreateScope();

        // Assign the current tenant's ID to the nested scope's ITenantProvider.TenantId
        ITenantProvider impersonalizationScopeTenantProvider =
            impersonalizationScope.ServiceProvider.GetRequiredService<ITenantProvider>();
        impersonalizationScopeTenantProvider.TenantId = tenantProvider.TenantId;

        // Use UserManager to obtain the current tenant's ServiceUser object.
        using IObjectSpace nonSecuredObjectSpace = impersonalizationScope.ServiceProvider
            .GetRequiredService<INonSecuredObjectSpaceFactory>().CreateNonSecuredObjectSpace<ApplicationUser>();
        ApplicationUser serviceUser = impersonalizationScope.ServiceProvider
            .GetRequiredService<UserManager>().FindUserByName<ApplicationUser>(
                nonSecuredObjectSpace, 
                String.Format("{0}@{1}", "ServiceUser", tenantProvider.TenantName)
            );

        SignInManager signInManager = impersonalizationScope.ServiceProvider.GetService<SignInManager>();
        signInManager.SignIn(serviceUser);

        using IObjectSpace objectSpace = impersonalizationScope.ServiceProvider
            .GetRequiredService<IObjectSpaceFactory>().CreateObjectSpace<MyActionPerMonth>();

        var actionThisMonth = objectSpace.FirstOrDefault<MyActionPerMonth>(
            r => r.Year == DateTime.Now.Year
                && r.Month == DateTime.Now.Month);

        if (actionThisMonth == null) {
            actionThisMonth = objectSpace.CreateObject<MyActionPerMonth>();
            actionThisMonth.Year = DateTime.Now.Year;
            actionThisMonth.Month = DateTime.Now.Month;
            actionThisMonth.ViewCount = 0;
        }

        actionThisMonth.ViewCount += 1;
        objectSpace.CommitChanges();
    }
}
```

***
