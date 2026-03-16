---
uid: DevExpress.ExpressApp.ApplicationBuilder.NonPersistentObjectSpaceProviderOptions.CustomCreateObjectSpaceProvider
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
You can use this property to create a custom [Object Space](xref:113707) provider used to manage [non-persistent objects](xref:116516) in WinForms, Blazor, and WebAPI applications.

# [C# (Integrated security)](#tab/tabid-csharp-int)
```csharp
builder.ObjectSpaceProviders 
    .AddNonPersistent((serviceProvider, options) => { 
        options.CustomCreateObjectSpaceProvider = (context) => { 
            return new MyCustomNonPersistentObjectSpaceProvider(...); 
        }; 
    }); 
```
***