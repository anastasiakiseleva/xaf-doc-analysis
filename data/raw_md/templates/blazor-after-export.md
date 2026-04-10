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
        blazorExportController.GridExported += blazorExportController_GridExported;
    }
    void blazorExportController_GridExported(object sender, GridExportEventArgs e) {
        Application.ShowViewStrategy.ShowMessage("Export successful!");
    }
    protected override void OnDeactivated() {
        blazorExportController.GridExported -= blazorExportController_GridExported;
        base.OnDeactivated();
    }
}
```

***

The following image illustrates the message that appears when export is complete.

![|Export notification](~/images/blazor-export-success.png)