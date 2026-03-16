---
uid: DevExpress.ExpressApp.SystemModule.IDataAwareExportableXlsx
name: IDataAwareExportableXlsx
type: Interface
summary: Implemented by [List Editors](xref:113189) that support [data-aware export](xref:17733) to the XLSX format.
syntax:
  content: 'public interface IDataAwareExportableXlsx : IDataAwareExportable'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableXlsx._members
  altText: IDataAwareExportableXlsx Members
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportable
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableCsv
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableXls
---
[](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) implements this interface.  This class uses the `DataAware` [](xref:DevExpress.Export.ExportType) when it exports to XLSX format. Other List Editors that do not implement `IDataAwareExportableXlsx` use the `WYSIWYG` export type.