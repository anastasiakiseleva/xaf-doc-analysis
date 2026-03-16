---
uid: DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor.Printable
name: Printable
type: Property
summary: Specifies the control to be exported via the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction).
syntax:
  content: public IBasePrintable Printable { get; }
  parameters: []
  return:
    type: DevExpress.XtraPrinting.IBasePrintable
    description: An **IPrintable** object that is the control used for exporting. The default value is the SchedulerListEditor's [SchedulerListEditor.SchedulerControl](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor.SchedulerControl) property value.
seealso: []
---
The **Printable** property is exposed by the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface supported by the **[](xref:DevExpress.ExpressApp.Scheduler.Win.SchedulerListEditor)** class.