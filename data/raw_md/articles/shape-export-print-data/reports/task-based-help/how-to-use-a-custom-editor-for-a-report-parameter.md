---
uid: "113608"
title: 'How to: Customize Report Parameter Editors in a Report Viewer'
seealso:
  - linkId: 113609
  - linkId: 403190#create-a-custom-editor-in-the-document-viewer
    altText: 'Create a Custom Editor in the Document Viewer'
---
# How to: Customize Report Parameter Editors in a Report Viewer

This topic explains how to customize the control used to edit a report parameter value in a Report Viewer.

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

## Customize Parameter Editor (Blazor)

Create a View Controller and handle the @DevExpress.ExpressApp.DashboardViewExtensions.CustomizeViewItemControl* method. In the handler, access the `ReportViewerModel` and use its API to access and customize parameter editors.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.ReportsV2.Blazor;

namespace SolutionName.Module.Blazor.Controllers {
public class CustomizeReportParameterEditorsController :ViewController<DetailView> {
    public CustomizeReportParameterEditorsController() {
        TargetViewId = ReportsBlazorModuleV2.ReportViewerDetailViewName;
    }
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<ReportViewerViewItem>(this, CustomizeReportViewer);
    }
    private void CustomizeReportViewer(ReportViewerViewItem reportViewerViewItem) {
        reportViewerViewItem.ReportViewerModel.OnCustomizeParameters = EventCallback.Factory.Create<ParametersModel>(this, CustomizeParameters);
    }
    private void CustomizeParameters(ParametersModel parametersModel) {
        // Customize parameter editors here
    }

}
```

## Custom Parameter Editor for Standard .NET Types (WinForms)

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

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.ReportsV2
Imports DevExpress.XtraEditors
Imports DevExpress.XtraReports.Parameters
' ...
Public Class WinModule
    Inherits ModuleBase

    Public Overrides Sub Setup(ByVal moduleManager As ApplicationModulesManager)
        MyBase.Setup(moduleManager)
        Dim [module] As ReportsModuleV2 = ReportsModuleV2.FindReportsModule(moduleManager.Modules)
        If [module] IsNot Nothing Then
            AddHandler [module].ReportsDataSourceHelper.BeforeShowPreview, AddressOf ReportsDataSourceHelper_BeforeShowPreview
        End If
    End Sub
    Private Sub ReportsDataSourceHelper_BeforeShowPreview(ByVal sender As Object, ByVal e As BeforeShowPreviewEventArgs)
        AddHandler e.Report.ParametersRequestBeforeShow, Sub(s, arg)
            For Each info As ParameterInfo In arg.ParametersInformation
                If info.Parameter.Name = "parameter1" Then
                    Dim lookUpEdit As New LookUpEdit()
                    lookUpEdit.Properties.DataSource = New List(Of String)(New String() { "One", "Two"})
                    info.Editor = lookUpEdit
                End If
            Next info
        End Sub
    End Sub
End Class
```

***

## Custom Parameter Editor for Custom Types (WinForms)

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

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.XtraEditors.Repository
Imports DevExpress.ExpressApp.ReportsV2.Win
' ...
Public Overrides Sub Setup(ByVal application As XafApplication)
    MyBase.Setup(application)
    AddHandler ReportsWindowsFormsModuleV2.CreateCustomReportDesignRepositoryItem, Sub(sender As Object, e As CreateCustomReportDesignRepositoryItemEventArgs)
        If e.Parameter.Name.Equals("parameterTitle") Then
            Dim item As New RepositoryItemLookUpEdit()
            item.NullText = "[Select Title Of Courtesy]"
            Dim st As New List(Of TitleOfCourtesy)()
            st.Add(TitleOfCourtesy.Dr)
            st.Add(TitleOfCourtesy.Mrs)
            item.DataSource = st
            e.RepositoryItem = item
            e.Handled = True
        End If
    End Sub
End Sub
```

***
