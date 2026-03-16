---
uid: "113008"
title: Validation Rules
seealso:
- linkId: "113251"
---
# Validation Rules

XAF provides several built-in types of Validation Rules. They are defined in the following table:

| Validation Rule type | Description |
|---|---|
| [RuleCombinationOfPropertiesIsUnique](xref:DevExpress.Persistent.Validation.RuleCombinationOfPropertiesIsUniqueAttribute) | Demands that the combination of particular property values should be unique. |
| [RuleCriteria](xref:DevExpress.Persistent.Validation.RuleCriteriaAttribute) | Demands that an object of a particular type should satisfy a specified criteria. |
| [RuleFromBoolProperty](xref:DevExpress.Persistent.Validation.RuleFromBoolPropertyAttribute) | Demands that a Boolean type property should have a True value. |
| [RuleIsReferenced](xref:DevExpress.Persistent.Validation.RuleIsReferencedAttribute) | Demands that an object should be referenced in objects of a specified type. |
| [RuleObjectExists](xref:DevExpress.Persistent.Validation.RuleObjectExistsAttribute) | Demands that an object of a particular type that satisfies specified criteria exists in the database. |
| [RuleRange](xref:DevExpress.Persistent.Validation.RuleRangeAttribute) | Demands that a particular property's value should be within a specified value range. |
| [RuleRegularExpression](xref:DevExpress.Persistent.Validation.RuleRegularExpressionAttribute) | Demands that a particular property should match a specified pattern. |
| [RuleRequiredField](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute) | Demands that a property should have a value. |
| [RuleStringComparison](xref:DevExpress.Persistent.Validation.RuleStringComparisonAttribute) | Demands that the value of a particular String type property should satisfy a specified condition. |
| [RuleValueComparison](xref:DevExpress.Persistent.Validation.RuleValueComparisonAttribute) | Demands that a particular property's value should satisfy a specified condition. |
| [RuleUniqueValue](xref:DevExpress.Persistent.Validation.RuleUniqueValueAttribute) | Demands that a particular property's value should be unique. |

All of these Validation Rule types implement the [](xref:DevExpress.Persistent.Validation.IRule) interface. You can develop your own Rules by implementing the **IRule** interface, or by inheriting from the [](xref:DevExpress.Persistent.Validation.RuleBase) abstract class, which implements this interface. For details, refer to the [Implement Custom Rules](xref:113051) topic.