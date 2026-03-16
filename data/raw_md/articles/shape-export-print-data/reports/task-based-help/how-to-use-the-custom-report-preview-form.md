---
uid: "113603"
seealso: []
title: 'How to: Use the Custom Report Preview Form'
owner: Ekaterina Kiseleva
---
# How to: Use the Custom Report Preview Form

This example demonstrates how to show a custom **Report Preview** form in a WinForms XAF application that uses the [Reports V2 Module](xref:113591). 

![Custom Report Preview form](~/images/Reports_CustomPreviewForm.png)

1. Create a new custom form (`CustomPreviewForm` in this example) in the [WinForms application project](xref:118045) (_MySolution.Win_). Design this form as described in the following help topic: [Create a Custom Print Preview](xref:2596).

    > [!TIP]
    > Refer to the [API and Customization](xref:5158) section in the XtraReports documentation to learn more about report preview customization.

2. Add the `ShowReport` method to `CustomPreviewForm`:

    [!include[<MySolution.Win\CustomPreviewForm.cs>](~/templates/platform_specific_file_path.md)]

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.XtraReports.UI;
    using System.Windows.Forms;
    // ...
    public partial class CustomPreviewForm : Form {
        // ...
        public void ShowReport(XtraReport report){
            documentViewer1.DocumentSource = report;
            report.CreateDocument();
            Show();
        }
    }
    ```
    
    ***

    In this example, `documentViewer1` is the [](xref:DevExpress.XtraPrinting.Preview.DocumentViewer) component added to this form in the previous step.

3. Create the following Controller to display a report preview in the `CustomPreviewForm` form in the [WinForms application project](xref:118045) (_MySolution.Win_).

    [!include[<MySolution.Win\Controllers\CustomPreviewController.cs>](~/templates/platform_specific_file_path.md)]

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.ReportsV2;
    using Microsoft.Extensions.DependencyInjection;
    // ...
    public class CustomPreviewController : ViewController {
        private ReportServiceController reportServiceController;
        protected override void OnActivated() {
            base.OnActivated();
            reportServiceController = Frame.GetController<ReportServiceController>();
            if(reportServiceController != null) {
                reportServiceController.CustomShowPreview += reportServiceController_CustomShowPreview;
            }
        }
        void reportServiceController_CustomShowPreview(object sender, CustomShowPreviewEventArgs e) {
            var reportStorage = Application.ServiceProvider.GetRequiredService<IReportStorage>();
            var reportContainer = reportStorage.GetReportContainerByHandle(e.ReportContainerHandle);
            reportServiceController.SetupBeforePrint(reportContainer.Report,
                e.ParametersObject, e.Criteria, e.CanApplyCriteria, e.SortProperty, e.CanApplySortProperty);
            CustomPreviewForm form = new CustomPreviewForm();
            form.ShowReport(reportContainer.Report);
            e.Handled = true;
        }
        protected override void OnDeactivated() {
            if(reportServiceController != null) {
                reportServiceController.CustomShowPreview -= reportServiceController_CustomShowPreview;
            }
        }
    }
    ```

    ***

    [`/\.(CustomShowPreview)/`]: xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.CustomShowPreview
    [`ViewController`]: xref:DevExpress.ExpressApp.ViewController
    [`ReportServiceController`]: xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController
    [`Frame`]: xref:DevExpress.ExpressApp.Controller.Frame
    [`GetController`]: xref:DevExpress.ExpressApp.Frame.GetController``1
    [`CustomShowPreviewEventArgs`]: xref:DevExpress.ExpressApp.ReportsV2.CustomShowPreviewEventArgs
    [`IReportContainer`]: xref:DevExpress.ExpressApp.ReportsV2.IReportContainer
    [`GetReportContainerByHandle`]: xref:DevExpress.ExpressApp.ReportsV2.IReportStorage.GetReportContainerByHandle*
    [`SetupBeforePrint`]: xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.SetupBeforePrint(DevExpress.XtraReports.UI.XtraReport,DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean,DevExpress.Xpo.SortProperty[],System.Boolean)
