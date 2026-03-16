---
uid: DevExpress.ExpressApp.Win.SystemModule.WinExportController.CustomShowSaveFileDialog
name: CustomShowSaveFileDialog
type: Event
summary: Occurs when the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) is executed, before data is exported to a stream.
syntax:
  content: public event EventHandler<CustomShowSaveFileDialogEventArgs> CustomShowSaveFileDialog
seealso: []
---
Before the data presented by the [ExportController.Exportable](xref:DevExpress.ExpressApp.SystemModule.ExportController.Exportable) editor is exported, the **CustomShowSaveFileDialog** event is raised. Handle it if you need to show the Save File Dialog in a custom way. For this purpose, use the handler's [CustomShowSaveFileDialogEventArgs.Dialog](xref:DevExpress.ExpressApp.Win.SystemModule.CustomShowSaveFileDialogEventArgs.Dialog) parameter to access the dialog box to be shown. In addition, use the [CustomShowSaveFileDialogEventArgs.DialogResult](xref:DevExpress.ExpressApp.Win.SystemModule.CustomShowSaveFileDialogEventArgs.DialogResult) parameter to set the return value of the dialog box, and set the handler's **Handled** parameter to **true** to cancel showing the dialog box in the default way.