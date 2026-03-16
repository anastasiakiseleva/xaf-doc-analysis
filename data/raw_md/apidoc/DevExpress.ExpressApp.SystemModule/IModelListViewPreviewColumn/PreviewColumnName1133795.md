---
uid: DevExpress.ExpressApp.SystemModule.IModelListViewPreviewColumn.PreviewColumnName
name: PreviewColumnName
type: Property
summary: Specifies the column whose content must be displayed in the preview section.
syntax:
  content: |-
    [DataSourceProperty("Columns", new string[]{})]
    IModelColumn PreviewColumnName { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelColumn
    description: An [](xref:DevExpress.ExpressApp.Model.IModelColumn) object specifying the column whose content must be displayed in the preview section. If you do not specify the property value, the preview section is hidden.
seealso: []
---
Use the `PreviewColumnName` property to show preview sections under each data row across all columns. These sections can display lengthy memo fields with images, values from data source fields, custom text, etc.

![|XAF Preview section in Note List View, DevExpress](~/images/how-to-show-preview-section-in-listview-result.png)

The `PreviewColumnName` property applies to List Views that use the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) and @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.

For step-by-step instructions on how to enable Row Preview Sections in XAF applications, refer to the following topic: [](xref:404210).

The topics below contain platform-specific information and examples related to Row Preview Sections:

* [Blazor Grid - The DetailRowTemplate property](xref:DevExpress.Blazor.DxGrid.DetailRowTemplate)
* [WinForms Data Grid - Row Preview Sections](xref:114725)