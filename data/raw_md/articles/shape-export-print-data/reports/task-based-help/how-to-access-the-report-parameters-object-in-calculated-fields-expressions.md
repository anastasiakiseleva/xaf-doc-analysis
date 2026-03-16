---
uid: "114454"
seealso:
- linkId: "114451"
title: 'How to: Access the Report Parameters Object in Calculated Fields Expressions'
owner: Ekaterina Kiseleva
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
***