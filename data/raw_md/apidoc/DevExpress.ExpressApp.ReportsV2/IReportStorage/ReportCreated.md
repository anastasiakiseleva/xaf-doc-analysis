---
uid: DevExpress.ExpressApp.ReportsV2.IReportStorage.ReportCreated
name: ReportCreated
type: Event
summary: Fires after a report is prepared for printing and allows you to modify the report settings.
syntax:
  content: |-
    [Browsable(false)]
    event EventHandler<BeforeShowPreviewEventArgs> ReportCreated
seealso: []
---
```csharp
private void ReportStorage_ReportCreated(object sender, BeforeShowPreviewEventArgs e) {
    e.Report.ParametersRequestBeforeShow += (s, e) => {
        var report = (XtraReport)s;
        if (report.DisplayName == "ContactReport") {
            var parameter = e.ParametersInformation.FirstOrDefault(t => t.Parameter.Name == "MyParameter");
            if (parameter != null) {
                parameter.Parameter.Value = "TEST!";
                parameter.Parameter.Visible = false;
            }
        }
    };
}
```