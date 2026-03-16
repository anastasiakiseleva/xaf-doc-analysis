---
uid: DevExpress.ExpressApp.ConditionalAppearance.CollectAppearanceRulesEventArgs.AppearanceRules
name: AppearanceRules
type: Property
summary: Provides access to the list of [conditional appearance rules](xref:113286) found for the target UI element in the Application Model.
syntax:
  content: public List<IAppearanceRuleProperties> AppearanceRules { get; }
  parameters: []
  return:
    type: System.Collections.Generic.List{DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties}
    description: A list of [](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties) objects representing [conditional appearance rules](xref:113286) found for the target UI element in the Application Model.
seealso: []
---
This property returns a list of conditional appearance rules found in the Application Model for the UI element specified by the [CollectAppearanceRulesEventArgs.Name](xref:DevExpress.ExpressApp.ConditionalAppearance.CollectAppearanceRulesEventArgs.Name) and [CollectAppearanceRulesEventArgs.ViewInfo](xref:DevExpress.ExpressApp.ConditionalAppearance.CollectAppearanceRulesEventArgs.ViewInfo) properties. You can add dynamically created conditional appearance rules to the list in the handler of the [AppearanceController.CollectAppearanceRules](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CollectAppearanceRules) event. After this event is raised, the rules from this list are filtered, leaving only those rules whose [IAppearanceRuleProperties.Criteria](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Criteria) and [IAppearanceRuleProperties.Method](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Method) properties are satisfied.