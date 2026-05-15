---
uid: "113593"
seealso: []
title: Data Sources for Reports V2
---
# Data Sources for Reports V2

The **Reports V2** module supports @DevExpress.Persistent.Base.ReportsV2.CollectionDataSource and @DevExpress.Persistent.Base.ReportsV2.ViewDataSource data sources.

Use @DevExpress.Persistent.Base.ReportsV2.CollectionDataSource for small datasets because it loads all object fields, including those not shown in the report. If this causes performance issues, use @DevExpress.Persistent.Base.ReportsV2.ViewDataSource instead. It loads only the fields specified in its Properties and can retrieve values directly from business class properties or database expressions.

Both sources require @DevExpress.ExpressApp.IObjectSpace for dynamic data binding. Use the following methods to access the data:

* @DevExpress.ExpressApp.IObjectSpace.CreateCollection*
* @DevExpress.ExpressApp.IObjectSpace.CreateDataView*


To print a report from code, use [ReportDataSourceHelper.SetupBeforePrint](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupBeforePrint*) to register a service with an [Object Space](xref:113707) and perform the required initialization.