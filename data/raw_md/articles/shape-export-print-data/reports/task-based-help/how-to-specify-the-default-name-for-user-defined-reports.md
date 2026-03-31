---
uid: "113607"
seealso: []
title: 'How to: Specify the Default Name for User-Defined Reports'
---
# How to: Specify the Default Name for User-Defined Reports

This example demonstrates how to change the default name of user-defined reports in XAF applications.

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

In the [!include[File_Module](~/templates/file_module11171.md)] file, override the [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method and handle the static [ReportServiceController.QueryRootReportComponentName](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.QueryRootReportComponentName) event to change the default name of user-defined reports. In the event handler, assign the new name to the `Name` parameter and set the `Handled` parameter to `true`.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ReportsV2;
// ...
public override void Setup(XafApplication application) {
    ReportServiceController.QueryRootReportComponentName +=
        delegate(object sender, QueryRootReportComponentNameEventArgs e) {
        e.Handled = true;
        e.Name = "MyNewReport";
    };
    base.Setup(application);
}
```

***

The following image demonstrates the result:

![XAF Windows Forms, ReportsV2 QueryRootReportComponentName, DevExpress](~/images/reportsv2_queryrootreportcomponentname117409.png)
