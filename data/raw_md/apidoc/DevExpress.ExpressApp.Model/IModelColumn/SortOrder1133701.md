---
uid: DevExpress.ExpressApp.Model.IModelColumn.SortOrder
name: SortOrder
type: Property
summary: Specifies the sorting type for the current column.
syntax:
  content: |-
    [DefaultValue(ColumnSortOrder.None)]
    ColumnSortOrder SortOrder { get; set; }
  parameters: []
  return:
    type: DevExpress.Data.ColumnSortOrder
    description: A [](xref:DevExpress.Data.ColumnSortOrder) enumeration value specifying the sorting type for the current column.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelColumn.SortIndex
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-sort-a-listview-in-code
  altText: 'GitHub example: XAF - How to sort a ListView in code'
---
Note that by default, if the [IModelColumn.SortIndex](xref:DevExpress.ExpressApp.Model.IModelColumn.SortIndex) property value does not equal **-1**, the **Ascending** sorting is applied. So, to disable sorting, you must set **SortOrder** to **None** and **SortIndex** to **-1**.
> [!IMPORTANT]
> Sorting, specified by this property is directly applied to the data-aware control. To sort the underlying data source, use the [](xref:DevExpress.ExpressApp.Model.IModelSorting) node instead.