---
uid: DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.CustomShowDesignForm
name: CustomShowDesignForm
type: Event
summary: Occurs before showing the **Report Designer** form.
syntax:
  content: public event EventHandler<CustomShowDesignFormEventArgs> CustomShowDesignForm
seealso: []
---
The **CustomShowDesignForm** event is raised when the [ReportServiceController.ShowDesigner](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowDesigner*) method shows the **Report Designer** form. Handle this event to implement the custom logic to be executed before showing the **Report Designer**. The following snippet illustrates how to perform customization of the **DesignForm** and **Report** objects - hide the **Report Designer** from the Windows taskbar and disable grid drawing.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ReportsV2.Win;
// ...
public class CustomizeReportDesignerController : ViewController {
    private WinReportServiceController reportService;
    protected override void OnActivated() {
        base.OnActivated();
        reportService = Frame.GetController<WinReportServiceController>();
        if (reportService != null) 
            reportService.CustomShowDesignForm += reportService_CustomShowDesignForm;
    }
    void reportService_CustomShowDesignForm(object sender, CustomShowDesignFormEventArgs e) {
        ((System.Windows.Forms.Form)e.DesignForm).ShowInTaskbar = false;
        e.Report.DrawGrid = false;
    }
    protected override void OnDeactivated() {
        if (reportService != null)
            reportService.CustomShowDesignForm -= reportService_CustomShowDesignForm;
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp.ReportsV2.Win
' ...
Public Class CustomizeReportDesignerController
    Inherits ViewController
    Private reportService As WinReportServiceController
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        reportService = Frame.GetController(Of WinReportServiceController)()
        If reportService IsNot Nothing Then
            AddHandler reportService.CustomShowDesignForm, _
            AddressOf reportService_CustomShowDesignForm
        End If
    End Sub
    Private Sub reportService_CustomShowDesignForm( _
    ByVal sender As Object, ByVal e As CustomShowDesignFormEventArgs)
        CType(e.DesignForm, System.Windows.Forms.Form).ShowInTaskbar = False
        e.Report.DrawGrid = False
    End Sub
    Protected Overrides Sub OnDeactivated()
        If reportService IsNot Nothing Then
            RemoveHandler reportService.CustomShowDesignForm, _
            AddressOf reportService_CustomShowDesignForm
        End If
    End Sub
End Class
```

***

You can set the **Handled** parameter to **true** to suppress the default **Report Designer**.