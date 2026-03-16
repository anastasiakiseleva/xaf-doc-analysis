---
uid: DevExpress.ExpressApp.ListView.MasterDetailMode
name: MasterDetailMode
type: Property
summary: Specifies whether to display the Detail View of the currently selected object near the current List View.
syntax:
  content: |-
    [Browsable(false)]
    public MasterDetailMode MasterDetailMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.MasterDetailMode
    description: A [](xref:DevExpress.ExpressApp.MasterDetailMode) enumeration value specifying whether to display the Detail View of the currently selected object near the current List View.
seealso: []
---
The `MasterDetailMode` property enables the [split layout](xref:113249#split-layout-the-masterdetailmode-property):

WinForms
:   ![SplitLayout](~/images/splitlayout116545.png)
ASP.NET Core Blazor
:   ![SplitLayoutBlazor](~/images/splitlayoutblazor.png)

You can also specify this property in the [](xref:DevExpress.ExpressApp.DefaultListViewOptionsAttribute) attribute (see [Data Annotations in Data Model](xref:112701)).

The value of this property is assigned to the [Application Model](xref:112580)'s **Application** | **Views** | **List View** node's [IModelListView.MasterDetailMode](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode) property. You can change this property's value using the [Model Editor](xref:112830).

The default value of this property is the value that is assigned to the **MasterDetailMode** property of the Application Model's **List View** node.

### Important Notes
[!include[MasterDetailMode_notes](~/templates/MasterDetailMode_notes.md)]
