---
uid: DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode
name: MasterDetailMode
type: Property
summary: Specifies whether to display the Detail View of the currently selected object near the current List View.
syntax:
  content: MasterDetailMode MasterDetailMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.MasterDetailMode
    description: A [](xref:DevExpress.ExpressApp.MasterDetailMode) enumeration value that specifies whether to display the Detail View of the currently selected object near the current List View.
seealso:
- linkId: "113249"
---
This property enables the [split layout](xref:113249#split-layout-the-masterdetailmode-property):

WinForms
:   ![SplitLayout](~/images/splitlayout116545.png)
ASP.NET Core Blazor
:   ![SplitLayoutBlazor](~/images/splitlayoutblazor.png)

To specify this property, invoke the [Model Editor](xref:112582) and navigate to the **Views** | **<_ListView_>** node:

![Model Designer: MasterDetailMode](~/images/tutorial_uic_lesson17_1115513.png)

You can also specify this property in code. Use the [DefaultListViewOptions](xref:DevExpress.ExpressApp.DefaultListViewOptionsAttribute) attribute to do this. Refer to the following topic for more information: [Data Annotations in Data Model](xref:112701).

### Important Notes

[!include[MasterDetailMode_notes](~/templates/MasterDetailMode_notes.md)]
