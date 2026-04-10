Handle this event to apply criteria and sorting manually. In the handler, you can use the `IReportDataSourceHelper.GetMasterReportDataSource` method to access the data source.

You can also use this event to use a custom Data Source component (inherited from [](xref:DevExpress.Persistent.Base.ReportsV2.DataSourceBase)).

The code snippets below demonstrate how to subscribe to this event:

## In Application Builder Code

In the application's _Startup.cs file_, add the `OnCustomSetupReportDataSource` event handler to the `builder.Modules.AddReports` method call as shown below:

**File:** _MySolution.Blazor.Server/Startup.cs_, _MySolution.Win/Startup.cs_, _MySolution.WebApi/Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp{6-8}
using DevExpress.ExpressApp.ApplicationBuilder;
// ...
builder.Modules
    .AddReports(options => {
        // ...
        options.Events.OnCustomSetupReportDataSource = context => {
            context.Report.DataSource = new CustomDataSource();
        };
    })
// ...
```

***

## Through Dependency Injection

> [!NOTE]
> The technique shown in this section is not supported for [Web API Service](xref:403394).

Use [Dependency Injection](xref:404364) to access the [IReportDataSourceHelper](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper) service and add a handler to its `CustomSetupReportDataSource` event.

# [C#](#tab/tabid-csharp)

```csharp{6-8}
using DevExpress.ExpressApp.ReportsV2;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var helper = serviceProvider.GetRequiredService<IReportDataSourceHelper>();
helper.CustomSetupReportDataSource += delegate (object sender, CustomSetupReportDataSourceEventArgs e) {
    e.Report.DataSource = new CustomDataSource();
};
```
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider

***