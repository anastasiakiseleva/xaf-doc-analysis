---
uid: DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.SetupReport(DevExpress.XtraReports.UI.XtraReport,DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean,DevExpress.Xpo.SortProperty[],System.Boolean)
name: SetupReport(XtraReport, ReportParametersObjectBase, CriteriaOperator, Boolean, SortProperty[], Boolean)
type: Method
summary: Initializes the specified report.
syntax:
  content: void SetupReport(XtraReport report, ReportParametersObjectBase parametersObject, CriteriaOperator criteria, bool canApplyCriteria, SortProperty[] sortProperty, bool canApplySortProperty)
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
    description: An array of [](xref:DevExpress.Xpo.SortProperty) objects that specify data sort order.
  - id: canApplySortProperty
    type: System.Boolean
    description: '`true` if the sorting can be applied; otherwise, `false`.'
seealso: []
---

If there is no need to apply criteria and sorting, and pass report parameters, use another overload of the **SetupReport** method that takes a single _report_ parameter. An example on how to use this method is available in the following topic: [](xref:113606).