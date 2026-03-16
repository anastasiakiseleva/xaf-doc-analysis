---
uid: DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor
name: DxChartListEditor
type: Class
summary: A [List Editor](xref:113189) that you can use in XAF ASP.NET Core Blazor applications to display data as a chart.
syntax:
  content: 'public class DxChartListEditor : ListEditor, IComponentContentHolder, ISupportFilterEditorEditor, IComplexListEditor, IExportable'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor._members
  altText: DxChartListEditor Members
---

List Views use List Editors to display object collections. The `DxChartListEditor` displays data as charts using the @DevExpress.Blazor.DxChart`1, @DevExpress.Blazor.DxPolarChart`1, and @DevExpress.Blazor.DxPieChart`1 classes.

![|XAF ASP.NET Core Blazor Chart List Editor, DevExpress](~/images/xaf-blazor-chartlist-editor-devexpress.png)

You do not need to enable the [](xref:113302) to work with @DevExpress.ExpressApp.Blazor.Editors.DxChartListEditor.

The `DxChartListEditor` supports popular chart types like Line, Area, Bar, Point, Range, Financial, Pie, Donut, Polar, Histogram, and Drill Down.

The `DxChartListEditor` supports the following features:

* [Client](xref:118449) and [DataView](xref:118452) modes
* Filtering: [Filter Builder](xref:112652#filter-builder), @DevExpress.Blazor.DxChartCommonSeries`4.Filter property, [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria) property
* PDF and Image export

For more information about chart configuration and customization in ASP.NET Core Blazor, refer to the following topic: [](xref:113302).

For an example, refer to the `Payroll Chart View` in the `MainDemo Blazor Server` demo application that ships with XAF. You can find this demo in the following folder: _[!include[PathToAllXafDemos](~/templates/path-to-all-xaf-demos.md)]\\MainDemo.NET.EFCore\CS\MainDemo.Blazor.Server_.