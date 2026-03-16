---
uid: DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated
name: OnObjectSpaceCreated
type: Property
summary: Occurs after an [Object Space](xref:113707) has been created by an @DevExpress.ExpressApp.IObjectSpaceFactory.
syntax:
  content: public Action<ObjectSpaceCreatedContext> OnObjectSpaceCreated { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.ObjectSpaceCreatedContext}
    description: A delegate method that takes a context object as an argument.
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated
  altText: XafApplication.ObjectSpaceCreated
- linkId: "116516"
- linkId: "115672"
---

You can handle this event in the following ways:

## Use the Application Builder

In the application's _Startup.cs_ file, add the following lines to the application builder code:


**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated += context => {
    // Use the `context.ObjectSpace` property to access the created Object Space.
    IObjectSpace os = context.ObjectSpace;
    // ...
};
// ...
```

***

## Use the Options Pattern 

In the application's _Startup.cs_ file, call the [`services.PostConfigure`](xref:Microsoft.Extensions.DependencyInjection.OptionsServiceCollectionExtensions.PostConfigure*) method to configure the `ObjectSpaceProviderOptions` as shown below: 

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
services.PostConfigure<ObjectSpaceProviderOptions>(options => {
    options.Events.OnObjectSpaceCreated += context => {
        // Use the `context.ObjectSpace` property to access the created Object Space.
        IObjectSpace os = context.ObjectSpace;
        //...
    };
});
```

***

