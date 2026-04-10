Open the application's _Startup.cs_ and ensure that the Non-Persistent Object Space Provider is registered in the Application Builder code. The [Template Kit](xref:405447) adds this code automatically.

**File:**  _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
// ...
builder.ObjectSpaceProviders
    // ...
    .AddNonPersistent();
// ...
```

***