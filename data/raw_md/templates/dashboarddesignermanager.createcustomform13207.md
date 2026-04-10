* Add the new [](xref:DevExpress.XtraEditors.XtraForm) or [](xref:DevExpress.XtraBars.Ribbon.RibbonForm) to the project.
* Add the [](xref:DevExpress.DashboardWin.DashboardDesigner) control to the newly created form according to the **Create a Designer Application** section of the [Create a WinForms Designer](xref:12137) topic.
* Add the `DashboardDesigner` type property to the custom form.
* Create a [Controller](xref:112621) in the [WinForms application project](xref:118045) (_MySolution.Win_). This Controller activates in the [](xref:DevExpress.Persistent.Base.IDashboardData) Views only.
* Use the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method to access the `WinShowDashboardDesignerController`.
* Use the `WinShowDashboardDesignerController.DashboardDesignerManager` property to access the [](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager) object.
* Handle the [DashboardDesignerManager.CreateCustomForm](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager.CreateCustomForm) event. Create and assign a custom form to the [CreateCustomFormEventArgs.Form](xref:DevExpress.ExpressApp.Dashboards.Win.CreateCustomFormEventArgs.Form) property.

> [!NOTE]
> A complete sample project is available at [https://github.com/DevExpress-Examples/xaf-how-to-show-a-custom-form-as-the-winforms-dashboard-designer](https://github.com/DevExpress-Examples/xaf-how-to-show-a-custom-form-as-the-winforms-dashboard-designer).

# [CustomDashboardDesignerFormController.cs](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Dashboards.Win;
using DevExpress.Persistent.Base;
// ...
public class CustomDashboardDesignerFormController : ObjectViewController<ObjectView, IDashboardData> {
    private WinShowDashboardDesignerController showDashboardDesignerController;
    protected override void OnActivated() {
        base.OnActivated();
        showDashboardDesignerController = Frame.GetController<WinShowDashboardDesignerController>();
        if(showDashboardDesignerController != null) {
            showDashboardDesignerController.DashboardDesignerManager.CreateCustomForm += Manager_CreateCustomForm;
        }
    }
    private void Manager_CreateCustomForm(object sender, CreateCustomFormEventArgs e) {
        e.Form = new CustomDashboardDesignerForm();
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if(showDashboardDesignerController != null) {
            showDashboardDesignerController.DashboardDesignerManager.CreateCustomForm -= Manager_CreateCustomForm;
        }
    }
}
```
***
# [CustomDashboardDesignerForm.cs](#tab/tabid-csharp)

```csharp
using DevExpress.DashboardWin;
// ...
public partial class CustomDashboardDesignerForm : DevExpress.XtraBars.Ribbon.RibbonForm {
    public CustomDashboardDesignerForm() {
        InitializeComponent();
    }
    public DashboardDesigner Designer {
        get { return dashboardDesigner; }
    }
}
```
***

<!--https://github.com/DevExpress-Examples/xaf-how-to-show-a-custom-form-as-the-winforms-dashboard-designer.git-->
