---
uid: DevExpress.ExpressApp.SystemModule.IExportable.SupportedExportFormats
name: SupportedExportFormats
type: Property
summary: Gets the list of export formats supported by the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) List Editor.
syntax:
  content: List<ExportTarget> SupportedExportFormats { get; }
  parameters: []
  return:
    type: System.Collections.Generic.List{DevExpress.XtraPrinting.ExportTarget}
    description: An **List\<**[](xref:DevExpress.XtraPrinting.ExportTarget)**>** object that is a list of export formats supported by the exportable List Editor.
seealso: []
---
This list is used to fill the **Items** collection of the [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction).

When supporting the **IExportable** interface in a custom List Editor,  the implementation of this property can be similar to the following:

# [C#](#tab/tabid-csharp)

```csharp
public List<ExportTarget> SupportedExportFormats {
   get {
      if(Printable == null) {
         return new List<ExportTarget>();
      }
      else {
         return new List<ExportTarget>(){
            ExportTarget.Csv,
            ExportTarget.Html,
            ExportTarget.Image,
            ExportTarget.Mht,
            ExportTarget.Pdf,
            ExportTarget.Rtf,
            ExportTarget.Text,
            ExportTarget.Xls,
            ExportTarget.Xlsx
         };
      }
   }
}
```
***