---
uid: DevExpress.ExpressApp.ReportsV2.ReportStorageBase.CanSetData(System.String)
name: CanSetData(String)
type: Method
summary: Determines whether it is allowed to store a report in a **Report Storage** using the specified handle.
syntax:
  content: public virtual bool CanSetData(string url)
  parameters:
  - id: url
    type: System.String
    description: A [](xref:System.String) specifying the handle to store a report.
  return:
    type: System.Boolean
    description: A [](xref:System.String) specifying the handle to store a report.
seealso: []
---
If the **CanSetData** method returns **true**, it is allowed to store a report using the [ReportsStorage.SetData](xref:DevExpress.ExpressApp.ReportsV2.ReportStorageBase.SetData(DevExpress.XtraReports.UI.XtraReport,System.String)) method.