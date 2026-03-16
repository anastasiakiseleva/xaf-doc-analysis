---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute
name: AppearanceAttribute
type: Class
summary: Applied to business classes and their properties. Declares a conditional appearance rule.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method | AttributeTargets.Property | AttributeTargets.Interface, AllowMultiple = true)]
    public class AppearanceAttribute : Attribute, IAppearanceRuleProperties, IAppearance
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute._members
  altText: AppearanceAttribute Members
- linkId: "113286"
- linkId: "113221"
---
The **Appearance** attribute is declared in the [Conditional Appearance Module](xref:113286). This module allows you to disable/enable, show/hide and change the look and feel of properties in List Views, Property Editors, Layout Items, Layout Groups and Actions based on business rules. The **Appearance** attribute is used to declare these business rules. The [Declare Conditional Appearance Rules in Code](xref:113371) topic contains a detailed explanation on how to use this attribute.