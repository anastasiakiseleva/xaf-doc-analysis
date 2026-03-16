---
uid: "113611"
seealso: []
title: 'How to: Use the XRSubreport Control with Reports V2 Data Sources'
owner: Ekaterina Kiseleva
---
# How to: Use the XRSubreport Control with Reports V2 Data Sources

This topic describes the specifics of using the [](xref:DevExpress.XtraReports.UI.XRSubreport) control when creating a [Master-Detail Report](xref:4785) with [Data Sources for Reports V2](xref:113593) ([](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) or [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource)).

## XRSubreport and CollectionDataSource
To create a report with a subreport in XAF, you can follow the [Creating a Master-Detail Report using Subreports](xref:4629) tutorial published in the XtraReports documentation, but using the [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) instead of binding to data directly. Then, you can register a master report using the [PredefinedReportsUpdater.AddPredefinedReport\<T>](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport*) method. No additional steps are required.

## XRSubreport and ViewDataSource
> [!NOTE]
> The complete example is available in the **FeatureCenter** application. By default, this demo is installed in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ path. The master report and its subreport are demonstrated in the following files.
> 
> * _FeatureCenter.Module\Reports\ContactReport.cs_
> * _FeatureCenter.Module\Reports\PhoneNumberReport.cs_

If you choose [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource), use the same approach described in the previous paragraph, but take into account that the master object's key column is added in the **Parameter Bindings Collection Editor** dialog demonstrated in the XtraReports tutorial. With the **ViewDataSource**, you should add the key column manually to the [ViewDataSource.Properties](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource.Properties) collection. The **Expression** value should refer to the key property of the business class specified by [DataSourceBase.ObjectTypeName](xref:DevExpress.Persistent.Base.ReportsV2.DataSourceBase.ObjectTypeName) (e.g., to the [BaseObject.Oid](xref:DevExpress.Persistent.BaseImpl.BaseObject.Oid) property). The image below demonstrates the key column added in the Reports Designer.

![ReportsV2_Subreport_ViewDataSource_Oid](~/images/reportsv2_subreport_viewdatasource_oid117422.png)