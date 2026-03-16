---
uid: DevExpress.ExpressApp.ApplicationBuilder.XPObjectSpaceProviderOptions.CustomCreateObjectSpaceProvider
name: CustomCreateObjectSpaceProvider
type: Property
summary: Allows you to create a custom [Object Space provider](xref:DevExpress.ExpressApp.IObjectSpaceProvider).
syntax:
  content: public Func<CustomCreateObjectSpaceProviderContext, IObjectSpaceProvider> CustomCreateObjectSpaceProvider { get; set; }
  parameters: []
  return:
    type: System.Func{DevExpress.ExpressApp.CustomCreateObjectSpaceProviderContext,DevExpress.ExpressApp.IObjectSpaceProvider}
    description: A delegate that accepts an instance of @DevExpress.ExpressApp.CustomCreateObjectSpaceProviderContext and must return the custom [Object Space](xref:113707) provider.
seealso:
- linkId: "405388"
---
You can use this property to create a custom [Object Space](xref:113707) provider in WinForms, Blazor, and WebAPI applications that use [Integrated Security](xref:113436) or no security tier.

# [C# (Integrated security)](#tab/tabid-csharp-int)
```csharp
builder.ObjectSpaceProviders 
    .AddSecuredXpo((serviceProvider, options) => { 
        options.ConnectionString = ...; 
        options.EnablePoolingInConnectionString = ...; 
        options.ThreadSafe = ...; 
        // ... 
        var dataStoreProvider = XPObjectSpaceProvider.GetDataStoreProvider(options.ConnectionString, null, true); 
        options.CustomCreateObjectSpaceProvider = (context) => { 
            var selectDataSecurityProvider = context.ServiceProvider.GetRequiredService<ISelectDataSecurityProvider>(); 
            return new MyCustomObjectSpaceProvider(context.ServiceProvider, selectDataSecurityProvider, dataStoreProvider, ...); 
        }; 
    }) 
```
# [C# (No security)](#tab/tabid-csharp-sec)
```csharp
builder.ObjectSpaceProviders 
    .AddXpo((serviceProvider, options) => { 
        options.ConnectionString = ...; 
        options.EnablePoolingInConnectionString = ...; 
        options.ThreadSafe = ...; 
        // ... 
        var dataStoreProvider = XPObjectSpaceProvider.GetDataStoreProvider(options.ConnectionString, null, true); 
        options.CustomCreateObjectSpaceProvider = (context) => { 
            return new MyCustomObjectSpaceProvider(context.ServiceProvider, dataStoreProvider, ...); 
        }; 
    }) 
```
***