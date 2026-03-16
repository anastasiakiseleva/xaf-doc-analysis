---
uid: DevExpress.ExpressApp.SystemModule.IDataAwareExportableXls
name: IDataAwareExportableXls
type: Interface
summary: Implemented by [List Editors](xref:113189) that support [data-aware export](xref:17733) to the XLS format.
syntax:
  content: 'public interface IDataAwareExportableXls : IDataAwareExportable'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableXls._members
  altText: IDataAwareExportableXls Members
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportable
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableCsv
- linkId: DevExpress.ExpressApp.SystemModule.IDataAwareExportableXlsx
---
[](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) implements this interface.  This class uses the `DataAware` [](xref:DevExpress.Export.ExportType) when it exports to XLS format. Other List Editors that do not implement `IDataAwareExportableXls` use the `WYSIWYG` export type.