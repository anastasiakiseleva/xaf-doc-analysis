---
uid: DevExpress.ExpressApp.Model.IModelListView.GroupSummary
name: GroupSummary
type: Property
summary: Specifies the current List View's group summary.
syntax:
  content: string GroupSummary { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the current List View's group summary
seealso: []
---
To specify group summaries, do the following:

1. Focus the **Columns** node of the list view (the grid control appears to the right instead of property grid).
2. Right-click the grid column header and select the **Show Group By Box** command from the context menu.
3. Drag a column to the group panel or right-click a column and select the **Group by this column** command from the context menu.
4. Right-click the column in the group panel and select **Group Summary Editor…** from the context menu.
5. Edit group summaries in the dialog (see [Group Summary](xref:3502)).

When you close the dialog, the `GroupSummary` value will be updated with a correctly formatted string.

![GroupSummary property in Model Editor](~/images/groupsummary-modeleditor.gif)