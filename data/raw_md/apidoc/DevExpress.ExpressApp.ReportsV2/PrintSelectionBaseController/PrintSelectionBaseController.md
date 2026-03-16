---
uid: DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController
name: PrintSelectionBaseController
type: Class
summary: An [](xref:DevExpress.ExpressApp.ObjectViewController) that provides the [PrintSelectionBaseController.ShowInReportAction](xref:DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController.ShowInReportAction) used to execute [In-Place Reports](xref:113602).
syntax:
  content: 'public class PrintSelectionBaseController : ObjectViewController'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController._members
  altText: PrintSelectionBaseController Members
---
Activated in all Views. The **ReportsControllerCoreAction** allows an end-user to execute an inplace report using the currently selected objects as the data source. If there are no in-place reports for the current View's object type, this Action is not activated. To specify that a report is in-place in the UI, set its [IInplaceReportV2.IsInplaceReport](xref:DevExpress.ExpressApp.ReportsV2.IInplaceReportV2.IsInplaceReport) property to **true**. To create an in-place report in code, call the [PredefinedReportsUpdater.AddPredefinedReport\<T>](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport*) method overload that takes the _isInplaceReport_ parameter and set this parameter to **true**.