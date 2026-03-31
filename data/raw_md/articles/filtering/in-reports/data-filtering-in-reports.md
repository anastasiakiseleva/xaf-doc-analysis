---
uid: "113594"
seealso: []
title: Data Filtering in Reports
---
# Data Filtering in Reports

The following data filtering options are available in **Reports V2**:

* [FilterString Property of the Report](#filterstring-property-of-the-report)
* [Criteria Property of the Data Source](#criteria-property-of-the-data-source)
* [Report Parameters](#report-parameters)
* [Parameters Object](#parameters-object)

## FilterString Property of the Report
The [XtraReportBase.FilterString](xref:DevExpress.XtraReports.UI.XtraReportBase.FilterString) property specifies the filter applied on the client side before a report is displayed. 

The ellipsis button displayed next to the **FilterString** value in the **Properties** window invokes the **FilterString Editor** dialog, which simplifies filter creation.

![XtraReport.FilterString](~/images/xtrareport.filterstring117535.png)

## Criteria Property of the Data Source
The [data source](xref:113593)'s [DataSourceBase.Criteria](xref:DevExpress.Persistent.Base.ReportsV2.DataSourceBase.Criteria) property is used to set a filter on the server side. 

The ellipsis button displayed next to the **Criteria** value in the **Properties** window invokes the **FilterString Editor** dialog that simplifies criteria creation.

![ReportsV2_Filtering](~/images/reportsv2_filtering117393.png)

You can also use the following code to modify [criteria](xref:2036#creating-criteria) from the [](xref:DevExpress.XtraReports.UI.XRControl.BeforePrint) event.

```csharp
using DevExpress.Data.Filtering;
using YourSolutionName.Module.BusinessObjects;
using System.ComponentModel;

namespace YourSolutionName.Blazor.Server {
    public partial class Report1 : DevExpress.XtraReports.UI.XtraReport {
        public Report1() {
            InitializeComponent();
            this.BeforePrint += Report1_BeforePrint;
        }
        private void Report1_BeforePrint(object sender, CancelEventArgs e) {
            var report = (DevExpress.XtraReports.UI.XtraReport)sender;
            var dataSource = (DevExpress.Persistent.Base.ReportsV2.ISupportCriteria)report.DataSource;
            dataSource.Criteria = CriteriaOperator.FromLambda<Contact>(x => x.Age > 20);
        }
    }
}
```
[`BeforePrint`]: xref:DevExpress.XtraReports.UI.XRControl.BeforePrint

## Report Parameters
You can use [Report Parameters](xref:4812) in Filter Criteria. To refer to a parameter value, precede the parameter value with a question mark (e.g., "[Name] = ?parameterName"). For additional information on parameter use in the Filter Builder, refer to the following article: [Data Filtering Overview](xref:1184).

## Parameters Object
You can use a custom [non-persistent class](xref:116516) inherited from the [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) abstract class included in the **Reports V2** module, instead of XtraReports parameters. This object's Detail View will be displayed in a popup dialog before a report is displayed. Filtering and sorting specified via this object's [ReportParametersObjectBase.GetCriteria](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase.GetCriteria) and [ReportParametersObjectBase.GetSorting](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase.GetSorting) methods are applied to the data source. This approach is useful for defining complex filtering and sorting.

To add your Parameters Object to the [Application Model](xref:112579) and to adjust the object's Detail View layout in the [Model Editor](xref:112582), apply the [](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) to the class' declaration.

```csharp
using DevExpress.Xpo;
using DevExpress.Xpo.DB;
using DevExpress.ExpressApp.DC;
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp.ReportsV2;
// ...
[DomainComponent]
public class DemoParameters : ReportParametersObjectBase {
    public bool SortByFirstName { get; set; }
    public bool FilterByFirstName { get; set; }
    public string FirstName { get; set; }
    public bool FilterByPosition { get; set; }
    public Position ContactPosition { get; set; }

    public DemoParameters(IObjectSpaceCreator provider) : base(provider) {
        ContactPosition = ObjectSpace.FirstOrDefault<Position>(position => position.Title == "Developer");
    }

    protected override IObjectSpace CreateObjectSpace() {
        return objectSpaceCreator.CreateObjectSpace(typeof(Contact));
    }

    public override CriteriaOperator GetCriteria() {
        CriteriaOperator criteriaName = null;
        CriteriaOperator criteriaPosition = null;
        if (FilterByFirstName) {
            criteriaName = CriteriaOperator.Parse("FirstName = ?", FirstName);
        }
        if (FilterByPosition) {
            criteriaPosition = CriteriaOperator.Parse("Position.Oid = ?", ContactPosition.Oid);
        }
        return CriteriaOperator.And(criteriaName, criteriaPosition);
    }

    public override SortProperty[] GetSorting() {
        List<SortProperty> sorting = new List<SortProperty>();
        if (SortByFirstName) {
            sorting.Add(new SortProperty(nameof(FirstName), SortingDirection.Ascending));
        }
        return sorting.ToArray();
    }
}
```

### Associate the Report Parameters Object with the Report

* If a report is created at runtime, you can associate the Report Parameters Object via the [IReportDataV2.ParametersObjectType](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.ParametersObjectType) property. Right-click the report in the **Reports** list view and choose **Edit**. Then, choose the **Parameters Object Type** in the invoked Detail View.
	
	![ReportsV2_ParametersObject](~/images/reportsv2_parametersobject117391.png)
* If a report is predefined (created at design time), the Parameters object type can be passed to the [PredefinedReportsUpdater.AddPredefinedReport](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport(DevExpress.ExpressApp.ReportsV2.IReportDataV2)) method.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	predefinedReportsUpdater.AddPredefinedReport<ContactsBaseReport>(
	    "Contacts by Department", typeof(ContactsReport), typeof(MyParametersObject));
	```
	***
	
	For details on adding predefined reports, refer to the [](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater) class description.

> [!TIP]
> * To validate parameters, you can use the approach from the [Non-Persistent Objects Validation](xref:113259) topic.
> * To support [Conditional Appearance](xref:113286) and other XAF features that imply certain reactions to object property changes, support the [INotifyPropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged) interface in your `ReportParametersObjectBase` descendant (see [The Importance of Property Change Notifications for Automatic UI Updates](xref:117395)).
