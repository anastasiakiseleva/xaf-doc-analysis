---
uid: DevExpress.ExpressApp.TreeListEditors.Win.IModelColumnTreeListWin.AllNodesSummary
name: AllNodesSummary
type: Property
summary: Specifies whether the current column's summary is calculated against all tree list nodes or against root nodes only.
syntax:
  content: |-
    [ModelBrowsable(typeof(AllNodesSummaryVisibilityCalculator))]
    bool AllNodesSummary { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: |-
      **true** if a summary is calculated against all nodes; otherwise, it is calculated only against root nodes.
      The default is **false**.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelColumnSummaryItem.SummaryType
- linkId: "112836"
---
The **AllNodesSummary** property is considered for List Views displayed by the [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor).
This property value is passed to the [TreeListColumn.AllNodesSummary](xref:DevExpress.XtraTreeList.Columns.TreeListColumn.AllNodesSummary) property. To specify the summary type, use the column's [IModelColumnSummaryItem.SummaryType](xref:DevExpress.ExpressApp.Model.IModelColumnSummaryItem.SummaryType) property.