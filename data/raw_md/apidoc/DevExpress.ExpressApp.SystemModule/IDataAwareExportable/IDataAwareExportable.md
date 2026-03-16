---
uid: DevExpress.ExpressApp.SystemModule.IDataAwareExportable
name: IDataAwareExportable
type: Interface
summary: Implemented by [List Editors](xref:113189) that support [data-aware export](xref:17733) to Excel formats.
syntax:
  content: public interface IDataAwareExportable
seealso: []
---
[](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) implements this interface. This class uses the `DataAware` @DevExpress.Export.ExportType by default when it exports to Excel formats. Other List Editors that do not implement `IDataAwareExportable` use the `WYSIWYG` export type.

The `IDataAwareExportable` interface declares no members. The following interfaces implement this interface and declare the format-specific `Export` method:

* [](xref:DevExpress.ExpressApp.SystemModule.IDataAwareExportableCsv)
* [](xref:DevExpress.ExpressApp.SystemModule.IDataAwareExportableXls)
* [](xref:DevExpress.ExpressApp.SystemModule.IDataAwareExportableXlsx)

You can use the static [ExportSettings.DefaultExportType](xref:DevExpress.Export.ExportSettings.DefaultExportType) property to switch from data-aware to the WYSIWYG mode of data export. Alternatively, you can handle the [ExportController.CustomExport](xref:DevExpress.ExpressApp.SystemModule.ExportController.CustomExport) event as demonstrated in the [How to: Customize the Export Action Behavior](xref:113287) topic and customize the [CustomExportEventArgs.ExportOptions](xref:DevExpress.ExpressApp.SystemModule.CustomExportEventArgs.ExportOptions) parameter as follows:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.Export;
// ...
public class CustomizeExportTypeController : ViewController {
    private ExportController exportController;
    protected override void OnActivated() {
        base.OnActivated();
        exportController = Frame.GetController<ExportController>();
        if (exportController != null) {
            exportController.CustomExport += CustomExport;
        }
    }
    protected virtual void CustomExport(object sender, CustomExportEventArgs e) {
        ((IDataAwareExportOptions)e.ExportOptions).ExportType = ExportType.WYSIWYG;
    }
    protected override void OnDeactivated() {
        if (exportController != null) {
             exportController.CustomExport -= new EventHandler<CustomExportEventArgs>(CustomExport);
        }
        base.OnDeactivated();
    }
}
```
***