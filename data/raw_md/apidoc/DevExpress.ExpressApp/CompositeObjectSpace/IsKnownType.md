---
uid: DevExpress.ExpressApp.CompositeObjectSpace.IsKnownType(System.Type,System.Boolean)
name: IsKnownType(Type, Boolean)
type: Method
summary: Checks whether the Object Space (or any Object Space from its @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection) can handle objects of the specified type.
syntax:
  content: public bool IsKnownType(Type objectType, bool checkAdditionalObjectSpaces)
  parameters:
  - id: objectType
    type: System.Type
    description: The type that this method checks.
  - id: checkAdditionalObjectSpaces
    type: System.Boolean
    description: Indicates if the method should also check Object Spaces from the @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection.
  return:
    type: System.Boolean
    description: '**true** if the Object Space (or any Object Space from its @DevExpress.ExpressApp.CompositeObjectSpace.AdditionalObjectSpaces collection) can handle objects of the specified type.'
seealso: []
---
The following example demonstrates how to use this property in Application Builder code:

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
    var nonPersistentObjectSpace = context.ObjectSpace as NonPersistentObjectSpace;
    if (nonPersistentObjectSpace != null) {
        if (!nonPersistentObjectSpace.IsKnownType(typeof(Person), true)) {
            // ...
        }
    }
};
// ...
```

***

[`/\.(ObjectSpaceCreated)/`]: xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceCreated
[`NonPersistentObjectSpace`]: xref:DevExpress.ExpressApp.NonPersistentObjectSpace
[`ObjectSpaceCreatedEventArgs`]: xref:DevExpress.ExpressApp.ObjectSpaceCreatedEventArgs