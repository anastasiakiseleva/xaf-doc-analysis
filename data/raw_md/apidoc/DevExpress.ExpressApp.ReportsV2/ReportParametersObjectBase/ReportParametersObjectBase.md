---
uid: DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase
name: ReportParametersObjectBase
type: Class
summary: The base class for classes that specify parameters shown in a popup Detail View before a report is executed.
syntax:
  content: public abstract class ReportParametersObjectBase
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase._members
  altText: ReportParametersObjectBase Members
- linkId: "114451"
- linkId: "114454"
---
To create a custom report parameters object, inherit this class. Override the [ReportParametersObjectBase.GetCriteria](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase.GetCriteria) and [ReportParametersObjectBase.GetSorting](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase.GetSorting) methods to specify criteria and sorting based on the user input (see [Data Filtering in Reports V2](xref:113594) and [Data Sorting in Reports V2](xref:113595)).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.ReportsV2;
using DevExpress.Xpo;
using DevExpress.Xpo.DB;
// ...
[DomainComponent]
public class DemoParameters : ReportParametersObjectBase {
    public bool SortByFirstName { get; set; }
    public bool FilterByFirstName { get; set; }
    public string FirstName { get; set; }
    public bool FilterByPosition { get; set; }
    public Position ContactPosition { get; set; }
    public DemoParameters(IObjectSpaceCreator provider) : base(provider) { }
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
    public override string ToString() {
        return "London";
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.Data.Filtering
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.DC
Imports DevExpress.ExpressApp.ReportsV2
Imports DevExpress.Xpo
Imports DevExpress.Xpo.DB
' ...
<DomainComponent> _
Public Class DemoParameters
    Inherits ReportParametersObjectBase

    Public Property SortByFirstName() As Boolean
    Public Property FilterByFirstName() As Boolean
    Public Property FirstName() As String
    Public Property FilterByPosition() As Boolean
    Public Property ContactPosition() As Position
    Public Sub New(ByVal provider As IObjectSpaceCreator)
        MyBase.New(provider)
    End Sub
    Protected Overrides Function CreateObjectSpace() As IObjectSpace
        Return objectSpaceCreator.CreateObjectSpace(GetType(Contact))
    End Function
    Public Overrides Function GetCriteria() As CriteriaOperator
        Dim criteriaName As CriteriaOperator = Nothing
        Dim criteriaPosition As CriteriaOperator = Nothing
        If FilterByFirstName Then
            criteriaName = CriteriaOperator.Parse("FirstName = ?", FirstName)
        End If
        If FilterByPosition Then
            criteriaPosition = CriteriaOperator.Parse("Position.Oid = ?", ContactPosition.Oid)
        End If
        Return CriteriaOperator.And(criteriaName, criteriaPosition)
    End Function
    Public Overrides Function GetSorting() As SortProperty()
        Dim sorting As New List(Of SortProperty)()
        If SortByFirstName Then
            sorting.Add(New SortProperty(NameOf(FirstName), SortingDirection.Ascending))
        End If
        Return sorting.ToArray()
    End Function
    Public Overrides Function ToString() As String
        Return "London"
    End Function
End Class
```

***

Do not forget to apply the [](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) to this class. Otherwise, the class will not be added to the Application Model and the report parameters Detail View will not be generated.

The CreateObjectSpace method should be overridden to create an object space capable of creating instances of a report's data source type. The IObjectSpaceCreator.CreateObjectSpace method operates in the same manner as the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method with the objectType argument.

To assign the implemented parameters type to a report stored in the database, use the  [IReportDataV2.ParametersObjectType](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.ParametersObjectType) property. To assign it to a predefined report, pass the _parametersObjectType_ parameter to the [PredefinedReportsUpdater.AddPredefinedReport\<T>](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport*) method.