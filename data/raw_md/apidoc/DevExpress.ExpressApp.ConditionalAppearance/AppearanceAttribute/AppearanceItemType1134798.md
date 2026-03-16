---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.AppearanceItemType
name: AppearanceItemType
type: Property
summary: Specifies the type of UI elements affected by the conditional appearance rule created using this attribute.
syntax:
  content: public string AppearanceItemType { get; set; }
  parameters: []
  return:
    type: System.String
    description: The string representation of an [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType) enumeration value specifying the type of UI elements affected by the conditional appearance rule.
seealso:
- linkId: "113286"
---
To specify the UI element to be affected, apply the `Appearance` attribute to the required business class or business class property and use the `AppearanceItemType` and [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems) attribute parameters. For details, refer to the [Declare Conditional Appearance Rules in Code](xref:113371) topic.

These are the following possible values for the `AppearanceItemType` attribute parameter:

* [AppearanceItemType.ViewItem](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.ViewItem)
    
    If you set the `AppearanceItemType` parameter to this value, [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems) specifies properties affected by this attribute's rule. Based on the [AppearanceAttribute.Context](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Context) parameter, properties are affected in List Views and/or Detail Views. In List Views, the rule affects the corresponding cells both in view and edit mode. In Detail Views, the rule affects the corresponding Property Editors. Static Text Detail View Items can be affected as well.
    
    In List Views, XAF supports conditional appearance in Grid List Editors and Tree List Editors.
* [AppearanceItemType.LayoutItem](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.LayoutItem)
    
    If you set the `AppearanceItemType` parameter to this value, [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems) specifies [Layout Item(s), Groups(), and Tabbed Group(s)](xref:112817) affected by this attribute's rule.
* [AppearanceItemType.Action](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceItemType.Action)
    
    If you set the `AppearanceItemType` parameter to this value, [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems)  specifies [Action(s)](xref:112622) affected by this attribute's rule.

This property is set to `ViewItem` by default.

## Examples
### Example 1.

[!include[ConditionalAppearance_ObjectColoredInListView](~/templates/conditionalappearance_objectcoloredinlistview11916.md)]

### Example 2.

[!include[ConditionalAppearance_LayoutItem](~/templates/conditionalappearance_layoutitem11921.md)]

### Example 3.

[!include[ConditionalFormatting_ActionVisibility](~/templates/conditionalformatting_actionvisibility11919.md)]

Additional examples are available in the [Declare Conditional Appearance Rules in Code](xref:113371) topic.

[!include[<`AppearanceItemType` property>](~/templates/main-demo-tip.md)]