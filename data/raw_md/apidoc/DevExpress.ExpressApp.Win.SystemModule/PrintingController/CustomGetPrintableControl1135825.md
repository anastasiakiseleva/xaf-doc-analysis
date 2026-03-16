---
uid: DevExpress.ExpressApp.Win.SystemModule.PrintingController.CustomGetPrintableControl
name: CustomGetPrintableControl
type: Event
summary: Occurs after the [View](xref:112611)'s controls have been instantiated.
syntax:
  content: public event EventHandler<PrintableControlEventArgs> CustomGetPrintableControl
seealso:
- linkId: DevExpress.ExpressApp.Win.SystemModule.PrintingController.PrintingSettingsLoaded
---
The **CustomGetPrintableControl** event is raised as a result of invoking the [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController)'s **OnActivated** method. Handle the **CustomGetPrintableControl** event to specify the control that must be printed.