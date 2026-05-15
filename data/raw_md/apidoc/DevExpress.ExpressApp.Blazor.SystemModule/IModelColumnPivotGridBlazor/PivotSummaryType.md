---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotSummaryType
name: PivotSummaryType
type: Property
summary: Specifies the type of summary function applied to the current data field values.
syntax:
  content: |-
    [DefaultValue(PivotTableSummaryType.Count)]
    [ModelBrowsable(typeof(IModelListViewPivotGridBlazorVisibilityCalculator))]
    PivotTableSummaryType PivotSummaryType { get; set; }
  parameters: []
  return:
    type: DevExpress.Blazor.PivotTable.PivotTableSummaryType
    description: |-
      A type of the summary function.

      The default value is `Sum` for numeric fields and `Count` for other field types.
seealso: []
---
Pivot Grid data cells display summaries calculated against data fields. The field's summary type specifies the aggregate function.

You can specify the `PivotSummaryType` property in the [Model Editor](xref:112582):

1. Open the _SolutionName.Blazor.Server\Model.xafml_ file.
2. Navigate to the **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView** | **Columns** | **FieldName**
3. Specify column settings for the field in the **Pivot Grid** section

![Pivot column settings in the Model Editor](~/images/pivot-grid/xaf-blazor-pivot-grid-column-settings.png)
