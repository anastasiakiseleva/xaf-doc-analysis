---
uid: DevExpress.ExpressApp.ReportsV2.ReportServiceController
name: ReportServiceController
type: Class
summary: The [](xref:DevExpress.ExpressApp.Controller) that contains the common code used to display the Preview Report and Report Designer windows.
syntax:
  content: 'public abstract class ReportServiceController : Controller'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.ReportServiceController._members
  altText: ReportServiceController Members
---
The WinForms-specific descendant of this Controller is [](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController).

`ReportServiceController` exposes methods that invoke dialogs used to create, edit and view reports - [ReportServiceController.ShowWizard](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowWizard(System.Type)), [ReportServiceController.ShowDesigner](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowDesigner*) and [ReportServiceController.ShowPreview](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowPreview*).

To customize the Controller's behavior, you can handle the following events:

* [ReportServiceController.CustomShowPreview](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.CustomShowPreview)
* [ReportServiceController.CreateCustomParametersDetailView](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.CreateCustomParametersDetailView)
* [ReportDataSourceHelper.CustomSetCriteria](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.CustomSetCriteria)
* [ReportDataSourceHelper.CustomSetSorting](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.CustomSetSorting)
* [ReportServiceController.QueryRootReportComponentName](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.QueryRootReportComponentName)