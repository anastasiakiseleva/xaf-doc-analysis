---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelColumnPivotGridBlazor.PivotGroupInterval
name: PivotGroupInterval
type: Property
summary: Specifies how the Pivot Grid groups values of the current column or row field.
syntax:
  content: |-
    [DefaultValue(PivotTableGroupInterval.Default)]
    [ModelBrowsable(typeof(IModelListViewPivotGridBlazorVisibilityCalculator))]
    PivotTableGroupInterval PivotGroupInterval { get; set; }
  parameters: []
  return:
    type: DevExpress.Blazor.PivotTable.PivotTableGroupInterval
    description: "A value that specifies the group interval type.\n\nDefault property value for date fields is `Date`, default value for other types is `Default`. "
seealso: []
---
The `PivotGroupInterval` property specifies how the Pivot Grid groups field values. Available options include `Alphabetical`, `Numeric`, and various DateTime options. 

You can specify the `PivotGroupInterval` property in the [Model Editor](xref:112582):

1. Open the _SolutionName.Blazor.Server\Model.xafml_ file.
2. Navigate to the **SolutionName** | **Views** | **SolutionName.Module.BusinessObjects** | **ClassName** | **ClassName_ListView** | **Columns** | **FieldName**
3. Specify column settings for the field in the **Pivot Grid** section

![Pivot column settings in the Model Editor](~/images/pivot-grid/xaf-blazor-pivot-grid-column-settings.png)