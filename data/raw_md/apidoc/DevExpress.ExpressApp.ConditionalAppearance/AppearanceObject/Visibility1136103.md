---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.Visibility
name: Visibility
type: Property
summary: Specifies a visibility state for the target UI element.
syntax:
  content: public ViewItemVisibility? Visibility { get; set; }
  parameters: []
  return:
    type: System.Nullable{DevExpress.ExpressApp.Editors.ViewItemVisibility}
    description: '`true`, to make the target UI element visible; `false`, to make it invisible.'
seealso: []
---
If there are conditional appearance rules that change the visibility state within the rules appropriate for the target UI element, the `AppearanceObject`'s `Visibility` property returns the visibility state specified by the rule with the higher priority (see [IAppearance.Priority](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Priority)). If there are no rules that change the visibility state, the `Visibility` property returns `null`.