---
uid: DevExpress.ExpressApp.ReportsV2.IInplaceReportV2.IsInplaceReport
name: IsInplaceReport
type: Property
summary: Specifies whether or not the report is [inplace](xref:113602).
syntax:
  content: bool IsInplaceReport { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the report is inplace; otherwise, **false**.'
seealso: []
---
Inplace reports can be executed for a selected set of business objects using the [PrintSelectionBaseController.ShowInReportAction](xref:DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController.ShowInReportAction) Action.