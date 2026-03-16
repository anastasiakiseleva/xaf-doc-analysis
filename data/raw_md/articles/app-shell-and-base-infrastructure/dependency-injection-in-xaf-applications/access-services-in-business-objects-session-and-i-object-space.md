---
uid: "404403"
title: Write Business Object Code that Accesses Services (Use Session or IObjectSpace)
owner: Anastasiya Kisialeva
seealso:
  - linkId: "404430"
  - linkId: "113152"
---
# Write Business Object Code that Accesses Services (Use Session or IObjectSpace)

You can obtain an @System.IServiceProvider instance when you write Business Object code. This functionality is available in the following cases:

* XAF ASP.NET Core Blazor and Windows Forms applications that use XAF Application Builder. 
* XAF Web API applications created by [Template Kit](xref:405447).
 
## XPO: Use Session.ServiceProvider

The `Session` class has constructors with the `IServiceProvider` parameter. XAF passes the `IServiceProvider` object when `IObjectSpace` creates a new instance of the `Session` object, if the `IServiceProvider` is available.

You can write code Business Object code that obtains any service. See the following example.

The code snippet below uses the `IServiceProvider` instance to obtain the `ISecurityStrategyBase` service. The service helps specify the `CreatedBy` property automatically when a new object is created. (Note: use this approach instead of the `SecuritySystem` static class. That class is outdated and cannot be used in XAF Web API applications.)

```csharp{10-13,18}
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;

public class Task : BaseObject {
    ApplicationUser? createdBy;
    public Task(Session session) : base(session) { }

    ApplicationUser GetCurrentUser() { 
        return Session.GetObjectByKey<ApplicationUser>( 
            Session.ServiceProvider.GetRequiredService<ISecurityStrategyBase>().UserId);
    }

    protected override void OnSaving() {
        base.OnSaving();
        if (Session.IsNewObject(this)) {
            SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
    }

    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public ApplicationUser? CreatedBy {
        get => createdBy;
        set => SetPropertyValue(nameof(CreatedBy), ref createdBy, value);
    }
} 
```

If you create a new instance of `Session`/`UnitOfWork` in your custom code, pass the `IServiceProvider` instance to the constructor as shown in following code sample:

```csharp
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;

public class Task : BaseObject {
    ApplicationUser? createdBy;
    public Task(Session session) : base(session) { }
     //...
    protected override void OnSaving() {
        base.OnSaving();
        using(var uow = new UnitOfWork(Session.ServiceProvider, Session.DataLayer)) {
            //...
            uow.CommitChanges();
        }
    }
}
```

## EF Core: Use IObjectSpace.ServiceProvider

If you develop an XAF Entity Framework Core application and write Business Object code, use `IObjectSpace.ServiceProvider` to obtain the `IServiceProvider` object. You can obtain the `IObjectSpace` instance if the `IObjectSpaceLink` interface is implemented or if the Business Object class is a descendant of the @DevExpress.Persistent.BaseImpl.EF.BaseObject class that already implements the `IObjectSpaceLink` interface. 

You can write code Business Object code that obtains any service. See the following example.

The code snippet below uses the `IServiceProvider` instance to obtain the `ISecurityStrategyBase` service. The service helps specify the `CreatedBy` property automatically when a new object is created. (Note: use this approach instead of the `SecuritySystem` static class. That class is outdated and cannot be used in XAF Web API applications.)

```csharp{10-13,18}
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.EF;
using Microsoft.Extensions.DependencyInjection;
using WebApiEFAdditional.Module.BusinessObjects;

public class Task : BaseObject {
    [ModelDefault(nameof(IModelCommonMemberViewItem.AllowEdit), "False")]
    public virtual ApplicationUser? CreatedBy { get; set; }

    ApplicationUser GetCurrentUser() {
        return ObjectSpace.GetObjectByKey<ApplicationUser>(
            ObjectSpace.ServiceProvider.GetRequiredService<ISecurityStrategyBase>().UserId);
    }

    public override void OnSaving() {
        base.OnSaving();
        if (ObjectSpace.IsNewObject(this)) {
            SetPropertyValueWithSecurityBypass(nameof(CreatedBy), GetCurrentUser());
        }
    }
}
```
> [!NOTE]
> You cannot use this technique in an Entity Framework Core Middle Tier Server application, since XAF does not use `IObjectSpace` for operations with Business Objects on the server side.

You can use the `IObjectSpace.ServiceProvider` property in any other part of an XAF application, but usually the `XafApplication` object is available, and you can use the `XafApplication.ServiceProvider` property instead. 

### Non-Persistent Objects

The `NonPersistentObjectSpaceProvider` class has constructors with the `IServiceProvider` parameter. You can obtain an `IObjectSpace` instance in a non-persistent Business Object class if it implements the `IObjectSpaceLink` interface. XAF passes the `IServiceProvider` to the new `NonPersistentObjectSpaceProvider` when it is created. If you create a new `NonPersistentObjectSpaceProvider` instance manually, you need to pass the `IServiceProvider` in its constructor to support dependency injection.
