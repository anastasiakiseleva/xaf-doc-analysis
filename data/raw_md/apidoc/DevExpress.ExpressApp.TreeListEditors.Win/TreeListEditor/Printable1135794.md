---
uid: DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.Printable
name: Printable
type: Property
summary: Specifies the control to be exported via the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction).
syntax:
  content: public IBasePrintable Printable { get; }
  parameters: []
  return:
    type: DevExpress.XtraPrinting.IBasePrintable
    description: An **IPrintable** object that is the control used for exporting. The default value is the TreeListEditor's [TreeListEditor.TreeList](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor.TreeList) property value.
seealso: []
---
The **Printable** property is exposed by the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface supported by the **[](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor)** class.