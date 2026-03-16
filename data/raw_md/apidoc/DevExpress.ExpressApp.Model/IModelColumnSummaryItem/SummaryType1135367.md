---
uid: DevExpress.ExpressApp.Model.IModelColumnSummaryItem.SummaryType
name: SummaryType
type: Property
summary: Specifies the function that calculates a value over all records within the current column (total summary).
syntax:
  content: SummaryType SummaryType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.SummaryType
    description: A [](xref:DevExpress.ExpressApp.Model.SummaryType) enumeration value specifying the function that calculates a value over all records within the current column (total summary).
seealso: []
---
This property is considered by a grid control that visualizes the current List View in a Windows Forms application.

The total summary value is displayed within the grid footer under the column, if the List View node's [IModelListView.IsFooterVisible](xref:DevExpress.ExpressApp.Model.IModelListView.IsFooterVisible) property is set to **true**.

By default, this property is set to [SummaryType.None](xref:DevExpress.ExpressApp.Model.SummaryType.None).