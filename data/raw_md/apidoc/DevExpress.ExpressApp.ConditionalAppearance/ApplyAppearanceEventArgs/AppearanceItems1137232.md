---
uid: DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.AppearanceItems
name: AppearanceItems
type: Property
summary: Gets the list of resulting items that were calculated by each appearance rule.
syntax:
  content: public List<IConditionalAppearanceItem> AppearanceItems { get; }
  parameters: []
  return:
    type: System.Collections.Generic.List{DevExpress.ExpressApp.ConditionalAppearance.IConditionalAppearanceItem}
    description: A **List\<IConditionalAppearanceItem>** list of resulting items that were calculated by each appearance rule.
seealso: []
---
Use this property instead of [ApplyAppearanceEventArgs.AppearanceObject](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.AppearanceObject) if you want to combine all appearance items in a custom manner. Set the **Handled** parameter to **true** to disable the default algorithm.