---
uid: "403850"
title: Execute Custom Operations on Endpoint Requests
---
# Execute Custom Operations on Endpoint Requests

You can add custom logic to methods that process HTTP requests. For this purpose, modify the built-in **Data Service** and register your custom implementation. This topic describes the basic steps you need to take:  

- [Create a Custom Data Service](#create-a-custom-data-service)
- [Override Endpoint Methods](#override-endpoint-methods)
- [Register Your Custom Data Service](#register-your-custom-data-service)

## Create a Custom Data Service

To implement a custom data service, create a class that extends the standard `DataService` class available in the following namespace: `DevExpress.ExpressApp.WebApi.Services`.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp.Core;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.WebApi.Services;
// ...
public class CustomDataService : DataService {
    public CustomDataService(IObjectSpaceFactory objectSpaceFactory, ITypesInfo typesInfo,
        IObjectDeltaHandler objectDeltaHandler) : base(objectSpaceFactory, typesInfo, objectDeltaHandler) { }
    protected override T CreateObject<T>(IObjectDelta<T> delta, IObjectSpace objectSpace) {
        return base.CreateObject(delta, objectSpace);
    }
}
```
***

## Override Endpoint Methods

To customize an endpoint method in your custom data service, override the corresponding **protected** method of the base class and add your custom logic to the method's implementation:

# [C#](#tab/tabid-csharp)
    
```csharp
// GET
protected override IQueryable<T> GetObjectsQuery<T>(IObjectSpace objectSpace) {
    if(typeof(T) == typeof(ApplicationUser)) {
        // Custom logic
    }
    return base.GetObjectsQuery<T>();
}

// PATCH
protected override T PatchObject<T>(string key, IObjectDelta<T> delta, 
 IObjectSpace objectSpace) where T : class {
    var original = GetObjectByKey<T>(key);
    // Custom logic before modifications
    delta.Patch(original);
    // Custom logic after modifications
    objectSpace.CommitChanges();
    return original;
}
// ...

```
***

### Access Object Space

The base `DataService` class manages Object Spaces internally and passes their correct instances to overridden methods based on the generic type parameter:

# [C#](#tab/tabid-csharp)
    
```csharp
// The method receives an Object Space for the type T
protected override IQueryable<T> GetObjectsQuery<T>(IObjectSpace objectSpace) { /** **/ }
```
***

To get an Object Space for a type that is unrelated to the current method, call the base class's `GetObjectSpace<T>` method:

# [C#](#tab/tabid-csharp)
    
```csharp
var userObjectSpace = GetObjectSpace<User>();
```
***

Keep in mind that you should not manually dispose of Object Spaces obtained through `GetObjectSpace`. The data service correctly disposes of them in the base `Dispose` method implementation.

If required, you can also use the `IObjectSpaceFactory` available through the data service class constructor to create a new Object Space. In this case, it is your responsibility to dispose of the created Object Space. To do it safely, we recommend that you override the data service's base `Dispose` method and use it to call the `Dispose` method for all manually created Object Spaces.

```csharp{4,7-10}
public class CustomDataService : DataService {
    private readonly IObjectSpace myTypeObjectSpace;
    public CustomDataService(IObjectSpaceFactory objectSpaceFactory, ITypesInfo typesInfo, IObjectDeltaHandler objectDeltaHandler) : base(objectSpaceFactory, typesInfo, objectDeltaHandler) { 
        myTypeObjectSpace = objectSpaceFactory.CreateObjectSpace(typeof(MyType));
    }
    // ...
    public override void Dispose() {
        base.Dispose();
        myTypeObjectSpace.Dispose();
    }
}
```

## Register Your Custom Data Service

Use the code below to register your custom data service. Add the registration line to the `ConfigureServices` method, after the `AddXafWebApi()` method call.

**File:** _MySolution.WebApi\Startup.cs_ (_MySolution.Blazor.Server\Startup.cs_)

# [C#](#tab/tabid-csharp)

```csharp{10} 
namespace MySolution.WebApi {
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            services.AddXafWebApi(builder => {
                // In XPO applications, uncomment the following line:
                // builder.AddXpoServices();
                // ...
            }, Configuration);
            services.AddScoped<IDataService, CustomDataService>();
        }
        // ...
    }
}
```

***

