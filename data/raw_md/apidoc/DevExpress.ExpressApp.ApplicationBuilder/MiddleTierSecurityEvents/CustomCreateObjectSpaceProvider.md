---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityEvents.CustomCreateObjectSpaceProvider
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
You can use this property to create a custom [Object Space](xref:113707) provider in WinForms applications that use [Middle Tier Security](xref:404389).

# [C#](#tab/tabid-csharp-int)
```csharp
builder.Security 
    .UseMiddleTierMode(options => { 
        options.BaseAddress = new Uri("http://localhost:5000/"); 
        options.WaitForMiddleTierServerReady(); 
        options.Events.OnHttpClientCreated = /* ... */ 
        options.Events.OnCustomAuthenticate = /* ... */ 
        // ... 
        options.Events.CustomCreateObjectSpaceProvider = (context) => { 
            return new MyCustomMiddleTierObjectSpaceProvider(context.ServiceProvider, ...); 
        }; 
    }) 
```
***