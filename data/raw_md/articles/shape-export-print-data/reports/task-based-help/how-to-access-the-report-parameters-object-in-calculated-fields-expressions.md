---
uid: "114454"
seealso:
- linkId: "114451"
title: 'How to: Access the Report Parameters Object in Calculated Fields Expressions'
---
# How to: Access the Report Parameters Object in Calculated Fields Expressions

This topic describes how you can access data of a report parameters object (inherited from [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) and specified using [IReportDataV2.ParametersObjectType](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.ParametersObjectType)) in [calculated field expressions](xref:4813).

Override the Parameters Object's **ToString** method.

# [C#](#tab/tabid-csharp)

```csharp
public class DemoParameters : ReportParametersObjectBase {
    // ...
    public override string ToString() {
        return City;
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Public Class DemoParameters
    Inherits ReportParametersObjectBase
    ' ...
    Public Overrides Function ToString() As String
        Return City
    End Function
End Class
```

***

As a result, you can refer to the **ToString** result with the "[Parameters.XafReportParametersObject]" expression, e.g.:

``Concat([Full Name],' from ', [Parameters.XafReportParametersObject])``

Alternatively, you can create a report script, handle the **GetValue** event of a certain field and then access a parameter value as demonstrated in the [How to: Access the Report Parameters Object in Report Scripts](xref:114451) topic.

# [C#](#tab/tabid-csharp)

```csharp
private void calculatedFieldCity_GetValue(object sender, DevExpress.XtraReports.UI.GetValueEventArgs e) {
    DevExpress.XtraReports.Parameters.Parameter param =
            (DevExpress.XtraReports.Parameters.Parameter)
                ((DevExpress.XtraReports.UI.XtraReport)e.Report).Parameters["XafReportParametersObject"];
    if (param != null) {
        ReportV2Demo.Module.BusinessObjects.Contact contact = 
        (ReportV2Demo.Module.BusinessObjects.Contact)e.Row;
        ReportV2Demo.Module.Reports.DemoParameters xafParameter =
            (ReportV2Demo.Module.Reports.DemoParameters)param.Value;
        e.Value = contact.FullName + " from " + xafParameter.City;
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Private Sub calculatedFieldCity_GetValue(ByVal sender As Object, ByVal e As DevExpress.XtraReports.UI.GetValueEventArgs)
    Dim param As DevExpress.XtraReports.Parameters.Parameter = _
    CType(((DevExpress.XtraReports.UI.XtraReport)e.Report).Parameters("XafReportParametersObject"), _
    DevExpress.XtraReports.Parameters.Parameter)
    If param IsNot Nothing Then
        Dim contact As ReportV2Demo.Module.BusinessObjects.Contact = _
        CType(e.Row, ReportV2Demo.Module.BusinessObjects.Contact)
        Dim xafParameter As ReportV2Demo.Module.Reports.DemoParameters = _
        CType(param.Value, ReportV2Demo.Module.Reports.DemoParameters)
        e.Value = contact.FullName & " from " & xafParameter.City
    End If
End Sub
```

***