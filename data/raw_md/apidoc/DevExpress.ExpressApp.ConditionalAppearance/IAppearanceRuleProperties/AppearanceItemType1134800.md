---
uid: DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.AppearanceItemType
name: AppearanceItemType
type: Property
summary: Specifies the type of UI elements affected by the conditional appearance rule.
syntax:
  content: string AppearanceItemType { get; set; }
  parameters: []
  return:
    type: System.String
    description: The string representation of an [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType) enumeration value specifying the type of UI elements affected by the conditional appearance rule.
seealso:
- linkId: "113286"
---
The UI elements affected by a conditional appearance rule are specified by the `AppearanceItemType` and [IAppearanceRuleProperties.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.TargetItems) properties. The following are the possible values for the `AppearanceItemType` rule property:

* [AppearanceItemType.ViewItem](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.ViewItem)
    
    If the `AppearanceItemType` parameter is set to this value, the rule affects the business class property(ies) specified by the [IAppearanceRuleProperties.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.TargetItems) property. Depending on the [IAppearanceRuleProperties.Context](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Context) property value, the business class property(ies) is affected in List Views and/or Detail Views. In List Views, the rule affects the corresponding cells both in view and edit mode. In Detail Views, the rule affects the corresponding Property Editors. Static Text Detail View Items can be affected as well.
    
     In List Views, XAF supports conditional appearance in Grid List Editors and Tree List Editors.
* [AppearanceItemType.LayoutItem](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.LayoutItem)
    
    If the `AppearanceItemType` property is set to this value, the rule affects the [Layout Item(s), Groups() and Tabbed Group(s)](xref:112817) specified by the [IAppearanceRuleProperties.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.TargetItems) property.
* [AppearanceItemType.Action](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.Action)
    
    If the `AppearanceItemType` property is set to this value, the rule affects the [Action(s)](xref:112622) specified by the [IAppearanceRuleProperties.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.TargetItems) property.

For details, refer to the [Declare Conditional Appearance Rules in the Application Model](xref:113372) topic.