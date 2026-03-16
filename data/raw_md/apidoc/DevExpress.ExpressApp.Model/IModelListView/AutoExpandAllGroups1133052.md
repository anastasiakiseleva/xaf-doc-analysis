---
uid: DevExpress.ExpressApp.Model.IModelListView.AutoExpandAllGroups
name: AutoExpandAllGroups
type: Property
summary: Specifies whether all group rows displayed within the List View are automatically expanded after each grouping operation.
syntax:
  content: |-
    [DefaultValue(false)]
    bool AutoExpandAllGroups { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, to expand all group rows; otherwise, `false`.'
seealso: []
---
This property applies when a List View uses grouping (see [IModelListView.IsGroupPanelVisible](xref:DevExpress.ExpressApp.Model.IModelListView.IsGroupPanelVisible)) and XAF displays the List View through the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor).