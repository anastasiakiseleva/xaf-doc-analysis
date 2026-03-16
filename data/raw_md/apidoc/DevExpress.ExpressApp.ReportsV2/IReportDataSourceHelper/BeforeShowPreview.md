---
uid: DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.BeforeShowPreview
name: BeforeShowPreview
type: Event
summary: Occurs when the [IReportDataSourceHelper.SetupBeforePrint](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.SetupBeforePrint*) method is executed.
syntax:
  content: event EventHandler<BeforeShowPreviewEventArgs> BeforeShowPreview
seealso: []
---
Handle this event to modify the report content before it is displayed. For instance, you can [merge two reports](xref:3321) immediately before they are displayed. See the following topic for details: [How to: Merge the Pages of Two Reports](xref:113606).

The following code snippet uses the `BeforeShowPreview` event to gain access to a report after it has been generated and to hide unwanted parameters:

```csharp{26,29,32-36}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using YourSolutionName.Module.BusinessObjects;

namespace YourSolutionName.Blazor.Server.Controllers;
public class CustomBlazorController :ViewController {
    public CustomBlazorController() {
        var myAction1 = new SimpleAction(this, "MyBlazorAction1", PredefinedCategory.Edit);
        myAction1.Execute += MyAction1_Execute;
    }

    private void MyAction1_Execute(object sender, SimpleActionExecuteEventArgs e) {
        var reportOsProvider = ReportDataProvider.GetReportObjectSpaceProvider(this.Application.ServiceProvider);
        var reportStorage = ReportDataProvider.GetReportStorage(this.Application.ServiceProvider);

        IObjectSpace objectSpace = reportOsProvider.CreateObjectSpace(typeof(ReportDataV2));
        Contact userReport = (Contact)e.CurrentObject;
        IReportDataV2 reportData = objectSpace.FirstOrDefault<ReportDataV2>(data => data.DisplayName == "test1");
        string handle = reportStorage.GetReportContainerHandle(reportData);
        ReportServiceController controller = Frame.GetController<ReportServiceController>();

        var dataSourceHelper = Application.ServiceProvider.GetRequiredService<IReportDataSourceHelper>();
        dataSourceHelper.BeforeShowPreview += DataSourceHelper_BeforeShowPreview;

        controller.ShowPreview(handle);
        dataSourceHelper.BeforeShowPreview -= DataSourceHelper_BeforeShowPreview;
    }

    private void DataSourceHelper_BeforeShowPreview(object sender, BeforeShowPreviewEventArgs e) {
        var rep = e.Report;
        rep.Parameters[0].Visible = false;
        rep.FilterString = null;
    }
}
```