---
uid: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetXafReportParametersObject(DevExpress.XtraReports.UI.XtraReport,DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase)
name: SetXafReportParametersObject(XtraReport, ReportParametersObjectBase)
type: Method
summary: Adds a [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) descendant object that specifies report parameters to the [XtraReport.Parameters](xref:DevExpress.XtraReports.UI.XtraReport.Parameters) collection (if this object exists).
syntax:
  content: public virtual void SetXafReportParametersObject(XtraReport report, ReportParametersObjectBase parametersObject)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object that specifies the report.
  - id: parametersObject
    type: DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase
    description: A [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) object that specifies report parameters.
seealso: []
---
The **SetXafReportParametersObject** method is called by the [ReportDataSourceHelperBase.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReport*) method. The **SetXafReportParametersObject** method is virtual, so you can override it to customize its behavior. To use your own implementation of the [](xref:DevExpress.ExpressApp.ReportsV2.ReportDataSourceHelper) class, assign its instance to the [ReportsModuleV2.ReportsDataSourceHelper](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportsDataSourceHelper) property.