---
uid: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor
name: DxPivotGridListEditor
type: Class
summary: 'A [List Editor](xref:113189) that you can use in XAF ASP.NET Core Blazor applications to display data as a Pivot Grid.'
syntax:
  content: 'public class DxPivotGridListEditor : ListEditor, IComplexListEditor, IComponentContentHolder, IDxGridLayoutChangedHolder, ISupportUpdate'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor._members
  altText: DxPivotGridListEditor Members
- linkId: 113303
---
[List Views](xref:112611) use List Editors to display object collections in the UI. The `DxPivotGridListEditor` uses instances of the DevExpress Blazor @DevExpress.Blazor.PivotTable.DxPivotTable component to display object collections. This component allows you to display and analyze multidimensional data from an underlying data source.

![|Blazor Pivot Grid Editor](~/images/pivot-grid/xaf-blazor-pivot-grid-overview.png)

### Supported Data Access Modes

- Client
- DataView
- Queryable

For general information on data access modes, refer to the following topic: [List View Data Access Modes](xref:113683).

### Display DxPivotGridListEditor in a List View

To display a List View as a Pivot Grid, follow these steps:

1. Open the [Model Editor](xref:112582) for the _SolutionName.Blazor.Server\Model.xafml_ file.
2. Navigate to the required List View node: **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView**.
3. Set the @DevExpress.ExpressApp.Model.IModelListView.EditorType property to `DxPivotGridListEditor`.

![PivotGrid list editor in the Model Editor](~/images/pivot-grid/xaf-blazor-pivot-grid-model-editor.png)

### Customize Pivot Grid Settings

You can customize the Pivot Grid settings in the following ways:

#### Specify Column Model Settings
Use the [Model Editor](xref:112582) to configure Pivot Grid column settings (navigate to the following node: **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView** | **Columns** | **ColumnName**). The most useful properties include: 
@DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.Caption
:   Specifies the caption of the current column.

: @DevExpress.ExpressApp.Model.IModelNode.Index
: @DevExpress.ExpressApp.Model.IModelColumn.SortOrder
: @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DisplayFormat
: @DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotFieldArea
: @DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotGroupInterval
: @DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotSummaryType

#### Customize DxPivotGridListEditor Settings
Use the [Model Editor](xref:112582) to configure Pivot Grid List Editor settings (navigate to the following node: **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView**). The most useful properties include:
@DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled
:   Controls the visibility of the **Show Field List** context menu item.

: @DevExpress.ExpressApp.Model.IModelListView.Filter
: @DevExpress.ExpressApp.Blazor.SystemModule.IModelListViewBlazor.VirtualScrollingEnabled

#### Customize the Pivot Grid Model
The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.PivotGridModel replicates parameters of the underlying @DevExpress.Blazor.PivotTable.DxPivotTable component. Use these parameters to configure the Pivot Grid before it is created. 

#### Handle the ComponentCaptured Event
The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.PivotGridModel does not allow direct access to the current component state or its methods. Handle the @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.ComponentCaptured event to access the underlying component instance and its full API.

### Data Summaries

The Pivot Grid displays summaries calculated against data fields (fields located in the [Data area](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotFieldArea)). The Pivot Grid calculates the total sum for numeric fields and the number of values for fields of other data types.

You can change the applied summary aggregate function in the following way:

1. Double click the _SolutionName.Blazor.Server\Model.xafml_ file to open the [Model Editor](xref:112582).
2. Navigate to **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView** | **Columns** | **FieldName**.
3. Specify the column's @DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotSummaryType property in the **Pivot Grid** section.

![Pivot column settings in the Model Editor](~/images/pivot-grid/xaf-blazor-pivot-grid-column-settings.png)

### Examples

You can find examples of the DxPivotGridListEditor implementation in the following demos:

* In the [Employee Management Demo (EF Core)](xref:113577#employee-management-demo-xpoef-core), navigate to **Payroll** > **Views** > **Pivot View** (see the [online demo](https://demos.devexpress.com/XAF/BlazorMainDemo/)).
* In the [Feature Center Demo (XPO)](xref:113577#feature-center-demo-xpo), navigate to **List Editors** > **Pivot Grid** (see the [online demo](https://demos.devexpress.com/XAF/featurecenter)).
