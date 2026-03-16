---
uid: DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.ItemType
name: ItemType
type: Property
summary: The type of the target UI element. Its appearance is refreshed when you apply [conditional appearance rules](xref:113286).
syntax:
  content: public string ItemType { get; }
  parameters: []
  return:
    type: System.String
    description: A string that specifies the type of the target UI element when you apply [conditional appearance rules](xref:113286).
seealso: []
---
The [Conditional Appearance module](xref:113286) applies conditional appearance rules to different UI elements. You identify these elements by their appearance item types.

| UI Element | `AppearanceItemType` |
|---|---|
| **Cells in the List View that a [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) or [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor) displays. | [AppearanceItemType.ViewItem](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.ViewItem) |
| **Property Editors** | [AppearanceItemType.ViewItem](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.ViewItem) |
| **Static Text** | [AppearanceItemType.ViewItem](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.ViewItem) |
| **Layout Items, Groups, and Tabs** | [AppearanceItemType.LayoutItem](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.LayoutItem) |
| **Actions** | [AppearanceItemType.Action](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.Action) |

The `ItemType` property returns a string that specifies the type of the target UI element.

If you apply a conditional appearance rule to an item with a custom type, you need a custom Controller. The Controller calls the [AppearanceController.RefreshItemAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance*) method when needed. The custom Controller passes the custom item type to the Appearance Controller. You receive the value in the `ItemType` property when you handle the [AppearanceController.CustomApplyAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomApplyAppearance) or [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied) event.