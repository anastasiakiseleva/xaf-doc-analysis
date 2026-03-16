---
uid: DevExpress.ExpressApp.Chart.Win.ChartListEditor.Printable
name: Printable
type: Property
summary: Specifies the control to be exported via the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction).
syntax:
  content: public IBasePrintable Printable { get; }
  parameters: []
  return:
    type: DevExpress.XtraPrinting.IBasePrintable
    description: An **IPrintable** object that is the control used for exporting. The default value is the ChartListEditor's [ChartListEditor.ChartControl](xref:DevExpress.ExpressApp.Chart.Win.ChartListEditor.ChartControl) property value.
seealso: []
---
The **Printable** property is exposed by the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface supported by the **[](xref:DevExpress.ExpressApp.Chart.Win.ChartListEditor)** class.