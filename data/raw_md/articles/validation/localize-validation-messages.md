---
uid: "113129"
seealso: []
title: Localize Validation Messages
owner: Ekaterina Kiseleva
---
# Localize Validation Messages

XAF applications can be localized to the required language. This topic explains localization of the validation messages that are shown to users when a rule is broken or the [Validation Action](xref:113008) is executed. Refer to the [Localization Basics](xref:112595) topic, to get general information on localization.

To localize validation messages, use the [Model Editor](xref:112582) invoked for the required language (see [Localize UI Elements](xref:403184)). In the sections below, you will learn which nodes should be localized.

## Localize Message Text
Navigate to the **Localization** | **Exceptions** | **UserVisibleExceptions** | **Validation** node.

![ValidationLocalizationNode](~/images/validationlocalizationnode116145.png)

The child nodes represent the messages that are displayed by the Validation System in different contexts:

* **ActionErrorMessageHeaderFormat**
	
	A rule can be checked when a particular [Action](xref:112622) is executed. In this instance, the value of the corresponding [!include[Node_Action](~/templates/node_action111373.md)] node's `ValidationContexts` property should be set as the rule's target context ID. When a rule is broken after the associated Action has been executed, a validation message is displayed. The text of this message is specified by the `ActionErrorMessageHeaderFormat` property. In this property, you can use the {0} format item. It will be replaced with the name of the executed Action.

* **AllContextsErrorMessageHeader**
	
	The [Validation Module](xref:113684) supplies the **ShowAllContexts** Action (see in [Validation Rules](xref:113008) topic). When this Action is executed, all rules that are specified for the current object are checked in all associated contexts. If at least one rule is broken, the displayed validation message contains the text specified by the `AllContextsErrorMessageHeader` property.
* **DeleteErrorMessageHeader**
	
	A rule's context can be set to the `DefaultContexts.Delete` value. In this instance, the rule will be checked when deleting the target object. If the rule is broken, the displayed validation message will contain the text specified by the `DeleteErrorMessageHeader` property.

* **SaveErrorMessageHeader**
	
	A rule's context can be set to the `DefaultContexts.Save` value. In this instance, the rule will be checked when saving the target object to the database. If the rule is broken, the displayed validation message will contain the text specified by the `SaveErrorMessageHeader` property.

* **ValidationSucceededMessageHeader**
	
	The [Validation Module](xref:113684) supplies the **ShowAllContexts** Action (see in [Validation Rules](xref:113008) topic). When this Action is executed, all rules that are specified for the current object are checked in all associated contexts. If all rules are valid, the displayed validation message contains the text specified by the `ValidationSucceededMessageHeader` property.

Write the appropriate localized text in the `Value` property of these nodes.

## Localize Rule Description
Navigate to the **Validation** node.

![ValidationNode](~/images/validationnode116146.png)

To localize the text that describes a broken rule in the validation message, use one of the following approaches:

* The **Validation** | **ErrorMessageTemplates** node
	
	This node defines the message templates that are used for built-in rule types. To localize a message template for a certain rule type, use the corresponding **Validation** | **ErrorMessageTemplates** | **RuleType** node. In this node, use the required `MessageTemplate…` property. The localized text will be used for all rules of the corresponding type.
* The **Validation** | **Rules** node
	
	This node defines all the rules used in the current application. To localize a message template for a particular rule, use the corresponding **Validation** | **Rules** | **Rule** node. In this node, use the required `MessageTemplate…` property or the `CustomMessageTemplate` property. The localized text will be used for the current rule only.

In a message template, you can use format items. For instance, when using the {TargetPropertyName} format item, the caption of the validated property will be inserted in the rule description. For details, refer to the [RuleBaseAttribute.CustomMessageTemplate](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.CustomMessageTemplate) property description.
