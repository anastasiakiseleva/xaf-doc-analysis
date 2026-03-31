---
uid: "113371"
seealso:
- linkId: "113374"
- linkId: "113221"
title: Declare Conditional Appearance Rules in Code
---
# Declare Conditional Appearance Rules in Code

The Conditional Appearance module allows you to change the appearance and visibility of different UI elements, as well as make them disabled/enabled. These elements include properties in List Views, built-in Property Editors and Static Text in Detail Views. In addition, you can make Actions visible/invisible or enabled/disabled. The required appearance can be applied under the specified conditions. To apply a particular appearance to the target UI element, define a rule in code or in the [Application Model](xref:112580). In this topic, you will learn how to define an appearance rule in code. To learn the general information on the Conditional Appearance module and appearance rules, refer to the [Conditional Appearance Module Overview](xref:113286) topic. To learn how to define appearance rules in the Application Model, refer to the [Declare Conditional Appearance Rules in the Application Model](xref:113372) topic.

[!include[conditional-appearance-module-prerequisites](~/templates/conditional-appearance-module-prerequisites.md)]

## General Information

To define an appearance rule in code, use the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute). This attribute is declared in the [](xref:DevExpress.ExpressApp.ConditionalAppearance) namespace of the _DevExpress.ExpressApp.ConditionalAppearance[!include[vX.Y.dll](~/templates/vx.y.dll11169.md)]_ assembly. So to use the attribute, you will need to add the corresponding _using_  directive.

When applying the **Appearance** attribute, set the rule's Id using the [AppearanceAttribute.Id](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Id) parameter. The remaining rule properties are specified using the attribute's named parameters.

* [AppearanceAttribute.AppearanceItemType](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.AppearanceItemType)
* [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems)
* [AppearanceAttribute.Context](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Context)
* [AppearanceAttribute.Criteria](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Criteria)
* [AppearanceAttribute.BackColor](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.BackColor)
* [AppearanceAttribute.FontColor](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontColor)
* [AppearanceAttribute.FontStyle](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontStyle)
* [AppearanceAttribute.Enabled](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Enabled)
* [AppearanceAttribute.Visibility](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Visibility)
* [AppearanceAttribute.Method](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Method)
* [AppearanceAttribute.Priority](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Priority)

When using the **Appearance** attribute, first specify which UI elements you are going to affect via the appearance rule: apply the **Appearance** attribute to either a [business class](xref:112570) or a business class property, and set its **AppearanceItemType** and **TargetItems** parameters. The following table illustrates several use cases.

| Element to be affected | Attribute Target | AppearanceItemType parameter | TargetItems parameter |
|---|---|---|---|
| Business class property - Approach 1 | Property | ViewItem | &nbsp; |
| Business class property - Approach 2 | Class | ViewItem | The required property's name |
| All business class properties | Class | ViewItem | "*" |
| Several properties - Approach 1 | Class | ViewItem | A semicolon-separated list of property names |
| Several properties - Approach 2 | Class | ViewItem | The "*" wildcard, followed by a semicolon-separated list of excluded properties. |
| Actions | Class | Action | A semicolon-separated list of Action identifiers |
| Property's Layout Item | Property | LayoutItem | &nbsp; |
| Layout Group(simple or tabbed group) | Class | LayoutItem | The Layout Group's Id specified in the Application Model |

Then, specify the rule's activity scope. For this purpose, use the following **Appearance** attribute parameters:

* [AppearanceAttribute.Context](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Context) - specify in which Views to activate the rule;
* [AppearanceAttribute.Criteria](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Criteria) - specify which criteria must be satisfied by the target object;
* [AppearanceAttribute.Method](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Method) - specify the method that returns **true** for the rule's activation (you can apply the **Appearance** attribute to this method and miss the **Method** parameter in the attribute's definition);
* [AppearanceAttribute.Priority](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Priority) - specify the current rule's volume when several rules affect the same UI element.

For details on these attribute parameters refer to their description in the Reference help section.

The last step in the appearance rule definition is specifying required appearance customizations. For this purpose, use the following attribute parameters.

* [AppearanceAttribute.BackColor](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.BackColor)
* [AppearanceAttribute.FontColor](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontColor)
* [AppearanceAttribute.FontStyle](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontStyle)
* [AppearanceAttribute.Enabled](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Enabled)
* [AppearanceAttribute.Visibility](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Visibility)

Rules declared via the **Appearance** attribute are reflected in the [Application Model](xref:112580). They are collected in the corresponding **Application** | **BOModel** | **_\<Class\>_** |**AppearanceRules** node. For details on this node, refer to the [Declare Conditional Appearance Rules in the Application Model](xref:113372) topic.

## Examples

[!include[ConditionalAppearance_ObjectColoredInListView](~/templates/conditionalappearance_objectcoloredinlistview11916.md)]

[!include[ConditionalFormatting_CategoryColoredInListViewRule](~/templates/conditionalformatting_categorycoloredinlistviewrule11918.md)]

[!include[ConditionalAppearance_LayoutItem](~/templates/conditionalappearance_layoutitem11921.md)]

[!include[ConditionalApearance_LayoutGroup](~/templates/conditionalapearance_layoutgroup11920.md)]

[!include[ConditionalFormatting_ActionVisibility](~/templates/conditionalformatting_actionvisibility11919.md)]

[!include[ConditionalAppearance_RuleMethod](~/templates/conditionalappearance_rulemethod11922.md)]

There are more examples demonstrated in the **FeatureCenter** demo installed with XAF. This demo is located in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder by default.
