---
uid: "113602"
seealso: []
title: In-Place Reports
---
# In-Place Reports

The **Reports V2** module allows you to design reports for a filtered [Reports V2 data source](xref:113593) (see [Data Filtering in Reports V2](xref:113594)). In some scenarios, you may need to preview a report for a certain object or a set of objects that are not related by criteria. For example, the **Invoice** business object(s) should be able to be printed in a specific manner. In this case, a specially designed report should be available for display for a particular set of **Invoice** objects. For this purpose, use the **Inplace Reporting** feature provided by the **Reports V2** module. This topic demonstrates how to use this feature.

To show selected object(s) in a specified report, the **Reports V2** module introduces the **ShowInReport** Action. This Action represents the [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) class instance. Its items represent so-called inplace reports that are designed for the current View's object type.

Windows Forms
:   ![InplaceReports](~/images/inplacereports116026.png)

ASP.NET Core Blazor  
:   ![InplaceReports_Blazor](~/images/InplaceReports_Blazor.png)

When executing this Action, the selected report is shown in the **Preview** window. The report presents the object(s) selected in the current **Detail View** or **List View**. To render it, XAF changes the [DataSourceBase.Criteria](xref:DevExpress.Persistent.Base.ReportsV2.DataSourceBase.Criteria) property of the report's [Data Source](xref:113593) according to the items selected.

Windows Forms  
:   ![InplaceReports_Preview](~/images/inplacereports_preview116029.png)

ASP.NET Core Blazor
:   ![InplaceReports_Preview_Blazor](~/images/InplaceReports_Preview_Blazor.png)

The **ShowInReport** Action is contained in **PrintSelectionBaseController**. This Controller collects the in-place reports that are appropriate for the current object type, and creates corresponding items for the Action. When there are no appropriate in-place reports for the current object type, the **ShowInReport** Action is not activated. Inherit from this controller or use its events when implementing a custom functionality. This controller has no platform-specific descendants.

In-place reports represent common reports that can be created in an XAF application. To make a report in-place, you should set the **ReportData.IsInplaceReport** property to **true**. (By default, this property is set to **false**.) To specify this property, invoke a **Detail View** for the required report. To do this, use the **EditReportController.Edit** Action in the WinForms or ASP.NET Core Blazor application.

![InplaceReports_EditAction](~/images/inplacereports_editaction116028.png)

> [!NOTE]
> * The **ShowInReport** Action is disabled if there are unsaved changes. You need to commit changes to preview a report.
> * The **ShowInReport** Action uses the in-place reports cache to generate and store the Action's items. Note that this cache is not updated automatically. Refer to the [](xref:DevExpress.ExpressApp.ReportsV2.InplaceReportsCacheHelper) class description for information on how to update this cache manually.

The [Application Model](xref:112580)'s [IModelNavigationItemsForReports.GenerateRelatedReportsGroup](xref:DevExpress.ExpressApp.ReportsV2.IModelNavigationItemsForReports.GenerateRelatedReportsGroup) property specifies whether or not context navigation is enabled for the **Reports V2** module. When this property is set to **true**, the **Reports V2** module adds navigation items for the items corresponding to business classes participating in existing in-place reports. Each added item represents an in-place report. For additional information on context navigation, refer to the [Navigation System](xref:113198) help topic.

You can disable the **Inplace Reports** feature. Before an [](xref:DevExpress.ExpressApp.XafApplication) object is created, set the static **ReportsModule.DefaultEnableInplaceReports** property to **false**.

To create a [predefined](xref:113591) in-place report, use the [PredefinedReportsUpdater.AddPredefinedReport](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport(DevExpress.ExpressApp.ReportsV2.IReportDataV2)) method overload that takes the _isInplaceReport_ parameter.

# [C#](#tab/tabid-csharp)

```csharp
predefinedReportsUpdater.AddPredefinedReport<XtraReport1>(
    "My Inplace Report", typeof(Contact), isInplaceReport: true);
```
***