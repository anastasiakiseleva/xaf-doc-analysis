---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomCreateAppearanceRule
name: CustomCreateAppearanceRule
type: Event
summary: Occurs when an **AppearanceRule** object is created.
syntax:
  content: public event EventHandler<CustomCreateAppearanceRuleEventArgs> CustomCreateAppearanceRule
seealso: []
---
Use this event to manually create an **AppearanceRule** object from the passed [](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties) object. 
By default, the passed **IAppearanceRuleProperties** object is wrapped to a **CachedAppearanceRuleProperties** object and additional custom properties are lost during this operation.