---
uid: DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater
name: PredefinedReportsUpdater
type: Class
summary: A [](xref:DevExpress.ExpressApp.Updating.ModuleUpdater) descendant intended to register [](xref:DevExpress.XtraReports.UI.XtraReport) objects created at design time for the use with the [Reports V2 Module](xref:113591).
syntax:
  content: 'public class PredefinedReportsUpdater : ModuleUpdater'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater._members
  altText: PredefinedReportsUpdater Members
- linkId: "113591"
---
To register a predefined XtraReport, override the [ModuleBase.GetModuleUpdaters](xref:DevExpress.ExpressApp.ModuleBase.GetModuleUpdaters(DevExpress.ExpressApp.IObjectSpace,System.Version)) method, instantiate the **PredefinedReportsUpdater** and add a report via the [PredefinedReportsUpdater.AddPredefinedReport](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport(DevExpress.ExpressApp.ReportsV2.IReportDataV2)) method. Then, add the **PredefinedReportsUpdater** instance to the result array of the **AddPredefinedReport** method.

# [C#](#tab/tabid-csharp)

```csharp
public override IEnumerable<ModuleUpdater> GetModuleUpdaters(IObjectSpace objectSpace, Version versionFromDB) {
    PredefinedReportsUpdater predefinedReportsUpdater = new PredefinedReportsUpdater(Application, objectSpace, versionFromDB);
    predefinedReportsUpdater.AddPredefinedReport<XtraReport1>("Contacts Report", typeof(Contact));
    return new ModuleUpdater[] { predefinedReportsUpdater };
}
```
***

> [!NOTE]
> [!include[PredefinedReportsUpdater_MultipleInstancesNote](~/templates/predefinedreportsupdater_multipleinstancesnote111179.md)]