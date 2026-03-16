---
uid: DevExpress.ExpressApp.SystemModule.IModelListViewShowFindPanel.ShowFindPanel
name: ShowFindPanel
type: Property
summary: Specifies whether the [List Editor](xref:113189) displays a search component at runtime.
syntax:
  content: bool ShowFindPanel { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if a search component is visible; otherwise, `false`.'
seealso: []
---

Platform-specific [List Editors](xref:113189) display different search components that allow users to filter the data in the list by keyword.

ASP.NET Core Blazor

:   @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor displays the [Search Box](xref:404142).

Windows Forms

:   @DevExpress.ExpressApp.Win.Editors.GridListEditor displays the [Find Panel](xref:8869).

You can access this property in the [Model Editor](xref:112582). 

If you change this property's value, you override the values of the following 
 properties: @DevExpress.ExpressApp.ListViewFindPanelAttribute and @DevExpress.ExpressApp.SystemModule.IModelClassShowFindPanel.DefaultListViewShowFindPanel.
