---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.IsCaptionVisible
name: IsCaptionVisible
type: Property
summary: Indicates whether the caption of the current Property Editor should be visible in a UI.
syntax:
  content: public override bool IsCaptionVisible { get; }
  parameters: []
  return:
    type: System.Boolean
    description: "`true` if the current Property's caption is visible; otherwise, `false`."
seealso: []
---
When the layout manager creates a layout item, it gets this property to determine whether a caption should be displayed for the current Property Editor.

This property returns `true`. However, it can be overridden in the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) class' descendants.