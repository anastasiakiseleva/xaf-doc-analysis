---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomGetIsRulePropertiesEmpty
name: CustomGetIsRulePropertiesEmpty
type: Event
summary: Occurs when the Appearance Controller collects the appearance rules and determines whether or not the specific [](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties) object is empty.
syntax:
  content: public event EventHandler<CustomGetIsRulePropertiesEmptyEventArgs> CustomGetIsRulePropertiesEmpty
seealso: []
---
By default, the [IAppearance.FontStyle](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.FontStyle), [IAppearance.FontColor](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.FontColor), [IAppearance.BackColor](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.BackColor), [IAppearance.Visibility](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Visibility) and [IAppearance.Enabled](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Enabled) nullable properties of the [](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties) object are checked for a value presence and a rule properties object is considered empty if there are no values found. Once a rule properties object is considered empty, it is excluded from the processing list and is not processed at all. The result is cached to avoid duplicated calculations. Handle the **CustomGetIsRulePropertiesEmpty** event in case you have introduced new properties and want to manually manage their values.