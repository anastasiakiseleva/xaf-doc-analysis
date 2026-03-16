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
***

You can set the **Handled** parameter to **true** to suppress the default **Report Designer**.