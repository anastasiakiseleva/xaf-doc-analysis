---
uid: DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor.Printable
name: Printable
type: Property
summary: Specifies the control to be exported via the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction).
syntax:
  content: public IBasePrintable Printable { get; }
  parameters: []
  return:
    type: DevExpress.XtraPrinting.IBasePrintable
    description: An **IPrintable** object that is the control used for exporting.
seealso: []
---
The **Printable** property is exposed by the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface supported by the **[](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor)** class.

A PivotGridListEditor can be presented in two modes. In each mode, the **Printable** property has an appropriate default value:

| Mode | **Printable** property's default value |
|---|---|
| A Pivot Grid | The [PivotGridListEditor.PivotGridControl](xref:DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor.PivotGridControl) property's value |
| A Pivot Grid together with a Chart. | A **XafLayoutControl** object that is a layout control |