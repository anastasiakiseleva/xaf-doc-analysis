The following code snippet implements a Controller in an ASP.NET Core Blazor module. The controller accesses export options (`GridXlExportOptions`):

# [C#](#tab/tabid-csharp1)
```csharp
using DevExpress.Blazor;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.SystemModule;
using DevExpress.ExpressApp.SystemModule;
// ...
public partial class CustomizeExportControllerBlazor : ViewController {
    public CustomizeExportControllerBlazor() {
        InitializeComponent();
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
        if(e.Options is GridXlExportOptions options) {
            options.ExportSelectedRowsOnly = true;
        }
    }
    protected override void OnDeactivated() {
        blazorExportController.CustomizeGridExport -= blazorExportController_CustomizeGridExport;
        base.OnDeactivated();
    }
}
```
***

![|XAF ASP.NET Core Blazor XLS Export of Selected Grid List Rows, DevExpress](~/images/blazor-listview-custom-export.png)
