---
uid: "405388"
title: 'Custom Object Space Provider'
---
# Custom Object Space Provider

Follow the steps below to add a custom [Object Space](xref:113707) provider to your application:
* Create a custom object space class
* Create a custom object space provider class
* Configure your application to use custom object space provider

## 1. Create a Custom Object Space Class

Create a custom object space class and override the methods you want to customize. The following examples customize the `DoCommit` method: 

# [EF Core](#tab/tabid-ef-core)
```csharp
// integrated security 
public class MyCustomSecuredEFCoreObjectSpace : SecuredEFCoreObjectSpace { 
    public MyCustomSecuredEFCoreObjectSpace(ITypesInfo typesInfo, IEntityStore entityStore, Func<DbContext> createDbContext, ISecurityStrategyBase security)  
        : base(typesInfo, entityStore, createDbContext, security) { } 
    protected override void DoCommit() { 
        // Write your custom code here or override other methods.  
        base.DoCommit(); 
    } 
} 

// no security or middle-tier security 
public class MyCustomEFCoreObjectSpace : EFCoreObjectSpace { 
    public MyCustomEFCoreObjectSpace(ITypesInfo typesInfo, IEntityStore entityStore, Func<DbContext> createDbContext)  
        : base(typesInfo, entityStore, createDbContext) { } 
    protected override void DoCommit() { 
        // Write your custom code here or override other methods.  
        base.DoCommit(); 
    } 
} 
```

# [XPO](#tab/tabid-xpo)
```csharp
// integrated security
public class MyCustomSecuredXPObjectSpace : SecuredXPObjectSpace {
    public MyCustomSecuredXPObjectSpace(ITypesInfo typesInfo, XpoTypeInfoSource xpoTypeInfoSource, CreateUnitOfWorkHandler createUnitOfWorkDelegate, ISecurityStrategyBase security)
        : base(typesInfo, xpoTypeInfoSource, createUnitOfWorkDelegate, security) { }
    protected override void DoCommit() {
        // Write your custom code here or override other methods.  
        base.DoCommit();
    }
}

// middle-tier security
public class MyCustomXPObjectSpace : XPObjectSpace {
    public MyCustomXPObjectSpace(ITypesInfo typesInfo, XpoTypeInfoSource xpoTypeInfoSource, CreateUnitOfWorkHandler createUnitOfWorkDelegate)
        : base(typesInfo, xpoTypeInfoSource, createUnitOfWorkDelegate) { }
    protected override void DoCommit() {
        // Write your custom code here or override other methods.  
        base.DoCommit();
    }
}

// no security
public class MyCustomXPObjectSpace : XPObjectSpace {
    public MyCustomXPObjectSpace(ITypesInfo typesInfo, XpoTypeInfoSource xpoTypeInfoSource, CreateUnitOfWorkHandler createUnitOfWorkDelegate)
        : base(typesInfo, xpoTypeInfoSource, createUnitOfWorkDelegate) { }
    protected override void DoCommit() {
        // Write your custom code here or override other methods.  
        base.DoCommit();
    }
}
```

# [Non-Persistent](#tab/tabid-non-persistent)
```csharp
public class MyCustomNonPersistentObjectSpace : NonPersistentObjectSpace {
    public MyCustomNonPersistentObjectSpace(IServiceProvider serviceProvider, ITypesInfo typesInfo, IEntityStore entityStore) 
        : base(serviceProvider, typesInfo, entityStore) { }
    protected override void DoCommit() {
        // Write your custom code here or override other methods.  
        base.DoCommit();
    }
}

```
***

## 2. Create a Custom Object Space Provider Class

Create a custom object space provider class. Override the `CreateObjectSpaceCore` method (`CreateObjectSpace` for non-persistent object space provider) to return your custom object space instance.

