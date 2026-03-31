---
uid: "113593"
seealso: []
title: Data Sources for Reports V2
---
# Data Sources for Reports V2

The **Reports V2** module supports XtraReports that utilize [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) and [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource) data sources only. These two components are available in the **DX: Report Controls** group in the Visual Studio **Toolbox**. 

![ReportsV2_DataSourcesToolbox](~/images/reportsv2_datasourcestoolbox117469.png)

These data sources require [](xref:DevExpress.ExpressApp.IObjectSpace) to dynamically bind data. If you want to print a report in code, you should use the [ReportDataSourceHelper.SetupBeforePrint](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupBeforePrint*) method to register a service that provides an [Object Space](xref:113707) and perform other necessary initializations.

## Data Source Comparison
| Data&nbsp;Source&nbsp;Type | Data&nbsp;Access&nbsp;Method | Usage Scenario |
|---|---|---|
| [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) | [IObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.IObjectSpace.CreateCollection*) | Use **CollectionDataSource** when you do not need to display a large amount of data, because this component loads objects in their entirety, including fields that are not displayed in the report. |
| [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource) | [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) | Use **ViewDataSource** instead of **CollectionDataSource** if you experience performance issues. The **ViewDataSource** data source loads only those fields that are listed in [ViewDataSource.Properties](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource.Properties). Field values can be obtained from specific business class properties directly, or be evaluated by the database server using complex expressions. |
