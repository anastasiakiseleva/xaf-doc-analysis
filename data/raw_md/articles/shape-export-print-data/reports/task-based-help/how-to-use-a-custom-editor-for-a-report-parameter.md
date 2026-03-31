---
uid: "113608"
seealso: []
title: 'How to: Use a Custom Editor for an XtraReport Parameter'
---
# How to: Use a Custom Editor for an XtraReport Parameter

This example demonstrates how to specify a custom control used to edit a report parameter value when a report is being previewed.

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

## Register the Parameter Type
For instance, assume you have a report with the `parameterTitle` parameter of the `TitleOfCourtesy` type. Open the code of your report and specify the [Parameter.Type](xref:DevExpress.XtraReports.Parameters.Parameter.Type) value in the report's constructor.

# [C#](#tab/tabid-csharp)

```csharp
public partial class XtraReport1 : DevExpress.XtraReports.UI.XtraReport {
    public XtraReport1() {
        InitializeComponent();
        this.parameterTitle.Type = typeof(TitleOfCourtesy);
    }
    // ...
}
```
***

If the registered type is not a standard .NET type (such as `string`, `int`, or others) and is not used for business object properties, it is also necessary to register this type by using the approach shown in the [How to: Register an Additional Type of XtraReport Parameter](xref:113609) topic.

## Specify a Custom Editor for Parameters of a Standard .NET Type in a WinForms Report Viewer

To provide a custom editor for parameters of a standard type in a Windows Forms application, handle the [XtraReport.ParametersRequestBeforeShow](xref:DevExpress.XtraReports.UI.XtraReport.ParametersRequestBeforeShow) event, and assign the custom editor to the [ParameterInfo.Editor](xref:DevExpress.XtraReports.Parameters.ParameterInfo.Editor) property of the [](xref:DevExpress.XtraReports.Parameters.ParameterInfo) object stored in the [ParametersRequestEventArgs.ParametersInformation](xref:DevExpress.XtraReports.Parameters.ParametersRequestEventArgs.ParametersInformation) collection. To get an [](xref:DevExpress.XtraReports.UI.XtraReport) instance, handle the [ReportDataSourceHelper.BeforeShowPreview](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.BeforeShowPreview) event.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.XtraEditors;
using DevExpress.XtraReports.Parameters;
// ...
public class WinModule : ModuleBase {
    public override void Setup(ApplicationModulesManager moduleManager) {
        base.Setup(moduleManager);
        ReportsModuleV2 module = ReportsModuleV2.FindReportsModule(moduleManager.Modules);
        if(module != null) {
            module.ReportsDataSourceHelper.BeforeShowPreview += ReportsDataSourceHelper_BeforeShowPreview;
        }
    }
    private void ReportsDataSourceHelper_BeforeShowPreview(object sender, BeforeShowPreviewEventArgs e) {
        e.Report.ParametersRequestBeforeShow += (s, arg) => {
            foreach(ParameterInfo info in arg.ParametersInformation) {
                if(info.Parameter.Name == "parameter1") {
                    LookUpEdit lookUpEdit = new LookUpEdit();
                    lookUpEdit.Properties.DataSource = new List<string>(new string[] { "One", "Two"});
                    info.Editor = lookUpEdit;
                }
            }
        };
    }
}
```
***

## Specify a Custom Editor for Parameters of a Custom Type in a WinForms Report Viewer

Handle the static [ReportsWindowsFormsModuleV2.CreateCustomReportDesignRepositoryItem](xref:DevExpress.ExpressApp.ReportsV2.Win.ReportsWindowsFormsModuleV2.CreateCustomReportDesignRepositoryItem) event to specify a custom [](xref:DevExpress.XtraEditors.Repository.RepositoryItem) used to edit a parameter value when a report is being previewed. Pass your repository item using the handler's [CreateCustomReportDesignRepositoryItemEventArgs.RepositoryItem](xref:DevExpress.ExpressApp.ReportsV2.Win.CreateCustomReportDesignRepositoryItemEventArgs.RepositoryItem) parameter and set the `Handled` parameter to `true`. The specified control will be used for any report in the application.

As the `CreateCustomReportDesignRepositoryItem` is `static`, which means that you can access it anywhere in your WinForms project. For instance, you can subscribe to the `CreateCustomReportDesignRepositoryItem` in the overridden [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method of a WinForms module (in the [!include[File_WinModule](~/templates/file_winmodule111231.md)] file).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.XtraEditors.Repository;	
using DevExpress.ExpressApp.ReportsV2.Win;
// ...

public override void Setup(XafApplication application) {
    base.Setup(application);
    ReportsWindowsFormsModuleV2.CreateCustomReportDesignRepositoryItem += 
        delegate(object sender, CreateCustomReportDesignRepositoryItemEventArgs e) {
        if(e.Parameter.Name.Equals("parameterTitle")) {
            RepositoryItemLookUpEdit item = new RepositoryItemLookUpEdit();
            item.NullText = "[Select Title Of Courtesy]";
            List<TitleOfCourtesy> st = new List<TitleOfCourtesy>();
            st.Add(TitleOfCourtesy.Dr);
            st.Add(TitleOfCourtesy.Mrs);
            item.DataSource = st;
            e.RepositoryItem = item;
            e.Handled = true;
        }
    };
}
```
***
