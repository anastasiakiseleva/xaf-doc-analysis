---
uid: DevExpress.ExpressApp.Editors.ViewItem.IsCaptionVisible
name: IsCaptionVisible
type: Property
summary: Indicates whether the caption of the current View Item should be visible.
syntax:
  content: public virtual bool IsCaptionVisible { get; }
  parameters: []
  return:
    type: System.Boolean
    description: "`true` if the current View Item's caption is visible; otherwise, `false`."
seealso: []
---
When the layout manager creates a layout item, it gets this property to determine whether a caption should be displayed for the current View Item.

This property returns `false`. However, you can override it in the [](xref:DevExpress.ExpressApp.Editors.ViewItem) class' descendants.
