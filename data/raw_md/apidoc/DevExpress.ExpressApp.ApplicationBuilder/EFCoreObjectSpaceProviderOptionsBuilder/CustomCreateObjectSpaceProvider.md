---
uid: DevExpress.ExpressApp.ApplicationBuilder.EFCoreObjectSpaceProviderOptionsBuilder.CustomCreateObjectSpaceProvider
name: CustomCreateObjectSpaceProvider
type: Property
summary: Allows you to create a custom [Object Space](xref:113707) provider.
syntax:
  content: public Func<CustomCreateObjectSpaceProviderContext, IObjectSpaceProvider> CustomCreateObjectSpaceProvider { get; set; }
  parameters: []
  return:
    type: System.Func{DevExpress.ExpressApp.CustomCreateObjectSpaceProviderContext,DevExpress.ExpressApp.IObjectSpaceProvider}
    description: A delegate that accepts an instance of @DevExpress.ExpressApp.CustomCreateObjectSpaceProviderContext and must return the custom [Object Space](xref:113707) provider.
seealso:
- linkId: "405388"
---
You can use this delegate to create a custom [Object Space](xref:113707) provider in WinForms, Blazor, and WebAPI applications that use [Integrated Security](xref:113436), [Middle Tier Security](xref:404389), or no security.

# [C# (Integrated security)](#tab/tabid-csharp-int)
```csharp
builder.ObjectSpaceProviders 
    .AddSecuredEFCore(o => { 
        // ... 
        o.CustomCreateObjectSpaceProvider = (context) => { 
            var selectDataSecurityProvider = context.ServiceProvider.GetRequiredService<ISelectDataSecurityProvider>(); 
            var dbContextFactory = context.ServiceProvider.GetRequiredService<IDbContextFactory<MainDemoDbContext>>(); 
            return new MyCustomEFCoreObjectSpaceProvider<ApplicationDbContext>(...); 
        }; 
    }) 
    .WithDbContext<ApplicationDbContext>(...) 
```
# [C# (No security or middle-tier security)](#tab/tabid-csharp-sec)
```csharp
builder.ObjectSpaceProviders 
    .AddEFCore(o => { 
        // ... 
        o.CustomCreateObjectSpaceProvider = (context) => { 
            var dbContextFactory = context.ServiceProvider.GetRequiredService<IDbContextFactory<MainDemoDbContext>>(); 
            return new MyCustomEFCoreObjectSpaceProvider<ApplicationDbContext>(...); 
        }; 
    }) 
    .WithDbContext<ApplicationDbContext>(...)
```
***