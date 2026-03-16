---
uid: DevExpress.ExpressApp.SystemModule.IModelClassNewItemRow.DefaultListViewNewItemRowPosition
name: DefaultListViewNewItemRowPosition
type: Property
summary: Indicate whether to display the new item row in the default editable List View.
syntax:
  content: NewItemRowPosition DefaultListViewNewItemRowPosition { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.NewItemRowPosition
    description: A [](xref:DevExpress.ExpressApp.NewItemRowPosition) enumeration value specifying whether to display the new item row in the default editable List View.
seealso:
- linkId: "113249"
---
In a Windows Forms application, the `DefaultListViewNewItemRowPosition` property specifies whether to display the `NewItemRow` in the default editable List View (see `DefaultListViewAllowEdit`). The `NewItemRow` allows users to create new objects directly in a ListView.

In an ASP.NET Core Blazor application, the `DefaultListViewNewItemRowPosition` property specifies whether to display the `New` button in the command column header of the default editable List View (see `DefaultListViewAllowEdit`). This button allows users to create new objects directly in a ListView.

The `DefaultListViewNewItemRowPosition` property default value is `None`. You can set a value for this attribute in code via the `DefaultListViewOptions` attribute (see [Data Annotations in Data Model](xref:112701)).