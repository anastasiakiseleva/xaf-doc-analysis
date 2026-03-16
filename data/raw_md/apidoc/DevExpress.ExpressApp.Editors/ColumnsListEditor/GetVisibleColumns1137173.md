---
uid: DevExpress.ExpressApp.Editors.ColumnsListEditor.GetVisibleColumns
name: GetVisibleColumns()
type: Method
summary: Returns the list of [](xref:DevExpress.ExpressApp.Editors.ColumnsListEditor)'s visible columns.
syntax:
  content: public List<ColumnWrapper> GetVisibleColumns()
  return:
    type: System.Collections.Generic.List{DevExpress.ExpressApp.Editors.ColumnWrapper}
    description: A **List\<ColumnWrapper>** list of visible columns.
seealso: []
---
The **GetVisibleColumns** method iterates through the [ColumnsListEditor.Columns](xref:DevExpress.ExpressApp.Editors.ColumnsListEditor.Columns) list and returns columns with the **ColumnWrapper.Visible** property set to true.