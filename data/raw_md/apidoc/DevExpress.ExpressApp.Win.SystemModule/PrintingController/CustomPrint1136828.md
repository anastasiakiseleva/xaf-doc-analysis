---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomPrint
name: CustomPrint
type: Event
summary: Occurs when the [PrintingController.PrintAction](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintAction) is executed.
syntax:
  content: public event EventHandler<HandledEventArgs> CustomPrint
seealso: []
---
Use this event to implement custom printing. Set the **Handled** parameter to **true** to disable standard processing.