---
uid: DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor
name: PivotGridListEditor
type: Class
summary: Represents the pivot grid [List Editor](xref:113189) used in the XAF Windows Forms applications.
syntax:
  content: 'public class PivotGridListEditor : PivotGridListEditorBase, IExportable, IDXPopupMenuHolder, ISupportFilter, IRequireContextMenu, IRequireDXMenuManager, ISupportBorderStyle, ISupportFilterEditor'
seealso:
- linkId: DevExpress.ExpressApp.PivotGrid.Win.PivotGridListEditor._members
  altText: PivotGridListEditor Members
- linkId: "113189"
---
List Editors are used by [List Views](xref:112611) to display object collections in a UI. `PivotGridListEditor` ships with the [Pivot Grid Module](xref:113303) and displays data in the form of a pivot table that can be accompanied by a chart:

![PivotGridListEditor](~/images/pivotgridlisteditor116777.png)

To display object collections, `PivotGridListEditor` uses instances of the [](xref:DevExpress.XtraPivotGrid.PivotGridControl) and [](xref:DevExpress.XtraCharts.ChartControl) classes.

To configure the `PivotGridListEditor`, invoke the [Model Editor](xref:112582), navigate to the required List View's **PivotSettings** node and click the ellipsis button of the `Settings` property. This will invoke the Pivot Grid Property Editor.

![PivotGridPropertyEditor](~/images/pivotgridpropertyeditor116781.png)

> [!NOTE]
> [!include[PivotSettingsNote](~/templates/pivotsettingsnote11183.md)]

End-users can also invoke the property editor via the **`PivotGridListEditor`**'s context menu, if the [Application Model](xref:112580)'s [IPivotSettings.CustomizationEnabled](xref:DevExpress.ExpressApp.PivotGrid.IPivotSettings.CustomizationEnabled) property is set to `true`.

To learn about the Pivot Grid Property Editor capabilities in detail, refer to the [PivotGrid Designer](xref:1825) help topic.

To hide and show the accompanying chart that visualizes the data selected in the pivot table, use the Show Chart item in the context menu invoked for the pivot table header region.

![PivotGridShowChart](~/images/pivotgridshowchart116786.png)

To configure the chart when it is displayed, use the Chart Options item.

![PivotGridChartOptions](~/images/pivotgridchartoptions116787.png)

Pivot table totals can be configured via the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.PivotGrid.IModelPivotSettings) node. You can do this, for example, via the Model Editor.

![PivotGridListEditorTotals](~/images/pivotgridlisteditortotals116785.png)

The `PivotGridListEditor` implements the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface - can be exported via the [](xref:DevExpress.ExpressApp.SystemModule.ExportController) and printed via the [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController):

![Export_PivotGridListEditor](~/images/export_pivotgridlisteditor116971.png)

![Printing_PivotGridListEditor](~/images/printing_pivotgridlisteditor116973.png)

For additional information on the `PivotGridListEditor` and an overview of the **PivotGrid** module, refer to the [Pivot Grid Module](xref:113303) topic.

> [!NOTE]
> `PivotGridListEditor` does not support [Server, ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) mode ([CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode)).