---
uid: "114451"
seealso:
- linkId: "114454"
title: 'How to: Access the Report Parameters Object in Report Scripts'
owner: Ekaterina Kiseleva
---
# How to: Access the Report Parameters Object in Report Scripts

This topic describes how you can access data of the report parameters object (inherited from [](xref:DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase) and specified using [IReportDataV2.ParametersObjectType](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.ParametersObjectType)) in [report scripts](xref:2593).

Use the following code to access the Parameters Object from a script.

# [C#](#tab/tabid-csharp)

```csharp
object xafParameters = 
    ((DevExpress.XtraReports.UI.XtraReport)sender).Parameters["XafReportParametersObject"].Value
```
***

For instance, the following script displays the name of the **Position** selected in the parameters dialog as a label text.

# [C#](#tab/tabid-csharp)

```csharp
private void ContactsBaseReport_BeforePrint(object sender, System.Drawing.Printing.PrintEventArgs e) {
    label1.Text ="";
    DevExpress.XtraReports.Parameters.Parameter param = 
        (DevExpress.XtraReports.Parameters.Parameter)((DevExpress.XtraReports.UI.XtraReport)sender).
            Parameters["XafReportParametersObject"];
    if(param != null) {
        MySolution.DemoParameters xafParameter = 
            (MySolution.DemoParameters)param.Value;
        label1.Text = xafParameter.ContactPosition.Name;
    }
}
```
***
