---
uid: DevExpress.ExpressApp.Win.SystemModule.CustomShowSaveFileDialogEventArgs
name: CustomShowSaveFileDialogEventArgs
type: Class
summary: Provides data for the [WinExportController.CustomShowSaveFileDialog](xref:DevExpress.ExpressApp.Win.SystemModule.WinExportController.CustomShowSaveFileDialog) event.
syntax:
  content: 'public class CustomShowSaveFileDialogEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.CustomShowSaveFileDialogEventArgs._members
  altText: CustomShowSaveFileDialogEventArgs Members
---
Declares the [CustomShowSaveFileDialogEventArgs.Dialog](xref:DevExpress.ExpressApp.Win.SystemModule.CustomShowSaveFileDialogEventArgs.Dialog) property returning the Save File Dioalog. You can customize this dialog in the event handler so that it is invoked with the required options for end-users. Set the Dialog's result to the [CustomShowSaveFileDialogEventArgs.DialogResult](xref:DevExpress.ExpressApp.Win.SystemModule.CustomShowSaveFileDialogEventArgs.DialogResult) property, to continue the export or cancel it, in dependence of this property's value.