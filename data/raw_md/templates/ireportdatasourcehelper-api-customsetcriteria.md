Handle this event to apply criteria in a custom manner. The following code snippets demonstrate how to subscribe to this event:

## In Application Builder Code

In the application's _Startup.cs file_, add the `OnCustomSetCriteria` event handler to the `builder.Modules.AddReports` method call as shown below:

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{6-8}
using DevExpress.ExpressApp.ApplicationBuilder;
// ...
builder.Modules
    .AddReports(options => {
        // ...
        options.Events.OnCustomSetCriteria = context => {
            // ...
        };
    })
// ...
```

***

## Through Dependency Injection

> [!NOTE]
> The technique shown in this section is not supported for [Web API Service](xref:403394).

Use [Dependency Injection](xref:404364) to access the [IReportDataSourceHelper](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper) service and add a handler to its `CustomSetCriteria` event.

# [C#](#tab/tabid-csharp)

```csharp{6-8}
using DevExpress.ExpressApp.ReportsV2;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var helper = serviceProvider.GetRequiredService<IReportDataSourceHelper>();
helper.CustomSetCriteria += delegate (object sender, CustomSetCriteriaEventArgs e) {
    // ...
};
```
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider

***