---
uid: "118348"
seealso: []
title: 'Open a Detail View When the Grid Row is Clicked in the Dashboard (WinForms)'
owner: Ekaterina Kiseleva
---
# Open a Detail View When the Grid Row is Clicked in the Dashboard (WinForms)

This topic describes how to invoke a Detail View when a user clicks a row in the [](xref:DevExpress.DashboardCommon.GridDashboardItem) created using the [Dashboards Module](xref:117449). In the invoked Detail View, a user can view or edit a [business object](xref:113664) corresponding to the clicked row.

[!example[XAF - Open a Detail View When a Grid Row is Clicked in the Dashboard](https://github.com/DevExpress-Examples/xaf-blazor-open-detail-view-when-grid-row-is-clicked-in-the-dashboard)]

* Add a key property to the [hidden measures](xref:15706) of a Dashboard and set its summary type to `Min` or `Max`. The key property in this example is `Oid`.

    ![DashboardDesigner_OidMeasure_Win](~/images/dashboarddesigner_oidmeasure_win129865.png)

* Add a [View Controller](xref:112621) to the [WinForms application project](xref:118045) (_MySolution.Win_).
* Access the [](xref:DevExpress.ExpressApp.Dashboards.Win.WinDashboardViewerViewItem) according to the [How to: Access the Dashboard Control](xref:117454) topic.
* Access the [](xref:DevExpress.DashboardWin.DashboardViewer) and subscribe to the [DashboardViewer.DashboardItemDoubleClick](xref:DevExpress.DashboardWin.DashboardViewer.DashboardItemDoubleClick) event.
* In the `DashboardItemDoubleClick` event handler, get the key property value using the [](xref:DevExpress.DashboardWin.DashboardItemMouseActionEventArgs) arguments.
* Create a new [Object Space](xref:113707) and use the [IObjectSpace.FirstOrDefault](xref:DevExpress.ExpressApp.IObjectSpace.FirstOrDefault*) method to find the clicked object.
* Pass the found object to the [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) method to create a Detail View.
* Pass the created Detail View to the @DevExpress.ExpressApp.ShowViewStrategyBase.ShowViewFromCommonView(DevExpress.ExpressApp.View,DevExpress.ExpressApp.Frame,DevExpress.ExpressApp.Actions.ActionBase) method to display it.

# [WinShowDetailViewFromDashboardController.cs](#tab/tabid-csharp)

```csharp
using DevExpress.DashboardCommon;
using DevExpress.DashboardCommon.ViewerData;
using DevExpress.DashboardWin;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Dashboards.Win;
using DevExpress.Persistent.Base;
using OpenViewFromDashboardEF.Module.BusinessObjects;

public class WinShowDetailViewFromDashboardController :ObjectViewController<DetailView, IDashboardData> {

    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<WinDashboardViewerViewItem>(this, item => {
            item.Viewer.DashboardItemDoubleClick += Viewer_DashboardItemDoubleClick;
        });
    }
    private bool IsGridDashboardItem(Dashboard dashboard, string dashboardItemName) {
        DashboardItem dashboardItem = dashboard.Items.SingleOrDefault(item => item.ComponentName == dashboardItemName);
        return dashboardItem is GridDashboardItem;
    }
    private static Guid GetID(DashboardItemMouseActionEventArgs e) {
        MultiDimensionalData data = e.Data.GetSlice(e.GetAxisPoint());
        MeasureDescriptor descriptor = data.GetMeasures().SingleOrDefault(item => item.DataMember == "ID");
        MeasureValue measureValue = data.GetValue(descriptor);
        return (Guid)measureValue.Value;
    }
    private void Viewer_DashboardItemDoubleClick(object sender, DashboardItemMouseActionEventArgs e) {
        Dashboard dashboard = ((DashboardViewer)sender).Dashboard;
        if(IsGridDashboardItem(dashboard, e.DashboardItemName)) {
            OpenDetailView(GetID(e));
        }
    }

    private void OpenDetailView(Guid contactId) {
        IObjectSpace objectSpace = Application.CreateObjectSpace<Contact>();
        Contact contact = objectSpace.FirstOrDefault<Contact>(c => c.ID == contactId);
        if(contact != null) {
            DetailView detailView = Application.CreateDetailView(objectSpace, contact, View);
            Application.ShowViewStrategy.ShowViewFromCommonView(detailView);
        }
    }

}
```
***