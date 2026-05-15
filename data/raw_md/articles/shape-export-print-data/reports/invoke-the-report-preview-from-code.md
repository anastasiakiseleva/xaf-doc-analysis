---
uid: "113703"
seealso:
- linkId: "113601"
- linkId: "114515"
- linkId: DevExpress.ExpressApp.ReportsV2.IReportStorage
- linkId: DevExpress.ExpressApp.ReportsV2.ReportStorageBase.GetReportContainerHandle(DevExpress.ExpressApp.ReportsV2.IReportDataV2)
- linkId: DevExpress.ExpressApp.Frame.GetController``1
title: Invoke the Report Preview from Code
---

# Invoke the Report Preview from Code

This topic describes how you can display a preview for an [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) object from custom [Controller](xref:112621) code.

The [](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController) exposes the [ReportServiceController.ShowPreview](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowPreview*) method that you can call to invoke the report preview window. The code below demonstrates how to use this method.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.Persistent.Base;
using Microsoft.Extensions.DependencyInjection;

public class MyPrintReportController : ObjectViewController<ListView, Contact> {
    public MyPrintReportController() {
        SimpleAction SalesInvoiceAction = new SimpleAction(this, "Print selected", PredefinedCategory.RecordEdit);
        SalesInvoiceAction.Execute += SalesInvoiceAction_Execute;
    }

    private void SalesInvoiceAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        ReportServiceController controller = Frame.GetController<ReportServiceController>();
        if(controller != null) {
            var reportStorage = Application.ServiceProvider.GetRequiredService<IReportStorage>();
            using IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(ReportDataV2));
            IReportDataV2 reportData = objectSpace.FirstOrDefault<ReportDataV2>(data => data.DisplayName == "Contacts Report");
            string handle = reportStorage.GetReportContainerHandle(reportData);
            controller.ShowPreview(handle);
        };
    }
}
```

## Filter Report Data in Code

To filter a report, pass a criterion to the [ReportServiceController.ShowPreview](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowPreview*) method. For example, the following code builds the criterion based on the objects selected in a view: 

```csharp
CriteriaOperator objectsCriteria = ((BaseObjectSpace)objectSpace).GetObjectsCriteria(View.ObjectTypeInfo, e.SelectedObjects);
controller.ShowPreview(handle, objectsCriteria);
```
You can use any other criteria here.

In the criteria string used in the code above, substitute `"Contacts Report"` with the actual [IReportDataV2.DisplayName](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.DisplayName) value of the report you want to display.

> [!TIP]
> Optionally, you can use the `criteria` and `sortProperty` parameters of the `ShowPreview` method to filter and sort data displayed in the report.

## Pass Parameters Values from the Current View to the Report

1. In your View Controller create a custom scoped service to pass parameters from the Controller to the Report:

    ```csharp
    private void ShowReportAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
    //...
        Application.ServiceProvider.GetService<MyReportPreviewContext>().ParameterValue = "my custom value";
        reportServiceController.ShowPreview(handle);
    //...
    public class MyReportPreviewContext {
        public object ParameterValue { get; set; }
    }
    ```

2. Register your service: 

    # [SolutionName.Blazor.Server\Startup.cs](#tab/tabid-blazor)
    
    ```csharp
    services.AddScoped<MyReportPreviewContext>();
    ```
    
    # [SolutionName.Win\Startup.cs](#tab/tabid-win)
    
    ```csharp
    builder.Services.AddScoped<MyReportPreviewContext>();
    ```
    
    ***

3. Handle the `ReportOptions.Events.OnReportLoaded` or `ReportOptions.Events.OnBeforeShowPreview` events to access an XtraReport instance. Use the [XtraReport.Parameters](xref:DevExpress.XtraReports.UI.XtraReport.Parameters) property to access report parameters and set the [Parameter.Value](xref:DevExpress.XtraReports.Parameters.Parameter.Value) property.

    **Files**: _SolutionName.Blazor.Server\Startup.cs_, _SolutionName.Win\Startup.cs_

    ```csharp
    builder.Modules
        .AddReports(options => {
            options.Events.OnBeforeShowPreview = context => {
                var report = context.Report;
                report.Parameters["MyParameter"].Value = 
                    context.ServiceProvider.GetService<MyReportPreviewContext>().ParameterValue;
                //...
            };
        })
    //...
    ```