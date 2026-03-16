---
uid: DevExpress.ExpressApp.SystemModule.IExportable.PrintableChanged
name: PrintableChanged
type: Event
summary: Occurs when the [IExportable.Printable](xref:DevExpress.ExpressApp.SystemModule.IExportable.Printable) property value is updated.
syntax:
  content: event EventHandler<PrintableChangedEventArgs> PrintableChanged
seealso: []
---
If it is required to change the control to be exported, trigger the **PrintableChanged** event in the **Printable** property's setter, to notify the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) that the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) state and items should be updated.