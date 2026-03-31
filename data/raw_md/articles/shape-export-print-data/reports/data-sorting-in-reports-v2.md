---
uid: "113595"
seealso: []
title: Data Sorting in Reports V2
---
# Data Sorting in Reports V2

The following data sorting approaches are available in **Reports V2**.

1. Use [XtraReports sorting](xref:4814).
2. Use the [CollectionSourceBase.Sorting](xref:DevExpress.ExpressApp.CollectionSourceBase.Sorting) property of the [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) or [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource) (see [Data Sources for Reports V2](xref:113593)).
3. Use [ReportParametersObjectBase.GetSorting](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase.GetSorting) method of the **Parameters Object** (a [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) descendant).

## Sorting Property of the Data Source
The [CollectionSourceBase.Sorting](xref:DevExpress.ExpressApp.CollectionSourceBase.Sorting) property of the **CollectionDataSource** and **ViewDataSource** components specifies a list of sorting rules. 

You can add rules by clicking the ellipsis button next to the **Sorting** value in the **Properties** window.

![ReportsV2_Sorting](~/images/reportsv2_sorting117392.png)

The data is sorted on the client side.

You can use the following code to modify **Sorting** from [Report Scripts](xref:2593).

# [C#](#tab/tabid-csharp)

```csharp
private void xtraReport1_BeforePrint(object sender, System.Drawing.Printing.PrintEventArgs e) {
    var report = (DevExpress.XtraReports.UI.XtraReport)sender;
    var dataSource = (DevExpress.Persistent.Base.ReportsV2.ISupportSorting)report.DataSource;
    dataSource.Sorting.Clear();
    dataSource.Sorting.Add(
        new DevExpress.Xpo.SortProperty("FullName", DevExpress.Xpo.DB.SortingDirection.Ascending));
}
```
***

## Parameters Object
Sorting via the Parameters Object is performed in a manner similar to filtering. For details, refer to the [Data Filtering in Reports V2](xref:113594) topic.