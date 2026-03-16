---
uid: DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces
name: AdditionalObjectSpaces
type: Property
summary: Gets the list of [Object Spaces](xref:113707) used to handle objects that do not belong to the current Object Space. We recommend that you call the @DevExpress.ExpressApp.CompositeObjectSpace.PopulateAdditionalObjectSpaces(DevExpress.ExpressApp.XafApplication) method to populate this collection automatically.
syntax:
  content: public IList<IObjectSpace> AdditionalObjectSpaces { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.ExpressApp.IObjectSpace}
    description: An [](xref:System.Collections.Generic.IList`1) collection of Object Spaces used to handle objects that do not belong to the current Object Space.
exceptions:
- type: System.InvalidOperationException
  description: Cannot add the Object Space to the CompositeObjectSpace.AdditionalObjectSpaces collection because another Object Space for the same object types already exists.
seealso: []
---
Use one of the following techniques to fill this collection.

## Automatically: Use PopulateAdditionalObjectSpaces (Recommended technique)

[!include[<all necessary Object Spaces>](~/templates/PopulateAdditionalObjectSpace_example.md)]

## Manually: Create Object Spaces and Add Them to the Collection

If you need to create an additional Object Space manually, follow the steps below:
1. Handle the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event in the Application Builder code in the application’s _Startup.cs_ file.
2. In the event handler, access @DevExpress.ExpressApp.NonPersistentObjectSpace and use its @DevExpress.ExpressApp.CompositeObjectSpace.IsKnownType(System.Type,System.Boolean) method to ensure that the `AdditionalObjectSpaces` collection does not already include a compatible Object Space. 

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
    var nonPersistentObjectSpace = context.ObjectSpace as NonPersistentObjectSpace;
    if (nonPersistentObjectSpace != null) {
        if (!nonPersistentObjectSpace.IsKnownType(typeof(Person), true)) {
            IObjectSpace additionalObjectSpace = context.ServiceProvider.GetRequiredService<IObjectSpaceFactory>()
                .CreateObjectSpace<Person>();
            // Customize the additionally created Object Space.
            nonPersistentObjectSpace.AdditionalObjectSpaces.Add(additionalObjectSpace);
            nonPersistentObjectSpace.Disposed += (s2, e2) => {
                additionalObjectSpace.Dispose();
            };
        }
    }
};
// ...
```

***

[`/\.(ObjectSpaceCreated)/`]: xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated
[`CompositeObjectSpace`]: xref:DevExpress.ExpressApp.CompositeObjectSpace 
[`NonPersistentObjectSpace`]: xref:DevExpress.ExpressApp.NonPersistentObjectSpace
[`IsKnownType`]: xref:DevExpress.ExpressApp.CompositeObjectSpace.IsKnownType(System.Type,System.Boolean)
[`CreateObjectSpace`]: xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)
[`ObjectSpaceCreatedEventArgs`]: xref:DevExpress.ExpressApp.ObjectSpaceCreatedEventArgs