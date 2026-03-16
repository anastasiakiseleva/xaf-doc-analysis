---
uid: DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController
name: WinReportServiceController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) descendant that contains platform-specific code, providing end-users with the capability to create, design and view reports.
syntax:
  content: 'public class WinReportServiceController : ReportServiceController'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController._members
  altText: WinReportServiceController Members
---
The **WinReportServiceController** [Controller](xref:112621) contains the Windows Forms specific code that displays:

* **Preview Report** window
    
    ![Tutorial_bMD_Lesson8_6](~/images/tutorial_bmd_lesson8_6115441.png)
* [Report Wizard](xref:4254)
    
    ![Reports_Win_1](~/images/reports_win_1115543.png)
* [Report Designer](xref:4256) window
    
    ![Tutorial_BMD_Lesson8_1_2](~/images/tutorial_bmd_lesson8_1_2116445.png)

You can customize the Controller's behavior by handling the following events:

* [WinReportServiceController.NewXafReportWizardShowing](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.NewXafReportWizardShowing)
* [WinReportServiceController.CreateCustomDesignForm](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.CreateCustomDesignForm)
* [WinReportServiceController.CustomShowDesignForm](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.CustomShowDesignForm)

Refer to these event descriptions for details.