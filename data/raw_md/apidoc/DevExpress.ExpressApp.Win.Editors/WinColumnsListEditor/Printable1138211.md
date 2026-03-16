---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.Printable
name: Printable
type: Property
summary: Gets the control to be exported via the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction).
syntax:
  content: public IBasePrintable Printable { get; }
  parameters: []
  return:
    type: DevExpress.XtraPrinting.IBasePrintable
    description: An **IPrintable** object that is the control used for exporting. The default value is the GridListEditor's [WinColumnsListEditor.Grid](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.Grid) property value.
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ExportController
---
The **Printable** property is exposed by the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface supported by the **[](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor)** class.