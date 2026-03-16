---
uid: DevExpress.ExpressApp.Model.IModelColumn.SortIndex
name: SortIndex
type: Property
summary: Specifies the sequence of column sorting.
syntax:
  content: |-
    [DefaultValue(-1)]
    int SortIndex { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the sequence of column sorting.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelColumn.SortOrder
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-sort-a-listview-in-code
  altText: 'GitHub example: XAF - How to sort a ListView in code'
---
List View records can be sorted by multiple columns. The **SortIndex** value is zero-based. It means that initially, List View records are sorted by the column with the zero **SortIndex** value, second - by the column with **SortIndex** set to 1, etc. The -1 value cancels data sorting by this column. When it is required to sort a List View by the single column, this column's **SortIndex** should be zero. Note that by default, if the **SortIndex** property value does not equal **-1**, the **Ascending** sorting is applied ([IModelColumn.SortOrder](xref:DevExpress.ExpressApp.Model.IModelColumn.SortOrder) is set to **ColumnSortOrder.Ascending**). So, to disable sorting, you must set **SortIndex** to **-1** and **SortOrder** to **None**.