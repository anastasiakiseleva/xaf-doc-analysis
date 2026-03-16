---
uid: DevExpress.Persistent.BaseImpl.ReportDataV2.IsPredefined
name: IsPredefined
type: Property
summary: Gets a boolean value that indicates whether or not the report is predefined.
syntax:
  content: |-
    [VisibleInDetailView(false)]
    [VisibleInListView(false)]
    public bool IsPredefined { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if a report is predefined in code; **false**, if a report is created at runtime.'
seealso: []
---
Predefined reports are registered in code via the [PredefinedReportsUpdater.AddPredefinedReport\<T>](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport*) method. Runtime reports are created manually by end users.