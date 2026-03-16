---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomForceGridControlMethods
name: CustomForceGridControlMethods
type: Event
summary: Occurs when the [PrintingController.PrintAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintAction) and [PrintingController.PrintPreviewAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintPreviewAction) are executed and the [PrintingController.CustomPrint](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomPrint) and [PrintingController.CustomShowPrintPreview](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomShowPrintPreview) events are not handled.
syntax:
  content: public event EventHandler<CustomForceGridControlMethodsEventArgs> CustomForceGridControlMethods
seealso: []
---
By default, native [](xref:DevExpress.XtraGrid.GridControl) methods are used instead of the [](xref:DevExpress.XtraPrinting.PrintableComponentLink) class when the [](xref:DevExpress.ExpressApp.CollectionSource) object is in the [Server](xref:118450) mode. Handle the **CustomForceGridControlMethods** event to enforce the use of **GridControl** methods, when required.