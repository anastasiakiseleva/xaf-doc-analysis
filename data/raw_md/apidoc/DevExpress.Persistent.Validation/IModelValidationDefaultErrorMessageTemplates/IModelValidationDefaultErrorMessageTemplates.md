---
uid: DevExpress.Persistent.Validation.IModelValidationDefaultErrorMessageTemplates
name: IModelValidationDefaultErrorMessageTemplates
type: Interface
summary: The ErrorMessageTemplates node defines the default templates for the messages displayed when validation rules are broken.
syntax:
  content: 'public interface IModelValidationDefaultErrorMessageTemplates : IModelNode'
seealso:
- linkId: DevExpress.Persistent.Validation.IModelValidationDefaultErrorMessageTemplates._members
  altText: IModelValidationDefaultErrorMessageTemplates Members
---
When rules are broken, some description should be written in the Validation Error window for every rule. This node defines the default message templates that are designed for built-in rule types. These messages are displayed in the Validation Error window, by default. You can customize them. In this instance, the custom text will be used for all rules of the corresponding type. To customize a message template for a certain rule, use the corresponding [](xref:DevExpress.ExpressApp.Validation.IModelRuleBase) node. In this node, use the required **MessageTempate…** property.

In message templates, you can use format items. For instance, when using the {TargetPropertyName} format item, the caption of the validated property will be inserted in the rule description. For details, refer to the [RuleBaseAttribute.CustomMessageTemplate](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.CustomMessageTemplate) property description.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.