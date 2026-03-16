---
uid: DevExpress.ExpressApp.BaseObjectSpace.NonPersistentChangesEnabled
name: NonPersistentChangesEnabled
type: Property
summary: Specifies whether the [](xref:DevExpress.ExpressApp.BaseObjectSpace) is marked as modified (see [BaseObjectSpace.IsModified](xref:DevExpress.ExpressApp.BaseObjectSpace.IsModified)) when a non-persistent property is changed.
syntax:
  content: public bool NonPersistentChangesEnabled { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, to mark the Object Space as modified when a non-persistent property is changed; otherwise, **false**. The default is **false**.'
seealso: []
---

To set this property for all Object Spaces created by the application, handle the @DevExpress.ExpressApp.ObjectSpaceProviderEvents.OnObjectSpaceCreated event in the Application Builder code:

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// ...
builder.ObjectSpaceProviders.Events.OnObjectSpaceCreated = context => {
    BaseObjectSpace os = context.ObjectSpace as BaseObjectSpace;
    if (os != null)
        os.NonPersistentChangesEnabled = true;
};
// ...
```

***
