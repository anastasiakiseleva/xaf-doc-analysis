---
uid: DevExpress.ExpressApp.SystemModule.IModelDetailViewDefaultFocusedItem.DefaultFocusedItem
name: DefaultFocusedItem
type: Property
summary: Specifies the Property Editor which will be focused when the current Detail View is displayed.
syntax:
  content: |-
    [DataSourceProperty("Items", new string[]{})]
    IModelViewItem DefaultFocusedItem { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelViewItem
    description: An [](xref:DevExpress.ExpressApp.Model.IModelViewItem) object representing the ViewItem node corresponding to the default View Item.
seealso: []
---
This property affects only the root Detail Views (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)). For instance, the Detail View shown alongside the List View (see [Display a Detail View with a List View](xref:404203)), is not root. The **DefaultFocusedItem** property does not take effect in this case. The reason for this behavior is that otherwise, focus will leave the grid bounds when iterating through the List View using the keyboard.