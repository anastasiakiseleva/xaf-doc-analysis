---
uid: DevExpress.Persistent.Base.ReportsV2.DataSourceBase.UpdateCriteriaWithReportParameters(System.Collections.Generic.IEnumerable{DevExpress.Data.IParameter})
name: UpdateCriteriaWithReportParameters(IEnumerable<IParameter>)
type: Method
summary: Adds report parameter values to the criteria string.
syntax:
  content: public void UpdateCriteriaWithReportParameters(IEnumerable<IParameter> parameters)
  parameters:
  - id: parameters
    type: System.Collections.Generic.IEnumerable{DevExpress.Data.IParameter}
    description: An IEnumerable\<[](xref:DevExpress.Data.IParameter)> list of report parameters.
seealso: []
---
The **UpdateCriteriaWithReportParameters** method replaces question marks ("?") with actual report parameter values in a [DataSourceBase.CriteriaString](xref:DevExpress.Persistent.Base.ReportsV2.DataSourceBase.CriteriaString).