# [EF Core](#tab/tabid-ef-core)
```csharp
// integrated security
public class MyCustomSecuredEFCoreObjectSpaceProvider<TDbContext>
    : SecuredEFCoreObjectSpaceProvider<TDbContext> where TDbContext : DbContext {
    readonly ISelectDataSecurityProvider selectDataSecurityProvider;
    public MyCustomSecuredEFCoreObjectSpaceProvider(ISelectDataSecurityProvider selectDataSecurityProvider, IDbContextFactory<TDbContext> dbContextFactory) 
        : base(selectDataSecurityProvider, dbContextFactory) {
        this.selectDataSecurityProvider = selectDataSecurityProvider;
    }
    protected override EFCoreObjectSpace CreateObjectSpaceCore() {
        return new MyCustomSecuredEFCoreObjectSpace(TypesInfo, EntityStore, CreateDbContext, (ISecurityStrategyBase)selectDataSecurityProvider);
    }
}

// no security or middle-tier security 
public class MyCustomEFCoreObjectSpaceProvider<TDbContext> 
    : EFCoreObjectSpaceProvider<TDbContext> where TDbContext: DbContext {
    public MyCustomEFCoreObjectSpaceProvider(IDbContextFactory<TDbContext> dbContextFactory)
        : base(dbContextFactory) { }
    protected override EFCoreObjectSpace CreateObjectSpaceCore() {
        return new MyCustomEFCoreObjectSpace(TypesInfo, EntityStore, CreateDbContext);
    }
}
```

# [XPO](#tab/tabid-xpo)
```csharp
// integrated security
public class MyCustomSecuredObjectSpaceProvider : SecuredObjectSpaceProvider {
    public MyCustomSecuredObjectSpaceProvider(IServiceProvider serviceProvider, ISelectDataSecurityProvider selectDataSecurityProvider, IXpoDataStoreProvider dataStoreProvider)
        : base(selectDataSecurityProvider, dataStoreProvider, true) {
    }
    protected override IObjectSpace CreateObjectSpaceCore() {
        var securityStrategy = ServiceProvider.GetRequiredService<ISecurityStrategyBase>();
        return new MyCustomSecuredXPObjectSpace(TypesInfo, XpoTypeInfoSource, () => CreateUnitOfWork(DataLayer), securityStrategy);
    }
}

// middle-tier security
public class MyCustomMiddleTierObjectSpaceProvider : MiddleTierServerObjectSpaceProvider {
    public MyCustomMiddleTierObjectSpaceProvider(IServiceProvider serviceProvider)
        : base(serviceProvider,
            (WebApiSecuredDataServerClient)serviceProvider.GetRequiredService<WebApiSecuredDataServerClientBase>(),
            serviceProvider.GetRequiredService<IMiddleTierXpoTypeInfoSourceProvider>()) {  }
   
 protected override XPObjectSpace CreateObjectSpaceCore(ITypesInfo typesInfo, XpoTypeInfoSource xpoTypeInfoSource, CreateUnitOfWorkHandler createUnitOfWork) {
        return new MyCustomXPObjectSpace(TypesInfo, XpoTypeInfoSource, () => CreateUnitOfWork(DataLayer));
    }
}

// no security
public class MyCustomObjectSpaceProvider : XPObjectSpaceProvider {
    public MyCustomObjectSpaceProvider(IServiceProvider serviceProvider, IXpoDataStoreProvider dataStoreProvider)
        : base(serviceProvider, dataStoreProvider, true) {
    }
    protected override IObjectSpace CreateObjectSpaceCore() {
        return new MyCustomXPObjectSpace(TypesInfo, XpoTypeInfoSource, () => CreateUnitOfWork(DataLayer));
    }
}
```

# [Non-Persistent](#tab/tabid-non-persistent)
```csharp
public class MyCustomNonPersistentObjectSpaceProvider : NonPersistentObjectSpaceProvider {
    public MyCustomNonPersistentObjectSpaceProvider(IServiceProvider serviceProvider) 
        : base(serviceProvider) { }
    public override IObjectSpace CreateObjectSpace() {
        return new NonPersistentObjectSpace(ServiceProvider, TypesInfo, EntityStore);
    }
}
```
***

## 3. Configure Your Application to Use Custom Object Space Provider

