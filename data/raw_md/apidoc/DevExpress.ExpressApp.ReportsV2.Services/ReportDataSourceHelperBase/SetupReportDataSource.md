---
uid: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReportDataSource(DevExpress.XtraReports.UI.XtraReport,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean,DevExpress.Xpo.SortProperty[],System.Boolean)
name: SetupReportDataSource(XtraReport, CriteriaOperator, Boolean, SortProperty[], Boolean)
type: Method
summary: Passes criteria and sorting to the report data source.
syntax:
  content: public void SetupReportDataSource(XtraReport report, CriteriaOperator criteria, bool canApplyCriteria, SortProperty[] sortProperty, bool canApplySortProperty)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object that specifies the report.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object used to filter data.
  - id: canApplyCriteria
    type: System.Boolean
    description: '**true**, if the criteria can be applied; otherwise, **false**.'
  - id: sortProperty
    type: DevExpress.Xpo.SortProperty[]
    description: An array of [](xref:DevExpress.Xpo.SortProperty) objects which specifies data sorting.
  - id: canApplySortProperty
    type: System.Boolean
    description: '**true**, if the sorting can be applied; otherwise, **false**.'
seealso: []
---
The **SetupReportDataSource** method is called by the [ReportDataSourceHelperBase.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReport*) method. You can customize the **SetupReportDataSource** method behavior by handling the [ReportDataSourceHelper.CustomSetupReportDataSource](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.CustomSetupReportDataSource) event.