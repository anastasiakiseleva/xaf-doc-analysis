Handle this event to apply sorting in a custom manner. The code snippets below demonstrate how to subscribe to this event:

## In Application Builder Code

In the application's _Startup.cs file_, add the `OnCustomSetSorting` event handler to the `builder.Modules.AddReports` method call as shown below:

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{6-8}
using DevExpress.ExpressApp.ApplicationBuilder;
// ...
builder.Modules
    .AddReports(options => {
        // ...
        options.Events.OnCustomSetSorting = context => {
            // ...
        };
    })
// ...
```

***

## Through Dependency Injection

> [!NOTE]
> The technique shown in this section is not supported for [Web API Service](xref:403394).

Use [Dependency Injection](xref:404364) to access the [IReportDataSourceHelper](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper) service and add a handler to its `CustomSetSorting` event.

# [C#](#tab/tabid-csharp)

```csharp{6-8}
using DevExpress.ExpressApp.ReportsV2;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var helper = serviceProvider.GetRequiredService<IReportDataSourceHelper>();
helper.CustomSetSorting += delegate (object sender, CustomSetSortingEventArgs e) {
    // ...
};
```
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider

***
