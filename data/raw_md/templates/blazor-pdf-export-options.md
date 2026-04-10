When you export data to PDF, subscribe to the [BlazorExportController.CustomizeGridExport](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController.CustomizeGridExport) event and use the event handler's [DocumentOptions](xref:DevExpress.ExpressApp.Blazor.SystemModule.GridExportEventArgs.DocumentOptions) parameter to access @DevExpress.Blazor.GridDocumentExportOptions.

The following code snippet specifies PDF export options (limits export to selected rows only):

# [C#](#tab/tabid-csharp1)
```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.SystemModule;
using DevExpress.ExpressApp.SystemModule;
// ...
public partial class CustomizeExportControllerBlazor : ViewController {
    public CustomizeExportControllerBlazor() {
        TargetViewType = ViewType.ListView;
    }
    private BlazorExportController blazorExportController;
    protected override void OnActivated() {
        base.OnActivated();
        blazorExportController = Frame.GetController<BlazorExportController>();
        // Subscribe to CustomizeGridExport event
        blazorExportController.CustomizeGridExport += blazorExportController_CustomizeGridExport;
    }
    void blazorExportController_CustomizeGridExport(object sender, GridExportEventArgs e) {
        // Export only selected rows
        if(e.DocumentOptions != null) {
            e.DocumentOptions.ExportSelectedRowsOnly = true;
        }
    }
    protected override void OnDeactivated() {
        blazorExportController.CustomizeGridExport -= blazorExportController_CustomizeGridExport;
        base.OnDeactivated();
    }
}
```
***

![XAF ASP.NET Core Blazor PDF Export of Selected Grid List Rows, DexExpress](~/images/xaf-pdf-export-customized-rows-devexpress.gif)