You can specify lockout options as follows.

**Files:** _SolutionName.Blazor.Server\Startup.cs_, _SolutionName.Win\Startup.cs_

# [C#](#tab/tabid-code)
 
```csharp
builder.Security
    .UseIntegratedMode(options => {
        options.Lockout.Enabled = true;
        options.Lockout.MaxFailedAccessAttempts = 3;
        options.Lockout.DefaultLockoutTimeSpan = TimeSpan.FromMinutes(3);
        // ...
    })
```
***