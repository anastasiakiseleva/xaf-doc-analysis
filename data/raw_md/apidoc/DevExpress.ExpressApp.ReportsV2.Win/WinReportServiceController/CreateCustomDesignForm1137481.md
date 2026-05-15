---
uid: DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.CreateCustomDesignForm
name: CreateCustomDesignForm
type: Event
summary: Occurs when the [Report Designer](xref:4256) form is created.
syntax:
  content: public event EventHandler<CreateCustomDesignFormEventArgs> CreateCustomDesignForm
seealso: []
---
Handle this event to specify a custom Report Designer form. In the event handler, pass your custom form to the **DesignForm** parameter. An example is provided in the [How to: Use the Custom WinForms Report Designer](xref:113605) topic.

You can also use the **CreateCustomDesignForm** event to customize the default Report Designer. For instance, you can add a custom Data Source component (inherited from [](xref:DevExpress.Persistent.Base.ReportsV2.DataSourceBase)) to the designer's toolbox:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ReportsV2.Win;
// ...
public class AddCustomDataSourceController : ViewController {
    private WinReportServiceController reportService;
    protected override void OnActivated() {
        base.OnActivated();
        reportService = Frame.GetController<WinReportServiceController>();
        if (reportService != null) {
             reportService.CreateCustomDesignForm += delegate(object sender, CreateCustomDesignFormEventArgs e) {
                e.DesignForm.DesignMdiController.DesignPanelLoaded += DesignMdiController_DesignPanelLoaded;
                ((XtraForm)designForm).FormClosed += designForm_FormClosed;
            };
        }
    }
    private void DesignMdiController_DesignPanelLoaded(object sender, DesignerLoadedEventArgs args) {
        AddToolboxItem(args.DesignerHost);
    }
    private void AddToolboxItem(IServiceProvider serviceProvider) {
        IToolboxService ts = (IToolboxService)serviceProvider.GetService(typeof(IToolboxService));
        ts.AddToolboxItem(new ToolboxItem(typeof(CustomDataSource)), "Custom Category");
    }
    private void designForm_FormClosed(object sender, FormClosedEventArgs e) {
        ((IDesignForm)sender).DesignMdiController.DesignPanelLoaded -= new DesignerLoadedEventHandler(DesignMdiController_DesignPanelLoaded);
        ((XtraForm)sender).FormClosed -= new FormClosedEventHandler(designForm_FormClosed);
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp.ReportsV2.Win
' ...
Public Class AddCustomDataSourceController
    Inherits ViewController

    Private reportService As WinReportServiceController
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        reportService = Frame.GetController(Of WinReportServiceController)()
        If reportService IsNot Nothing Then
             AddHandler reportService.CreateCustomDesignForm, Sub(sender As Object, e As CreateCustomDesignFormEventArgs)
                AddHandler e.DesignForm.DesignMdiController.DesignPanelLoaded, AddressOf DesignMdiController_DesignPanelLoaded
                AddHandler CType(designForm, XtraForm).FormClosed, AddressOf designForm_FormClosed
             End Sub
        End If
    End Sub
    Private Sub DesignMdiController_DesignPanelLoaded(ByVal sender As Object, ByVal args As DesignerLoadedEventArgs)
        AddToolboxItem(args.DesignerHost)
    End Sub
    Private Sub AddToolboxItem(ByVal serviceProvider As IServiceProvider)
        Dim ts As IToolboxService = CType(serviceProvider.GetService(GetType(IToolboxService)), IToolboxService)
        ts.AddToolboxItem(New ToolboxItem(GetType(CustomDataSource)), "Custom Category")
    End Sub
    Private Sub designForm_FormClosed(ByVal sender As Object, ByVal e As FormClosedEventArgs)
        RemoveHandler CType(sender, IDesignForm).DesignMdiController.DesignPanelLoaded, AddressOf DesignMdiController_DesignPanelLoaded
        RemoveHandler CType(sender, XtraForm).FormClosed, AddressOf designForm_FormClosed
    End Sub
End Class
```

***