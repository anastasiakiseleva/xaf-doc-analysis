---
uid: DevExpress.ExpressApp.SystemModule.IDataAwareExportableCsv
name: IDataAwareExportableCsv
type: Interface
summary: Implemented by [List Editors](xref:113189) that support [data-aware export](xref:17733) to the CSV format.
syntax:
  content: 'public interface IDataAwareExportableCsv : IDataAwareExportable'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableCsv._members
  altText: IDataAwareExportableCsv Members
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportable
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableXls
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableXlsx
---

[](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) implements this interface.  This class uses the `DataAware` [](xref:DevExpress.Export.ExportType) when it exports to CSV format. Other List Editors that do not implement `IDataAwareExportableCsv` use the `WYSIWYG` export type.