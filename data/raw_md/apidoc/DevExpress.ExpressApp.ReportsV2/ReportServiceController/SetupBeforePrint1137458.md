---
uid: DevExpress.ExpressApp.ReportsV2.ReportServiceController.SetupBeforePrint(DevExpress.XtraReports.UI.XtraReport,DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean,DevExpress.Xpo.SortProperty[],System.Boolean)
name: SetupBeforePrint(XtraReport, ReportParametersObjectBase, CriteriaOperator, Boolean, SortProperty[], Boolean)
type: Method
summary: Prepares the report for further printing.
syntax:
  content: public void SetupBeforePrint(XtraReport report, ReportParametersObjectBase parametersObject, CriteriaOperator criteria, bool canApplyCriteria, SortProperty[] sortProperty, bool canApplySortProperty)
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
    description: '**true**, if the criteria can be applied; otherwise, **false**.'
  - id: sortProperty
    type: DevExpress.Xpo.SortProperty[]
    description: An array of [](xref:DevExpress.Xpo.SortProperty) objects which specifies data sorting.
  - id: canApplySortProperty
    type: System.Boolean
    description: '**true**, if the sorting can be applied; otherwise, **false**.'
seealso: []
---
To see an example of using this method, refer to the [How to: Use the Custom Report Preview Form](xref:113603) topic.