Use the `CustomCreateObjectSpaceProvider` method to add your custom object space provider to the application.

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [EF Core](#tab/tabid-ef-core)
```csharp
// integrated security
builder.ObjectSpaceProviders
    .AddSecuredEFCore(o => {
        // ...
        o.CustomCreateObjectSpaceProvider = (context) => {
            var selectDataSecurityProvider = context.ServiceProvider.GetRequiredService<ISelectDataSecurityProvider>();
            var dbContextFactory = context.ServiceProvider.GetRequiredService<IDbContextFactory<MainDemoDbContext>>();
            return new MyCustomSecuredEFCoreObjectSpaceProvider<ApplicationDbContext>(selectDataSecurityProvider, dbContextFactory);
        };
    })
    .WithDbContext<ApplicationDbContext>(...)

// no security or middle-tier security 
builder.ObjectSpaceProviders
    .AddEFCore(o => {
        // ...
        o.CustomCreateObjectSpaceProvider = (context) => {
            var dbContextFactory = context.ServiceProvider.GetRequiredService<IDbContextFactory<MainDemoDbContext>>();
            return new MyCustomEFCoreObjectSpaceProvider<ApplicationDbContext>(dbContextFactory);
        };
    })
    .WithDbContext<ApplicationDbContext>(...)
```

# [XPO](#tab/tabid-xpo)
```csharp
// integrated security
var dataStoreProviderManager = new DevExpress.ExpressApp.ApplicationBuilder.DataStoreProviderManager();
builder.ObjectSpaceProviders
    .AddSecuredXpo((serviceProvider, options) => {
        options.ConnectionString = ...;
        // ...
        options.CustomCreateObjectSpaceProvider = (context) => {
            var selectDataSecurityProvider = context.ServiceProvider.GetRequiredService<ISelectDataSecurityProvider>();
            var dataStoreProvider = dataStoreProviderManager.GetSharedDataStoreProvider(options.ConnectionString, true);
            return new MyCustomSecuredObjectSpaceProvider(context.ServiceProvider, selectDataSecurityProvider, dataStoreProvider);
        };
    })

// middle-tier security
builder.Security
    .UseMiddleTierMode(options => {
        options.BaseAddress = new Uri("http://localhost:5000/");
        // ...
        options.Events.CustomCreateObjectSpaceProvider = (context) => {
            return new MyCustomMiddleTierObjectSpaceProvider(context.ServiceProvider, ...);
        };
    })

// no security
var dataStoreProviderManager = new DevExpress.ExpressApp.ApplicationBuilder.DataStoreProviderManager();
builder.ObjectSpaceProviders
    .AddXpo((serviceProvider, options) => {
        options.ConnectionString = ...;
        // ...
        options.CustomCreateObjectSpaceProvider = (context) => {
            var dataStoreProvider = dataStoreProviderManager.GetSharedDataStoreProvider(options.ConnectionString, true);
            return new MyCustomObjectSpaceProvider(context.ServiceProvider, dataStoreProvider);
        };
    })
```
# [Non-Persistent](#tab/tabid-non-persistent)
```csharp
builder.ObjectSpaceProviders
    .AddNonPersistent((serviceProvider, options) => {
        options.CustomCreateObjectSpaceProvider = (context) => {
            return new MyCustomNonPersistentObjectSpaceProvider(context.ServiceProvider);
        };
    });
```
***

## XPO ORM-specific Object Space Provider and Data Store Customizations

* [How to use XPO data layer caching in XAF](https://supportcenter.devexpress.com/ticket/details/k18356/how-to-use-xpo-data-layer-caching-in-xaf)
* [How to customize the underlying database provider options and data access behavior in XAF](https://supportcenter.devexpress.com/ticket/details/e411/how-to-customize-the-underlying-database-provider-options-and-data-access-behavior-in-xaf)


[`SecuredEFCoreObjectSpace`]: xref:DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpace
[`ITypesInfo`]: xref:DevExpress.ExpressApp.DC.ITypesInfo
[`ISecurityStrategyBase`]: xref:DevExpress.ExpressApp.Security.ISecurityStrategyBase
[`EFCoreObjectSpace`]: xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace
[`SecuredXPObjectSpace`]: xref:DevExpress.ExpressApp.Security.SecuredXPObjectSpace
[`XPObjectSpace`]: xref:DevExpress.ExpressApp.Xpo.XPObjectSpace
[`NonPersistentObjectSpace`]: xref:DevExpress.ExpressApp.NonPersistentObjectSpace
[`SecuredEFCoreObjectSpaceProvider`]: xref:DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1
[`EFCoreObjectSpaceProvider`]: xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpaceProvider`1
[`SecuredObjectSpaceProvider`]: xref:DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider
[`XPObjectSpaceProvider`]: xref:DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider
[`NonPersistentObjectSpaceProvider`]: xref:DevExpress.ExpressApp.NonPersistentObjectSpaceProvider