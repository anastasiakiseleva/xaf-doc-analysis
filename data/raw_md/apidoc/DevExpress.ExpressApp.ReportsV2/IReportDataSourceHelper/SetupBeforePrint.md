---
uid: DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.SetupBeforePrint(DevExpress.XtraReports.UI.XtraReport,DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean,DevExpress.Xpo.SortProperty[],System.Boolean)
name: SetupBeforePrint(XtraReport, ReportParametersObjectBase, CriteriaOperator, Boolean, SortProperty[], Boolean)
type: Method
summary: Prepares the report for further printing.
syntax:
  content: void SetupBeforePrint(XtraReport report, ReportParametersObjectBase parametersObject, CriteriaOperator criteria, bool canApplyCriteria, SortProperty[] sortProperty, bool canApplySortProperty)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object that specifies the report.
  - id: parametersObject
    type: DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase
    description: A [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) object that specifies report parameters.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) object used to filter data.
  - id: canApplyCriteria
    type: System.Boolean
    description: '`true` if the criteria can be applied; otherwise, `false`.'
  - id: sortProperty
    type: DevExpress.Xpo.SortProperty[]
    description: An array of [](xref:DevExpress.Xpo.SortProperty) objects that specifies the sort order.
  - id: canApplySortProperty
    type: System.Boolean
    description: '`true` if sorting can be applied; otherwise, `false`.'
seealso: []
---

If you want to print a report in code, you should use the `SetupBeforePrint` method that executes the [IReportDataSourceHelper.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.SetupReport*) method and triggers the [IReportDataSourceHelper.BeforeShowPreview](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.BeforeShowPreview) event.

If there is no need to apply criteria and sorting, and pass report parameters, use another overload of the `SetupBeforePrint` method that takes a single _report_ parameter. An example on how to use this overload is available in the [How to: Print a Report Without Displaying a Preview](xref:113601) topic.