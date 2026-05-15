---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotFieldArea
name: PivotFieldArea
type: Property
summary: Specifies the area where the field is displayed.
syntax:
  content: |-
    [DefaultValue(PivotTableArea.Row)]
    [ModelBrowsable(typeof(IModelListViewPivotGridBlazorVisibilityCalculator))]
    PivotTableArea PivotFieldArea { get; set; }
  parameters: []
  return:
    type: DevExpress.Blazor.PivotTable.PivotTableArea
    description: The target area.
seealso: []
---
The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor consists of four areas where you or your user can place database fields.

Rows Area
:   Field headers allow users to re-arrange fields and sort or filter data. Unique values from corresponding fields are displayed as row headers.
Columns Area
:   Field headers allow users to re-arrange fields and sort or filter data. Unique values from corresponding fields are displayed as column headers.
Data Area
:   Field headers allow users to re-arrange fields and sort or filter data. Data cells display information from these fields. Each cell value is a summary calculated against the dataset (filtered by corresponding row/column values).
Filter Area
:   Filter fields do not affect data layout. Use field headers to filter data against fields that are not used in row, column, or data areas. Refer to Filter Data for additional information.

![Field Areas in Pivot Grid](~/images/pivot-grid/xaf-blazor-pivot-grid-field-area.png)

You can specify the `PivotFieldArea` property in the [Model Editor](xref:112582):

1. Open the _SolutionName.Blazor.Server\Model.xafml_ file.
2. Navigate to the **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView** | **Columns** | **FieldName**
3. Specify column settings for the field in the **Pivot Grid** section

![Pivot column settings in the Model Editor](~/images/pivot-grid/xaf-blazor-pivot-grid-column-settings.png)