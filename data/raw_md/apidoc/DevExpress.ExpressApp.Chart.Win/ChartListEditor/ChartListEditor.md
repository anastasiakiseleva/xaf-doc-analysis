---
uid: DevExpress.ExpressApp.Chart.Win.ChartListEditor
name: ChartListEditor
type: Class
summary: The charting [List Editor](xref:113189) used in XAF Windows Forms applications.
syntax:
  content: 'public class ChartListEditor : ChartListEditorBase, IExportable, ISupportBorderStyle, IRequireContextMenu, IComplexListEditor'
seealso:
- linkId: DevExpress.ExpressApp.Chart.Win.ChartListEditor._members
  altText: ChartListEditor Members
- linkId: "113189"
- linkId: "113314"
---
List Editors are used by [List Views](xref:112611) to display object collections in a UI. The `ChartListEditor` ships with the [Chart Module](xref:113302), and displays data in the form of a chart:

![ChartListEditor](~/images/chartlisteditor116775.png)

To display object collections, the `ChartListEditor` uses an instance of the [](xref:DevExpress.XtraCharts.ChartControl) class.

For additional information on the `ChartListEditor` and an overview of the Chart Module, refer to the following topic: [Chart Module](xref:113302).

> [!NOTE]
> `ChartListEditor` supports only [Client](xref:118449) [data access mode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode).