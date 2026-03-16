---
uid: DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.AppearanceObject
name: AppearanceObject
type: Property
summary: The appearance that is currently applied to the target UI element.
syntax:
  content: public AppearanceObject AppearanceObject { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject
    description: An [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject) that specifies the appearance currently applied.
seealso: []
---
You can customize the appearance to be applied to a certain range of items by changing the object returned by the **AppearanceObject** property in the [AppearanceController.CustomApplyAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomApplyAppearance) event handler. For this purpose, use the object's [AppearanceObject.Enabled](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.Enabled), [AppearanceObject.Visibility](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.Visibility), [AppearanceObject.BackColor](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.BackColor), [AppearanceObject.FontColor](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.FontColor) and [AppearanceObject.FontStyle](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.FontStyle) properties. But in this instance, do not set the **CustomApplyAppearanceEventArgs.Handled** event handler parameter to true, to apply the customized appearance to the target items.

When you get the object specified by the **AppearanceObject** property in the [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied) event handler, you can only view the appearance that has been just applied to the target item. To change the appearance applied, access the target item using the [ApplyAppearanceEventArgs.Item](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.Item) property.