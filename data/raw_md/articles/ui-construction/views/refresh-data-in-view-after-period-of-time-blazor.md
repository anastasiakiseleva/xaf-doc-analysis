---
uid: "405253"
title: Refresh Data in a View After a Period of Time (ASP.NET Core Blazor)
owner: Georgiy Gorislov
seealso:
  - linkType: HRef
    linkId: xref:DevExpress.ExpressApp.Blazor.BlazorApplication.InvokeAsync*
    altText: BlazorApplication.InvokeAsync method overloads
---
# Refresh Data in a View After a Period of Time (ASP.NET Core Blazor)

The following example refreshes data in a List View at a specified time interval:

**File:** _MySolution.Blazor.Server\\Controllers\\AutoRefreshDataController.cs_

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor;

public class AutoRefreshDataController : ViewController<ListView> {
    private readonly System.Timers.Timer timer = new();

    public AutoRefreshDataController() {
        TargetViewNesting = Nesting.Root;
        timer.Interval = 3000;
        timer.Elapsed += (s, e) => RefreshData();
    }
    private void RefreshData() {
        ((BlazorApplication)Application).InvokeAsync(() => {
            bool canRefresh = View is not null && View.SelectedObjects.Count is 0;
            if (canRefresh) {
                View.ObjectSpace.Refresh();
            }
        });
    }
    protected override void OnActivated() {
        base.OnActivated();
        timer.Start();
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        timer.Stop();
    }
    protected override void Dispose(bool disposing) {
        base.Dispose(disposing);
        timer.Dispose();
    }
}
```
***

The controller in this example adds the following functionality:

- When a user opens the root List View, a [timer](https://learn.microsoft.com/en-us/dotnet/api/system.timers.timer) starts.  
  The timer stops when the View is closed, and is disposed when the Controller is disposed.
- Every 3 seconds, the [Timer.Elapsed](https://learn.microsoft.com/en-us/dotnet/api/system.timers.timer.elapsed) event fires and the `RefreshData` event handler is executed.
- The [BlazorApplication.InvokeAsync](xref:DevExpress.ExpressApp.Blazor.BlazorApplication.InvokeAsync*) method is used to safely execute the code that refreshes the view.  
  Because `Timer.Elapsed` is raised on a thread pool thread, the `RefreshData` event handler must not execute XAF code directly to avoid competing with another thread for access to shared resources. The `BlazorApplication.InvokeAsync` method ensures that only one thread executes XAF logic at a time.
- Finally, the view is refreshed if the View is not `null`, and no objects are currently selected - otherwise the selection could be lost after the data is refreshed.

[`InvokeAsync`]: xref:DevExpress.ExpressApp.Blazor.BlazorApplication.InvokeAsync*
[`System.Timers.Timer`]: xref:System.Timers.Timer
[`Refresh`]: xref:DevExpress.ExpressApp.IObjectSpace.Refresh
