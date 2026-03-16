---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomShowPrintPreview
name: CustomShowPrintPreview
type: Event
summary: Occurs when the [PrintingController.PrintPreviewAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintPreviewAction) is executed.
syntax:
  content: public event EventHandler<CustomShowPrintPreviewEventArgs> CustomShowPrintPreview
seealso: []
---
Use this event to implement a custom print preview display. Set the **Handled** parameter to **true** to disable standard processing.