---
uid: DevExpress.ExpressApp.SystemModule.CustomExportEventArgs
name: CustomExportEventArgs
type: Class
summary: Arguments, specific to the [ExportController.CustomExport](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomExport) and [ExportController.Exported](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exported) events of the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) class.
syntax:
  content: 'public class CustomExportEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.CustomExportEventArgs._members
  altText: CustomExportEventArgs Members
---
Declares properties, specific to the following events:

* [ExportController.CustomExport](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomExport)
* [ExportController.Exported](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exported)

These events are designed to customize the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) [Action](xref:112622) functionality (see [How to: Customize the Export Action Behavior](xref:113287)).

The [CustomExportEventArgs.ExportOptions](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportOptions) property exposed by this class can be used for customizing export options specific to the export format before exporting. The [CustomExportEventArgs.ExportTarget](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportTarget) property can be used to determine the export format selected when executing the **Export** Action. The [CustomExportEventArgs.Stream](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.Stream) property can be used to access the exporting (exported) output stream.

This class is inherited from the **HandledEventArgs** class. So, you can use the handler's **Handled** parameter to suppress default exporting when handling the **CustomExport** event.