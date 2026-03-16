---
uid: DevExpress.ExpressApp.Win.SystemModule.WinExportController
name: WinExportController
type: Class
summary: The Windows Forms specific descendant of the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) class.
syntax:
  content: 'public class WinExportController : ExportController'
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.WinExportController._members
  altText: WinExportController Members
---
Implements the base class' **Export** abstract method. Within this method implementation, the Save File Dialog is invoked with the appropriate file filter applied.

![Export_1](~/images/export_1116692.png)

![Export_SaveAs](~/images/export_saveas116766.png)

Using the file name and extension specified in the Save File Dialog, a **System.IO.FileStream** object is created and passed to the [](xref:DevExpress.ExpressApp.SystemModule.ExportController)'s base **ExportCore** method. The **ExportController** uses the **XtraPrintingLibrary** to export data to the specified stream in the required format.

To localize the **Save as type** filter captions in the Save File Dialog, use the **Localization** | **OpenSaveDialogFilters** node in the [Model Editor](xref:112582).

To customize Save File Dialog options, handle the [WinExportController.CustomShowSaveFileDialog](xref:DevExpress.ExpressApp.Win.SystemModule.WinExportController.CustomShowSaveFileDialog) event. To see an example of accessing the **WinExportController** [Controller](xref:112621), refer to the [How to: Customize the Export Action Behavior](xref:113287) topic.